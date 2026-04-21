
> 学习日期：2026-04-07

---

## 1. 速查表

| 函数 | 用途 | 关键参数 |
|------|------|----------|
| `plt.plot()` | 折线图 | `color`, `linewidth`, `linestyle`, `marker` |
| `plt.scatter()` | 散点图 | `c`, `s`, `alpha`, `edgecolors` |
| `plt.bar()` | 柱状图 | `color`, `width` |
| `plt.hist()` | 直方图 | `bins`, `edgecolor` |
| `plt.pie()` | 饼图 | `labels`, `autopct`, `colors` |
| `plt.subplot()` | 子图 | 行数, 列数, 位置 |
| `plt.savefig()` | 保存 | `dpi`, `bbox_inches` |

---

## 2. 线型样式

| 符号 | 颜色 | 符号 | 线型 |
|------|------|------|------|
| `b` | 蓝 | `-` | 实线 |
| `r` | 红 | `--` | 虚线 |
| `g` | 绿 | `:` | 点线 |
| `k` | 黑 | `-.` | 点划线 |

---

## 3. 折线图 `plot`

```python
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 100)  # 生成等差数列
y = np.sin(x)

plt.figure(figsize=(8, 5))           # 画布大小
plt.plot(x, y, 'b-', linewidth=5, label='sin(x)')    # 蓝色实线
plt.plot(x, np.cos(x), 'r--', label='cos(x)')        # 红色虚线

plt.xlabel('x')
plt.ylabel('y')
plt.title('sin and cos function')
plt.legend()              # 显示图例
plt.grid(True, alpha=0.3) # 显示网格
plt.show()
```
![[Pasted image 20260407191521.png]]
---

## 4. 散点图 `scatter`

**常用参数**：
- `c`：颜色（可用数组映射颜色）
- `s`：点的大小
- `alpha`：透明度（0-1）
- `edgecolors`：边缘颜色

```python
np.random.seed(42)
x = np.random.randn(50)
y = x ** 2 + np.random.randn(50) * 0.5

plt.figure(figsize=(8, 5))
plt.scatter(x, y, c='blue', s=50, alpha=0.7, edgecolors='k', label='data point')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot Example')
plt.legend()
plt.show()
```
![[Pasted image 20260407191528.png]]
---

## 5. 柱状图 `bar`

```python
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 32]

plt.figure(figsize=(8, 5))
plt.bar(categories, values, color=['#3498db', '#e74c3c', '#2ecc71', '#f39c12'])

plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart Example')
plt.show()
```

**水平柱状图**：用 `plt.barh()`
![[Pasted image 20260407191623.png]]
---

## 6. 直方图 `hist`

**`bins` 参数**：箱子的数量，决定数据分成多少组。

| bins | 效果 |
|------|------|
| 小（如10） | 箱子宽，细节少 |
| 大（如100） | 箱子窄，细节多 |
| 适中（如30） | 平衡细节与平滑度 |

```python
data = np.random.randn(1000)

plt.figure(figsize=(8, 5))
plt.hist(data, bins=20, color='skyblue', edgecolor='black', alpha=0.7)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()![[Pasted image 20260407191627.png]]
```
![[Pasted image 20260407191638.png]]
---

## 7. 饼图 `pie`

```python
labels = ['A', 'B', 'C', 'D']
sizes = [30, 25, 25, 20]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

plt.title('Pie Chart Example')
plt.show()
```
![[Pasted image 20260407191558.png]]
---

## 8. 子图 `subplot`

```python
x = np.linspace(0, 10, 100)

plt.figure(figsize=(12, 8))

# 2行2列，第1个位置
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x), 'b-')
plt.title('sin(x)')

# 2行2列，第2个位置
plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x), 'r--')
plt.title('cos(x)')

# 2行2列，第3个位置
plt.subplot(2, 2, 3)
plt.plot(x, np.exp(-x), 'g:')
plt.title('exp(-x)')

# 2行2列，第4个位置
plt.subplot(2, 2, 4)
plt.plot(x, np.log(x+1), 'k-.')
plt.title('log(x+1)')

plt.tight_layout()  # 自动调整间距
plt.show()
```

**跨越多格**：
```python
plt.subplot(2, 2, (1, 2))  # 占据第1、2格（横向跨两列）
```
![[Pasted image 20260407191644.png]]
---

## 9. 保存图片 `savefig`

```python
plt.figure(figsize=(8, 5))
plt.plot(x, np.sin(x))
plt.title('Save Example')

plt.savefig('output.png', dpi=300, bbox_inches='tight')
plt.show()
```

**常用参数**：
- `dpi`：分辨率
- `bbox_inches='tight'`：裁剪空白边缘
![[Pasted image 20260407191651.png]]
---

## 10. 中文字体设置

如果出现 `Glyph missing from current font` 警告，说明字体不支持中文。

**解决方法**：

```python
# 方法1：设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']      # Windows
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 方法2：使用英文标签（推荐）
plt.xlabel('x')
plt.ylabel('y')
plt.title('English Title')
```

---

## 11. 完整模板

```python
import matplotlib.pyplot as plt
import numpy as np

# 数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 画图
plt.figure(figsize=(10, 6))
plt.plot(x, y1, 'b-', linewidth=2, label='sin(x)')
plt.plot(x, y2, 'r--', linewidth=2, label='cos(x)')

# 装饰
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Trigonometric Functions', fontsize=14)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

# 保存与显示
plt.savefig('output.png', dpi=300, bbox_inches='tight')
plt.show()
```
