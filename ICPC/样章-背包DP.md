# 样章 - 背包DP

> ICPC 竞赛笔记 · 动态规划入门专题

---

## 一、0/1 背包

**模型描述：** 有 $N$ 件物品和一个容量为 $V$ 的背包。每件物品只能选**0次或1次**，物品 $i$ 体积为 $w_i$，价值为 $v_i$。求总价值最大。

**状态定义：** $dp[j]$ 表示容量为 $j$ 的背包能装的最大价值。

**转移方程：**

$$
dp[j] = \max(dp[j],\; dp[j - w] + v) \quad (j \text{ 倒序枚举})
$$

**关键：** 内层循环倒序，保证每个物品只取一次。

### 模板代码

```python
def zero_one_knapsack(N, V, weights, values):
    """0/1 背包通用模板"""
    dp = [0] * (V + 1)
    for i in range(N):
        w, v = weights[i], values[i]
        for j in range(V, w - 1, -1):    # 倒序
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[V]
```

### 例题

#### P1048 [NOIP2005 普及组] 采药

| 题意 | 解法 |
|------|------|
| $T$ 时间采 $M$ 株药，每株采 $t_i$ 时间价值 $v_i$ | 裸 0/1 背包，$dp[T]$ 即为答案 |

```python
T, M = map(int, input().split())
dp = [0] * (T + 1)
for _ in range(M):
    t, v = map(int, input().split())
    for j in range(T, t - 1, -1):
        dp[j] = max(dp[j], dp[j - t] + v)
print(dp[T])
```

#### P1060 [NOIP2006 普及组] 开心的金明

| 题意 | 解法 |
|------|------|
| $N$ 元预算买 $m$ 件物品，每件价格 $v$、重要度 $p$，价值 = $v \times p$ | 价值改为 $v \times p$ 的 0/1 背包 |

```python
N, m = map(int, input().split())
dp = [0] * (N + 1)
for _ in range(m):
    v, p = map(int, input().split())
    for j in range(N, v - 1, -1):
        dp[j] = max(dp[j], dp[j - v] + v * p)
print(dp[N])
```

---

## 二、完全背包

**模型描述：** 每件物品可以取**无限次**。

**转移方程：**

$$
dp[j] = \max(dp[j],\; dp[j - w] + v) \quad (j \text{ 正序枚举})
$$

**关键：** 内层循环正序，允许同一物品被反复选取。

### 模板代码

```python
def complete_knapsack(N, V, weights, values):
    """完全背包通用模板"""
    dp = [0] * (V + 1)
    for i in range(N):
        w, v = weights[i], values[i]
        for j in range(w, V + 1):        # 正序
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[V]
```

### 例题

#### P1616 疯狂的采药

| 题意 | 解法 |
|------|------|
| $t$ 时间采药，每种无限采，时间 $a_i$ 价值 $b_i$ | 裸完全背包 |

```python
t, m = map(int, input().split())
dp = [0] * (t + 1)
for _ in range(m):
    a, b = map(int, input().split())
    for j in range(a, t + 1):
        dp[j] = max(dp[j], dp[j - a] + b)
print(dp[t])
```

---

## 三、多重背包（二进制优化）

**模型描述：** 第 $i$ 种物品有 $c_i$ 件，每件体积 $w_i$、价值 $v_i$。

**二进制优化思想：** 将 $c_i$ 件物品拆成 $\lceil \log_2 c_i \rceil$ 组（每组 1, 2, 4, …, 剩余件数），使每组 0/1 选或不选能组合出 $0 \ldots c_i$ 所有数量。然后跑 0/1 背包。

### 模板代码

```python
def multiple_knapsack(N, V, weights, values, counts):
    """多重背包（二进制优化）"""
    items = []  # (weight, value)
    for i in range(N):
        w, v, c = weights[i], values[i], counts[i]
        k = 1
        while k <= c:
            items.append((w * k, v * k))
            c -= k
            k <<= 1
        if c > 0:
            items.append((w * c, v * c))

    dp = [0] * (V + 1)
    for w, v in items:
        for j in range(V, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[V]
```

### 例题

#### P1776 宝物筛选

| 题意 | 解法 |
|------|------|
| $n$ 种宝物，每种有 $m_i$ 件，价值 $v_i$、重量 $w_i$，背包容 $W$ | 裸多重背包（二进制优化） |

```python
W, n = map(int, input().split())
items = []
for _ in range(n):
    v, w, m = map(int, input().split())
    k = 1
    while k <= m:
        items.append((w * k, v * k))
        m -= k
        k <<= 1
    if m > 0:
        items.append((w * m, v * m))

dp = [0] * (W + 1)
for w, v in items:
    for j in range(W, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)
print(dp[W])
```

---

## 四、实战要点速查表

| 背包类型 | 物品限制 | 内层循环 | 初始化 | 适用场景 |
|----------|----------|----------|--------|----------|
| **0/1 背包** | 每件 0/1 次 | 倒序 | $dp[0]=0$ | 选或不选类问题 |
| **完全背包** | 无限次 | 正序 | $dp[0]=0$ | 无限选取类问题 |
| **多重背包** | 每件 $c_i$ 次 | 倒序（拆后） | $dp[0]=0$ | 有限数量类问题 |
| **恰好装满** | — | 同对应背包 | $dp[0]=0,\;其他=-\infty$ | 凑额度、凑时间 |
| **最小化价值** | — | 同对应背包 | $dp[0]=0,\;其他=+\infty$ | 费用最小化 |
| **二维费用** | 两种容量 | 双层倒序 | $dp[0][0]=0$ | 同时限制时间+金钱 |
| **分组背包** | 每组至多选一个 | 组外倒序、组内正序 | $dp[0]=0$ | 类别互斥选择 |

### 常见技巧

1. **滚动数组** — 一维 $dp$ 数组替代二维，压缩空间
2. **恰好装满** — 初始化 $dp[0]=0$，其余 $-\infty$，最后检查 $dp[V]$
3. **至少达到** — 容量无上限时，将 $V$ 视为所需**最小值**，做完全背包
4. **方案数** — 把 $\max$ 换成 $+$，初始化 $dp[0]=1$
5. **输出方案** — 用 `choice` 数组记录转移来源，倒推路径

---

> **提示：** 本样章覆盖了背包 DP 三大基础模型。实战中先判断物品限制（0/1 / 无限 / 有限），再套对应模板即可快速解题。遇到数据范围大的多重背包，优先写二进制优化。
