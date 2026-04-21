
---

## `curve_fit` 是什么？

它是一个**曲线拟合工具**，用最小二乘法把数据拟合到你指定的任意函数形式。

核心优势：**可以拟合任意形式的函数**，不限于多项式，还能给出参数的误差估计。但是这个函数还是要**自己来设计**

---

## 基本用法

```python
from scipy.optimize import curve_fit

# 语法
popt, pcov = curve_fit(func, xdata, ydata, p0=None)
```

**参数说明**：
| 参数 | 说明 |
|------|------|
| `func` | 你定义的拟合函数，第一个参数是x，后面是待拟合参数 |
| `xdata` | 自变量数据 |
| `ydata` | 因变量数据 |
| `p0` | 参数初始猜测值（可选，不填默认全1） |

**返回值**：
| 返回 | 说明 |
|------|------|
| `popt` | 拟合出的最优参数值数组 |
| `pcov` | 参数的协方差矩阵，对角线是方差 |

---

## 实际例子

### 1. 线性拟合 `y = kx + b`

```python
def linear_func(x, k, b):
    return k * x + b

popt, pcov = curve_fit(linear_func, x_data, y_data)
k, b = popt  # 拟合结果
```

### 2. 指数拟合 `y = a * e^(bx) + c`

```python
def exp_func(x, a, b, c):
    return a * np.exp(b * x) + c

popt, pcov = curve_fit(exp_func, x_data, y_data)
a, b, c = popt
```

### 3. 自定义复杂函数

```python
# 高斯函数
def gaussian(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))

popt, pcov = curve_fit(gaussian, x_data, y_data, p0=[1, 0, 1])  # 给初始值很重要
```

---

## 误差估计怎么算？

```python
popt, pcov = curve_fit(func, x_data, y_data)

# 参数标准差
p_std = np.sqrt(np.diag(pcov))

# 95%置信区间（1.96倍标准差）
lower = popt - 1.96 * p_std
upper = popt + 1.96 * p_std
```

---

## 实际跑一下你的代码