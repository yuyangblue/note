# 线性方程组迭代法的收敛性笔记

> 来源：手写笔记 `cm+opt_迭代收敛性.pdf`（共 7 页）。
> 本笔记逐页忠实转录原文内容与批注，公式保持原样；（红）/（蓝）/（灰）标注原文颜色批注。

---

## 第 1 页

**可约**：存在排列矩阵 $P$ 使得

$$
P^{\mathsf T} A P =
\begin{bmatrix}
A_{11} & A_{12}\\
0 & A_{22}
\end{bmatrix},
\qquad A_{11}\in\mathbb{R}^{r\times r},\ A_{22}\in\mathbb{R}^{(n-r)\times(n-r)},
$$

则 $A$ 为**可约矩阵**。

**（红）例**：设 $M$ 为可约矩阵，$M=\begin{bmatrix} M_{11} & M_{12}\\ 0 & M_{22}\end{bmatrix}$，则

$$
M\vec{x}
=
\begin{bmatrix} M_{11} & M_{12}\\ 0 & M_{22} \end{bmatrix}
\begin{bmatrix} \vec{x}_1\\ \vec{x}_2 \end{bmatrix}
=
\begin{bmatrix} M_{11}\vec{x}_1 + M_{12}\vec{x}_2\\ M_{22}\vec{x}_2 \end{bmatrix}
=
\begin{bmatrix} \vec{y}_1\\ \vec{y}_2 \end{bmatrix}.
$$

**可约 $\Longleftrightarrow$**：令 $W=\{1,2,\cdots,n\}$，存在 $S,\,T\subset W$，s.t. $S\cap T=\varnothing$，$S\cup T = W$，且 $\forall\, i\in S,\ j\in T$，$a_{ij}=0$。

**定理 1**：若 $A$ 严格对角占优／不可约弱对角占优，则 $A$ 非奇异。

**证明**：① 严格对角占优：

若 $A$ 奇异 $\Longrightarrow A\vec{x}=\vec{0}$ 有非零解 $\Longrightarrow$ 存在 $i\in W=\{1,2,\cdots,n\}$。

（红）☆ 若 $A\vec{x}=\vec{0}$，取 $\vec{x}=\vec{x}/\|\vec{x}\|_\infty$，此时应 $\|\vec{x}\|_\infty = 1$。

设 $|x_i| = \|\vec{x}\|_\infty = 1$。

此时只需看第 $i$ 行，有

$$
\sum_{j=1}^{n} a_{ij}x_j = 0
\ \Longrightarrow\
a_{ii}x_i = -\sum_{\substack{j=1\\ j\ne i}}^{n} a_{ij}x_j .
$$

$$
|a_{ii}\cdot x_i|
= \Big|\sum_{\substack{j=1\\ j\ne i}}^{n} a_{ij}x_j\Big|
\le \sum_{\substack{j=1\\ j\ne i}}^{n} |a_{ij}x_j|
= \sum_{\substack{j=1\\ j\ne i}}^{n} |a_{ij}|\cdot|x_j|
\le \sum_{\substack{j=1\\ j\ne i}}^{n} |a_{ij}|
$$

$$
\Longrightarrow\ |a_{ii}\cdot x_i| = |a_{ii}|
\ \Longrightarrow\
|a_{ii}| \le \sum_{\substack{j=1\\ j\ne i}}^{n} |a_{ij}|
\ \Longrightarrow\ \text{✗（矛盾）}
$$

---

## 第 2 页

② 不可约弱对角占优：（原文此处留白，未写出证明）

**推论**：若 $A$ 严格对角占优／不可约弱对角占优，$A=A^{\mathsf T}$，$A$ 对角元为正，则 $A$ 正定。

**（红）证明**：证明 $A$ 正定，即证明 $A$ 特征值全正。

$$
A\vec{v} = \lambda\vec{v}
\ \Longrightarrow\ (A-\lambda I)\vec{v} = \vec{0}
\ \Longrightarrow\ \det(A-\lambda I) = 0 .
$$

由于 $A$ 严格对角占优／不可约弱对角占优，且 $a_{ii}>0$：

若 $\lambda\le 0$，此时 $C = A-\lambda I$，

$$
C=\begin{bmatrix}
a_{11}-\lambda & a_{12} & \cdots\\
a_{21} & a_{22}-\lambda & \cdots\\
\vdots & \vdots &
\end{bmatrix}
\qquad
\text{※ } a_{11}-\lambda \ge a_{11},\ \ a_{22}-\lambda \ge a_{22}\ \text{（等等）}
$$

$\Longrightarrow$ $C$ 为严格对角占优／不可约弱对角占优 $\Longrightarrow \det(C)\ne 0$

$\Longrightarrow \lambda > 0$。

**定理 2**：若 $A$ 为严格对角占优／不可约弱对角占优，则 J／GS 迭代收敛。

**证明**：迭代收敛，即证明 $\vec{x}^{k+1} = B\vec{x}^{k} + \vec{f}$ 中 $\rho(B) < 1$。

① J 迭代：

$$
\vec{x}^{k+1} = \underbrace{D^{-1}(L+U)}_{B_J}\vec{x}^{k} + D^{-1}\vec{b}
$$

---

## 第 3 页

设 $B_J\vec{v} = \lambda\vec{v}$，若 $|\lambda|\ge 1$：

$$
B_J - \lambda I = D^{-1}(L+U) - \lambda I = D^{-1}(L+U-\lambda D).
$$

设 $C = L+U-\lambda D$，则 $c_{ii} = -\lambda a_{ii}$，$c_{ij} = -a_{ij}\ (i\ne j)$：

$$
\text{※ } C = \begin{bmatrix}
-\lambda a_{11} & -a_{12} & -a_{13} & \cdots\\
-a_{21} & -\lambda a_{22} & -a_{23} & \cdots\\
\vdots & \vdots & \vdots &
\end{bmatrix}
$$

$\Longrightarrow$ $C$ 为严格对角占优／不可约弱对角占优。

$\Longrightarrow$ $L+U-\lambda D$ 非奇异 $\Longrightarrow \det\!\big(D^{-1}(L+U-\lambda D)\big)\ne 0$

$\Longrightarrow \det(B_J - \lambda I)\ne 0 \Longrightarrow$ 矛盾 $\Longrightarrow |\lambda| < 1$。

② GS 迭代：

$$
B_{GS} - \lambda I = (D-L)^{-1}U - \lambda I = (D-L)^{-1}\big(U - \lambda(D-L)\big).
$$

**若 $A$ 具有对称性质：**

**定理 3**：若 $A = A^{\mathsf T}$，且 $a_{ii} > 0\ (i = 1,2,3,\cdots,n)$，则 J 迭代收敛 $\Longleftrightarrow$ $A$ 与 $2D - A$ 均为正定。

**定理 4**：若 $A$ 对称正定，则 GS 迭代收敛。

**定理 4 推论**：若 $A = A^{\mathsf T}$，$\det(A)\ne 0$，$a_{ii}>0$，若 GS 收敛，则 $A$ 正定。

---

## 第 4 页

### 2.2.4. 一维模型问题

- 求解一维 Poisson 方程，考虑 Dirichlet 边界条件。

**例 1**：

$$
\begin{cases}
\dfrac{d^2 u}{dx^2} = -f(x)\\[4pt]
u(0) = u(1) = 0
\end{cases}
\qquad x\in[0,1]
$$

**离散化**：$x\in[0,1]\ \Longrightarrow\ [x_0,\,x_1,\,x_2,\,\cdots,\,x_N]$（数轴上标记 $x_0\ x_1\ x_2\ \cdots\ x_N$，两端为 $0$ 与 $1$）。在 $x_0,\cdots,x_N$ 上计算 $u(x_i)$。※ $x_{i+1}-x_i = h,\ \forall i$。

利用

$$
\frac{u(x_{i+1}) - 2u(x_i) + u(x_{i-1})}{h^2} \simeq \frac{d^2 u(x_i)}{dx^2}
$$

**（红）☆ 推导**：

$$
u(x_{i+1}) = u(x_i+h) = u(x_i) + u'(x_i)\cdot h + \tfrac{1}{2}u''(x_i)h^2 + O(h^3)
$$

$$
u(x_{i-1}) = u(x_i-h) = u(x_i) - u'(x_i)\cdot h + \tfrac{1}{2}u''(x_i)h^2 + O(h^3)
$$

$$
\Longrightarrow\ \frac{u(x_{i+1}) - 2u(x_i) + u(x_{i-1})}{h^2} = u''(x_i) + O(h^2) \simeq u''(x_i)\quad (h\to 0)
$$

——**中心差分**。

$\Longrightarrow$ 对 $\forall\, x_i$：

$$
u(x_{i+1}) - 2u(x_i) + u(x_{i-1}) = -h^2\cdot f(x_i)
$$

$\Longrightarrow$

$$
u_{i+1} - 2u_i + u_{i-1} = -h^2 f_i
\qquad
\text{※ } h^2 \text{ 先知量，} f \text{ 已知。}
$$

$\Longrightarrow$

$$
\begin{aligned}
-u_0 + 2u_1 - u_2 &= h^2 f_1\\
-u_1 + 2u_2 - u_3 &= h^2 f_2\\
&\ \vdots\\
-u_{i-1} + 2u_i - u_{i+1} &= h^2 f_i\\
&\ \vdots\\
-u_{n-2} + 2u_{n-1} - \underbrace{u_n}_{=0} &= h^2 f_{n-1}
\end{aligned}
$$

$\Longrightarrow$

$$
\begin{bmatrix}
2 & -1 & & &\\
-1 & 2 & -1 & &\\
 & -1 & 2 & -1 &\\
 & & \ddots & \ddots & \ddots\\
 & & & -1 & 2
\end{bmatrix}
\begin{bmatrix} u_1\\ u_2\\ u_3\\ \vdots\\ u_{n-1} \end{bmatrix}
=
\begin{bmatrix} h^2 f_1\\ h^2 f_2\\ h^2 f_3\\ \vdots\\ h^2 f_n \end{bmatrix}
$$

（注：右端向量末项原文写作 $h^2 f_n$，按上文方程组末式应为 $h^2 f_{n-1}$。）

---

## 第 5 页

**例 2**：

$$
\begin{cases}
\dfrac{d^2 u}{dx^2} = f(u)\\[4pt]
u(0) = u(1) = 0
\end{cases}
\ \Longrightarrow\
\begin{cases}
\dfrac{d^2 u^{k+1}}{dx^2} = -f(u^k)\\[4pt]
u^{k+1}(0) = u^{k+1}(1) = 0
\end{cases}
$$

对 $k = 1, 2, 3, \cdots, M$：

$$
\begin{bmatrix}
2 & -1 & & &\\
-1 & 2 & -1 & &\\
 & -1 & 2 & -1 &\\
 & & \ddots & \ddots & \ddots\\
 & & 0 & -1 & 2
\end{bmatrix}
\begin{bmatrix} u_1^{k+1}\\ u_2^{k+1}\\ u_3^{k+1}\\ \vdots\\ u_N^{k+1} \end{bmatrix}
=
\begin{bmatrix} h^2 f(u_1^k)\\ h^2 f(u_2^k)\\ h^2 f(u_3^k)\\ \vdots\\ h^2 f(u_{N-1}^k) \end{bmatrix}
$$

### 2.2.5. 例题

**例 1**：考察系数矩阵

$$
A_1=\begin{bmatrix} 2 & -1 & 1\\ 1 & 1 & 1\\ 1 & 1 & -2 \end{bmatrix},
\qquad
A_2=\begin{bmatrix} 1 & 2 & -2\\ 1 & 1 & 1\\ 2 & 2 & 1 \end{bmatrix}
$$

**证明**：对于 $A_1$，J 迭代不收敛，GS 迭代收敛；对于 $A_2$，J 迭代收敛，GS 迭代不收敛。

**解**：①

$$
D_1=\begin{bmatrix} 2 & & \\ & 1 & \\ & & -2 \end{bmatrix},\quad
L_1=\begin{bmatrix} 0 & 0 & 0\\ -1 & 0 & 0\\ -1 & -1 & 0 \end{bmatrix},\quad
U_1=\begin{bmatrix} 0 & 1 & -1\\ 0 & 0 & -1\\ 0 & 0 & 0 \end{bmatrix}
$$

---

## 第 6 页

$$
B_J = D_1^{-1}(L_1+U_1)
= \begin{bmatrix} 1/2 & & \\ & 1 & \\ & & -1/2 \end{bmatrix}
\begin{bmatrix} 0 & 1 & -1\\ -1 & 0 & -1\\ -1 & -1 & 0 \end{bmatrix}
= \begin{bmatrix} 0 & 1/2 & -1/2\\ -1 & 0 & -1\\ 1/2 & 1/2 & 0 \end{bmatrix}
$$

$$
\det(\lambda I - B_J) = 0
\ \Longrightarrow\ \lambda\big(\lambda^2 + \tfrac{5}{4}\big) = 0
\ \Longrightarrow\ \lambda = 0,\ \pm\tfrac{\sqrt{5}}{2}i
$$

$\Longrightarrow$ J 迭代**不收敛**。

$$
B_{GS} = (D_1 - L_1)^{-1}\cdot U_1
= \begin{bmatrix} 2 & & \\ 1 & 1 & \\ 1 & 1 & -2 \end{bmatrix}^{-1}
\cdot \begin{bmatrix} 0 & 1 & -1\\ & 0 & -1\\ & & 0 \end{bmatrix}
= \begin{bmatrix} 0 & 1/2 & -1/2\\ 0 & -1/2 & -1/2\\ 0 & 0 & 1/2 \end{bmatrix}
$$

$$
\Longrightarrow\ \det(\lambda I - B_{GS}) = 0
\ \Longrightarrow\ \lambda\big(\lambda+\tfrac{1}{2}\big)^2 = 0
\ \Longrightarrow\ \lambda = 0,\ -\tfrac{1}{2}
$$

$\Longrightarrow$ GS 迭代**收敛**。

（注：上式 $B_{GS}$ 的 $(3,3)$ 元原文写作 $1/2$；与特征方程 $\lambda(\lambda+\frac12)^2=0$ 及计算 $(D_1-L_1)^{-1}U_1$ 的结果 $-1/2$ 相比，此处应为 $-\tfrac12$。）

**（红）※ 迭代格式**：$A_1\vec{x} = \vec{b}_1$，$A_2\vec{x} = \vec{b}_2$。

① 对 $A_1$，J 迭代：

$$
x_1^{k+1} = \tfrac{1}{2}\big(1\cdot x_2^{k} - 1\cdot x_3^{k}\big) + \tfrac{1}{2}\cdot b_{11}
$$

$$
x_2^{k+1} = \big(-1\cdot x_1^{k} - 1\cdot x_3^{k}\big) + b_{12}
$$

$$
x_3^{k+1} = -\tfrac{1}{2}\big(-1\cdot x_1^{k} - 1\cdot x_2^{k}\big) - \tfrac{1}{2}\, b_{13}
$$

CS（GS）迭代：

$$
x_1^{k+1} = \tfrac{1}{2}\big(1\cdot x_2^{k} - 1\cdot x_3^{k}\big) + \tfrac{1}{2}\cdot b_{21}
$$

$$
x_2^{k+1} = \big(-1\cdot x_1^{k+1} - 1\cdot x_3^{k}\big) + b_{23}
$$

$$
x_3^{k+1} = -\tfrac{1}{2}\big(-1\cdot x_1^{k+1} - 1\cdot x_2^{k+1}\big) - \tfrac{1}{2}\, b_{23}
$$

（注：以上 $b$ 的双下标为原文写法，J 迭代行依次为 $b_{11}, b_{12}, b_{13}$，GS 迭代行原文写作 $b_{21}, b_{23}, b_{23}$。）

**（蓝）** 迭代法中：

$$
\vec{x}^{k+1} = B\cdot\vec{x}^{k} + \vec{g}
= B\big(B\vec{x}^{k-1} + \vec{g}\big) + \vec{g}
= B\big(B(B\vec{x}^{k-2} + \vec{g}) + \vec{g}\big) + \vec{g}
$$

---

## 第 7 页

（接上页）

$$
= B^{3}\vec{x}^{k-2} + B^{2}\vec{g} + B\vec{g} + \vec{g}
$$

$$
\Longrightarrow\ \vec{x}^{k+1} = B^{k+1}\cdot\vec{x}^{0} + \big(B^{k} + B^{k-1} + \cdots + B + I\big)\vec{g}
= B^{k+1}\cdot\vec{x}^{0} + \sum_{i=1}^{k} B^{i}\cdot\vec{g}
$$

- ※ $\displaystyle\lim_{k\to\infty} B^{k} = 0\ \Longleftrightarrow\ \rho(B) < 1$
- ※ $\displaystyle (I - B)\big(I + B + B^2 + \cdots + B^k\big) = I - B^{k+1}$
