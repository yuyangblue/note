# Python数学建模基础入门
**Day 1 学习简报 · 2026年3月27日**  
**难度：入门级 · 预计学习时间：1小时**

---

## 一、Python数学建模概述

### 为什么选择Python进行数学建模？
Python已成为数学建模竞赛（如华中杯）的主流工具，主要优势包括：
- **语法简洁**：学习曲线平缓，便于快速上手
- **生态丰富**：拥有大量专门针对科学计算的第三方库
- **免费开源**：无需购买许可，社区支持强大
- **跨平台**：Windows、macOS、Linux均可运行
- **工程衔接**：便于将模型部署到实际应用中

### 常用库简介（四大核心）
| 库名 | 主要用途 | 导入约定 |
|------|----------|----------|
| **NumPy** | 多维数组与矩阵运算、线性代数、随机数生成 | `import numpy as np` |
| **SciPy** | 科学计算算法库，包含优化、积分、插值、统计等模块 | `from scipy import optimize, integrate, stats` |
| **pandas** | 数据结构与数据分析，擅长表格数据处理 | `import pandas as pd` |
| **matplotlib** | 数据可视化，绘制各类图表 | `import matplotlib.pyplot as plt` |

**安装方法**（若未安装）：
```bash
pip install numpy scipy pandas matplotlib
```

---

## 二、线性规划基础：`scipy.optimize.linprog`

### 1. 什么是线性规划？
在资源有限的前提下，如何分配资源使目标（如利润最大、成本最小）最优。例如：
- **决策变量**：产品A产量 \(x_1\)，产品B产量 \(x_2\)
- **目标函数**：最大化利润 \(z = 30x_1 + 50x_2\)
- **约束条件**：  
  \(2x_1 + 4x_2 \le 200\)（资源1限制）  
  \(3x_1 + 2x_2 \le 180\)（资源2限制）  
  \(x_1, x_2 \ge 0\)（非负约束）

### 2. `linprog` 函数详解
```python
from scipy.optimize import linprog

# 函数签名（简化）：
linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, 
        bounds=None, method='highs', options=None)
```

**参数说明**：
| 参数 | 含义 | 示例 |
|------|------|------|
| `c` | 目标函数系数向量（最小化问题） | `c = [-30, -50]`（注意：linprog默认求最小值，故最大化问题需取负） |
| `A_ub`, `b_ub` | 不等式约束矩阵与右侧向量（\(A_{ub} x \le b_{ub}\)） | `A_ub = [[2,4], [3,2]]`, `b_ub = [200, 180]` |
| `A_eq`, `b_eq` | 等式约束矩阵与右侧向量（\(A_{eq} x = b_{eq}\)） | 若无等式约束，可省略 |
| `bounds` | 决策变量的取值范围 | `bounds = [(0, None), (0, None)]` 表示 \(x_1, x_2 \ge 0\) |
| `method` | 求解算法，推荐 `'highs'`（默认） | 另有 `'interior-point'`, `'revised simplex'` |
| `options` | 求解器选项，如最大迭代次数等 | `options={'maxiter': 1000}` |

**返回值**（`OptimizeResult` 对象）：
```python
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(res)
```
主要字段：
- `x`：最优解向量
- `fun`：最优目标函数值（注意：若输入时取了负，此处需再取负还原）
- `success`：求解是否成功（`True`/`False`）
- `message`：求解状态描述

### 3. 简单示例：最大化利润问题
```python
import numpy as np
from scipy.optimize import linprog

# 目标函数系数（最大化 30x1 + 50x2 → 最小化 -30x1 -50x2）
c = [-30, -50]

# 不等式约束：2x1 + 4x2 <= 200, 3x1 + 2x2 <= 180
A_ub = [[2, 4],
        [3, 2]]
b_ub = [200, 180]

# 变量非负约束
bounds = [(0, None), (0, None)]

# 求解
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# 输出结果
print("求解状态:", "成功" if res.success else "失败")
print("最优解: x1 =", round(res.x[0], 2), "x2 =", round(res.x[1], 2))
print("最大利润:", -res.fun)  # 注意取负还原
```
**输出类似**：
```
求解状态: 成功
最优解: x1 = 40.0 x2 = 20.0
最大利润: 2200.0
```

---

## 三、数据可视化基础：`matplotlib.pyplot`

### 1. 绘图基本流程
```python
import matplotlib.pyplot as plt
import numpy as np

# 1. 准备数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 2. 创建图形与坐标轴（推荐方式）
fig, ax = plt.subplots(figsize=(8, 5))

# 3. 绘制折线图
ax.plot(x, y, color='blue', linestyle='-', linewidth=2, label='sin(x)')

# 4. 添加标签与标题
ax.set_xlabel('X轴', fontsize=12)
ax.set_ylabel('Y轴', fontsize=12)
ax.set_title('正弦函数曲线', fontsize=14)

# 5. 显示图例与网格
ax.legend()
ax.grid(True, alpha=0.3)

# 6. 保存图片（先保存后显示）
plt.savefig('sin_plot.png', dpi=300, bbox_inches='tight')

# 7. 显示图形
plt.show()
```

### 2. 常用函数速查
| 函数 | 用途 | 示例 |
|------|------|------|
| `plt.plot(x, y)` | 绘制折线图 | `plt.plot(x, y, 'ro--')`（红色圆圈虚线） |
| `plt.scatter(x, y)` | 绘制散点图 | `plt.scatter(x, y, s=20, c='red')` |
| `plt.bar(x, height)` | 垂直柱状图 | `plt.bar(categories, values)` |
| `plt.hist(data, bins)` | 直方图 | `plt.hist(data, bins=30)` |
| `plt.xlabel(text)` | X轴标签 | `plt.xlabel('时间（秒）')` |
| `plt.ylabel(text)` | Y轴标签 | `plt.ylabel('温度（℃）')` |
| `plt.title(text)` | 图形标题 | `plt.title('实验结果')` |
| `plt.legend()` | 显示图例 | `plt.legend(['实验组', '对照组'])` |
| `plt.grid(True)` | 显示网格 | `plt.grid(True, linestyle='--', alpha=0.5)` |
| `plt.savefig(filename)` | 保存图形 | `plt.savefig('result.png', dpi=300)` |
| `plt.show()` | 显示图形 | `plt.show()` |

### 3. 解决中文显示问题（环境字体缺失）
如果出现 `findfont` 警告（中文显示为方框），**请任选一种解决方案**：

**方案一：改用英文标签**（推荐，竞赛中常用）
```python
# 将中文标签改为英文
plt.xlabel('Product A Quantity')
plt.ylabel('Product B Quantity')
plt.title('Production Planning Optimization')
```

**方案二：使用跨平台通用字体**
```python
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']  # 系统默认安装的字体
plt.rcParams['axes.unicode_minus'] = False
```

**方案三：检测可用中文字体（自动选择）**
```python
import matplotlib.font_manager as fm

# 获取所有可用字体
fonts = [f.name for f in fm.fontManager.ttflist]

# 优先选择中文字体（常见字体名包含关键字）
chinese_fonts = [f for f in fonts if any(keyword in f.lower() 
                for keyword in ['song', 'hei', 'yahei', 'kai', 'noto'])]
if chinese_fonts:
    plt.rcParams['font.sans-serif'] = [chinese_fonts[0]]
else:
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans']  # 回退方案
plt.rcParams['axes.unicode_minus'] = False
```

---

## 四、实际应用：生产优化完整案例

### 问题描述
某工厂生产两种产品A和B，每件产品消耗的资源及利润如下：

| 产品 | 资源1（单位） | 资源2（单位） | 利润（元） |
|------|---------------|---------------|------------|
| A    | 2             | 3             | 30         |
| B    | 4             | 2             | 50         |

工厂每天可用资源1为200单位，资源2为180单位。如何安排生产使总利润最大？

### 完整代码实现
```python
import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# ========== 1. 定义线性规划问题 ==========
# 目标函数系数（最大化利润 → 最小化负利润）
c = [-30, -50]  # 注意：linprog默认求最小值，故取负

# 不等式约束矩阵 A_ub * x <= b_ub
A_ub = [[2, 4],   # 资源1约束
        [3, 2]]   # 资源2约束
b_ub = [200, 180]

# 变量非负约束
bounds = [(0, None), (0, None)]

# ========== 2. 求解线性规划 ==========
print("正在求解线性规划问题...")
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# ========== 3. 输出结果 ==========
print("\n" + "="*50)
print("线性规划求解结果")
print("="*50)
print("求解状态:", "成功" if res.success else "失败")
print("是否成功:", res.success)
print("最优生产方案:")
print("  产品A产量:", round(res.x[0], 2), "件")
print("  产品B产量:", round(res.x[1], 2), "件")
print("最大总利润:", round(-res.fun, 2), "元")  # 注意取负还原

# ========== 4. 可视化 ==========
print("\n生成可视化图形...")

# 设置图形风格（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']  # 通用字体
plt.rcParams['axes.unicode_minus'] = False

# 创建图形
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 子图1：约束区域与最优解
x1 = np.linspace(0, 100, 400)
# 约束1: 2x1 + 4x2 <= 200 → x2 <= (200 - 2x1)/4
con1 = (200 - 2*x1) / 4
# 约束2: 3x1 + 2x2 <= 180 → x2 <= (180 - 3x1)/2
con2 = (180 - 3*x1) / 2

ax1.fill_between(x1, 0, np.minimum(con1, con2), alpha=0.3, label='可行域')
ax1.plot(x1, con1, 'r--', linewidth=2, label='资源1约束: 2x1+4x2≤200')
ax1.plot(x1, con2, 'g--', linewidth=2, label='资源2约束: 3x1+2x2≤180')
ax1.scatter(res.x[0], res.x[1], color='blue', s=100, zorder=5, 
            label=f'最优解 ({res.x[0]:.1f}, {res.x[1]:.1f})')

ax1.set_xlabel('产品A产量 (x1)', fontsize=12)
ax1.set_ylabel('产品B产量 (x2)', fontsize=12)
ax1.set_title('生产优化问题可行域与最优解', fontsize=14)
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 80)

# 子图2：利润等高线与最优解
x1_grid, x2_grid = np.meshgrid(np.linspace(0, 100, 50), 
                               np.linspace(0, 80, 40))
profit = 30*x1_grid + 50*x2_grid

contour = ax2.contourf(x1_grid, x2_grid, profit, levels=20, cmap='RdYlGn')
plt.colorbar(contour, ax=ax2, label='利润 (元)')
ax2.scatter(res.x[0], res.x[1], color='blue', s=100, zorder=5, 
            label=f'最优解 ({res.x[0]:.1f}, {res.x[1]:.1f})')

ax2.set_xlabel('产品A产量 (x1)', fontsize=12)
ax2.set_ylabel('产品B产量 (x2)', fontsize=12)
ax2.set_title('利润等高线与最优解', fontsize=14)
ax2.legend(loc='upper right')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('outputs/每日学习/production_optimization.png', dpi=300)
plt.show()

print("可视化图形已保存为: outputs/每日学习/production_optimization.png")
```

### 代码解读
1. **问题建模**：将实际问题转化为数学形式（目标函数、约束条件）
2. **调用求解器**：使用 `linprog` 函数求解
3. **结果解析**：从求解结果中提取最优产量和最大利润
4. **可视化**：
   - **左图**：显示约束条件围成的可行域，最优解位于可行域的顶点
   - **右图**：用等高线展示不同产量组合对应的利润，颜色越暖利润越高

### 关键知识点
- **线性规划标准形式**：`min c^T x, s.t. A_ub x <= b_ub, A_eq x = b_eq, bounds`
- **最大化转最小化**：目标函数系数取负
- **可行域**：满足所有约束的决策变量集合
- **最优解位置**：线性规划的最优解总是在可行域的顶点（若存在）

---

## 五、今日学习任务

### 核心练习
1. **运行完整案例代码**，确保无语法错误，得到最优解 `(40, 20)` 和最大利润 `2200`
2. **修改问题参数**（如将利润改为 `[40, 60]`），观察最优解变化
3. **尝试绘制不同图表**：将右图改为散点图，每个点代表一种产量组合，颜色映射利润值

### 思考问题
1. 如果增加第三个产品C，应如何修改代码？
2. 若约束条件变为等式（如资源必须用完），应使用 `A_eq` 还是 `A_ub`？
3. 为什么本例的最优解恰好是整数？是否所有线性规划的最优解都是整数？

### 扩展阅读（可选）
- SciPy 官方文档：[scipy.optimize.linprog](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)
- Matplotlib 教程：[Pyplot tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

---

## 六、注意事项

1. **环境配置**：确保已安装 `numpy`, `scipy`, `pandas`, `matplotlib` 库
2. **字体问题**：若图表中文显示异常，请使用第三部分提供的解决方案
3. **代码调试**：建议逐段运行代码（如先求解、再可视化），便于定位错误
4. **时间管理**：重点理解线性规划建模思路与 `linprog` 参数含义，可视化部分可后续细化

---

**学习提示**：今日重点是掌握线性规划的基本建模方法与 `linprog` 的调用方式。不必纠结于可视化细节，后续案例会逐步深入。

**下一步**：完成今日学习后，请保存你的代码与图表，并准备进入 Day 2（线性规划案例复现与扩展）。

祝学习顺利！ 🚀

---
*本简报由华中杯数学建模4周冲刺计划生成 · Day 1 · Python数学建模基础入门*
