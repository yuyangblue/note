Numpy 是 Python 中用于数值计算的核心库，主要用来处理数组（ndarray），以下是最常用的基础用法：

### 一、核心：创建数组（ndarray）

```python
import numpy as np  # 导入Numpy（约定简写为np）

# 1. 从列表/元组创建
arr1 = np.array([1, 2, 3, 4])  # 一维数组
arr2 = np.array([[1,2], [3,4]])  # 二维数组（矩阵）

# 2. 快速创建特殊数组
arr_zero = np.zeros((2,3))  # 全0数组，形状(2,3)
arr_one = np.ones((3,2))    # 全1数组
arr_eye = np.eye(3)         # 3×3单位矩阵
arr_rand = np.random.rand(2,4)  # 0-1随机数数组
```

### 二、数组的基本操作

#### 1. 查看数组属性

```python
arr = np.array([[1,2,3], [4,5,6]])
print(arr.shape)   # 形状：(2,3)
print(arr.dtype)   # 数据类型：int64
print(arr.ndim)    # 维度：2（二维数组）
print(arr.size)    # 元素总数：6
```

#### 2. 数组索引 / 切片

```python
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr[0, 1])    # 取第0行第1列元素：2
print(arr[1:3, :2]) # 取第1-2行、第0-1列：[[4,5], [7,8]]
```

#### 3. 数组变形

```python
arr = np.array([[1,2], [3,4], [5,6]])
arr_reshape = arr.reshape(2,3)  # 变形为2×3数组：[[1,2,3], [4,5,6]]
```

### 三、数值计算（核心功能）

#### 1. 基本运算（元素级）

```python
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + b)  # 逐元素加：[5,7,9]
print(a * 2)  # 逐元素乘：[2,4,6]
```

#### 2. 矩阵运算

```python
mat1 = np.array([[1,2], [3,4]])
mat2 = np.array([[5,6], [7,8]])
print(mat1 @ mat2)  # 矩阵乘：[[19,22], [43,50]]
print(np.dot(mat1, mat2))  # 和@等价
```

#### 3. 统计计算

```python
arr = np.array([[1,2,3], [4,5,6]])
print(arr.mean())   # 平均值：3.5
print(arr.sum(axis=0))  # 按列求和：[5,7,9]
print(arr.max(axis=1))  # 按行求最大值：[3,6]
```

### 四、广播机制（Numpy 特色）

当两个数组形状不完全匹配时，Numpy 会自动扩展数组以匹配形状（满足广播规则）：

```python
a = np.array([[1,2,3], [4,5,6]])  # 形状(2,3)
b = np.array([10, 20, 30])        # 形状(3,)
print(a + b)  # b自动扩展为(2,3)，结果：[[11,22,33], [14,25,36]]
```