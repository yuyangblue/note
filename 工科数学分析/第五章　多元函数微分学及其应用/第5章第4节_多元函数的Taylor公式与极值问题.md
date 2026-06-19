---
AIGC:
  Label: "1",
  "ContentProducer":   "00191310104MAC2G6EG4100000003",
  "ContentPropagator": "00191310104MAC2G6EG4100000003",
  "ProduceID":         "u-4dc2a7-313cc7fe-a1a2-436b-b572-24534dcc518e",
  "PropagateID":       "u-4dc2a7-313cc7fe-a1a2-436b-b572-24534dcc518e",
  "ReservedCode1":     "",
  "ReservedCode2":     "",
---
# 第五章 第四节　多元函数的 Taylor 公式与极值问题

> 详尽学习笔记（基于《工科数学分析基础（第三版）下册》马知恩、王绵森 著）
> 本节将一元函数的 Taylor 公式推广到多元函数，然后讨论多元函数的极值问题与最大、最小值问题。本节与第五节中的向量均写成列向量。

---

## 4.1　多元函数的 Taylor 公式

### 1. 回顾：一元函数 Taylor 公式

设 $f(x)$ 在 $x_0$ 的邻域有 $n+1$ 阶导数，则
$$
f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k+R_n,
$$
其中余项 $R_n$ 可取 **Lagrange 型**或 **Peano 型**。

### 2. 二元函数的一阶 Taylor 公式（带 Lagrange 余项）

**定理 4.1**  设 $z=f(x,y)$ 在点 $(x_0,y_0)$ 的某邻域 $U(x_0,y_0)$ 内有连续的二阶偏导数，$(x_0+\Delta x,y_0+\Delta y)\in U$，则存在 $\theta\in(0,1)$，使得

$$
f(x_0+\Delta x,y_0+\Delta y)=f(x_0,y_0)+f_x(x_0,y_0)\Delta x+f_y(x_0,y_0)\Delta y+R_1, \tag{4.1}
$$

其中

$$
R_1=\frac{1}{2!}\Bigl[f_{xx}\,\Delta x^2+2f_{xy}\,\Delta x\Delta y+f_{yy}\,\Delta y^2\Bigr]_{(x_0+\theta\Delta x,\,y_0+\theta\Delta y)}. \tag{4.2}
$$

### 3. 证明思路（化多为一）

引入辅助函数 $\varphi(t)=f(x_0+t\Delta x,\,y_0+t\Delta y)$，$t\in[0,1]$，则 $\varphi(0)=f(x_0,y_0)$，$\varphi(1)=f(x_0+\Delta x,y_0+\Delta y)$。

由链式法则：
$$\varphi'(t)=f_x\Delta x+f_y\Delta y,$$
$$\varphi''(t)=f_{xx}\Delta x^2+2f_{xy}\Delta x\Delta y+f_{yy}\Delta y^2.$$

对一元函数 $\varphi$ 在 $t=0$ 处用一阶 Lagrange Taylor 公式：
$$\varphi(1)=\varphi(0)+\varphi'(0)+\tfrac{1}{2}\varphi''(\theta),\quad \theta\in(0,1),$$
代回即得 (4.1)、(4.2)。$\square$

### 4. 高阶二元 Taylor 公式（算子形式）

记微分算子 $D=\Delta x\,\dfrac{\partial}{\partial x}+\Delta y\,\dfrac{\partial}{\partial y}$，则

$$
f(x_0+\Delta x,y_0+\Delta y)=\sum_{k=0}^{n}\frac{1}{k!}D^k f(x_0,y_0)+R_n,
$$

其中 Lagrange 余项
$$R_n=\frac{1}{(n+1)!}D^{n+1}f(x_0+\theta\Delta x,\,y_0+\theta\Delta y),\quad \theta\in(0,1).$$

其中
$$D^k f=\sum_{i=0}^{k}\binom{k}{i}\Delta x^{k-i}\Delta y^{i}\,\frac{\partial^k f}{\partial x^{k-i}\partial y^{i}}.$$

### 5. $n$ 元函数 Taylor 公式（矩阵形式）

记 $\boldsymbol{x}_0=(x_{0,1},\dots,x_{0,n})^{\mathrm T}$，$\Delta\boldsymbol{x}=(\Delta x_1,\dots,\Delta x_n)^{\mathrm T}$。定义 $f$ 在 $\boldsymbol{x}_0$ 处的**梯度**与 **Hesse 矩阵**：

$$
\nabla f(\boldsymbol{x}_0)=\left(\frac{\partial f(\boldsymbol{x}_0)}{\partial x_1},\dots,\frac{\partial f(\boldsymbol{x}_0)}{\partial x_n}\right)^{\mathrm T},
$$

$$
H_f(\boldsymbol{x}_0)=\begin{pmatrix}
f_{x_1x_1}&f_{x_1x_2}&\cdots&f_{x_1x_n}\\
f_{x_2x_1}&f_{x_2x_2}&\cdots&f_{x_2x_n}\\
\vdots&\vdots&\ddots&\vdots\\
f_{x_nx_1}&f_{x_nx_2}&\cdots&f_{x_nx_n}
\end{pmatrix}_{\boldsymbol{x}_0}.
$$

**带 Lagrange 余项的一阶 Taylor 公式（矩阵形式）**：存在 $\theta\in(0,1)$ 使

$$
\boxed{\;f(\boldsymbol{x}_0+\Delta\boldsymbol{x})=f(\boldsymbol{x}_0)+\langle\nabla f(\boldsymbol{x}_0),\Delta\boldsymbol{x}\rangle+\frac{1}{2!}\,\Delta\boldsymbol{x}^{\mathrm T}H_f(\boldsymbol{x}_0+\theta\Delta\boldsymbol{x})\Delta\boldsymbol{x}.\;} \tag{4.4}
$$

**带 Peano 余项的二阶 Taylor 公式**：

$$
f(\boldsymbol{x}_0+\Delta\boldsymbol{x})=f(\boldsymbol{x}_0)+\langle\nabla f(\boldsymbol{x}_0),\Delta\boldsymbol{x}\rangle+\frac{1}{2!}\Delta\boldsymbol{x}^{\mathrm T}H_f(\boldsymbol{x}_0)\Delta\boldsymbol{x}+o(\|\Delta\boldsymbol{x}\|^2). \tag{4.5}
$$

### 6. 例题

**例 4.1**  设 $z=z(x,y)$ 由方程 $z^2-2xz+y=0$ 确定，且 $z(1,1)=1$。求 $z(x,y)$ 在 $(1,1)$ 处带 Peano 余项的二阶 Taylor 公式。

**解**  由隐函数求导：对方程两端关于 $x$ 求偏导：$2zz_x-2z-2xz_x=0$，解得 $z_x=\dfrac{z}{z-x}$。在 $(1,1,1)$ 处分母为 $0$，需要对方程整体重新分析；可直接用 Taylor 展开求系数（教材中给出具体计算）。

**例**  求 $f(x,y)=\sin x\sin y$ 在 $(0,0)$ 处的三阶 Taylor 公式。

$$f(0,0)=0,\;f_x=\cos x\sin y,\;f_y=\sin x\cos y,$$
$$f_x(0,0)=f_y(0,0)=0;$$
$$f_{xx}(0,0)=f_{yy}(0,0)=0,\quad f_{xy}(0,0)=1;$$

故二阶 Taylor 公式为
$$\sin x\sin y= xy + o(x^2+y^2).$$

**例**（近似计算）  求 $f(x,y)=x^y$ 在 $(1,4)$ 附近的二阶 Taylor 公式，用以估算 $1.08^{3.96}$。

$$f_x=yx^{y-1},\;f_y=x^y\ln x;\;f_x(1,4)=4,\;f_y(1,4)=0.$$
$$f_{xx}=y(y-1)x^{y-2}=12,\;f_{xy}=x^{y-1}(1+y\ln x)=1,\;f_{yy}=x^y(\ln x)^2=0.$$

记 $\Delta x=0.08,\Delta y=-0.04$，则
$$1.08^{3.96}\approx 1+4(0.08)+0+\tfrac{1}{2}\bigl[12(0.08)^2+2(1)(0.08)(-0.04)\bigr]\approx 1.3552.$$

---

## 4.2　无约束极值、最大值与最小值

### 1. 极值定义

**定义 4.2**  设 $f:U(\boldsymbol{x}_0)\subset\mathbb{R}^n\to\mathbb{R}$。若 $\forall\,\boldsymbol{x}\in U(\boldsymbol{x}_0)$ 恒有
$$f(\boldsymbol{x})\le f(\boldsymbol{x}_0)\quad(\text{相应地，}\ge),$$
则称 $f$ 在 $\boldsymbol{x}_0$ 取得**无约束极大值（极小值）**，$\boldsymbol{x}_0$ 称为**极值点**。

**注**：极值是局部概念；最大值/最小值是整体概念。

### 2. 极值的必要条件（驻点条件）

**定理 4.3**  若 $n$ 元函数 $f$ 在 $\boldsymbol{x}_0$ 可微，且 $\boldsymbol{x}_0$ 是极值点，则
$$
\boxed{\;\nabla f(\boldsymbol{x}_0)=\boldsymbol{0}.\;}
$$

满足 $\nabla f(\boldsymbol{x}_0)=\boldsymbol{0}$ 的点称为 $f$ 的**驻点**（或临界点）。

**反例（鞍点）**：$f(x,y)=x^2-y^2$ 在 $(0,0)$ 处 $\nabla f=\boldsymbol{0}$，但 $f(x,0)=x^2>0$，$f(0,y)=-y^2<0$，故 $(0,0)$ 不是极值点（鞍点）。

**注**：若 $f$ 在 $\boldsymbol{x}_0$ 处不可微（例如偏导数不存在），$\boldsymbol{x}_0$ 仍可能是极值点。例如 $z=\sqrt{x^2+y^2}$ 在 $(0,0)$ 取得极小值，但偏导数不存在。

### 3. 极值的充分条件（Hesse 矩阵判别法）

**定理 4.4**  设 $f\in C^{(2)}(U(\boldsymbol{x}_0))$，$\nabla f(\boldsymbol{x}_0)=\boldsymbol{0}$，$H_f(\boldsymbol{x}_0)$ 为 $f$ 在 $\boldsymbol{x}_0$ 处的 Hesse 矩阵。则

| Hesse 矩阵 $H_f(\boldsymbol{x}_0)$ | $f(\boldsymbol{x}_0)$ |
|------|------|
| 正定 | 极小值 |
| 负定 | 极大值 |
| 不定 | 不是极值（鞍点） |
| 半定（含零特征值） | 需进一步判断 |

**证明思路**：由 Taylor 公式 (4.5)，
$$f(\boldsymbol{x}_0+\Delta\boldsymbol{x})-f(\boldsymbol{x}_0)=\tfrac{1}{2}\Delta\boldsymbol{x}^{\mathrm T}H_f(\boldsymbol{x}_0)\Delta\boldsymbol{x}+o(\|\Delta\boldsymbol{x}\|^2).$$

当 $H_f$ 正定时，设其最小特征值为 $\lambda_1>0$，则
$$\Delta\boldsymbol{x}^{\mathrm T}H_f\Delta\boldsymbol{x}\ge \lambda_1\|\Delta\boldsymbol{x}\|^2>0,$$
故
$$f(\boldsymbol{x}_0+\Delta\boldsymbol{x})-f(\boldsymbol{x}_0)\ge \tfrac{\lambda_1}{2}\|\Delta\boldsymbol{x}\|^2+o(\|\Delta\boldsymbol{x}\|^2)=\left(\tfrac{\lambda_1}{2}+o(1)\right)\|\Delta\boldsymbol{x}\|^2>0.$$
即 $f(\boldsymbol{x}_0)$ 是极小值。负定情形类似。$\square$

### 4. 二元情形的实用判别式

设 $(x_0,y_0)$ 是 $f$ 的驻点，记
$$A=f_{xx}(x_0,y_0),\quad B=f_{xy}(x_0,y_0),\quad C=f_{yy}(x_0,y_0).$$

则 Hesse 矩阵 $H_f=\begin{pmatrix}A&B\\B&C\end{pmatrix}$，其判别式为 $\Delta=AC-B^2$。

| 条件 | 结论 |
|------|------|
| $\Delta>0,\;A>0$ | $f(x_0,y_0)$ 为**极小值** |
| $\Delta>0,\;A<0$ | $f(x_0,y_0)$ 为**极大值** |
| $\Delta<0$ | $f(x_0,y_0)$ **不是极值**（鞍点） |
| $\Delta=0$ | 临界情况，需用更高阶 Taylor 或其他方法 |

### 5. 求极值的步骤

1. 解方程组 $\nabla f=\boldsymbol{0}$ 求出所有驻点；
2. 在每个驻点处求 Hesse 矩阵；
3. 由 Hesse 矩阵的正定/负定/不定性判断极值类型；
4. 对偏导数不存在的点单独考察。

### 6. 例题

**例 4.2**  求 $f(x,y)=x^3-y^3+3x^2+3y^2-9x$ 的极值。

驻点方程：
$$f_x=3x^2+6x-9=3(x+3)(x-1)=0,\quad f_y=-3y^2+6y=-3y(y-2)=0.$$
故驻点为 $(1,0),(1,2),(-3,0),(-3,2)$。

二阶偏导：$f_{xx}=6x+6,\;f_{yy}=-6y+6,\;f_{xy}=0$。

| 驻点 | $A$ | $C$ | $B$ | $\Delta=AC-B^2$ | 结论 |
|------|-----|-----|-----|------|------|
| $(1,0)$ | $12$ | $6$ | $0$ | $72>0$ | 极小值 $f=-5$ |
| $(1,2)$ | $12$ | $-6$ | $0$ | $-72<0$ | 鞍点 |
| $(-3,0)$ | $-12$ | $6$ | $0$ | $-72<0$ | 鞍点 |
| $(-3,2)$ | $-12$ | $-6$ | $0$ | $72>0$ | 极大值 $f=31$ |

### 7. 闭区域上的最大值与最小值

**定理**（多元 Weierstrass 定理）  有界闭区域上的连续函数必取得最大值与最小值。

**求法**：
1. 求 $f$ 在区域**内部**的所有驻点和不可导点，计算函数值；
2. 求 $f$ 在**边界**上的最大值与最小值（边界上可化为低维问题，常用参数化或 Lagrange 乘数法）；
3. 比较以上所有候选值，得最大值与最小值。

**例 4.3**  求 $z=x^2 y(4-x-y)$ 在区域 $D=\{(x,y)\mid x\ge 0,\,y\ge 0,\,x+y\le 4\}$ 上的最大值与最小值。

- 区域内部驻点：$z_x=2xy(4-x-y)-x^2 y=xy(8-3x-2y)=0$，$z_y=x^2(4-x-y)-x^2 y=x^2(4-x-2y)=0$。在内部得 $x=2,y=1$，对应 $z=4$。
- 边界 $x=0$ 上 $z=0$；$y=0$ 上 $z=0$；$x+y=4$ 上 $z=0$。

故最大值 $=4$（在 $(2,1)$ 处），最小值 $=0$（在边界上）。

---

## 4.3　有约束极值，Lagrange 乘数法

### 1. 问题模型

求目标函数
$$z=f(x_1,\dots,x_n) \tag{4.17}$$
在 $m$ 个约束条件
$$\varphi_k(x_1,\dots,x_n)=0,\quad k=1,2,\dots,m\;(m<n) \tag{4.18}$$
下的极值，称为**有约束极值（条件极值）** 问题。

### 2. 几何直观（二元、单约束）

设求 $f(x,y)$ 在 $\varphi(x,y)=0$ 下的极值。考察 $f$ 的等值线 $f(x,y)=C$ 与约束曲线 $\Gamma:\varphi(x,y)=0$：极值点必为 $\Gamma$ 与某等值线相切之点。在该切点处，两曲线有公共法线方向，即 $\nabla f$ 与 $\nabla\varphi$ 平行：

$$
\nabla f(x_0,y_0)=-\lambda_0\,\nabla\varphi(x_0,y_0).
$$

### 3. Lagrange 乘数法（单约束二元情形）

构造 **Lagrange 函数**
$$
\boxed{\;L(x,y,\lambda)=f(x,y)+\lambda\,\varphi(x,y).\;} \tag{4.24}
$$

极值点的必要条件是 $L$ 取无约束极值，即
$$
\begin{cases}
L_x=f_x+\lambda\,\varphi_x=0,\\
L_y=f_y+\lambda\,\varphi_y=0,\\
L_\lambda=\varphi(x,y)=0.
\end{cases} \tag{4.25}
$$

从此方程组解出 $(x_0,y_0,\lambda_0)$，则 $(x_0,y_0)$ 即为可能的有约束极值点。$\lambda_0$ 称为 **Lagrange 乘数**。

### 4. 推导（用隐函数求导法）

设由约束 $\varphi(x,y)=0$ 在 $(x_0,y_0)$ 附近可解出 $y=y(x)$，则约束极值化为一元无约束极值。由一元极值必要条件：
$$
\frac{\mathrm{d}f(x,y(x))}{\mathrm{d}x}\bigg|_{x=x_0}=f_x(x_0,y_0)+f_y(x_0,y_0)\,y'(x_0)=0. \tag{4.21}
$$

由隐函数求导：$y'(x_0)=-\dfrac{\varphi_x(x_0,y_0)}{\varphi_y(x_0,y_0)}$。代入 (4.21)：

$$
f_x(x_0,y_0)\,\varphi_y(x_0,y_0)-f_y(x_0,y_0)\,\varphi_x(x_0,y_0)=0,
$$

即向量 $(f_x,f_y)$ 与 $(\varphi_x,\varphi_y)$ 平行；设比例系数为 $-\lambda_0$，则得 (4.25) 前两式。

### 5. 多约束情形

对一般问题 (4.17)、(4.18)，构造

$$
L(x_1,\dots,x_n,\lambda_1,\dots,\lambda_m)=f(x_1,\dots,x_n)+\sum_{k=1}^{m}\lambda_k\,\varphi_k(x_1,\dots,x_n).
$$

极值点的必要条件是 $L$ 关于 $x_1,\dots,x_n,\lambda_1,\dots,\lambda_m$ 的所有偏导数为零：

$$
\frac{\partial L}{\partial x_i}=\frac{\partial f}{\partial x_i}+\sum_{k=1}^{m}\lambda_k\,\frac{\partial \varphi_k}{\partial x_i}=0,\quad i=1,\dots,n;
$$

$$
\frac{\partial L}{\partial \lambda_k}=\varphi_k(x_1,\dots,x_n)=0,\quad k=1,\dots,m.
$$

### 6. 例题

**例 4.6**  求函数 $f(x,y,z)=xyz$ 在条件 $x+y+z=a\;(x,y,z>0,\,a>0)$ 下的极大值。

构造 $L=xyz+\lambda(x+y+z-a)$。

$$
\begin{cases}
L_x=yz+\lambda=0,\\
L_y=xz+\lambda=0,\\
L_z=xy+\lambda=0,\\
L_\lambda=x+y+z-a=0.
\end{cases}
$$

由前三式得 $yz=xz=xy$，即 $x=y=z$。结合约束得 $x=y=z=a/3$，对应函数值 $f=(a/3)^3=a^3/27$。

由实际意义（紧集上连续函数取最值），此为极大值。

**推论（均值不等式）**：对 $x,y,z>0$，
$$\sqrt[3]{xyz}\le \frac{x+y+z}{3},$$
即三个正数的几何平均不超过算术平均。

**例 4.7**  求体积为 $V$ 的长方体盒子（无盖）的最小表面积。

设三边长为 $x,y,z>0$，体积约束 $xyz=V$，目标函数为表面积
$$S=xy+2yz+2xz.$$

构造 $L=xy+2yz+2xz+\lambda(xyz-V)$：
$$
\begin{cases}
L_x=y+2z+\lambda yz=0,\\
L_y=x+2z+\lambda xz=0,\\
L_z=2y+2x+\lambda xy=0,\\
xyz=V.
\end{cases}
$$
解得 $x=y=2z$，结合 $xyz=V$ 得 $z=\sqrt[3]{V/4},\;x=y=2\sqrt[3]{V/4}$。此时最小表面积存在（由实际意义）。

---

## 学习要点小结

1. **二元 Taylor 公式**：算子形式 $\bigl(\Delta x\partial_x+\Delta y\partial_y\bigr)^k f$ 是关键记忆点。
2. **Hesse 矩阵**：$H_f=[f_{x_ix_j}]$，是判断多元函数极值的核心工具。
3. **极值判别三步**：求驻点 → 算 Hesse 矩阵 → 看正定/负定。
4. **二元 $AC-B^2$ 判别表**必须烂熟。
5. **闭区域上最值**：内部驻点 + 边界极值 + 不可导点，全部比较。
6. **Lagrange 乘数法的本质**：约束极值点处 $\nabla f$ 与各 $\nabla \varphi_k$ 线性相关。
7. 实际问题中，若解唯一且最值显然存在，可直接断定该解即为最值点（如盒子表面积问题）。
