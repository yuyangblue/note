
# Cholesky分解完整笔记

---

## 一、什么是Cholesky分解

对于一个**对称正定矩阵** $A$，可以分解成：

$$A = LL^T$$

其中：
- $L$ 是**下三角矩阵**（主对角线上方全为0）
- $L^T$ 是 $L$ 的转置（上三角矩阵）

---

## 二、适用条件

矩阵 $A$ 必须满足：

| 条件 | 说明 |
|------|------|
| **对称** | $A = A^T$，即 $a_{ij} = a_{ji}$ |
| **正定** | 所有特征值 $> 0$，或等价地 $\forall x \neq 0, x^TAx > 0$ |

---

## 三、推导过程

### 3.1 从矩阵乘法角度

设：
$$A = LL^T = \begin{bmatrix} l_{11} & 0 & 0 \\ l_{21} & l_{22} & 0 \\ l_{31} & l_{32} & l_{33} \end{bmatrix} \begin{bmatrix} l_{11} & l_{21} & l_{31} \\ 0 & l_{22} & l_{32} \\ 0 & 0 & l_{33} \end{bmatrix}$$

展开：
$$LL^T = \begin{bmatrix} l_{11}^2 & l_{11}l_{21} & l_{11}l_{31} \\ l_{21}l_{11} & l_{21}^2 + l_{22}^2 & l_{21}l_{31} + l_{22}l_{32} \\ l_{31}l_{11} & l_{31}l_{21} + l_{32}l_{22} & l_{31}^2 + l_{32}^2 + l_{33}^2 \end{bmatrix}$$

对比 $A$ 的元素，得到方程组：
$$\begin{cases} a_{11} = l_{11}^2 \\ a_{21} = l_{11}l_{21} \\ a_{22} = l_{21}^2 + l_{22}^2 \\ a_{31} = l_{11}l_{31} \\ a_{32} = l_{21}l_{31} + l_{22}l_{32} \\ a_{33} = l_{31}^2 + l_{32}^2 + l_{33}^2 \end{cases}$$

---

### 3.2 一般公式推导

对于 $n \times n$ 矩阵：

**对角元素**（$i = j$）：
$$a_{ii} = l_{i1}^2 + l_{i2}^2 + \cdots + l_{ii}^2 = \sum_{k=1}^{i} l_{ik}^2$$

解得：
$$l_{ii} = \sqrt{a_{ii} - \sum_{k=1}^{i-1} l_{ik}^2}$$

**非对角元素**（$i > j$）：
$$a_{ij} = \sum_{k=1}^{j} l_{ik}l_{jk} = l_{ij}l_{jj} + \sum_{k=1}^{j-1} l_{ik}l_{jk}$$

解得：
$$l_{ij} = \frac{1}{l_{jj}} \left( a_{ij} - \sum_{k=1}^{j-1} l_{ik}l_{jk} \right)$$

---

## 四、计算步骤（手算）

### 例题：分解矩阵 $A = \begin{bmatrix} 4 & 2 & 2 \\ 2 & 10 & 4 \\ 2 & 4 & 14 \end{bmatrix}$

**Step 1：计算第一列**

$$l_{11} = \sqrt{a_{11}} = \sqrt{4} = 2$$

$$l_{21} = \frac{a_{21}}{l_{11}} = \frac{2}{2} = 1$$

$$l_{31} = \frac{a_{31}}{l_{11}} = \frac{2}{2} = 1$$

**Step 2：计算第二列**

$$l_{22} = \sqrt{a_{22} - l_{21}^2} = \sqrt{10 - 1} = \sqrt{9} = 3$$

$$l_{32} = \frac{a_{32} - l_{31}l_{21}}{l_{22}} = \frac{4 - 1 \times 1}{3} = 1$$

**Step 3：计算第三列**

$$l_{33} = \sqrt{a_{33} - l_{31}^2 - l_{32}^2} = \sqrt{14 - 1 - 1} = \sqrt{12} = 2\sqrt{3}$$

**结果**：

$$L = \begin{bmatrix} 2 & 0 & 0 \\ 1 & 3 & 0 \\ 1 & 1 & 2\sqrt{3} \end{bmatrix}$$

**验证**：

$$LL^T = \begin{bmatrix} 2 & 0 & 0 \\ 1 & 3 & 0 \\ 1 & 1 & 2\sqrt{3} \end{bmatrix} \begin{bmatrix} 2 & 1 & 1 \\ 0 & 3 & 1 \\ 0 & 0 & 2\sqrt{3} \end{bmatrix} = \begin{bmatrix} 4 & 2 & 2 \\ 2 & 10 & 4 \\ 2 & 4 & 14 \end{bmatrix} = A \checkmark$$

---

## 五、Python实现

### 方法一：使用 NumPy（推荐）

```python
import numpy as np

# 对称正定矩阵
A = np.array([
    [4, 2, 2],
    [2, 10, 4],
    [2, 4, 14]
], dtype=float)

# Cholesky分解
L = np.linalg.cholesky(A)

print("L =\n", L)
print("\n验证 LL^T =\n", L @ L.T)
print("\n是否等于 A:", np.allclose(A, L @ L.T))
```

---

### 方法二：手动实现（理解原理）

```python
import numpy as np

def cholesky_decomposition(A):
    """
    手动实现Cholesky分解
    """
    n = A.shape[0]
    L = np.zeros((n, n))
    
    for i in range(n):
        # 计算对角元素
        sum_sq = sum(L[i, k]**2 for k in range(i))
        L[i, i] = np.sqrt(A[i, i] - sum_sq)
        
        # 计算非对角元素（i行以下的元素）
        for j in range(i + 1, n):
            sum_prod = sum(L[j, k] * L[i, k] for k in range(i))
            L[j, i] = (A[j, i] - sum_prod) / L[i, i]
    
    return L

# 测试
A = np.array([
    [4, 2, 2],
    [2, 10, 4],
    [2, 4, 14]
], dtype=float)

L = cholesky_decomposition(A)
print("L =\n", L)
```

---

### 方法三：带正定性检查

```python
def cholesky_safe(A):
    """
    带正定性检查的Cholesky分解
    """
    n = A.shape[0]
    L = np.zeros((n, n))
    
    for i in range(n):
        # 计算对角元素
        sum_sq = sum(L[i, k]**2 for k in range(i))
        diag = A[i, i] - sum_sq
        
        if diag <= 0:
            raise ValueError(f"矩阵不是正定的！第{i}个对角元素计算值为{diag}")
        
        L[i, i] = np.sqrt(diag)
        
        # 计算非对角元素
        for j in range(i + 1, n):
            sum_prod = sum(L[j, k] * L[i, k] for k in range(i))
            L[j, i] = (A[j, i] - sum_prod) / L[i, i]
    
    return L
```

---

## 六、图解计算过程

```
矩阵 A (3×3)                    下三角矩阵 L
┌─────────────────────┐        ┌─────────────────────┐
│ a₁₁  a₁₂  a₁₃      │        │ l₁₁   0    0       │
│ a₂₁  a₂₂  a₂₃      │   →    │ l₂₁  l₂₂   0       │
│ a₃₁  a₃₂  a₃₃      │        │ l₃₁  l₃₂  l₃₃     │
└─────────────────────┘        └─────────────────────┘

计算顺序（按列）：
┌─────────────────────────────────────────────────┐
│ 第1列: l₁₁ = √a₁₁                               │
│        l₂₁ = a₂₁ / l₁₁                          │
│        l₃₁ = a₃₁ / l₁₁                          │
├─────────────────────────────────────────────────┤
│ 第2列: l₂₂ = √(a₂₂ - l₂₁²)                     │
│        l₃₂ = (a₃₂ - l₃₁·l₂₁) / l₂₂             │
├─────────────────────────────────────────────────┤
│ 第3列: l₃₃ = √(a₃₃ - l₃₁² - l₃₂²)              │
└─────────────────────────────────────────────────┘
```

---

## 七、为什么叫"平方根分解"

从 $A = LL^T$ 可以看出：

如果 $L$ 是对称的（$L = L^T$），则 $A = L^2$

即：**$L$ 是 $A$ 的"平方根"**

类比标量：
- $a = l \cdot l = l^2$ → $l = \sqrt{a}$
- 矩阵：$A = LL^T$ → $L$ 是 $A$ 的"矩阵平方根"

---

## 八、应用场景

### 8.1 求解线性方程组 $Ax = b$

```python
# 传统方法：直接求逆
x = np.linalg.inv(A) @ b  # 计算量大，数值不稳定

# Cholesky方法：更高效稳定
L = np.linalg.cholesky(A)

# 分解成两步：Ly = b, L^T x = y
y = np.linalg.solve(L, b)      # 前代（下三角）
x = np.linalg.solve(L.T, y)    # 回代（上三角）
```

**计算量对比**：

| 方法 | 计算量 |
|------|--------|
| 直接求逆 | $O(n^3)$ |
| Cholesky + 前代回代 | $\frac{1}{3}n^3 + O(n^2)$ |

---

### 8.2 生成相关随机变量

```python
import numpy as np

# 目标协方差矩阵
Sigma = np.array([
    [1.0, 0.6, 0.3],
    [0.6, 1.0, 0.4],
    [0.3, 0.4, 1.0]
])

# Cholesky分解
L = np.linalg.cholesky(Sigma)

# 生成独立正态随机变量
Z = np.random.randn(10000, 3)

# 转换成相关的
X = Z @ L.T  # Cov(X) = L @ I @ L^T = LL^T = Sigma

# 验证协方差
print("目标协方差:\n", Sigma)
print("实际协方差:\n", np.cov(X.T))
```

---

### 8.3 蒙特卡洛模拟

```python
# 期权定价中的相关性处理
# 假设多个资产价格有相关性，用Cholesky分解生成相关路径
```

---

## 九、与其他分解的对比

| 分解 | 适用矩阵 | 分解形式 | 主要应用 |
|------|----------|----------|----------|
| **Cholesky** | 对称正定 | $A = LL^T$ | 线性方程组、协方差模拟 |
| **LU分解** | 方阵（非奇异） | $A = LU$ | 线性方程组、行列式 |
| **QR分解** | 任意矩阵 | $A = QR$ | 最小二乘、特征值 |
| **SVD** | 任意矩阵 | $A = U\Sigma V^T$ | 降维、推荐、压缩 |
| **特征值分解** | 方阵 | $A = Q\Lambda Q^{-1}$ | 主成分分析、稳定性分析 |

---

## 十、常见问题

### Q1：为什么只能用于对称正定矩阵？

**答**：因为只有正定矩阵才能保证所有对角元素 $l_{ii} = \sqrt{a_{ii} - \sum l_{ik}^2} > 0$，根号内为正。

### Q2：如果矩阵不是正定的怎么办？

**答**：用 **LDL分解**（无需开方）：
$$A = LDL^T$$
其中 $L$ 是单位下三角，$D$ 是对角矩阵。

### Q3：Cholesky分解唯一吗？

**答**：唯一（如果要求 $L$ 的对角元素为正）。

---

## 十一、总结

```
Cholesky分解的核心思想
┌──────────────────────────────────────────────────────┐
│                                                      │
│   对称正定矩阵 A  ──分解──>  下三角矩阵 L             │
│                                                      │
│   A = LL^T                                           │
│       ↓                                              │
│   把 A 拆成"平方根"的形式                             │
│                                                      │
│   优点：                                              │
│   ① 计算量小（比LU分解快一倍）                        │
│   ② 数值稳定                                         │
│   ③ 存储量小（只需存储L，是A的一半）                  │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

好的，笔记整理完毕！核心就是：**对称正定矩阵可以分解成下三角矩阵乘它的转置，按列逐个算就完事儿了** 🎯