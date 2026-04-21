**`numpy.polyfit` 是 NumPy 库中用于**多项式拟合**的核心函数**，通过最小二乘法将一组数据点拟合成指定次数的多项式曲线。这是数学建模中数据拟合、趋势分析的常用工具。

### **函数语法与参数详解**

```python
numpy.polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False)
```

表格

|参数|类型|作用|示例|
|---|---|---|---|
|`x`|一维数组|自变量数据点|`[0, 1, 2, 3, 4]`|
|`y`|一维数组|因变量数据点（与 `x` 等长）|`[1.2, 2.8, 6.1, 10.5, 16.3]`|
|`deg`|整数|拟合多项式的**次数**|`1`（线性拟合）、`2`（二次拟合）|
|`rcond`|浮点数（可选）|拟合过程中的条件数阈值，默认 `None`|`1e-15`|
|`full`|布尔值（可选）|是否返回完整诊断信息，默认 `False`|`True`|
|`w`|一维数组（可选）|权重数组（用于加权最小二乘）|`[1, 0.5, 1, 0.5, 1]`|
|`cov`|布尔值（可选）|是否返回协方差矩阵，默认 `False`|`True`|

**返回值**（当 `full=False`, `cov=False` 时）：

- `p`：多项式系数数组，按**降幂排列**（如`[` $\mathbf{a_n, a_{n-1}, …, a_0 }$`]`对应 
### **典型使用流程（三步法）**

**1. 数据准备与拟合**

```python
# 方法1：线性最小二乘法拟合
import numpy as np

# 一次多项式拟合（degree=1）
coeff_linear = np.polyfit(x_data, y_data, deg=1)
k_fit_linear = coeff_linear[0]  # 斜率
b_fit_linear = coeff_linear[1]  # 截距

print("="*60)
print("方法1：线性最小二乘法拟合结果")
print("="*60)
print(f"拟合劲度系数 k = {k_fit_linear:.4f} mm/g")
print(f"拟合初始伸长量 b = {b_fit_linear:.4f} mm")
print(f"真实参数: k_true = {k_true:.4f}, b_true = {b_true:.4f}")
print(f"绝对误差: Δk = {abs(k_fit_linear - k_true):.4f}, Δb = {abs(b_fit_linear - b_true):.4f}")

# 生成拟合直线
x_fit = np.linspace(0, 80, 100)
y_fit_linear = np.polyval(coeff_linear, x_fit)
```


```
============================================================
方法1：线性最小二乘法拟合结果
============================================================
拟合劲度系数 k = 2.4974 mm/g
拟合初始伸长量 b = 5.7605 mm
真实参数: k_true = 2.5000, b_true = 5.0000
绝对误差: Δk = 0.0026, Δb = 0.7605

拟合方程: y = 2.4974x + 5.7605
决定系数 R² = 0.999719

```