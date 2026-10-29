# 最小二乘法笔记

> 来源：手写笔记 `cm+opt_最小二乘.pdf`（共 20 页）。
> 本笔记逐页忠实转录原文内容与批注，公式保持原样；（红）/（蓝）/（灰）标注原文颜色批注。

---

## 第 1 页

$$
A\vec{x} = \vec{b},\qquad \text{其中 } A\in\mathbb{R}^{n\times n}\text{；若 } A\in\mathbb{R}^{m\times n},\ m\ne n\ \text{？}
$$

**例**：

$$
\begin{cases}
x_1 + x_2 = 2\\
x_1 + 2x_2 = 3\\
x_1 - x_2 = -1
\end{cases}
\Longrightarrow
\begin{bmatrix}1\\1\\1\end{bmatrix}x_1 + \begin{bmatrix}1\\2\\-1\end{bmatrix}x_2 = \begin{bmatrix}2\\3\\-1\end{bmatrix}
$$

$\vec{b} = (2,3,-1)^{\mathsf T}$，$\vec{v}_1 = (1,1,1)^{\mathsf T}$，$\vec{v}_2 = (1,2,-1)^{\mathsf T}$。

（图示：平面 $\Omega$ 上有 $\vec{v}_1$、$\vec{v}_2$，$\vec{b}$ 在平面外，$\vec{b}'$ 为投影。）

$$
\vec{b}' = \vec{v}_1\cdot m_1 + \vec{v}_2\cdot m_2 \in \Omega,\qquad \Omega = \mathrm{Span}\{\vec{v}_1, \vec{v}_2\}
$$

$$
\min\ \|\vec{b} - x_1\vec{v}_1 - x_2\vec{v}_2\|_2
\qquad\Longrightarrow\qquad \text{最小二乘。}
$$

### 第三章 最小二乘法

### 1. 最小二乘问题及法方程方法

- 设：$\exists\,\vec{x}^*$ 使 $A\vec{x}^* = \vec{b}$ 成立，则 $A\vec{x} = \vec{b}$ 为相容的。
- 定理：若存在 $\vec{x}^*$ 使 $\|\vec{b} - A\vec{x}^*\|_2$ 为最小，则 $\vec{x}^*$ 为 $A\vec{x} = \vec{b}$ 的最小二乘解。
- 注意：$A\vec{x} = \vec{b}$ 的最小二乘解总存在；最小二乘解唯一的条件为 $\mathrm{null}(A) = \{\vec{0}\}$，$\forall\,\vec{\eta}\in\mathrm{null}(A)$，$A\vec{\eta} = \vec{0}$。

（图示：平面 $\Omega$ 上 $\vec{v}_1,\vec{v}_2,\vec{v}_3$，$\vec{b}$ 在外，$\vec{b}'$ 为投影；$A = [\times\ \times\ \times;\ \times\ \times\ \times;\ \times\ \times\ \times]$，列向量为 $\vec{v}_1,\vec{v}_2,\vec{v}_3$，$\vec{b}' = x_1\vec{v}_1 + x_2\vec{v}_2 + x_3\vec{v}_3$，中 $x_1, x_2, x_3$ 不唯一。）

---

## 第 2 页

最小二乘解：使 $\|\vec{b} - A\vec{x}\|_2^2$ 达到最小，$A\in\mathbb{R}^{m\times n}$。

定义

$$
g(\vec{x}) = \|\vec{b} - A\vec{x}\|_2^2 = \sum_{i=1}^{m}\Big(b_i - \sum_{j=1}^{n} a_{ij}x_j\Big)^2
$$

$$
\Longrightarrow\ \frac{\partial g}{\partial x_k}
= \frac{\partial}{\partial x_k}\Big(\sum_{i=1}^{m}\big(b_i - \textstyle\sum_{j=1}^{n}a_{ij}x_j\big)^2\Big)
= 2\sum_{i=1}^{m}\Big(a_{ik}\cdot\sum_{j=1}^{n}a_{ij}\cdot x_j - a_{ik}\cdot b_i\Big) = 0
$$

$$
\begin{cases}
k=1:\quad \displaystyle\sum_{i=1}^{m}\Big(a_{i1}\cdot\sum_{j=1}^{n}a_{ij}x_j - a_{i1}\cdot b_i\Big) = 0\\
\quad\vdots\\
k=n:\quad \displaystyle\sum_{i=1}^{m}\Big(a_{in}\cdot\sum_{j=1}^{n}a_{ij}x_j - a_{in}b_i\Big) = 0
\end{cases}
\qquad\Longrightarrow\ \text{$n$ 个方程，$n$ 个未知量。（右注）}
$$

$$
\sum_{i=1}^{m}\Big(a_{ik}\cdot\sum_{j=1}^{n}a_{ij}\cdot x_j\Big) = \sum_{i=1}^{m} a_{ik}\cdot b_i
$$

$$
\Longrightarrow\ \sum_{i=1}^{m}\sum_{j=1}^{n} a_{ik}\cdot a_{ij}\cdot x_j = \sum_{i=1}^{m} a_{ik}\cdot b_i
\qquad \text{※ 定义 } C = A^{\mathsf T},\ a_{ik} = c_{ki}
$$

$$
\Longrightarrow\ \sum_{j=1}^{n}\sum_{i=1}^{m} c_{ki}\cdot a_{ij}\cdot x_j = \sum_{i=1}^{m} c_{ki}\cdot b_i
$$

$$
\Longrightarrow\ \sum_{j=1}^{n}\Big(\sum_{i=1}^{m} c_{ki}a_{ij}\Big)\cdot x_j = \sum_{i=1}^{m} c_{ki}b_i
\ \Longrightarrow\ (CA)\vec{x} = C\cdot\vec{b}
$$

$$
\Longrightarrow\ A^{\mathsf T}A\vec{x} = A^{\mathsf T}\vec{b}
\qquad \text{考虑 } A \text{ 非行}>\text{列，}A\text{ 为列满秩。}
$$

（注：「考虑 A 非行>列」为原文写法，意指 $A$ 非方阵且行数大于列数（$m>n$）。）

**（红）☆** $g(\vec{x}) = \|\vec{b} - A\vec{x}\|_2^2$ 为凸函数 $\Longrightarrow A^{\mathsf T}A\vec{x} = A^{\mathsf T}\vec{b}$。

---

## 第 3 页

### 最小二乘问题几何解释

（图示：平面与 $\vec{v}_1,\vec{v}_2$，$\vec{b}$ 在外，$\vec{b}'$ 为垂线投影。）

$$
\min_{x_1,x_2}\ \|\vec{b} - \vec{v}_1\cdot x_1 - \vec{v}_2\cdot x_2\|_2^2
\ \Longleftrightarrow\ \min\ \|\vec{b}' - \vec{v}_1\cdot x_1 - \vec{v}_2\cdot x_2\|_2^2
$$

$$
A\vec{x} = \vec{b}\ \Longleftrightarrow\ \begin{bmatrix}\vec{v}_1 & \vec{v}_2\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix} = \vec{b}
$$

$$
A^{\mathsf T} = \begin{bmatrix}\vec{v}_1^{\mathsf T}\\ \vec{v}_2^{\mathsf T}\end{bmatrix}
\ \Longrightarrow\ A^{\mathsf T}\vec{b} = \begin{bmatrix}\vec{v}_1^{\mathsf T}\vec{b}\\ \vec{v}_2^{\mathsf T}\vec{b}\end{bmatrix}
$$

由于 $\vec{b} = \vec{b}' + \vec{b}_\perp$（$\vec{b}_\perp\perp\Omega$），有 $\vec{b}_\perp\cdot\vec{v}_1 = \vec{b}_\perp\cdot\vec{v}_2 = 0$。

（旁注（蓝）：$\vec{b}' = \vec{v}_1 x_1 + \vec{v}_2 x_2$。）

$$
\Longrightarrow\ (\vec{b} - \vec{b}')^{\mathsf T}\cdot\vec{v}_1 = 0,\qquad (\vec{b} - \vec{b}')^{\mathsf T}\cdot\vec{v}_2 = 0
$$

$$
\Longrightarrow\ \begin{cases}
(\vec{b} - \vec{v}_1x_1 - \vec{v}_2x_2)^{\mathsf T}\cdot\vec{v}_1 = 0\\[2pt]
(\vec{b} - \vec{v}_1x_1 - \vec{v}_2x_2)^{\mathsf T}\cdot\vec{v}_2 = 0
\end{cases}
$$

$$
\Longrightarrow\ \begin{cases}
(\vec{v}_1^{\mathsf T}\cdot\vec{v}_1)x_1 + (\vec{v}_2^{\mathsf T}\cdot\vec{v}_1)\cdot x_2 = \vec{b}^{\mathsf T}\cdot\vec{v}_1\\[2pt]
(\vec{v}_1^{\mathsf T}\cdot\vec{v}_2)\cdot x_1 + (\vec{v}_2^{\mathsf T}\cdot\vec{v}_2)x_2 = \vec{b}^{\mathsf T}\cdot\vec{v}_2
\end{cases}
\qquad \text{（标注：法方程）}
$$

$$
\Longrightarrow
\begin{bmatrix}
\vec{v}_1^{\mathsf T}\vec{v}_1 & \vec{v}_2^{\mathsf T}\vec{v}_1\\
\vec{v}_1^{\mathsf T}\vec{v}_2 & \vec{v}_2^{\mathsf T}\vec{v}_2
\end{bmatrix}
\begin{bmatrix}x_1\\x_2\end{bmatrix}
=
\begin{bmatrix}\vec{v}_1^{\mathsf T}\vec{b}\\ \vec{v}_2^{\mathsf T}\vec{b}\end{bmatrix}
\ \Longrightarrow\ A^{\mathsf T}A\vec{x} = A^{\mathsf T}\vec{b}
$$

### 应用：数据拟合问题

**☆** $\|\vec{b} - A\vec{x}\|_2$ 达到最小

$$
\downarrow
$$

$$
\vec{b} - \sum_i x_i\cdot\vec{a}_i\ (\Delta)
\ \Longleftrightarrow\
y(x) - \sum_i c_i\cdot f_i(x)
$$

---

## 第 4 页

**例**：若设 $g(x) = a + bx + cx^2$。选择 $a, b, c$ 使 $g(x_i)$ 可以拟合

| $i$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $x_i$ | 0 | 1 | 2 | 3 | 4 |
| $y_i$ | 4 | 7 | 12 | 39 | 54 |

**（红）☆** $a\cdot e^{-bx}$（$b$ 处有「√」标记）

**☆**

$$
\begin{cases}
y_1 = a + bx_1 + cx_1^2\\
y_2 = a + bx_2 + cx_2^2\\
\quad\vdots\\
y_5 = a + bx_5 + cx_5^2
\end{cases}
\qquad \text{不相容方程}
$$

$$
\Longrightarrow\ y(x)\ \bumpeq\ g(x) = a + bx + cx^2 = a\cdot f_1(x) + b\cdot f_2(x) + c\cdot f_3(x)
$$

其中 $f_1(x) = 1$，$f_2(x) = x$，$f_3(x) = x^2$。

（图示：$y$–$x$ 散点与红色拟合曲线。）

此时

$$
\|\vec{y} - \bar{\vec{y}}\|_2^2 = \sum_{i=1}^{5}\big(y_i - af_1(x_i) - bf_2(x_i) - cf_3(x_i)\big)^2\ \text{最小}
$$

$$
\Longrightarrow\ \|\vec{y} - F\vec{x}\|_2^2\ \text{最小}
$$

其中

$$
\vec{y} = \begin{bmatrix}y_1\\y_2\\y_3\\y_4\\y_5\end{bmatrix},\qquad
\vec{x} = \begin{bmatrix}a\\b\\c\end{bmatrix},\qquad
F = \begin{bmatrix}
f_1(x_1) & f_2(x_1) & f_3(x_1)\\
f_1(x_2) & f_2(x_2) & f_3(x_2)\\
\vdots & \vdots & \vdots\\
f_1(x_5) & f_2(x_5) & f_3(x_5)
\end{bmatrix}
$$

$$
\Longrightarrow\ F^{\mathsf T}\cdot F\cdot\vec{x} = F^{\mathsf T}\cdot\vec{y}\qquad (\text{法方程求解})
$$

---

## 第 5 页

### 2. 初等变换矩阵

变换矩阵形式：$E\in\mathbb{C}^{n\times n}$，

$$
E(\vec{u}, \vec{v}, \sigma) = I - \sigma\cdot\vec{u}\cdot\vec{v}^{\mathsf T}
$$

### 2.1 Gauss 变换

取 $\sigma = -1$，

$$
\vec{u}^{\mathsf T} = [\,0,\cdots,0,\ 0,\ l_{j+1,j},\ l_{j+2,j},\ \cdots,\ l_{n,j}\,],\qquad
\vec{v}^{\mathsf T} = [\,0,\cdots,0,\ 1,\ 0,\cdots,0\,]\ (j\text{-th})
$$

$$
L_j = I + \vec{u}\cdot\vec{v}^{\mathsf T}
= \begin{bmatrix}
1 & & & & \\
 & \ddots & & & \\
 & & 1 & & \\
 & & l_{j+1,j} & & \\
 & & l_{j+2,j} & \ddots & \\
 & & \vdots & & \\
 & & l_{n,j} & & 1
\end{bmatrix}
$$

### 2.2 Householder 变换

取 $\sigma = \dfrac{2}{\vec{v}^{\mathsf T}\cdot\vec{v}}$，$\vec{u} = \vec{v}$，$\vec{v}$ 可以任意取。

$$
H = I - \sigma\cdot\vec{u}\cdot\vec{v}^{\mathsf T}
= I - \frac{2}{\vec{v}^{\mathsf T}\cdot\vec{v}}\cdot\vec{v}\cdot\vec{v}^{\mathsf T}
= I - \frac{2}{\|\vec{v}\|_2^2}\cdot\vec{v}\cdot\vec{v}^{\mathsf T}
= I - 2\vec{w}\cdot\vec{w}^{\mathsf T}
\qquad (\vec{w} = \vec{v}/\|\vec{v}\|_2)
$$

$\vec{v}$：Householder 向量。

### Householder 变换基本性质

**定理**：若 $H\in\mathbb{R}^{n\times n}$ 为一 Householder 矩阵，则有：

$$
(1)\ H^{\mathsf T} = H;\quad
(2)\ H^{\mathsf T}\cdot H = I;\quad
(3)\ H^2 = I;\quad
(4)\ \det(H) = -1.
$$

（5）$H$ 有特征值 $1, -1$，其中特征值 $1$ 的代数重数为 $n-1$。

**证明**：

(1) $H^{\mathsf T} = (I - 2\vec{w}\vec{w}^{\mathsf T})^{\mathsf T} = I - 2(\vec{w}\cdot\vec{w}^{\mathsf T}) = H$.

(2) $H^{\mathsf T}\cdot H = (I - 2\vec{w}\vec{w}^{\mathsf T})\cdot(I - 2\vec{w}\vec{w}^{\mathsf T}) = I - 4\vec{w}\vec{w}^{\mathsf T} + 4\vec{w}(\vec{w}^{\mathsf T}\vec{w})\vec{w}^{\mathsf T} = I$.

(3) $H^2 = H^{\mathsf T}\cdot H = I$.

**（几何反射性）** $\forall\,\vec{x}\in\mathbb{R}^n$，若 $\vec{x} = \beta\vec{w} + \alpha\vec{w}$，其中 $\vec{w}^{\mathsf T}\vec{w} = 0$，$\beta\ne 0$（且 $\vec{w}\ne\vec{0}$）。

（注：原文此处两个向量均写作 $\vec{w}$（记号略有区别），其一与 $\vec{w}$ 正交（$\vec{w}^{\mathsf T}\vec{w}=0$ 的两个向量）。）

---

## 第 6 页

（接上页）

$$
\Longrightarrow\ H\vec{x} = (I - 2\vec{w}\vec{w}^{\mathsf T})(\beta\vec{w} + \alpha\vec{w})
= \beta\vec{w} + \alpha\vec{w} - 2\beta\vec{w}(\vec{w}^{\mathsf T}\cdot\vec{w}) - 2\alpha\vec{w}(\vec{w}^{\mathsf T}\cdot\vec{w})
$$

$$
= \beta\vec{w} + \alpha\vec{w} - \textcircled{0} - 2\alpha\vec{w} = \beta\vec{w} - \alpha\vec{w}
$$

（图示：平面 $\Omega$ 上的反射，$\beta\vec{x}$、$H\vec{x}$、$-\alpha\vec{w}$、$\vec{w}$、$\alpha\vec{w}$。）

※ $H\vec{x}$ 与 $\vec{x}$ 关于 $\Omega$（平面）对称；$\Omega$ 法向量为 $\vec{w}$。

### 利用反射性确定 $H$ 的特征值与特征向量

$$
H\vec{x} = \lambda\vec{x}
\qquad \text{※ } H\vec{x} \text{ 与 } \vec{x} \text{ 关于 } \Omega \text{ 镜面对称}
$$

① $\vec{x}\parallel\vec{w}$：$H\vec{x} = -\vec{x}$，特征值为 $-1$，特征向量为 $\vec{w}$。

② $\vec{x}^{\mathsf T}\cdot\vec{w} = 0$：$H\vec{x} = \vec{x}$，特征值为 $1$，特征向量可以为 $\Omega$ 内任意向量，对应代数重数为 $n-1$。

$$
\vec{x}^{\mathsf T}\cdot\vec{w} = 0
\ \Longleftrightarrow\
(w_1, w_2, \cdots, w_n)\begin{bmatrix}t_1\\t_2\\\vdots\\t_n\end{bmatrix} = 0
\ \Longrightarrow\ \text{$n$ 个未知量，$1$ 个方程。}
$$

（右图示：$\vec{x}\perp\vec{w}$ 与 $\vec{x}\parallel\vec{w}$ 两种情形。）

---

## 第 7 页

### 利用 Householder 变换性质，确定 $H$，将给定列向量变换到搜索方向上

给定 $\vec{x}\in\mathbb{R}^n$，$\|\vec{x}\|_2 = 1$。（红：要求 $H\vec{x}_1 = \vec{e}$。）

① （图：$\vec{e}$ 与 $\vec{x}$，$H\vec{x}\to\|\vec{x}\|_2\vec{e}$）

$$
H = I - 2\vec{w}\vec{w}^{\mathsf T},\qquad
\vec{w} = \frac{\vec{x} - \|\vec{x}\|_2\cdot\vec{e}}{\|\vec{x} - \|\vec{x}\|_2\cdot\vec{e}\|_2}
$$

② （红注：$H\vec{x}\to-\|\vec{x}\|_2\vec{e}$；图：$\vec{x}$ 与 $-\|\vec{x}\|_2\vec{e}$）

$$
H = I - 2\vec{w}\vec{w}^{\mathsf T},\qquad
\vec{w} = \frac{\vec{x} + \|\vec{x}\|_2\cdot\vec{e}}{\|\vec{x} + \|\vec{x}\|_2\cdot\vec{e}\|_2}
$$

### 2.3 Givens 变换

$G$ 变换矩阵：

$$
G = I + (\cos\theta - 1)\underbrace{(\vec{e}_i\vec{e}_i^{\mathsf T} + \vec{e}_j\vec{e}_j^{\mathsf T})}_{\text{下划线}}
+ \sin\theta\underbrace{(\vec{e}_i\vec{e}_j^{\mathsf T} - \vec{e}_j\vec{e}_i^{\mathsf T})}_{\text{下划线}}
$$

---

## 第 8 页（原文第 7 页）

$$
\vec{e}_i = [\,0,\ 0,\ \cdots,\ 0,\ 1,\ 0,\ \cdots,\ 0\,]\quad (i\text{-th})
$$

$$
\vec{e}_i\cdot\vec{e}_i^{\mathsf T} = \begin{bmatrix} & & \\ & 1 & \\ & & \end{bmatrix}
\quad \to i\text{-th 行},\ \downarrow i\text{-th 列}
\qquad
\vec{e}_i\cdot\vec{e}_j^{\mathsf T} = \begin{bmatrix} & & \\ & 1 & \\ & & \end{bmatrix}
\quad \to i\text{-th 行},\ \downarrow j\text{-th 列}
$$

$$
G = \begin{bmatrix}
1 & & & & & & \\
 & \ddots & & & & & \\
 & & \cos\theta & \textcircled{2}\sin\theta & & & \\
 & & -\sin\theta & \textcircled{1}\cos\theta & & & \\
 & & & & \ddots & & \\
 & & & & & & 1
\end{bmatrix}
$$

（原文在 $(i,i)$、$(i,j)$、$(j,i)$、$(j,j)$ 处分别标注 $\textcircled{1}\cos\theta$、$\textcircled{2}\sin\theta$（蓝色「$S=\theta$」）、$-\sin\theta$、$\textcircled{2}\cos\theta$；并注明：$\Longrightarrow$ $i$-th 行：$[\cos\theta,\ \sin\theta]$；$\Longrightarrow$ $j$-th 行：$[-\sin\theta,\ \cos\theta]$。）

对于 $\vec{x}\in\mathbb{R}^n$，

$$
G\vec{x} =
\begin{bmatrix}
1 & & & & & \\
 & \ddots & & & & \\
 & & \cos\theta & \sin\theta & & \\
 & & -\sin\theta & \cos\theta & & \\
 & & & & \ddots & \\
 & & & & & 1
\end{bmatrix}
\begin{bmatrix}x_1\\ \vdots\\ x_i\\ \vdots\\ x_j\\ \vdots\\ x_n\end{bmatrix}
=
\begin{bmatrix}y_1\\ \vdots\\ y_i\\ \vdots\\ y_j\\ \vdots\\ y_n\end{bmatrix}
$$

$$
\Longrightarrow\ \begin{cases}
x_1 = y_1\\
x_2 = y_2\\
\cos\theta\cdot x_i + \sin\theta\cdot x_j = y_i\\
x_{i+1} = y_{i+1}\\
\quad\vdots\\
-\sin\theta\cdot x_i + \cos\theta\cdot x_j = y_j\\
\quad\vdots\\
x_n = y_n
\end{cases}
$$

$$
\Longrightarrow\ \begin{cases}
y_i = \cos\theta\cdot x_i + \sin\theta\cdot x_j\\
y_j = -\sin\theta\cdot x_i + \cos\theta\cdot x_j\\
y_k = x_k\quad (k\ne i, j)
\end{cases}
$$

（图示：$(y_i, x_i)$ 圆与角 $\theta$ 的旋转关系；右下：$x_1, x_2, x_3$ 坐标系中 $(x_1,x_2)$ 旋转到 $(y_1, y_2, x_3)$。）

---

## 第 9 页（原文第 8 页）

若需要 $y_j = 0$，取

$$
\cos\theta = \frac{x_i}{\sqrt{x_i^2 + x_j^2}},\qquad
\sin\theta = \frac{x_j}{\sqrt{x_i^2 + x_j^2}}
\ \Longrightarrow\ y_i = \sqrt{x_i^2 + x_j^2},\quad y_j = 0
$$

**（红）☆** Householder 与 Givens 变换都是正交变换：

$$
\|H\vec{x}\|_2^2 = (H\vec{x})^{\mathsf T}(H\vec{x}) = \vec{x}^{\mathsf T}H^{\mathsf T}H\vec{x} = \vec{x}^{\mathsf T}\vec{x} = \|\vec{x}\|_2^2
$$

Householder 变换可以一次性使 $x$ 中大量分量变为 0；Givens 变换一次只需一个。

### 3. QR 分解　（红注：$Q^{\mathsf T}\cdot Q = I$）

**QR 分解**：给定 $A\in\mathbb{R}^{m\times n}$（$m\ge n$），找到单位列正交矩阵 $Q\in\mathbb{C}^{m\times n}$ 与上三角矩阵 $R\in\mathbb{C}^{n\times n}$，使 $A = Q\cdot R$，则称 $Q, R$ 构成 $A$ 的 QR 分解。

※ 若 $A$ 为列满秩，则 $R$ 中对角元为正，且 $Q, R$ 唯一。

$$
Q = [\vec{q}_1, \vec{q}_2, \cdots, \vec{q}_n],\quad \vec{q}_i\in\mathbb{C}^m
\qquad
\text{（蓝注：} \Longrightarrow Q \text{ 构成 } m \text{ 维空间中一组标准正交基。}）
$$

$$
A = QR = [\vec{q}_1, \vec{q}_2, \cdots, \vec{q}_n]\cdot
\begin{bmatrix}
r_{11} & r_{12} & \cdots & r_{1n}\\
0 & r_{22} & \cdots & r_{2n}\\
0 & 0 & \ddots & \vdots\\
0 & 0 & \cdots & r_{nn}
\end{bmatrix}
$$

$$
= \big[\,r_{11}\vec{q}_1,\ \ r_{12}\vec{q}_1 + r_{22}\vec{q}_2,\ \ r_{13}\vec{q}_1 + r_{23}\vec{q}_2 + r_{33}\vec{q}_3,\ \ \cdots,\ \ \sum_{k=1}^{i}\vec{q}_k r_{ki},\ \ \cdots,\ \ \sum_{k=1}^{n}\vec{q}_k r_{kn}\,\big]
$$

$$
= [\vec{a}_1,\ \vec{a}_2,\ \cdots,\ \vec{a}_i,\ \cdots,\ \vec{a}_n]
$$

$$
\Longrightarrow\ \vec{a}_i = \sum_{k=1}^{i} \vec{q}_k\cdot r_{ki}
$$

对于 $Q$ 为单位正交矩阵，$\vec{q}_i^{\mathsf T}\vec{q}_j = \delta_{ij}$：

$$
\Longrightarrow\ r_{ji} = \vec{q}_j^{\mathsf T}\cdot\vec{a}_i = \vec{q}_j^{\mathsf T}\Big(\sum_{k=1}^{i}\vec{q}_k r_{ki}\Big) = \sum_{k=1}^{i}\delta_{jk}\cdot r_{ki}
\qquad (j\le i)
$$

### QR 分解计算

**① Gram–Schmidt 正交化**

第 1 步：$\vec{a}_1 = r_{11}\vec{q}_1$ $\Longrightarrow$ $r_{11} = \|\vec{a}_1\|_2$，$\vec{q}_1 = \vec{a}_1/r_{11}$；

第 2 步：$\vec{a}_2 = r_{12}\vec{q}_1 + r_{22}\vec{q}_2$ $\Longrightarrow$ $r_{12} = \vec{q}_1^{\mathsf T}\cdot\vec{a}_2$，$r_{22} = \|\vec{a}_2 - r_{12}\vec{q}_1\|_2$，$\vec{q}_2 = (\vec{a}_2 - r_{12}\vec{q}_1)/r_{22}$；

---

## 第 10 页（原文第 9 页）

第 3 步：$\vec{a}_3 = r_{13}\vec{q}_1 + r_{23}\vec{q}_2 + r_{33}\vec{q}_3$ $\Longrightarrow$ $r_{13} = \vec{q}_1^{\mathsf T}\cdot\vec{a}_3$，$r_{23} = \vec{q}_2^{\mathsf T}\cdot\vec{a}_3$

$$
r_{33} = \|\vec{a}_3 - r_{13}\vec{q}_1 - r_{23}\vec{q}_2\|_2,\qquad
\vec{q}_3 = (\vec{a}_3 - r_{13}\vec{q}_1 - r_{23}\vec{q}_2)/r_{33}
$$

$\vdots$

第 $i$ 步：$\vec{a}_i = \sum_{k=1}^{i} r_{ki}\vec{q}_k\ (\vec{q}_1, \cdots, \vec{q}_{i-1}\text{ 已知})$ $\Longrightarrow$ $r_{ji} = \vec{q}_j^{\mathsf T}\cdot\vec{a}_i\ (j < i)$

$$
r_{ii} = \|\vec{a}_i - \sum_{k=1}^{i-1} r_{ki}\vec{q}_k\|_2,\qquad
\vec{q}_i = \big(\vec{a}_i - \sum_{k=1}^{i-1} r_{ki}\vec{q}_k\big)\Big/r_{ii}
$$

**GS 正交化计算流程：**

```
给定 A, Q = A, y = 0
for i in 1~n:                （外循环）
    y = a_i
    for j in 1~i−1:          （内循环）
        r_{ji} = q_j^T · a_i     （a_i 有红色下划线）
        y = y − r_{ji}·q_j
    r_{ii} = ‖y‖₂
    q_i = y / r_{ii}
```

（红注：第 3 步　① $r_{13}$，$\vec{y} = \vec{a}_3 - r_{13}\vec{q}_1$；② $r_{23}$，$\vec{y} = \vec{y} - r_{23}\vec{q}_2$；☆ $\vec{y} = \vec{a}_3 - r_{13}\vec{q}_1 - r_{23}\vec{q}_2$。）

**（蓝）☆ Modified GS 正交化（MGS 正交化）计算流程：**

```
给定 A, Q = 0
for i in 1~n:
    y = a_i
    for j in 1~i−1:
        r_{ji} = q_j^T · y
        y = y − r_{ji}·q_j
    r_{ii} = ‖y‖₂
    q_i = y / r_{ii}
```

---

## 第 11 页（原文第 10 页）

**② Householder 消元**（设 $A\in\mathbb{R}^{5\times 4}$）

**（红）☆** $A = [\vec{a}_1, \vec{a}_2, \cdots, \vec{a}_n]$，将 $\vec{a}_1 \to m\cdot[1, 0, 0, \cdots, 0]^{\mathsf T}$。

**第 1 步**：取 $\vec{v} = \|\vec{a}_1\|_2\cdot\vec{e} = \|\vec{a}_1\|_2\cdot[1, 0, 0, \cdots, 0]^{\mathsf T}$（$m$ 个），构造 $H_1$，使 $H_1\vec{a}_1 = \vec{v}$。

$$
\Longrightarrow\ H_1A = H_1[\vec{a}_1, \vec{a}_2, \cdots, \vec{a}_n]
= [H_1\vec{a}_1,\ H_1\vec{a}_2,\ \cdots,\ H_1\vec{a}_n]
= [\vec{v},\ H_1\vec{a}_2,\ \cdots,\ H_1\vec{a}_n]
$$

$$
\Longrightarrow\ H_1\begin{bmatrix}\times&\times&\times\\ \times&\times&\times\\ \times&\times&\times\\ \times&\times&\times\\ \times&\times&\times\end{bmatrix}
= \begin{bmatrix} \|\vec{a}_1\|_2 & *' & *'\\ 0 & *' & *'\\ 0 & *' & *'\\ 0 & *' & *'\\ 0 & *' & *' \end{bmatrix}
= A_1 =
\begin{bmatrix} \|\vec{a}_1\|_2 & \Big| & \\ 0 & \Big| & \tilde{A}_1\\ 0 & \Big| & \\ 0 & \Big| & \\ 0 & \Big| & \end{bmatrix},
\qquad \tilde{A}_1\in\mathbb{R}^{4\times 3}
$$

其中 $H_1 = I - 2\vec{w}_1\vec{w}_1^{\mathsf T}$，$\vec{w}_1 = (\vec{a}_1 + \|\vec{a}_1\|_2\vec{e})/\|\vec{a}_1 + \|\vec{a}_1\|_2\vec{e}\|_2$。

**第 2 步**：构造 $H_2$，使 $\tilde{A}_1$ 第 1 列 $\to \|\tilde{\vec{a}}_1\|_2\cdot[1, 0, 0, \cdots, 0]^{\mathsf T}$（$(m-1)$ 个）。

（红色图示：$\tilde{A}_1$ 的第一列（蓝色框出）$\to$ 下方元素变为 0。）

令

$$
H_2 = \begin{bmatrix} I_{1\times 1} & 0\\ 0 & \tilde{H}_2 \end{bmatrix}
= \begin{bmatrix}
1 & 0 & 0 & 0 & 0\\
0 & & & & \\
0 & & & & \\
\vdots & & \tilde{H}_2 & & \\
0 & & & &
\end{bmatrix}
$$

$$
\Longrightarrow\ H_2A_1 = \begin{bmatrix} I & 0\\ 0 & \tilde{H}_2 \end{bmatrix}
\begin{bmatrix} * \\ 0 \\ \tilde{\vec{a}}_1\Big| \tilde{A}_1 \end{bmatrix}
\ \longrightarrow\ \mathbb{R}^{5\times 3}
= \begin{bmatrix} * \\ 0 \\ \textcircled{$\tilde{H}_2\tilde{A}_1$} \end{bmatrix}
$$

（旁注：$\tilde{H}\in\mathbb{R}^{4\times 4}$，$\tilde{A}_1\in\mathbb{R}^{4\times 3}$。）

$$
= \begin{bmatrix} * & \times & \times & \times\\ 0 & \times & \times & \times\\ 0 & \times & \times & \times\\ 0 & \times & \times & \times\\ 0 & \times & \times & \times \end{bmatrix}
= \begin{bmatrix} \times & \times & \times & \times\\ 0 & \times & \times & \times\\ 0 & 0 & \times & \times\\ 0 & 0 & \times & \times\\ 0 & 0 & \times & \times \end{bmatrix}
= A_2
\qquad \text{（红圈：} \tilde{A}_2 = A_2 \text{ 的右下子块）}
$$

---

## 第 12 页（原文第 11 页）

※ $\tilde{H}_2 = I - 2\vec{w}'_2\cdot(\vec{w}'_2)^{\mathsf T}$，

$$
\vec{w}'_2 = \frac{\tilde{\vec{a}}_1 - \|\tilde{\vec{a}}_1\|_2\cdot\vec{e}'_1}{\|\tilde{\vec{a}}_1 - \|\tilde{\vec{a}}_1\|_2\cdot\vec{e}'_1\|_2},
\qquad
\vec{e}'_1 = [1, 0, 0, \cdots, 0]^{\mathsf T}\ (m-1 \text{ 个})
$$

$$
H_2 = I - 2\vec{w}_2\cdot\vec{w}_2^{\mathsf T},\qquad \vec{w}_2 = \begin{bmatrix} 0\\ \vec{w}'_2 \end{bmatrix}
$$

**第 3 步**：构造 $H_3$，使 $H_3$ 作用在 $\tilde{A}_2$ 第 1 列 $\to q\cdot[1, 0, 0, \cdots, 0]^{\mathsf T}$（$(m-2)$ 个）。

（注：系数原文写作单个字符「$q$」。）

令

$$
H_3 = \begin{bmatrix} I_{2\times 2} & 0\\ 0 & \tilde{H}_3 \end{bmatrix}
= \begin{bmatrix}
1 & 0 & 0 & 0 & 0\\
0 & 1 & 0 & 0 & 0\\
0 & 0 & & & \\
0 & 0 & & \tilde{H}_3 & \\
0 & 0 & & &
\end{bmatrix}
$$

$$
H_3A_2 = A_3 =
\begin{bmatrix}
\times & \times & \times & \times\\
0 & \times & \times & \times\\
0 & 0 & * & \times\\
0 & 0 & * & \times\\
0 & 0 & 0 & \times
\end{bmatrix}
\qquad
\text{（蓝注：} = I_{m-k+1} - \beta_R\,\vec{v}_R\,\vec{v}_R^{\mathsf T}\text{）}
$$

$\vdots$

**第 $k$ 步**：构造

$$
H_k = \begin{bmatrix} I_{k-1} & 0\\ 0 & \tilde{H}_k \end{bmatrix},
\qquad \tilde{H}_k\in\mathbb{R}^{(m-k+1)\times(m-k+1)},
\qquad \tilde{H}_k = I - \beta_R\cdot\vec{v}_R\vec{v}_R^{\mathsf T}
\ \text{（蓝，下划线）}
$$

$H_kA_{k-1} = A_k$，使 $A_k$ 第 $k$ 列对角元以下元素 $=0$。

**最后一步**（若 $m = n$，最后一步是第 $n-1$ 步；若 $m > n$，则最后一步为第 $n$ 步）：

$$
A_n = H_nA_{n-1} =
\begin{bmatrix}
\times & \times & \times & \times\\
0 & \times & \times & \times\\
0 & 0 & \times & \times\\
0 & 0 & 0 & \times\\
0 & 0 & 0 & 0
\end{bmatrix}\in\mathbb{R}^{m\times n}
$$

---

## 第 13 页（原文第 12 页）

### 总结之前计算流程

$$
A_n = H_nA_{n-1} = H_nH_{n-1}\cdot A_{n-2} = \cdots = H_nH_{n-1}\cdots H_1A
$$

※ 由于 $A_n$ 可以看作上三角矩阵，$(H_nH_{n-1}\cdots H_1)^{-1}$ 是否为正交？（红注：「正交？」）

$$
\Longrightarrow\ A = (H_nH_{n-1}\cdots H_1)^{-1}\cdot A_n
$$

※ 由于 $H_i$ 为 Householder 矩阵，$H_i^{-1} = H_i^{\mathsf T} = H_i$，$A_n\in\mathbb{R}^{m\times n}$：

$$
\Longrightarrow\ A = (H_1H_2\cdots H_n)\cdot A_n = H\cdot A_n
\ \Longrightarrow\ H\ \text{为正交矩阵}，\ H\in\mathbb{R}^{m\times m}
$$

※ $H^{\mathsf T}\cdot H = (H_1\cdots H_n)^{\mathsf T}\cdot(H_1\cdots H_n) = H_n^{\mathsf T}\cdots H_1^{\mathsf T}\cdot H_1\cdots H_n = I$

$$
\Longrightarrow\ A = [\vec{a}_1, \vec{a}_2, \cdots, \vec{a}_n],\qquad
H = [\vec{h}_1, \vec{h}_2, \cdots, \vec{h}_m]
\qquad \text{（旁注：前 } n \text{ 列构成 } Q \text{ 矩阵）}
$$

$$
A_n = \begin{bmatrix}
r_{11} & r_{12} & \cdots & r_{1n}\\
0 & r_{22} & \cdots & r_{2n}\\
\vdots & & \ddots & \vdots\\
0 & 0 & \cdots & r_{nn}\\
0 & 0 & \cdots & 0\\
\vdots & \vdots & & \vdots\\
0 & 0 & \cdots & 0
\end{bmatrix}\ \longrightarrow\ R\ \text{（红框）}
$$

$$
\Longrightarrow\ \vec{a}_1 = \vec{h}_1\cdot r_{11},\quad
\vec{a}_2 = \vec{h}_1r_{12} + \vec{h}_2r_{22},\quad
\vec{a}_3 = \vec{h}_1r_{13} + \vec{h}_2r_{23} + \vec{h}_3r_{33},\ \cdots
$$

$$
\vec{a}_i = \sum_{j=1}^{i}\vec{h}_j\cdot r_{ji},\ \cdots,\ \vec{a}_n = \sum_{j=1}^{n}\vec{h}_j r_{jn}
$$

因此 $A = H\cdot A_n$ 以及 $A = Q\cdot R$，其中 $Q = [\vec{q}_1, \vec{q}_2, \cdots, \vec{q}_n]$，$R$ 为上三角。

习得 $Q = [\vec{q}_1, \cdots, \vec{q}_n] = [\vec{h}_1, \cdots, \vec{h}_n]$，$A_n$ 前 $n$ 行与 $R$ 相同。

**（红）☆** $A = QR$，其中 $A\in\mathbb{R}^{m\times n}$，$Q$ 为正交阵且 $Q\in\mathbb{R}^{m\times m}$，$R$ 为上三角阵且 $R\in\mathbb{R}^{m\times n}$，则称 $QR$ 为 $A$ 的**完全 QR 分解**。

### 其 Householder 变换的 QR 分解计算流程

**☆** 计算中每一步需要

$$
H_k = I_{m+1-k} - 2\vec{w}_k\cdot\vec{w}_k^{\mathsf T}\quad (\|\vec{w}_k\|_2 = 1)
$$

---

## 第 14 页（原文第 13 页）

$$
= I_{m+1-k} - 2\cdot\frac{\vec{v}_k\vec{v}_k^{\mathsf T}}{\vec{v}_k^{\mathsf T}\vec{v}_k}
= I_{m+1-k} - \beta_k\vec{v}_k\vec{v}_k^{\mathsf T}
$$

其中

$$
\beta_k = \frac{2}{\vec{v}_k^{\mathsf T}\vec{v}_k},\qquad
\vec{v}_k = [v_{k1},\ v_{k2},\ \cdots,\ v_{k,m+1-k}]^{\mathsf T}
$$

对（$\vec{v}_k = \vec{a} - \|\vec{a}\|_2\cdot\vec{e}_1$）$\downarrow$

$$
\vec{v}_k = [1,\ v'_{k2},\ v'_{k3},\ \cdots,\ v'_{k,m+1-k}]^{\mathsf T}
$$

通过计算得到：

$$
\begin{bmatrix}
r_{11} & r_{12} & r_{13} & \cdots & r_{1n}\\
v_{12} & r_{22} & r_{23} & \cdots & r_{2n}\\
v_{13} & v_{23} & r_{33} & \cdots & r_{3n}\\
v_{14} & v_{24} & v_{34} & \cdots & r_{4n}\\
\vdots & \vdots & \vdots & & \vdots\\
v'_{1,m} & v'_{2,m-1} & v'_{3,m-2} & \cdots & v'_{n,m-n+1}
\end{bmatrix}
$$

（蓝注：对角线为 $r$，以下分别对每一个 $H$（Householder）的 $\vec{v}$ 向量。）

**计算过程中不保留 $H_k$ 矩阵（也不保留 $\tilde{H}_k$），只保留 $\vec{v}_k$。**

**计算流程：**

```
for k in 1~n:
    计算 A 的第 k 列 m 行, 第 k 列 (m−k) 阶 Householder 变换 ⟹ ṽ_k, β_k
    更新 A 第 k 行 ~ m 行, 第 k 列 ~ 第 n 列 (子矩阵) 中的元素:
        A(k:m, k:n) = (I − β_k·ṽ_k·ṽ_k^T)·A(k:m, k:n)
                    = A(k:m, k:n) − β_k·ṽ_k·(ṽ_k^T·A(k:m, k:n))
```

---

## 第 15 页（原文第 14 页）

**例**：$A = \begin{bmatrix} 1 & 2 & 3\\ 0 & 3 & 2\\ 2 & 0 & 1 \end{bmatrix}$，利用 Householder 变换的 QR 分解。

**解**：① $\vec{y} = [1;\ 0;\ 2]$

$$
\Longrightarrow\ \vec{v}_1 = \vec{y} - \|\vec{y}\|_2\cdot\begin{bmatrix}1\\0\\0\end{bmatrix}
= \begin{bmatrix} 1-\sqrt{5}\\ 0\\ 2 \end{bmatrix}
$$

$$
\Longrightarrow\ H_1 = I_3 - \frac{2}{\vec{v}_1^{\mathsf T}\vec{v}_1}\cdot\vec{v}_1\vec{v}_1^{\mathsf T}
= \begin{bmatrix} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1 \end{bmatrix}
- \frac{2}{(1-\sqrt{5})^2 + 2^2}\cdot\vec{v}_1\vec{v}_1^{\mathsf T}
= \begin{bmatrix} 1/\sqrt{5} & 0 & 2/\sqrt{5}\\ 0 & 1 & 0\\ 2/\sqrt{5} & 0 & -1/\sqrt{5} \end{bmatrix}
$$

$$
\Longrightarrow\ A_1 = H_1A =
\begin{bmatrix}
\sqrt{5} & 2/\sqrt{5} & \sqrt{5}\\
0 & 3 & 2\\
0 & 4/\sqrt{5} & \sqrt{5}
\end{bmatrix}
$$

② $\vec{y} = \begin{bmatrix} 3\\ 4/\sqrt{5} \end{bmatrix}$

$$
\Longrightarrow\ \vec{v}_2 = \vec{y} - \|\vec{y}\|_2\begin{bmatrix}1\\0\end{bmatrix}
= \begin{bmatrix} 3 - \sqrt{61}/5\\ 4/\sqrt{5} \end{bmatrix}
$$

（注：末项为原文写法；按 $\|\vec{y}\|_2 = \sqrt{3^2 + (4/\sqrt{5})^2} = \sqrt{61/5}$ 理解。）

$$
\Longrightarrow\ \tilde{H}_2 = I_2 - \frac{2}{\vec{v}_2^{\mathsf T}\cdot\vec{v}_2}\cdot\vec{v}_2\cdot\vec{v}_2^{\mathsf T}
= \begin{bmatrix} * & *\\ * & * \end{bmatrix}
$$

$$
\Longrightarrow\ H_2 = \begin{bmatrix} 1 & 0 & 0\\ 0 & * & *\\ 0 & * & * \end{bmatrix}
$$

$$
\Longrightarrow\ A_2 = H_2A_1
$$

最后 $R = A_2$，$Q = (H_2H_1)^{-1} = H_1H_2$。

---

## 第 16 页（原文第 15 页）

### 4. 基于 QR 分解的最小二乘　（蓝注：且 $A$ 列满秩）

**完全 QR 分解**：考虑 $A\in\mathbb{R}^{m\times n}$，$A = QR$，其中 $Q\in\mathbb{R}^{m\times m}$，$R\in\mathbb{R}^{m\times n}$（$m\ge n$）。

$$
\text{☆ } R = \begin{bmatrix} \tilde{R} \\ \hline 0 \end{bmatrix}
\begin{matrix} \leftarrow n \text{ 行}\\ \leftarrow m-n \text{ 行} \end{matrix}
$$

※ $A = Q'R'$，其中 $Q'\in\mathbb{R}^{m\times n}$ 列正交，$R'\in\mathbb{R}^{n\times n}$ 上三角。

$$
Q = [Q',\ Q''],\quad Q', Q'' \text{ 均为列正交}，\ Q''\in\mathbb{R}^{m\times(m-n)};
\qquad R = \begin{bmatrix} R' \\ \hline 0 \end{bmatrix}
\begin{matrix} n\times n\\ (m-n)\times n \end{matrix}
$$

### 回到最小二乘问题

$$
\|A\vec{x} - \vec{b}\|_2^2 = \|QR\vec{x} - \vec{b}\|_2^2 = (QR\vec{x} - \vec{b})^{\mathsf T}(QR\vec{x} - \vec{b})
$$

$$
= (\vec{x}^{\mathsf T}R^{\mathsf T}Q^{\mathsf T} - \vec{b}^{\mathsf T})(QR\vec{x} - \vec{b})
= \vec{x}^{\mathsf T}R^{\mathsf T}Q^{\mathsf T}QR\vec{x} - \vec{b}^{\mathsf T}QR\vec{x} - \vec{x}^{\mathsf T}R^{\mathsf T}Q^{\mathsf T}\vec{b} + \vec{b}^{\mathsf T}\vec{b}
$$

$$
= \vec{x}^{\mathsf T}R^{\mathsf T}R\vec{x} - (Q^{\mathsf T}\vec{b})^{\mathsf T}\cdot R\vec{x} - (R\vec{x})^{\mathsf T}\cdot Q^{\mathsf T}\vec{b} + \vec{b}^{\mathsf T}(Q^{\mathsf T}Q)\vec{b}
= \|R\vec{x} - Q^{\mathsf T}\vec{b}\|_2^2
$$

**☆**

$$
R\vec{x} =
\begin{bmatrix}
r_{11} & r_{12} & \cdots & r_{1n}\\
0 & r_{22} & \cdots & r_{2n}\\
\vdots & & \ddots & \vdots\\
0 & 0 & \cdots & r_{nn}\\
0 & 0 & \cdots & 0\\
\vdots & \vdots & & \vdots\\
0 & 0 & \cdots & 0
\end{bmatrix}
\begin{bmatrix} x_1\\ x_2\\ \vdots\\ x_n \end{bmatrix}
=
\begin{bmatrix}
\sum_{k=1}^{n} r_{1k}x_k\\
\sum_{k=2}^{n} r_{2k}x_k\\
\vdots\\
r_{nn}x_n\\
0\\
\vdots\\
0
\end{bmatrix}
\begin{matrix} \left\} n\ \text{项} \right.\\ \\ \\ \\ \left\} m-n\ \text{项} \right. \end{matrix}
$$

$$
Q^{\mathsf T}\vec{b} = [\vec{q}_1, \cdots, \vec{q}_m]^{\mathsf T}\cdot\vec{b}
= \begin{bmatrix}
\vec{q}_1^{\mathsf T}\cdot\vec{b}\\
\vec{q}_2^{\mathsf T}\cdot\vec{b}\\
\vdots\\
\vec{q}_n^{\mathsf T}\cdot\vec{b}\\
\vec{q}_{n+1}^{\mathsf T}\cdot\vec{b}\\
\vdots\\
\vec{q}_m^{\mathsf T}\cdot\vec{b}
\end{bmatrix}
\begin{matrix} \left\} n\ \text{项} \right.\\ \\ \\ \left\} m-n\ \text{项} \right. \end{matrix}
$$

---

## 第 17 页（原文第 16 页）

$$
\Longrightarrow\ R\vec{x} - Q^{\mathsf T}\vec{b} =
\begin{bmatrix}
\sum_{k=1}^{n} r_{1k}x_k - \vec{q}_1^{\mathsf T}\cdot\vec{b}\\[3pt]
\sum_{k=2}^{n} r_{2k}x_k - \vec{q}_2^{\mathsf T}\cdot\vec{b}\\
\vdots\\
r_{nn}x_n - \vec{q}_n^{\mathsf T}\cdot\vec{b}\\[3pt]
0 - \vec{q}_{n+1}^{\mathsf T}\cdot\vec{b}\\
0 - \vec{q}_{n+2}^{\mathsf T}\cdot\vec{b}\\
\vdots\\
0 - \vec{q}_m^{\mathsf T}\cdot\vec{b}
\end{bmatrix}
$$

$$
\Longrightarrow\ \min_{\vec{x}\in\mathbb{R}^n}\|R\vec{x} - Q^{\mathsf T}\vec{b}\|_2^2
= \min_{x_1,\cdots,x_n}\Big(\sum_{i=1}^{n}\big(\sum_{k=i}^{n}r_{ik}x_k - \vec{q}_i^{\mathsf T}\vec{b}\big)^2\Big)\ \text{（蓝注：前 } n \text{ 项）}
$$

$$
\ge C
\qquad +\ \min_{x_1,\cdots,x_n}\Big(\sum_{i=n+1}^{m}\big(0 - \vec{q}_i^{\mathsf T}\vec{b}\big)^2\Big)\ \text{（后 } m-n \text{ 项，常数）}
$$

$$
= \min_{x_1,\cdots,x_n}\Big(\sum_{i=1}^{n}\big(\sum_{k=i}^{n}r_{ik}x_k - \vec{q}_i^{\mathsf T}\vec{b}\big)^2\Big) + C
$$

$$
\Longrightarrow\ \min_{\vec{x}\in\mathbb{R}^n}\|R\vec{x} - Q^{\mathsf T}\vec{b}\|_2^2
\ \Longleftrightarrow\ \sum_{k=i}^{n} r_{ik}x_k = \vec{q}_i^{\mathsf T}\cdot\vec{b},\quad \forall\, i\in\{1, \cdots, n\}
$$

**（红框）☆**

$$
\begin{cases}
r_{11}x_1 + r_{12}x_2 + \cdots + r_{1n}x_n = b'_1 = \vec{q}_1^{\mathsf T}\cdot\vec{b}\\
\phantom{r_{11}x_1 +{}} r_{22}x_2 + \cdots + r_{2n}x_n = b'_2 = \vec{q}_2^{\mathsf T}\vec{b}\\
\quad\vdots\\
\phantom{r_{11}x_1 + \cdots +{}} r_{nn}x_n = b'_n = \vec{q}_n^{\mathsf T}\cdot\vec{b}
\end{cases}
\qquad \text{回代}
$$

---

## 第 18 页（原文第 17 页）

参数中 $r_{ij}$ 来源于 QR 分解中的 $R$ 矩阵，在 QR 分解已知后，方程组可利用回代快速求解。

※ 如何快速计算 $b'_i = \vec{q}_i^{\mathsf T}\cdot\vec{b}\ (i = 1, 2, \cdots, n)$？

若完全 QR 分解中，$Q = H_1^{\mathsf T}H_2^{\mathsf T}\cdots H_{m-1}^{\mathsf T}$

此时

$$
\vec{b}' = Q^{\mathsf T}\cdot\vec{b} = H_{m-1}H_{m-2}\cdots H_2H_1\vec{b}\quad (\text{红注：} m-1 \text{ 个})
$$

$$
= \underbrace{\big(H_{m-1}H_{m-2}\cdots H_{n+1}\big)}_{\text{红下划线；}H_{n+1}\text{ 上有红叉}}\cdot\underbrace{\big(H_nH_{n-1}\cdots H_1\big)}_{\text{红下划线}}\vec{b}
$$

此时对于 $H_p$，当 $p\in[n+1,\ m-1]$：

$$
H_p = \begin{bmatrix} I_{p-1} & 0\\ 0 & \tilde{H}_p \end{bmatrix},
\qquad \tilde{H}_p\in\mathbb{R}^{m-p+1}
$$

$$
\Longrightarrow\ H_p\cdot\vec{q} = \begin{bmatrix} I_{p-1} & \\ & \tilde{H}_p \end{bmatrix}
\begin{bmatrix} \vec{q}_1 \\ \tilde{\vec{q}}_p \end{bmatrix}
\to\ \begin{matrix} p-1\ \text{项}\\ m-p+1\ \text{项} \end{matrix}
= \begin{bmatrix} \vec{q}_1 \\ \tilde{H}_p\tilde{\vec{q}}_p \end{bmatrix}
$$

$$
\Longrightarrow\ H_p\ \text{作用于向量时，不改变向量前 } p-1 \text{ 个分量，只改变后 } m-p+1 \text{ 个分量。}
$$

若 $p > n+1$，$H_p$ 作用于向量时不改变前 $n$ 个分量

$$
\Longrightarrow\ \text{求解最小二乘问题，只需考虑 } H_nH_{n-1}\cdots H_1\vec{b}\ \text{向量。}
$$

---

## 第 19 页（原文第 18 页）

（续前页）取前 $n$ 项，将其作为最后得到的解 $(\vec{x})$ 的左端项。

$$
\Longrightarrow\ \vec{b}' = H_nH_{n-1}\cdots H_2H_1\vec{b}\qquad \downarrow\ \vec{b}_1 = H_1\vec{b}
$$

$$
= H_nH_{n-1}\cdots H_2\vec{b}_1\qquad \downarrow\ \vec{b}_2 = H_2\vec{b}_1
$$

$$
= H_nH_{n-1}\cdots H_3\vec{b}_2
$$

※ $\vec{b}_i = H_i\cdot\vec{b}_{i-1}$，$\vec{b}' = H_n\cdot\vec{b}_{n-1} = \vec{b}_n$

此时

$$
\vec{b}_k = H_k\cdot\vec{b}_{k-1}
= \begin{bmatrix} I_{k-1} & 0\\ 0 & \tilde{H}_k \end{bmatrix}\vec{b}_{k-1}
= \begin{bmatrix} I_{k-1} & \\ & I_{m-k+1} - \beta_k\vec{v}_k\vec{v}_k^{\mathsf T} \end{bmatrix}\cdot\vec{b}_{k-1}
$$

$$
= \begin{bmatrix} I_{k-1} & \\ & I_{m-k+1} - \beta_k\vec{v}_k\vec{v}_k^{\mathsf T} \end{bmatrix}
\begin{bmatrix} \vec{b}_{k-1,1} \\ \vec{b}_{k-1,2} \end{bmatrix}
\to\ \begin{matrix} \text{前 } k-1 \text{ 行}\\ \text{后 } m-k+1 \text{ 行} \end{matrix}
= \begin{bmatrix} \vec{b}_{k-1,1} \\ \vec{b}_{k-1,2} - \beta_k(\vec{v}_k^{\mathsf T}\cdot\vec{b}_{k-1,2})\cdot\vec{v}_k \end{bmatrix}
$$

**（蓝）☆ 对比：**

| | 方程 | 说明 |
|---|---|---|
| 法方程 | $A^{\mathsf T}A\vec{x} = A^{\mathsf T}\vec{b}$ | $\mathrm{cond}(A^{\mathsf T}A)\sim(\mathrm{cond}(A))^2$ → 病态问题 |
| QR 分解 | $R\vec{x} = Q^{\mathsf T}\vec{b}$（上三角阵） | $\mathrm{cond}(R)\sim\mathrm{cond}(A)$ |

---

## 第 20 页（原文第 19 页）

### 5. 非满秩矩阵最小二乘问题

**（蓝）☆** 利用法方程：$A^{\mathsf T}A\vec{x} = A^{\mathsf T}\vec{b}$，$A\in\mathbb{R}^{m\times n}$，$A^{\mathsf T}A\in\mathbb{R}^{n\times n}$，$\det(A^{\mathsf T}A) = 0$。

若将 $A$ 做完全 QR 分解，$Q\in\mathbb{R}^{m\times m}$，$R\in\mathbb{R}^{m\times n}$

$$
\text{☆ } R = \begin{bmatrix}
r_{11} & r_{12} & r_{13} & r_{14}\\
0 & r_{22} & r_{23} & r_{24}\\
0 & 0 & r_{33} & r_{34}\\
0 & 0 & 0 & 0
\end{bmatrix}
$$

此时 $A = QR = Q[\vec{r}_1, \vec{r}_2, \vec{r}_3, \vec{r}_4]$ $\Longrightarrow$ $\vec{a}_i = Q\vec{r}_i$

对于 $A\vec{x} = \vec{b}$ 的最小二乘问题：$\min_{\vec{x}\in\mathbb{R}^n}\|A\vec{x} - \vec{b}\|_2^2$

设 $\mathrm{rank}(A) = k < n$，则 $\vec{b} = \vec{b}_1 + \vec{b}_2$，$\vec{b}_1\in R(A)$，$\vec{b}_2\in R(A)^{\perp}$。

其中

$$
R(A) = \{\vec{y}\in\mathbb{R}^m\ |\ \vec{y} = k_1\vec{a}_1 + k_2\vec{a}_2 + \cdots + k_n\vec{a}_n,\ \forall\, k_1, \cdots, k_n\in\mathbb{R}\}
$$

**① 若有 $m\ge n$**。设 $R(A) = R(Q_k)$，$Q_k\in\mathbb{R}^{m\times k}$（$m\ge n > k$）。

※ $Q_k$ 的列向量构成 $A$ 的列空间的一组基（标准正交基）。

$$
\Longrightarrow\ A = Q_k\cdot S\quad (S\in\mathbb{R}^{k\times n})
$$

$$
A\vec{x} = \vec{b}\ \Longrightarrow\ Q_k\cdot S\cdot\vec{x} = \vec{b}_1
\ \Longrightarrow\ Q_k^{\mathsf T}Q_k\cdot S\cdot\vec{x} = Q_k^{\mathsf T}\cdot\vec{b}_1
\ \Longrightarrow\ S\vec{x} = Q_k^{\mathsf T}(\vec{b} - \vec{b}_2) = Q_k^{\mathsf T}\cdot\vec{b}
$$

（蓝注：$S\in\mathbb{R}^{k\times n}$、$\vec{x}\in\mathbb{R}^{n\times 1}$；$Q_k^{\mathsf T}\in\mathbb{R}^{k\times m}$、$\vec{b}\in\mathbb{R}^{m\times 1}$；$Q_k^{\mathsf T}Q_k = I_k$。）

$$
\Longrightarrow\ \text{得到 } k \text{ 个方程，} n \text{ 个未知量}\ \Longrightarrow\ \text{多解问题}
$$

（蓝注：此时 $S$ 并不一定为上三角阵，也不一定具备部分上三角性质。）

**定理**：设 $A\in\mathbb{R}^{m\times n}$（$m\ge n$），$\mathrm{rank}(A) = k < n$，则存在列交换矩阵 $P$ 以及正交矩阵 $Q$（$Q\in\mathbb{R}^{m\times m}$），使

$$
AP = Q\begin{bmatrix} R_{11} & R_{12}\\ 0 & 0 \end{bmatrix}_{m\times n},
\qquad \text{其中 } R_{11}\in\mathbb{R}^{k\times k} \text{ 为非奇异上三角矩阵。}
$$

☆ $P = \begin{bmatrix} \ddots & & \bigcirc & \cdots & 1\\ & \ddots & \vdots & \udot & \\ & & 1 & \cdots & \bigcirc & \ddots\\ & & & & & \ddots & 1\\ & & & & & & \ddots \end{bmatrix}$ 型 0/1 交换矩阵（原文示意）。

---

## 第 21 页（原文第 20 页）

$$
\text{由于 } AP = Q\begin{bmatrix} R_{11} & R_{12}\\ 0 & 0 \end{bmatrix}
\begin{matrix} \to k\ \text{列}\\ \to m-k\ \text{行} \end{matrix}
\quad\begin{matrix} \downarrow\ \ k\ \text{列}\\ \downarrow\ n-k\ \text{列} \end{matrix}
\ \Longrightarrow\ A = Q\begin{bmatrix} R_{11} & R_{12}\\ 0 & 0 \end{bmatrix}P^{\mathsf T}
$$

$$
\Longrightarrow\ S = Q_k^{\mathsf T}\cdot A = Q_k^{\mathsf T}\cdot Q\begin{bmatrix} R_{11} & R_{12}\\ 0 & 0 \end{bmatrix}P^{\mathsf T}
= Q_k^{\mathsf T}\big[\,Q_k\quad Q_k'\,\big]\begin{bmatrix} R_{11} & R_{12}\\ 0 & 0 \end{bmatrix}P^{\mathsf T}
$$

（蓝注：「挪到拆分」，并有大括号连接 $Q$ 与 $[Q_k\ Q_k']$。）

$$
\Longrightarrow\ \big[\,Q_k^{\mathsf T}Q_k\quad Q_k^{\mathsf T}Q_k'\,\big]\begin{bmatrix} R_{11} & R_{12}\\ 0 & 0 \end{bmatrix}P^{\mathsf T}
= \begin{bmatrix} I_k & 0\\ \underset{k\times k}{\downarrow} & \underset{k\times(m-k)}{\downarrow} \end{bmatrix}
\begin{bmatrix} R_{11} & R_{12}\\ \underset{(m-k)\times k}{\underbrace{0\ \ 0}} & \underset{(m-k)\times(m-k)}{\underbrace{0\ \ 0}} \end{bmatrix}P^{\mathsf T}
$$

$$
= \big[\,R_{11}\quad R_{12}\,\big]P^{\mathsf T}
$$

$$
\Longrightarrow\ S\vec{x} = \big[\,R_{11}\quad R_{12}\,\big]\underbrace{P^{\mathsf T}\vec{x}}_{\vec{y}}
= \big[\,R_{11}\quad R_{12}\,\big]\vec{y} = Q_k^{\mathsf T}\cdot\vec{b}
$$

（旁注：$P$ 作用在 $\vec{x}$ 上使其中部分行交换。）

$$
\Longrightarrow\ \big[\,R_{11}\quad R_{12}\,\big]\begin{bmatrix}\vec{y}_1\\ \vec{y}_2\end{bmatrix} = Q_k^{\mathsf T}\cdot\vec{b}
\ \Longrightarrow\ R_{11}\vec{y}_1 + R_{12}\vec{y}_2 = Q_k^{\mathsf T}\cdot\vec{b}
$$

$$
\Longrightarrow\ \begin{bmatrix} \vec{y}_1\\ \vec{y}_2 \end{bmatrix}
= \begin{bmatrix} R_{11}^{-1}(Q_k^{\mathsf T}\vec{b} - R_{12}\vec{y}_2)\\ \vec{y}_2 \end{bmatrix}
\ \Longrightarrow\ \vec{x} = P^{\mathsf T}\vec{y} = P^{\mathsf T}\begin{bmatrix} R_{11}^{-1}(Q_k^{\mathsf T}\vec{b} - R_{12}\vec{y}_2)\\ \vec{y}_2 \end{bmatrix}
$$

其中 $\vec{y}_2\in\mathbb{R}^{n-k}$ 为一任意向量。

**② $m < n$**（$k = m$，$k < m$）：

- $k = m$：$A = Q[\tilde{R}\ \ \square]$，$Q\in\mathbb{R}^{m\times m}$
- $k < m$：$A = Q[\tilde{R}\ \ \square\ \ \square]$（图示）

### （蓝）线性方程组求解（知识总结图）

```
线性方程组求解
├── 相容（方阵, 可逆）
│     ├── 直接: Gauss消元、LU、Cholesky —— 是 O(n³)，特殊情况更快
│     └── Iteration（迭代）
│           ├── 单步多次 Iter.: x^{k+1} = B·x^k + q   (Jacobi, GS, O(kn²))
│           └── 梯度法 (正定 A)：SD / CG
│                 Ax = b ⟺ min ½x^T·A·x − x^T·b
│                 ☆(红) A = L·L^T ⟺ ½x^T·A·x = ½(L^T·x)^T·(L·x)
│
└── 不相容（非方阵, 非满秩）—— 最小二乘
      ├── 法方程: A^T·A·x = A^T·b ⟺ min‖L^T·x − ⋯‖₂²   (m ≥ n, 列满秩)
      └── 基于QR分解的正交化方法:
            min‖A·x − b‖₂² = min‖R·x − Q^T·b‖₂²
```
