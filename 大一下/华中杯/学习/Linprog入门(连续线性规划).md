相比于**PuLp** ，linporg只处理连续变量，即**连续线性规划**
### **`scipy.optimize.linprog` 基础调用**

标准形式：最小化 c^T·x，满足 A_ub·x ≤ b_ub, A_eq·x = b_eq, bounds
```python
from scipy.optimize import linprog

# 标准形式：最小化 c^T·x，满足 A_ub·x ≤ b_ub, A_eq·x = b_eq, bounds
res = linprog(
    c,                # 目标函数系数向量（若为最大化问题，取负号）
    A_ub=A_ub,        # 不等式约束系数矩阵（≤）
    b_ub=b_ub,        # 不等式约束右侧向量
    A_eq=A_eq,        # 等式约束系数矩阵（=）
    b_eq=b_eq,        # 等式约束右侧向量
    bounds=bounds,    # 变量上下界，如 [(0, None), (0, 20)]
    method='highs'    # 推荐使用 'highs'（默认）
)
```

**关键参数解析**

- `c`：目标函数系数。若要求 **最大化**，需传入 `-c`（例如：`c = [-40, -30]`）。
- `A_ub`, `b_ub`：不等式约束。每行对应一个 `≤` 约束，例如 `2x₁ + 4x₂ ≤ 200` 写作 `[[2, 4]]` 和 `[200]`。
- `A_eq`, `b_eq`：等式约束（若无，可不传或传 `None`）。
- `bounds`：每个变量的 (min, max) 元组列表。`None` 表示无界（正无穷）。
- `method`：求解器。`'highs'` 是目前最稳定高效的选项。

### **连续版本案例（Day 2 问题的连续化）**

将 Day 2 的三产品问题**去掉整数约束**，用 `linprog` 求解：

```python
from scipy.optimize import linprog
import numpy as np

# 目标函数系数（最大化总利润 → 取负号）
c = [-40, -30, -25]  # 对应 x1, x2, x3 的利润系数

# 不等式约束 A_ub·x ≤ b_ub
A_ub = [
    [2, 4, 3],   # 资源1消耗
    [3, 2, 2],   # 资源2消耗
    [1, 0, 0],   # x1 ≤ 30
    [0, 1, 0]    # x2 ≤ 10
]
b_ub = [200, 180, 30, 10]

# 等式约束 A_eq·x = b_eq（本例无）

# 变量下界（非负）
bounds = [(0, None), (0, None), (0, None)]

# 求解
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

if res.success:
    print("连续最优解:")
    print(f"x1 = {res.x[0]:.2f}, x2 = {res.x[1]:.2f}, x3 = {res.x[2]:.2f}")
    print(f"最大利润 = {-res.fun:.2f}")  # 目标函数取负，需反转为正
else:
    print("求解失败:", res.message)
```