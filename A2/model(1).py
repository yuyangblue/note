"""
model.py  第十八届华中杯 A 题
城市绿色物流配送调度 — 数学模型数据层（支持虚拟客户）

修复更新点：
- 补充了速度方差，使能耗的数学期望计算严谨无误：E[v^2] = μ^2 + σ^2。
"""

import math
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd


# ══════════════════════════════════════════════════════════════════════════════
# 一、全局常量
# ══════════════════════════════════════════════════════════════════════════════

BASE_MINUTE        = 8 * 60    # 计时起点 08:00（换算为全天分钟数）
SERVICE_TIME       = 20        # 每客户固定服务时长（分钟）
WAIT_RATE          = 20 / 60   # 早到等待惩罚：20 元/h → 元/min
LATE_RATE          = 50 / 60   # 晚到超时惩罚：50 元/h → 元/min
STARTUP_COST       = 400.0     # 每辆车启动固定成本（元）
FUEL_PRICE         = 7.61      # 燃油单价（元/升）
ELEC_PRICE         = 1.64      # 电费单价（元/kWh）
CARBON_PRICE       = 0.65      # 碳排放成本（元/kg CO₂）
CARBON_COEFF_FUEL  = 2.547     # 燃油碳排放转换系数（kg CO₂/升）
CARBON_COEFF_ELEC  = 0.501     # 电力碳排放转换系数（kg CO₂/kWh）
GREEN_ZONE_RADIUS  = 10.0      # 绿色配送区半径（km），圆心为市中心 (0, 0)
GREEN_ZONE_BAN_START = 0       # 限行开始（自 08:00 起分钟数，即 08:00）
GREEN_ZONE_BAN_END   = 8 * 60  # 限行结束（自 08:00 起分钟数，即 16:00）


# ══════════════════════════════════════════════════════════════════════════════
# 二、交通时段定义与速度计算
# ══════════════════════════════════════════════════════════════════════════════

class TrafficPeriod(Enum):
    """交通时段枚举：根据不同时段的交通状况定义速度分布。"""
    CONGESTED = "拥堵"    # 08:00–09:00, 11:30–13:00
    SMOOTH    = "顺畅"    # 09:00–10:00, 13:00–15:00
    MODERATE  = "一般"    # 10:00–11:30, 15:00–17:00
    EVENING   = "夜间"    # 17:00 以后（按顺畅处理）

# 速度分布参数 N(μ, σ²)，表中数字为方差，转换为标准差 σ = sqrt(方差)
_SPEED_PARAMS: Dict[TrafficPeriod, Tuple[float, float]] = {
    TrafficPeriod.CONGESTED: ( 9.8, math.sqrt(4.72)),   # 拥堵：均值9.8 km/h，方差4.72
    TrafficPeriod.SMOOTH:    (55.3, math.sqrt(0.12)),   # 顺畅：均值55.3 km/h，方差0.12
    TrafficPeriod.MODERATE:  (35.4, math.sqrt(5.22)),   # 一般：均值35.4 km/h，方差5.22
    TrafficPeriod.EVENING:   (55.3, math.sqrt(0.12)),   # 夜间：同顺畅时段
}

# 提取方差常量，用于公式推导期望 E[v^2] = μ^2 + σ^2
_SPEED_VARIANCES: Dict[TrafficPeriod, float] = {
    TrafficPeriod.CONGESTED: 4.72,
    TrafficPeriod.SMOOTH:    0.12,
    TrafficPeriod.MODERATE:  5.22,
    TrafficPeriod.EVENING:   0.12,
}

# 各时段区间（左闭右开，单位：自 08:00 起分钟数）
# 17:00 以后自动归入夜间时段，无需在表中列出
_PERIOD_TABLE: List[Tuple[int, int, TrafficPeriod]] = [
    (  0,  60, TrafficPeriod.CONGESTED),   # 08:00–09:00
    ( 60, 120, TrafficPeriod.SMOOTH),      # 09:00–10:00
    (120, 210, TrafficPeriod.MODERATE),    # 10:00–11:30
    (210, 300, TrafficPeriod.CONGESTED),   # 11:30–13:00
    (300, 420, TrafficPeriod.SMOOTH),      # 13:00–15:00
    (420, 540, TrafficPeriod.MODERATE),    # 15:00–17:00
]


def get_traffic_period(minute_from_8: float) -> TrafficPeriod:
    """根据时刻（自08:00起分钟数）返回对应交通时段。"""
    for start, end, period in _PERIOD_TABLE:
        if start <= minute_from_8 < end:
            return period
    return TrafficPeriod.EVENING


def get_period_end(minute_from_8: float) -> float:
    """返回当前时段结束时刻（从08:00起算的分钟数），夜间返回无穷大。"""
    for start, end, period in _PERIOD_TABLE:
        if start <= minute_from_8 < end:
            return float(end)
    return float('inf')


def get_period_speed(period: TrafficPeriod) -> float:
    """返回指定时段的平均速度（km/h），用于确定性计算。"""
    return _SPEED_PARAMS[period][0]


def get_period_variance(period: TrafficPeriod) -> float:
    """返回指定时段的速度方差，用于能耗公式的数学期望计算。"""
    return _SPEED_VARIANCES[period]


def sample_speed(period: TrafficPeriod, rng: Optional[np.random.Generator] = None) -> float:
    """
    从给定交通时段的正态分布中采样车速（km/h）。
    rng 为可复现的随机数生成器，不传时自动创建。
    返回值保证 ≥ 1.0 km/h。
    """
    mu, sigma = _SPEED_PARAMS[period]
    generator = rng if rng is not None else np.random.default_rng()
    return max(float(generator.normal(mu, sigma)), 1.0)


# ══════════════════════════════════════════════════════════════════════════════
# 三、车辆类型定义
# ══════════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class VehicleType:
    """
    单一车辆类型的规格，同类型所有车共享此对象。
    """

    type_id:      str    # "O1"/"O2"/"O3"/"E1"/"E2"
    category:     str    # "fuel" | "electric"
    max_weight:   float  # 最大载重（kg）
    max_volume:   float  # 最大容积（m³）
    fleet_count:  int    # 车队总数量（辆）
    load_factor:  float  # 满载额外能耗比例（燃油 0.40，新能源 0.35）

    def base_consumption(self, speed: float, variance: float) -> float:
        """
        空载百公里能耗（L 或 kWh）。
        严格计算数学期望：由于能耗与v^2有关，E[v^2] = (E[v])^2 + Var(v)。
        """
        expected_v2 = speed ** 2 + variance
        if self.category == "fuel":
            return 0.0025 * expected_v2 - 0.2554 * speed + 31.75
        return 0.0014 * expected_v2 - 0.12 * speed + 36.19

    def consumption(self, speed: float, variance: float, load_ratio: float) -> float:
        """实际百公里能耗数学期望，考虑负载修正（L 或 kWh）。"""
        return self.base_consumption(speed, variance) * (1.0 + self.load_factor * load_ratio)

    def energy_cost(self, distance_km: float, speed: float, variance: float, load_ratio: float) -> float:
        """行驶 distance_km 公里的燃料/电力成本期望值（元）。"""
        unit_price = FUEL_PRICE if self.category == "fuel" else ELEC_PRICE
        return self.consumption(speed, variance, load_ratio) / 100 * distance_km * unit_price

    def carbon_emission(self, distance_km: float, speed: float, variance: float, load_ratio: float) -> float:
        """行驶 distance_km 公里的碳排放量期望值（kg CO₂）。"""
        coeff = CARBON_COEFF_FUEL if self.category == "fuel" else CARBON_COEFF_ELEC
        return self.consumption(speed, variance, load_ratio) / 100 * distance_km * coeff

    def carbon_cost(self, distance_km: float, speed: float, variance: float, load_ratio: float) -> float:
        """碳排放对应的货币成本期望值（元）。"""
        return self.carbon_emission(distance_km, speed, variance, load_ratio) * CARBON_PRICE

    def banned_in_green_zone(self, minute_from_8: float) -> bool:
        """
        问题 2：08:00–16:00 禁止燃油车进入绿色配送区。
        minute_from_8 为当前时刻（自 08:00 起分钟数）。
        """
        if self.category != "fuel":
            return False
        return GREEN_ZONE_BAN_START <= minute_from_8 < GREEN_ZONE_BAN_END

    def __repr__(self) -> str:
        return (
            f"VehicleType({self.type_id}, {self.category}, "
            f"{self.max_weight}kg/{self.max_volume}m³, ×{self.fleet_count})"
        )


# 五种车型，构成车辆类型池
VEHICLE_TYPES: Dict[str, VehicleType] = {
    "O1": VehicleType("O1", "fuel",     3000, 13.5, 60, 0.40),
    "O2": VehicleType("O2", "fuel",     1500, 10.8, 50, 0.40),
    "O3": VehicleType("O3", "fuel",     1250,  6.5, 50, 0.40),
    "E1": VehicleType("E1", "electric", 3000, 15.0, 10, 0.35),
    "E2": VehicleType("E2", "electric", 1250,  8.5, 15, 0.35),
}

# 燃油车集合 O，新能源车集合 E
FUEL_TYPES     = {k: v for k, v in VEHICLE_TYPES.items() if v.category == "fuel"}
ELECTRIC_TYPES = {k: v for k, v in VEHICLE_TYPES.items() if v.category == "electric"}

# 全车队中单车最大载重与容积上限（用于判断是否需要多次配送）
MAX_SINGLE_WEIGHT = max(v.max_weight for v in VEHICLE_TYPES.values())   # 3000 kg
MAX_SINGLE_VOLUME = max(v.max_volume for v in VEHICLE_TYPES.values())   # 15.0 m³


# ══════════════════════════════════════════════════════════════════════════════
# 四、车辆实例（用于建模时的 0/1 使用变量）
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class VehicleInstance:
    """单辆具体车辆，参与路径分配。"""
    vehicle_id:   int
    type_id:      str
    vehicle_type: VehicleType
    used:         int = 0   # 0-未使用, 1-已使用

    def __repr__(self) -> str:
        return f"Vehicle({self.vehicle_id}, {self.type_id}, used={self.used})"


def create_full_fleet() -> List[VehicleInstance]:
    """根据 VEHICLE_TYPES 中的 fleet_count 生成所有车辆实例（初始全部未使用）。"""
    fleet = []
    vid = 1
    for type_id, vt in VEHICLE_TYPES.items():
        for _ in range(vt.fleet_count):
            fleet.append(VehicleInstance(vid, type_id, vt, used=0))
            vid += 1
    return fleet


# ══════════════════════════════════════════════════════════════════════════════
# 五、节点定义：配送中心与客户
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class Depot:
    """节点 0：配送中心。"""
    node_id: int   = 0
    x:       float = 0.0
    y:       float = 0.0

    def __repr__(self) -> str:
        return f"Depot(id={self.node_id}, pos=({self.x:.2f}, {self.y:.2f}))"


@dataclass
class Customer:
    """
    节点 i ∈ N：客户节点。
    """

    node_id:       int
    x:             float
    y:             float
    demand_weight: float
    demand_volume: float
    order_count:   int
    tw_start:      int          # 自 08:00 起分钟数
    tw_end:        int          # 自 08:00 起分钟数
    service_time:  int   = SERVICE_TIME
    wait_rate:     float = WAIT_RATE
    late_rate:     float = LATE_RATE

    # 推导属性，不参与构造
    dist_to_center: float = field(init=False)
    in_green_zone:  bool  = field(init=False)
    min_trips:      int   = field(init=False)

    def __post_init__(self) -> None:
        self.dist_to_center = math.sqrt(self.x ** 2 + self.y ** 2)
        self.in_green_zone  = self.dist_to_center <= GREEN_ZONE_RADIUS
        self.min_trips = max(
            math.ceil(self.demand_weight / MAX_SINGLE_WEIGHT),
            math.ceil(self.demand_volume / MAX_SINGLE_VOLUME),
        )

    def time_window_cost(self, arrival: float) -> float:
        """时间窗惩罚成本。"""
        if arrival < self.tw_start:
            return (self.tw_start - arrival) * self.wait_rate
        if arrival > self.tw_end:
            return (arrival - self.tw_end) * self.late_rate
        return 0.0

    def __repr__(self) -> str:
        zone = "绿色区内" if self.in_green_zone else "绿色区外"
        return (
            f"Customer(id={self.node_id}, {zone}, "
            f"w={self.demand_weight:.1f}kg, v={self.demand_volume:.3f}m3, "
            f"tw=[{self.tw_start}, {self.tw_end}]min, "
            f"orders={self.order_count}, min_trips={self.min_trips})"
        )


# ══════════════════════════════════════════════════════════════════════════════
# 六、配送网络（支持虚拟客户）
# ══════════════════════════════════════════════════════════════════════════════

class Network:
    """
    加载附件数据，构建配送网络 G = (V, A)。
    """

    def __init__(self, data_dir: Path) -> None:
        self.depot:       Depot                = Depot()
        self.customers:   Dict[int, Customer]  = {}
        self.dist_matrix: pd.DataFrame         = pd.DataFrame()
        self.virtual_to_original: Dict[int, int] = {}  # 虚拟客户ID → 原始客户ID
        self._load(data_dir)

    @staticmethod
    def _detect_files(data_dir: Path):
        """自动识别附件目录中的四个数据文件。"""
        order_fp = coord_fp = window_fp = dist_fp = None
        for fp in sorted(data_dir.glob("*.xlsx")):
            cols = set(pd.read_excel(fp, nrows=3).columns.astype(str))
            if "订单编号" in cols and "目标客户编号" in cols:
                order_fp = fp
            elif "类型" in cols and "X (km)" in cols:
                coord_fp = fp
            elif "开始时间" in cols and "结束时间" in cols:
                window_fp = fp
            else:
                dist_fp = fp
        if not all([order_fp, coord_fp, window_fp, dist_fp]):
            raise FileNotFoundError("附件目录下未能识别全部4个数据文件。")
        return order_fp, coord_fp, window_fp, dist_fp

    def _load(self, data_dir: Path) -> None:
        """加载所有数据文件并构建网络。"""
        order_fp, coord_fp, window_fp, dist_fp = self._detect_files(data_dir)

        dist_raw = pd.read_excel(dist_fp, index_col=0)
        dist_raw.index   = dist_raw.index.astype(int)
        dist_raw.columns = dist_raw.columns.astype(int)
        self.dist_matrix = dist_raw

        orders = pd.read_excel(order_fp).dropna(
            subset=["订单编号", "重量", "体积", "目标客户编号"]
        ).copy()
        orders["目标客户编号"] = orders["目标客户编号"].astype(int)
        demand = orders.groupby("目标客户编号").agg(
            demand_weight=("重量",    "sum"),
            demand_volume=("体积",    "sum"),
            order_count  =("订单编号", "count"),
        )

        def _to_minute(time_val) -> int:
            if isinstance(time_val, str):
                t = pd.to_datetime(time_val, format="%H:%M")
            else:
                t = pd.to_datetime(str(time_val))
            return t.hour * 60 + t.minute - BASE_MINUTE

        windows = pd.read_excel(window_fp)
        windows["客户编号"] = windows["客户编号"].astype(int)
        windows["tw_start"] = windows["开始时间"].apply(_to_minute)
        windows["tw_end"]   = windows["结束时间"].apply(_to_minute)
        tw = windows.set_index("客户编号")[["tw_start", "tw_end"]].to_dict("index")

        coords = pd.read_excel(coord_fp)
        depot_row = coords[coords["类型"] == "配送中心"].iloc[0]
        self.depot = Depot(
            node_id=0,
            x=float(depot_row["X (km)"]),
            y=float(depot_row["Y (km)"]),
        )

        for _, row in coords[coords["类型"] != "配送中心"].iterrows():
            cid = int(row["ID"])
            if cid not in demand.index:
                continue
            window = tw.get(cid, {"tw_start": 0, "tw_end": 9999})
            self.customers[cid] = Customer(
                node_id       = cid,
                x             = float(row["X (km)"]),
                y             = float(row["Y (km)"]),
                demand_weight = float(demand.loc[cid, "demand_weight"]),
                demand_volume = float(demand.loc[cid, "demand_volume"]),
                order_count   = int(demand.loc[cid, "order_count"]),
                tw_start      = window["tw_start"],
                tw_end        = window["tw_end"],
            )

    @property
    def node_ids(self) -> List[int]:
        return [0] + sorted(self.customers.keys())

    def distance(self, i: int, j: int) -> float:
        """节点 i → j 的道路距离（km）。支持虚拟客户映射。"""
        real_i = self.virtual_to_original.get(i, i)
        real_j = self.virtual_to_original.get(j, j)
        return float(self.dist_matrix.loc[real_i, real_j])

    def travel_info(
        self,
        i: int,
        j: int,
        depart_minute: float,
        vehicle_type: VehicleType,
        load_ratio: float,
    ) -> Tuple[float, float, float]:
        """
        带缓存的精确分段计算。将 depart_minute 取整到 0.1 分钟以提高缓存命中率。
        """
        # 1. 基础检查
        D = self.distance(i, j)
        if D < 1e-7:
            return 0.0, 0.0, 0.0

        # 2. 构造缓存键 (忽略 load_ratio，先计算基础能耗)
        # load_ratio 对时间无影响，对能耗是线性修正
        t_key = round(depart_minute, 1)
        cache_key = (i, j, t_key, vehicle_type.category)
        
        if not hasattr(self, '_travel_cache'):
            self._travel_cache = {}
        
        if cache_key in self._travel_cache:
            base_t, base_e, base_c = self._travel_cache[cache_key]
            # 根据当前的 load_ratio 修正能耗和碳排
            # 修正因子: (1 + load_factor * load_ratio)
            factor = (1.0 + vehicle_type.load_factor * load_ratio)
            return base_t, base_e * factor, base_c * factor

        # 3. 缓存未命中，执行计算 (计算 load_ratio=0 的基础值)
        d_remaining = D
        current_time = depart_minute
        total_time = 0.0
        total_e_base = 0.0
        total_c_base = 0.0

        while d_remaining > 1e-6:
            period = get_traffic_period(current_time)
            v_mean = get_period_speed(period)
            v_var = get_period_variance(period)
            period_end = get_period_end(current_time)

            if period_end == float('inf'):
                time_in_this_leg = d_remaining / v_mean * 60.0
            else:
                remain_time = max(0.0, period_end - current_time)
                d_possible = v_mean * remain_time / 60.0
                if d_possible >= d_remaining:
                    time_in_this_leg = d_remaining / v_mean * 60.0
                else:
                    time_in_this_leg = remain_time

            dist_this_leg = v_mean * (time_in_this_leg / 60.0)
            if dist_this_leg > d_remaining: dist_this_leg = d_remaining

            # 计算 load_ratio=0 的基础成本
            total_e_base += vehicle_type.energy_cost(dist_this_leg, v_mean, v_var, 0.0)
            total_c_base += vehicle_type.carbon_cost(dist_this_leg, v_mean, v_var, 0.0)

            d_remaining -= dist_this_leg
            total_time += time_in_this_leg
            if period_end != float('inf') and abs(current_time + time_in_this_leg - period_end) < 1e-9:
                current_time = period_end
            else:
                current_time += time_in_this_leg
            if time_in_this_leg < 1e-10: break

        # 4. 存入缓存并返回
        # 为了防止缓存无限增长，简单的清理策略
        if len(self._travel_cache) > 20000:
            self._travel_cache.clear()
            
        self._travel_cache[cache_key] = (total_time, total_e_base, total_c_base)
        factor = (1.0 + vehicle_type.load_factor * load_ratio)
        return total_time, total_e_base * factor, total_c_base * factor

    def travel_time(self, i: int, j: int, depart_minute: float) -> float:
        vt = VEHICLE_TYPES["O1"]
        t, _, _ = self.travel_info(i, j, depart_minute, vt, 0.0)
        return t

    def green_zone_customers(self) -> List[int]:
        return sorted(cid for cid, c in self.customers.items() if c.in_green_zone)

    def normal_customers(self) -> List[int]:
        return sorted(cid for cid, c in self.customers.items() if not c.in_green_zone)

    def overload_customers(self) -> List[int]:
        return sorted(cid for cid, c in self.customers.items() if c.min_trips > 1)

    def summary(self) -> None:
        over = self.overload_customers()
        only_w = [
            c for cid in over
            for c in [self.customers[cid]]
            if math.ceil(c.demand_weight / MAX_SINGLE_WEIGHT) > 1
            and math.ceil(c.demand_volume / MAX_SINGLE_VOLUME) <= 1
        ]
        both = [
            c for cid in over
            for c in [self.customers[cid]]
            if math.ceil(c.demand_weight / MAX_SINGLE_WEIGHT) > 1
            and math.ceil(c.demand_volume / MAX_SINGLE_VOLUME) > 1
        ]
        print("=" * 60)
        print("  配送网络摘要")
        print("=" * 60)
        print(f"  配送中心：节点 {self.depot.node_id}  "
              f"坐标 ({self.depot.x:.2f}, {self.depot.y:.2f})")
        print(f"  客户节点总数    : {len(self.customers)}")
        print(f"  绿色区内客户    : {len(self.green_zone_customers())} 个")
        print(f"  绿色区外客户    : {len(self.normal_customers())} 个")
        print(f"  需多次配送客户  : {len(over)} 个")
        print(f"    ├ 仅重量超限  : {len(only_w)} 个")
        print(f"    └ 重量+体积均超: {len(both)} 个")
        print(f"  距离矩阵规模    : {self.dist_matrix.shape}")
        print("-" * 60)
        print("  车辆类型池")
        for vt in VEHICLE_TYPES.values():
            print(f"    {vt.type_id}  {vt.category:<9}  "
                  f"{int(vt.max_weight):>5} kg  {vt.max_volume:>5.1f} m3  "
                  f"x{vt.fleet_count}")
        print("=" * 60)