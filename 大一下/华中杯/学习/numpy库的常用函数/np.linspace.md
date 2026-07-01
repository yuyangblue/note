**`np.linspace` 是 NumPy 库中用于生成等差数列（线性间隔点）的核心函数**，常用于创建绘图、拟合、仿真所需的均匀坐标网格。

**基本语法**

```python
import numpy as np
x = np.linspace(start, 终止, num=50, endpoint=True, retstep=False, dtype=None)
```

- `start`：序列起始值
- `终止`：序列结束值
- `num`：生成的点数（默认50）
- `endpoint`：是否包含结束点（默认 `True`）
- `retstep`：是否同时返回步长（默认 `False`）

**示例**

```python
# 生成 0 到 10 之间的 5 个等间隔点
x = np.linspace(0, 10, 5)
print(x)  # 输出: [ 0.   2.5  5.   7.5 10. ]