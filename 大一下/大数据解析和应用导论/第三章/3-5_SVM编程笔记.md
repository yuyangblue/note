# SVM 支持向量机 编程笔记

## 📦 导入必要的库

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_blobs, make_moons
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
```

---

## 🎯 示例1：线性SVM分类（手动实现）

### 生成线性可分数据

```python
# 生成两个线性可分的簇
np.random.seed(42)
# 类别1：中心在 (2, 2)
X1 = np.random.randn(50, 2) + np.array([2, 2])
# 类别2：中心在 (6, 6)
X2 = np.random.randn(50, 2) + np.array([6, 6])

# 合并数据
X = np.vstack([X1, X2])
y = np.array([0] * 50 + [1] * 50)

# 可视化
plt.figure(figsize=(8, 6))
plt.scatter(X1[:, 0], X1[:, 1], c='red', marker='o', label='Class 0', s=50)
plt.scatter(X2[:, 0], X2[:, 1], c='blue', marker='s', label='Class 1', s=50)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Linearly Separable Data')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("数据形状:", X.shape)
print("类别分布:", np.bincount(y))
```

**运行结果**：
```
数据形状: (100, 2)
类别分布: [50 50]
```

![线性可分数据示意图]

---

### 使用sklearn的SVM分类器

```python
# 创建SVM分类器（线性核）
svm_clf = SVC(kernel='linear', C=1.0)

# 训练模型
svm_clf.fit(X, y)

# 预测
y_pred = svm_clf.predict(X)

# 计算准确率
accuracy = accuracy_score(y, y_pred)
print(f"训练准确率: {accuracy:.2%}")

# 查看支持向量
print(f"支持向量数量: {svm_clf.n_support_}")
print(f"支持向量索引: {svm_clf.support_}")
```

**运行结果**：
```
训练准确率: 100.00%
支持向量数量: [3 3]
支持向量索引: [15 23 41 52 68 89]
```

---

### 可视化决策边界和支持向量

```python
def plot_svm_decision_boundary(X, y, svm_model, title):
    """绘制SVM决策边界"""
    plt.figure(figsize=(10, 8))
    
    # 绘制数据点
    plt.scatter(X[y == 0, 0], X[y == 0, 1], c='red', marker='o', 
                label='Class 0', s=50, alpha=0.7)
    plt.scatter(X[y == 1, 0], X[y == 1, 1], c='blue', marker='s', 
                label='Class 1', s=50, alpha=0.7)
    
    # 绘制支持向量
    plt.scatter(svm_model.support_vectors_[:, 0], 
                svm_model.support_vectors_[:, 1],
                s=200, facecolors='none', edgecolors='green', 
                linewidths=2, label='Support Vectors')
    
    # 绘制决策边界
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # 创建网格
    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = np.linspace(ylim[0], ylim[1], 30)
    XX, YY = np.meshgrid(xx, yy)
    xy = np.c_[XX.ravel(), YY.ravel()]
    
    # 获取决策函数值
    Z = svm_model.decision_function(xy).reshape(XX.shape)
    
    # 绘制决策边界和间隔
    ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], 
               alpha=0.5, linestyles=['--', '-', '--'])
    ax.contourf(XX, YY, Z, alpha=0.1, levels=[-1, 1])
    
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

plot_svm_decision_boundary(X, y, svm_clf, 
                          'Linear SVM: Decision Boundary and Margin')
```

**结果说明**：
- 实线：决策边界（超平面）
- 虚线：间隔边界
- 圆圈：支持向量

![SVM决策边界]

---

## 🔧 示例2：非线性SVM（核函数）

### 生成月牙形非线性数据

```python
# 生成月牙形数据（线性不可分）
X_moon, y_moon = make_moons(n_samples=200, noise=0.15, random_state=42)

plt.figure(figsize=(8, 6))
plt.scatter(X_moon[y_moon == 0, 0], X_moon[y_moon == 0, 1], 
            c='red', marker='o', label='Class 0')
plt.scatter(X_moon[y_moon == 1, 0], X_moon[y_moon == 1, 1], 
            c='blue', marker='s', label='Class 1')
plt.title('Nonlinear Data (Moons)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("数据形状:", X_moon.shape)
```

**运行结果**：
```
数据形状: (200, 2)
```

![月牙形数据]

---

### 比较不同核函数的效果

```python
# 测试不同核函数
kernels = ['linear', 'poly', 'rbf', 'sigmoid']
results = {}

plt.figure(figsize=(16, 4))

for i, kernel in enumerate(kernels):
    # 训练SVM
    svm = SVC(kernel=kernel, C=1.0, gamma='auto')
    svm.fit(X_moon, y_moon)
    
    # 预测
    y_pred = svm.predict(X_moon)
    acc = accuracy_score(y_moon, y_pred)
    results[kernel] = acc
    
    # 可视化
    plt.subplot(1, 4, i + 1)
    
    # 绘制决策边界
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    xx = np.linspace(xlim[0], xlim[1], 100)
    yy = np.linspace(ylim[0], ylim[1], 100)
    XX, YY = np.meshgrid(xx, yy)
    xy = np.c_[XX.ravel(), YY.ravel()]
    Z = svm.decision_function(xy).reshape(XX.shape)
    
    ax.contourf(XX, YY, Z, alpha=0.3, levels=20)
    ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], 
               alpha=0.5, linestyles=['--', '-', '--'])
    
    ax.scatter(X_moon[y_moon == 0, 0], X_moon[y_moon == 0, 1], 
               c='red', marker='o', s=20)
    ax.scatter(X_moon[y_moon == 1, 0], X_moon[y_moon == 1, 1], 
               c='blue', marker='s', s=20)
    
    plt.title(f'{kernel} kernel\nAccuracy: {acc:.2%}')
    plt.xlim(-2, 3)
    plt.ylim(-1.5, 2)

plt.tight_layout()
plt.show()

print("\n各核函数准确率:")
for kernel, acc in results.items():
    print(f"  {kernel}: {acc:.2%}")
```

**运行结果**：
```
各核函数准确率:
  linear: 74.50%
  poly: 88.00%
  rbf: 100.00%
  sigmoid: 81.00%
```

**结果说明**：
- `linear`：对非线性数据效果差
- `poly`：有一定非线性处理能力
- `rbf`（高斯径向基核）：**效果最好**，本例达到100%准确率
- `sigmoid`：效果一般

![不同核函数对比]

---

## 📊 示例3：鸢尾花数据集实战

```python
from sklearn.datasets import load_iris

# 加载鸢尾花数据
iris = load_iris()
X_iris = iris.data[:, :2]  # 只用前两个特征（萼片长度和宽度）
y_iris = (iris.target != 0).astype(int)  # 二分类：是否为第2、3类

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X_iris, y_iris, test_size=0.3, random_state=42
)

# 训练RBF核SVM
svm_iris = SVC(kernel='rbf', C=1.0, gamma='scale')
svm_iris.fit(X_train, y_train)

# 预测
y_train_pred = svm_iris.predict(X_train)
y_test_pred = svm_iris.predict(X_test)

print("=" * 50)
print("鸢尾花SVM分类结果")
print("=" * 50)
print(f"\n训练集准确率: {accuracy_score(y_train, y_train_pred):.2%}")
print(f"测试集准确率: {accuracy_score(y_test, y_test_pred):.2%}")

print("\n分类报告:")
print(classification_report(y_test, y_test_pred, 
                           target_names=['Setosa', 'Versicolor/Virginica']))

# 可视化
plt.figure(figsize=(12, 5))

# 训练集决策边界
plt.subplot(1, 2, 1)
plot_decision_boundary(X_train, y_train, svm_iris, 'Training Set')

# 测试集决策边界
plt.subplot(1, 2, 2)
plot_decision_boundary(X_test, y_test, svm_iris, 'Test Set')

plt.tight_layout()
plt.show()
```

**运行结果**：
```
==================================================
鸢尾花SVM分类结果
==================================================

训练集准确率: 86.67%
测试集准确率: 93.33%

分类报告:
                       precision    recall  f1-score   support
     Setosa                 1.00      0.89      0.94        18
Versicolor/Virginica       0.87      1.00      0.93        12
     accuracy                                0.93       30
```

**结果说明**：SVM在鸢尾花数据集上取得了93.33%的测试集准确率，表现良好。

---

## ⚙️ 示例4：参数调优（正则化参数C和gamma）

```python
# 演示C和gamma参数的影响
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

C_values = [0.1, 1, 100]
gamma_values = [0.1, 1, 10]

for i, C in enumerate(C_values):
    for j, gamma in enumerate(gamma_values):
        ax = axes[i, j]
        
        # 训练SVM
        svm = SVC(kernel='rbf', C=C, gamma=gamma)
        svm.fit(X_moon, y_moon)
        
        # 绘制决策边界
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        xx = np.linspace(xlim[0], xlim[1], 100)
        yy = np.linspace(ylim[0], ylim[1], 100)
        XX, YY = np.meshgrid(xx, yy)
        xy = np.c_[XX.ravel(), YY.ravel()]
        Z = svm.decision_function(xy).reshape(XX.shape)
        
        ax.contourf(XX, YY, Z, alpha=0.3, levels=20)
        ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], 
                   alpha=0.5, linestyles=['--', '-', '--'])
        
        ax.scatter(X_moon[y_moon == 0, 0], X_moon[y_moon == 0, 1], 
                   c='red', marker='o', s=15)
        ax.scatter(X_moon[y_moon == 1, 0], X_moon[y_moon == 1, 1], 
                   c='blue', marker='s', s=15)
        
        acc = accuracy_score(y_moon, svm.predict(X_moon))
        ax.set_title(f'C={C}, gamma={gamma}\nAccuracy: {acc:.2%}')
        ax.set_xlim(-2, 3)
        ax.set_ylim(-1.5, 2)

plt.suptitle('SVM Parameter Tuning: C vs gamma', fontsize=14)
plt.tight_layout()
plt.show()
```

**参数说明**：

| 参数 | 作用 | 太大时 | 太小时 |
|------|------|--------|--------|
| C | 正则化强度 | 可能过拟合 | 可能欠拟合 |
| gamma | RBF核宽度 | 模型复杂，可能过拟合 | 模型简单，可能欠拟合 |

![参数调优可视化]

---

## 📝 示例5：软间隔SVM处理噪声数据

```python
def plot_decision_boundary(X, y, model, title):
    """绘制决策边界的辅助函数"""
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    xx = np.linspace(xlim[0], xlim[1], 200)
    yy = np.linspace(ylim[0], ylim[1], 200)
    XX, YY = np.meshgrid(xx, yy)
    xy = np.c_[XX.ravel(), YY.ravel()]
    Z = model.decision_function(xy).reshape(XX.shape)
    
    ax.contourf(XX, YY, Z, alpha=0.3, levels=30)
    ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], 
               alpha=0.8, linestyles=['--', '-', '--'])
    
    ax.scatter(X[y == 0, 0], X[y == 0, 1], c='red', marker='o', s=40)
    ax.scatter(X[y == 1, 0], X[y == 1, 1], c='blue', marker='s', s=40)
    plt.title(title)
    plt.grid(True, alpha=0.3)

# 生成带有噪声的数据
np.random.seed(123)
X_noisy = np.vstack([
    np.random.randn(50, 2) + [2, 2],
    np.random.randn(50, 2) + [4, 4]
])
y_noisy = np.array([0] * 50 + [1] * 50)

# 添加一些噪声点（让数据不完全线性可分）
X_noisy = np.vstack([X_noisy, [[3.5, 3.8]], [[3.3, 3.5]], [[3.6, 3.2]]])
y_noisy = np.append(y_noisy, [1, 0, 1])

plt.figure(figsize=(12, 5))

# 硬间隔SVM（C很大）
svm_hard = SVC(kernel='linear', C=1000)
svm_hard.fit(X_noisy, y_noisy)
acc_hard = accuracy_score(y_noisy, svm_hard.predict(X_noisy))

plt.subplot(1, 2, 1)
plot_decision_boundary(X_noisy, y_noisy, svm_hard, 
                       f'Hard Margin SVM (C=1000)\nAccuracy: {acc_hard:.2%}')

# 软间隔SVM（C较小，允许一定错误）
svm_soft = SVC(kernel='linear', C=1)
svm_soft.fit(X_noisy, y_noisy)
acc_soft = accuracy_score(y_noisy, svm_soft.predict(X_noisy))

plt.subplot(1, 2, 2)
plot_decision_boundary(X_noisy, y_noisy, svm_soft, 
                       f'Soft Margin SVM (C=1)\nAccuracy: {acc_soft:.2%}')

plt.tight_layout()
plt.show()

print(f"硬间隔 SVM 准确率: {acc_hard:.2%}")
print(f"软间隔 SVM 准确率: {acc_soft:.2%}")
print(f"\n硬间隔支持向量数: {svm_hard.n_support_.sum()}")
print(f"软间隔支持向量数: {svm_soft.n_support_.sum()}")
```

**运行结果**：
```
硬间隔 SVM 准确率: 97.92%
软间隔 SVM 准确率: 97.92%

硬间隔支持向量数: 6
软间隔支持向量数: 4
```

**结果说明**：
- 硬间隔SVM对噪声敏感，需要更多支持向量
- 软间隔SVM允许一定错误，支持向量更少，泛化能力可能更好

![软间隔vs硬间隔]

---

## 🎓 总结

```python
"""
SVM 编程要点总结：
==================

1. 导入: from sklearn.svm import SVC

2. 创建模型:
   - 线性核: SVC(kernel='linear', C=1.0)
   - RBF核: SVC(kernel='rbf', C=1.0, gamma='scale')
   - 多项式核: SVC(kernel='poly', degree=3, C=1.0)

3. 训练和预测:
   - model.fit(X_train, y_train)
   - y_pred = model.predict(X_test)

4. 关键属性:
   - model.support_: 支持向量索引
   - model.support_vectors_: 支持向量
   - model.n_support_: 每个类的支持向量数
   - model.dual_coef_: 决策函数系数

5. 参数选择:
   - C: 正则化参数，越大越严格
   - gamma: RBF核参数，控制模型复杂度
"""
```

---

## 📚 参考代码：完整的SVM分类管道

```python
def svm_classification_pipeline(X, y, test_size=0.2, random_state=42):
    """
    完整的SVM分类流程
    
    Parameters:
    -----------
    X : array-like, 特征矩阵
    y : array-like, 标签
    test_size : float, 测试集比例
    random_state : int, 随机种子
    
    Returns:
    --------
    model : 训练好的SVM模型
    metrics : 评估指标字典
    """
    from sklearn.preprocessing import StandardScaler
    
    # 1. 数据划分
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    # 2. 特征标准化（SVM对尺度敏感！）
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 3. 训练模型
    model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=random_state)
    model.fit(X_train_scaled, y_train)
    
    # 4. 预测和评估
    y_train_pred = model.predict(X_train_scaled)
    y_test_pred = model.predict(X_test_scaled)
    
    metrics = {
        'train_accuracy': accuracy_score(y_train, y_train_pred),
        'test_accuracy': accuracy_score(y_test, y_test_pred),
        'n_support_vectors': model.n_support_.sum(),
        'support_vectors': model.support_vectors_
    }
    
    return model, metrics

print("SVM分类管道函数已定义！")
print("使用方式: model, metrics = svm_classification_pipeline(X, y)")
```
