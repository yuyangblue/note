`from mpl_toolkits.mplot3d import Axes3D` 是 Matplotlib 中用于**绘制三维图形**的核心模块。在数学建模中，常用它可视化**可行域曲面、利润等高线、数据拟合曲面**等。

# **Axes3D 三维坐标系快速入门**

**1. 创建三维坐标轴**

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 必须导入

fig = plt.figure(figsize=(10, 7))        # 创建画布
ax = fig.add_subplot(111, projection='3d')  # 得到三维坐标轴对象 `ax`
```

- `ax` 就是你操作三维绘图的“手柄”，所有三维绘图指令（`plot_surface`, `scatter`, `contour3D` 等）都通过它调用。

**2. 绘制三维散点图（`ax.scatter`）**

```python
import numpy as np

# 生成示例数据
n = 100
x = np.random.randn(n)  # X坐标
y = np.random.randn(n)  # Y坐标  
z = np.random.randn(n)  # Z坐标

# 绘制散点
ax.scatter(x, y, z, 
           c='red',      # 颜色（支持字符串、颜色列表）
           marker='o',   # 点标记形状
           s=50,         # 点大小
           alpha=0.6,    # 透明度（0~1）
           label='Data Points')

ax.set_xlabel('X轴标签')
ax.set_ylabel('Y轴标签')  
ax.set_zlabel('Z轴标签')
ax.set_title('三维散点图示例')
ax.legend()
plt.show()
```

### **关键参数详解**

表格

|参数|作用|示例|
|---|---|---|
|`x, y, z`|数据点的三轴坐标（等长数组）|`[1,2,3]`, `[4,5,6]`, `[7,8,9]`|
|`c`|点颜色|`'red'`（统一颜色）<br><br>`np.arange(len(x))`（按数值映射色彩）|
|`s`|点尺寸（标量或数组）|`50`（统一大小）<br><br>`np.abs(z)*100`（按Z值比例缩放）|
|`marker`|点形状|`'o'`（圆）<br><br>`'^'`（三角形）<br><br>`'s'`（正方形）|
|`alpha`|透明度|`0.6`（60%不透明）|
|`label`|图例标签|`'原始数据'`|

# **绘制三维曲面的核心步骤**

在 Matplotlib 中绘制三维曲面需要以下四步：

1. **准备数据网格**
    
    ```python
    import numpy as np
    # 生成 X、Y 方向的坐标点
    x = np.linspace(-5, 5, 50)   # 50 个点，范围 -5 到 5
    y = np.linspace(-5, 5, 50)
    # 生成网格坐标矩阵
    X, Y = np.meshgrid(x, y)
    # 计算每个网格点的 Z 值（示例：旋转抛物面）
    Z = X**2 + Y**2
    ```
    
2. **创建三维坐标轴**
    
    ```python
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # 必须导入
    
    fig = plt.figure(figsize=(10, 7))        # 创建画布
    ax = fig.add_subplot(111, projection='3d')  # 生成三维坐标系对象
    ```
    
3. **绘制曲面**
    
    ```python
    surf = ax.plot_surface(X, Y, Z, 
                           cmap='viridis',   # 颜色映射
                           alpha=0.8,        # 透明度
                           linewidth=0,      # 网格线宽度（0 为无）
                           antialiased=True) # 抗锯齿
    ```
    
4. **添加标签与颜色条**
    
    ```python
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Surface Plot')
    fig.colorbar(surf, ax=ax, shrink=0.6)  # 添加颜色条
    plt.show()
    ```
    

**关键参数说明**

- `X, Y, Z`：必须是 **二维数组**（通过 `meshgrid` 生成）
- `cmap`：颜色映射，可选 `'viridis'`、`'plasma'`、`'coolwarm'` 等
- `alpha`：透明度（0 全透明，1 不透明）
- `linewidth`：网格线粗细，设为 `0` 可隐藏网格线

# **三维曲面 vs 三维散点的核心区别**

表格

|维度|`plot_surface`（曲面）|`scatter`（散点）|
|---|---|---|
|**数据形态**|**连续表面**，由 `np.meshgrid` 生成的规则网格点（X, Y, Z 均为二维数组）|**离散点集**，每个点独立（x, y, z 为一维数组）|
|**视觉表达**|平滑或分片连续的“面”，适合展现函数关系、优化可行域、拟合曲面|孤立的“点”，适合展现观测样本、实验数据、可行解分布|
|**在建模中的应用**|模型输出（如拟合曲面、利润函数、可行域边界）|原始输入（如观测数据、历史样本、候选解）|
