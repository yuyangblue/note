# NumPy 随机数生成教程

## 一、基础随机数

### 1.1 均匀分布 [0, 1)

```python
import numpy as np

# 生成一个随机数
x = np.random.rand()
print(x)  # 0.548...

# 生成指定形状的数组
arr = np.random.rand(3, 4)  # 3行4列
print(arr.shape)  # (3, 4)

# 生成一维数组
arr1d = np.random.rand(10)  # 10个随机数
```

### 1.2 标准正态分布 N(0, 1)

```python
# 标准正态分布：均值0，标准差1
x = np.random.randn()

# 生成数组
arr = np.random.randn(3, 4)  # 3行4列
```

---

## 二、常用分布

### 2.1 均匀分布整数

```python
# randint(low, high, size)
# 生成 [low, high) 范围内的整数

# 一个随机整数 [0, 10)
x = np.random.randint(0, 10)

# 指定形状
arr = np.random.randint(0, 100, size=(3, 4))

# 只指定上限，默认下限为0
arr = np.random.randint(10, size=5)  # [0, 10) 的5个整数
```

### 2.2 正态分布

```python
# normal(loc, scale, size)
# loc: 均值
# scale: 标准差

# 标准正态分布 N(0, 1)
x = np.random.normal(0, 1)

# 均值5，标准差2
arr = np.random.normal(loc=5, scale=2, size=1000)

# 验证
print(f"均值: {arr.mean():.2f}")    # 接近5
print(f"标准差: {arr.std():.2f}")    # 接近2
```

### 2.3 均匀分布

```python
# uniform(low, high, size)
# 生成 [low, high) 范围内的均匀分布

arr = np.random.uniform(0, 10, size=5)
# [3.42, 7.18, 2.56, 9.01, 4.33]
```

---

## 三、随机抽样

### 3.1 从数组中随机选择

```python
arr = np.array([10, 20, 30, 40, 50])

# 随机选一个
x = np.random.choice(arr)

# 随机选多个（可重复）
choices = np.random.choice(arr, size=3)

# 不重复抽样
choices = np.random.choice(arr, size=3, replace=False)

# 按概率抽样
choices = np.random.choice(arr, size=3, p=[0.1, 0.1, 0.1, 0.3, 0.4])
# 40和50被抽中的概率更大
```

### 3.2 从范围中抽样

```python
# 等价于 np.random.randint，但更灵活
choices = np.random.choice(10, size=5)  # 从 [0,1,...,9] 中选5个
```

---

## 四、随机排列

### 4.1 打乱顺序

```python
arr = np.array([1, 2, 3, 4, 5])

# 原地打乱（修改原数组）
np.random.shuffle(arr)
print(arr)  # [3, 1, 5, 2, 4]
```

### 4.2 返回打乱后的副本

```python
arr = np.array([1, 2, 3, 4, 5])

# 返回新数组，原数组不变
shuffled = np.random.permutation(arr)
print(arr)       # [1, 2, 3, 4, 5] 不变
print(shuffled)  # [4, 1, 5, 2, 3]
```

---

## 五、设置随机种子

```python
# 设置随机种子，保证结果可复现
np.random.seed(42)

print(np.random.rand(3))  # 每次运行都一样
# [0.37454012, 0.95071431, 0.73199394]
```

**重要**：在机器学习、科学计算中，设置种子可以保证实验可复现。

---

## 六、其他分布

### 6.1 二项分布

```python
# binomial(n, p, size)
# n: 试验次数
# p: 成功概率

# 抛10次硬币，正面朝上的次数
x = np.random.binomial(n=10, p=0.5, size=1000)
print(f"平均正面次数: {x.mean()}")  # 接近5
```

### 6.2 泊松分布

```python
# poisson(lam, size)
# lam: 期望值

# 单位时间内事件发生的次数
x = np.random.poisson(lam=5, size=1000)
```

### 6.3 指数分布

```python
# exponential(scale, size)
# scale: 1/λ，即均值的倒数

x = np.random.exponential(scale=2, size=1000)
```

### 6.4 卡方分布

```python
# chisquare(df, size)
# df: 自由度

x = np.random.chisquare(df=3, size=1000)
```

### 6.5 Beta分布

```python
# beta(a, b, size)

x = np.random.beta(a=2, b=5, size=1000)  # 值在 [0, 1] 之间
```

---

## 七、速查表

| 函数 | 分布 | 范围/参数 |
|------|------|-----------|
| `rand(d0, d1, ...)` | 均匀分布 | [0, 1) |
| `randn(d0, d1, ...)` | 标准正态 | N(0, 1) |
| `randint(low, high, size)` | 整数均匀 | [low, high) |
| `uniform(low, high, size)` | 均匀分布 | [low, high) |
| `normal(loc, scale, size)` | 正态分布 | N(loc, scale²) |
| `choice(arr, size, replace, p)` | 随机抽样 | 按概率p |
| `shuffle(arr)` | 原地打乱 | 修改原数组 |
| `permutation(arr)` | 返回打乱副本 | 不修改原数组 |
| `seed(n)` | 设置种子 | 可复现 |
| `binomial(n, p, size)` | 二项分布 | n次试验，成功概率p |
| `poisson(lam, size)` | 泊松分布 | 期望λ |
| `exponential(scale, size)` | 指数分布 | 均值scale |
| `chisquare(df, size)` | 卡方分布 | 自由度df |
| `beta(a, b, size)` | Beta分布 | 参数a, b |

---

## 八、常用技巧

### 8.1 生成指定范围的随机数

```python
# 方法1：线性变换
arr = np.random.rand(100) * 10 + 5  # [5, 15)

# 方法2：直接用 uniform
arr = np.random.uniform(5, 15, 100)
```

### 8.2 生成随机矩阵

```python
# 3x4 矩阵，元素在 [0, 10)
matrix = np.random.randint(0, 10, size=(3, 4))

# 3x4 矩阵，标准正态分布
matrix = np.random.randn(3, 4)
```

### 8.3 随机采样索引

```python
indices = np.random.choice(100, size=10, replace=False)
# 从 0-99 中不重复抽取10个索引
```

### 8.4 随机打乱数据集

```python
X = np.random.rand(100, 5)  # 100个样本，5个特征
y = np.random.randint(0, 2, 100)  # 100个标签

# 打乱数据
indices = np.random.permutation(100)
X_shuffled = X[indices]
y_shuffled = y[indices]
```

---

## 九、完整示例

```python
import numpy as np
import matplotlib.pyplot as plt

# 设置种子
np.random.seed(42)

# 生成三种分布的数据
data1 = np.random.normal(0, 1, 1000)      # 标准正态
data2 = np.random.uniform(-3, 3, 1000)    # 均匀分布
data3 = np.random.exponential(1, 1000)    # 指数分布

# 可视化
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(data1, bins=30, alpha=0.7, color='blue')
plt.title('Normal(0, 1)')

plt.subplot(1, 3, 2)
plt.hist(data2, bins=30, alpha=0.7, color='green')
plt.title('Uniform(-3, 3)')

plt.subplot(1, 3, 3)
plt.hist(data3, bins=30, alpha=0.7, color='red')
plt.title('Exponential(1)')

plt.tight_layout()
plt.show()
```

---

**总结**：
- `rand` / `randn` 最常用，记住形状参数即可
- `randint` 生成整数，注意是 `[low, high)`
- `normal` 指定均值和标准差
- `choice` 用于抽样
- `seed` 保证可复现
