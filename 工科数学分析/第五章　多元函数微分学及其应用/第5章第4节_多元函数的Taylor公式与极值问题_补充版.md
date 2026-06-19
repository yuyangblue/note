---
AIGC:
  Label: "1",
  "ContentProducer":   "00191310104MAC2G6EG4100000003",
  "ContentPropagator": "00191310104MAC2G6EG4100000003",
  "ProduceID":         "u-4dc2a7-2f9a1161-b6ea-4bf0-a2db-f7acf890add4",
  "PropagateID":       "u-4dc2a7-2f9a1161-b6ea-4bf0-a2db-f7acf890add4",
  "ReservedCode1":     "",
  "ReservedCode2":     "",
---
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

### 1. 问题模型与引入

#### 1.1 有约束极值的概念

求目标函数
$$z=f(x_1,\dots,x_n) \tag{4.17}$$
在 $m$ 个约束条件
$$\varphi_k(x_1,\dots,x_n)=0,\quad k=1,2,\dots,m\;(m<n) \tag{4.18}$$
下的极值，称为**有约束极值（条件极值）** 问题。

#### 1.2 与无约束极值的对比（引例）

考察 $z=x^2+y^2$：

- **无约束**：极小值在 $(0,0)$ 取得，值为 $0$。
- **约束 $x+y-1=0$**：极小值不可能在 $(0,0)$ 取得（不满足约束）。容易算得有约束极小值为 $\tfrac{1}{2}$，在 $\bigl(\tfrac12,\tfrac12\bigr)$ 取得。

**几何解释**：

- 前者是曲面 $z=x^2+y^2$ 上各点 $z$ 坐标的极小值；
- 后者是曲面与平面 $x+y-1=0$ 的**交线**上 $z$ 坐标的极小值；
- 用等值线看：$x^2+y^2=C^2$ 是一族同心圆，约束直线 $l$ 与圆相切的点即为约束极小值点。

### 2. 化为无约束极值的方法

**思路**：从约束 (4.18) 中解出 $m$ 个变量，代回 $f$，化为 $n-m$ 元的无约束极值问题。

**例 4.5（教材）**　证明：在周长为 $2p$ 的所有三角形中，以等边三角形的面积最大。

**解**　由 Heron 公式
$$S^2=p(p-x)(p-y)(p-z),\quad x+y+z=2p,\;x,y,z>0.$$
由约束解出 $z=2p-x-y$，代入：
$$F(x,y):=S^2=p(p-x)(p-y)(x+y-p).$$
求 $F$ 的无约束极值：
$$F_x=p(p-y)(p-2x-y+p)\cdot(-1)+\cdots,$$
解 $F_x=F_y=0$ 得 $x=y=\tfrac{2p}{3}$，从而 $z=\tfrac{2p}{3}$，即**等边三角形**面积最大，最大面积为 $\dfrac{\sqrt 3}{9}p^2$。$\square$

> **方法局限**：当约束方程 (4.18) 难以显式解出（或解析不便）时，"化无约束"行不通。此时需要更通用的 **Lagrange 乘数法**。

### 3. Lagrange 乘数法（二元单约束情形）

#### 3.1 几何直观

设求 $f(x,y)$ 在 $\varphi(x,y)=0$ 下的极值。$f$ 的等值线 $f(x,y)=C$ 与约束曲线 $\Gamma:\varphi(x,y)=0$ 的关系：

- 若 $\Gamma$ 与某等值线相交（穿出），则交点不可能是极值点（沿 $\Gamma$ 仍可使 $f$ 增大或减小）；
- 故极值点必为 $\Gamma$ 与某等值线的**切点**。

切点处两曲线有公共法线，即 $\nabla f \parallel \nabla \varphi$：
$$\nabla f(x_0,y_0)=-\lambda_0\,\nabla\varphi(x_0,y_0).$$

#### 3.2 严格推导（隐函数法）

**正则性条件**：设在候选点 $P_0(x_0,y_0)$ 处
$$\varphi(x_0,y_0)=0,\quad \varphi_y(P_0)\ne 0.$$
由隐函数存在定理，$\varphi(x,y)=0$ 在 $P_0$ 附近确定 $y=y(x)$。

约束极值问题化为一元无约束问题 $z=f(x,y(x))$，由一元极值必要条件：
$$
\frac{\mathrm{d}z}{\mathrm{d}x}\bigg|_{x_0}=f_x(P_0)+f_y(P_0)\,y'(x_0)=0. \tag{4.19}
$$
**几何含义**：$\nabla f(P_0)\perp$ 切向量 $(1,y'(x_0))$。

对 $\varphi(x,y(x))\equiv 0$ 求导：
$$
\varphi_x(P_0)+\varphi_y(P_0)\,y'(x_0)=0. \tag{4.20}
$$
即 $\nabla\varphi(P_0)\perp$ 同一切向量。

故 $\nabla f(P_0)\parallel \nabla\varphi(P_0)$。把 $y'(x_0)=-\varphi_x/\varphi_y$ 代入 (4.19)：
$$
f_x(P_0)\,\varphi_y(P_0)-f_y(P_0)\,\varphi_x(P_0)=0,
$$
即用**行列式形式**：
$$
\begin{vmatrix} f_x(P_0) & f_y(P_0)\\ \varphi_x(P_0) & \varphi_y(P_0)\end{vmatrix}=0. \tag{4.22}
$$
两行对应元素成比例，记比例系数为 $-\lambda_0$，得有约束极值的必要条件：
$$
\begin{cases}
f_x(P_0)+\lambda_0\,\varphi_x(P_0)=0,\\
f_y(P_0)+\lambda_0\,\varphi_y(P_0)=0,\\
\varphi(P_0)=0.
\end{cases} \tag{4.23}
$$

#### 3.3 Lagrange 函数

构造
$$
\boxed{\;L(x,y,\lambda)=f(x,y)+\lambda\,\varphi(x,y).\;} \tag{4.24}
$$
则 (4.23) 等价于 $L$ 在 $(x_0,y_0,\lambda_0)$ 处的驻点条件：
$$
\begin{cases}
L_x=f_x+\lambda\,\varphi_x=0,\\
L_y=f_y+\lambda\,\varphi_y=0,\\
L_\lambda=\varphi(x,y)=0.
\end{cases} \tag{4.25}
$$
解出的 $(x_0,y_0)$ 即为可能的有约束极值点，$\lambda_0$ 称为 **Lagrange 乘数**。

#### 3.4 ⚠ 关于 Lagrange 函数驻点的判定说明

> Lagrange 函数 $L$ 的驻点 $(x_0,y_0,\lambda_0)$ 中的 $(x_0,y_0)$ **是否真是条件极值点**？是极大值还是极小值？严格说来需要另行判定（见后 §6 的充分条件）。但对**具体实际问题**（如盒子表面积、最短距离等），往往可由问题的实际意义直接断定，且必要条件求得的点常常就是所求条件极值点。

### 4. 三元单约束情形

求 $u=f(x,y,z)$ 在 $\varphi(x,y,z)=0$ 下的极值。在 $P_0(x_0,y_0,z_0)$ 处设 $\varphi_z(P_0)\ne 0$，由约束解出 $z=z(x,y)$。

化为二元无约束问题 $u=f(x,y,z(x,y))$。极值必要条件：
$$
u_x=f_x+f_z\,z_x=0,\qquad u_y=f_y+f_z\,z_y=0.
$$
对约束 $\varphi(x,y,z(x,y))\equiv 0$ 分别求偏导：
$$
\varphi_x+\varphi_z z_x=0,\qquad \varphi_y+\varphi_z z_y=0.
$$
消去 $z_x,z_y$ 得 $\nabla f(P_0)\parallel \nabla\varphi(P_0)$，即存在 $\lambda_0$ 使
$$
\nabla f(P_0)+\lambda_0\,\nabla\varphi(P_0)=\boldsymbol 0,\quad \varphi(P_0)=0.
$$

**Lagrange 函数**：$L(x,y,z,\lambda)=f(x,y,z)+\lambda\,\varphi(x,y,z)$，驻点方程组：
$$
\begin{cases}
L_x=f_x+\lambda\varphi_x=0,\\
L_y=f_y+\lambda\varphi_y=0,\\
L_z=f_z+\lambda\varphi_z=0,\\
L_\lambda=\varphi(x,y,z)=0.
\end{cases}
$$

> **几何推广**：二元情形是等值线与约束曲线的切点；三元情形则是 $f$ 的**等值面** $f(x,y,z)=C$ 与**约束曲面** $\varphi(x,y,z)=0$ 的切点（公共法向量 $\nabla f \parallel \nabla\varphi$）。

#### 例 4.8（教材）：无盖长方体最小表面积——完整消元

求体积为 $V$ 的无盖盒子，表面积 $f=2xz+2yz+xy$ 最小。约束 $\varphi=xyz-V=0$，$x,y,z>0$。

构造 $L=2xz+2yz+xy+\lambda(xyz-V)$，得方程组
$$
\begin{aligned}
&\text{①}\;\;L_x=2z+y+\lambda yz=0,\\
&\text{②}\;\;L_y=2z+x+\lambda xz=0,\\
&\text{③}\;\;L_z=2x+2y+\lambda xy=0,\\
&\text{④}\;\;L_\lambda=xyz-V=0.
\end{aligned}
$$

**消元过程**：

- ① − ②：$(y-x)+\lambda z(y-x)=(y-x)(1+\lambda z)=0$。由 $x,y,z>0$ 易验 $1+\lambda z\ne 0$（否则代回 ① 得 $2z+y=0$，矛盾），故 $y=x$。
- $2\cdot$② − ③：$(4z+2x+2\lambda xz)-(2x+2y+\lambda xy)=2(2z-y)+\lambda x(2z-y)=(2z-y)(2+\lambda x)=0$。同理 $2+\lambda x\ne 0$，得 $y=2z$，即 $x=y=2z$。
- 代入 ④：$(2z)(2z)(z)=4z^3=V$，故
$$
z=\tfrac{1}{2}\sqrt[3]{2V},\qquad x=y=\sqrt[3]{2V}.
$$

Lagrange 函数有唯一驻点。由实际意义（极薄/极长的盒子表面积都很大，故最小表面积必存在），此即所求。

### 5. 多约束情形

#### 5.1 双约束情形（三元两约束）

求 $u=f(x,y,z)$ 在
$$
\varphi(x,y,z)=0,\qquad \psi(x,y,z)=0
$$
下的极值。设两约束在 $P_0$ 附近确定隐函数 $x=x(z),\,y=y(z)$。则 $u=f(x(z),y(z),z)$，极值必要条件：
$$
\frac{\mathrm{d}u}{\mathrm{d}z}=f_x x'(z)+f_y y'(z)+f_z=0,
$$
即
$$\bigl(f_x,f_y,f_z\bigr)\cdot\bigl(x'(z),y'(z),1\bigr)=0.$$

对 $\varphi,\psi$ 分别求 $z$ 的全导数：
$$
\bigl(\varphi_x,\varphi_y,\varphi_z\bigr)\cdot\bigl(x'(z),y'(z),1\bigr)=0,
$$
$$
\bigl(\psi_x,\psi_y,\psi_z\bigr)\cdot\bigl(x'(z),y'(z),1\bigr)=0.
$$

三个向量 $\nabla f,\nabla\varphi,\nabla\psi$ 都与非零向量 $(x'(z),y'(z),1)$ 正交，故它们**线性相关**。结合 $\nabla\varphi,\nabla\psi$ 线性无关（隐函数 Jacobi 条件），存在常数 $\lambda,\mu$ 使
$$
\nabla f(P_0)+\lambda\,\nabla\varphi(P_0)+\mu\,\nabla\psi(P_0)=\boldsymbol 0.
$$

**Lagrange 函数**：
$$
L(x,y,z,\lambda,\mu)=f+\lambda\varphi+\mu\psi.
$$
共 5 个方程、5 个未知数：$L_x=L_y=L_z=0,\;L_\lambda=\varphi=0,\;L_\mu=\psi=0$。

#### 5.2 ⭐ 一般情形：$n$ 元 $m$ 约束

$$
\begin{cases}
u=f(\boldsymbol x),\quad \boldsymbol x=(x_1,\dots,x_n)\in\mathbb R^n,\\[2pt]
\varphi_k(\boldsymbol x)=0,\quad k=1,2,\dots,m\;(m<n).
\end{cases}
$$
记约束集
$$S=\{\boldsymbol x\in\mathbb R^n:\varphi_k(\boldsymbol x)=0,\;k=1,\dots,m\}.$$

**第一步**：构造 Lagrange 函数
$$
L(\boldsymbol x,\boldsymbol\lambda)=f(\boldsymbol x)+\sum_{k=1}^{m}\lambda_k\,\varphi_k(\boldsymbol x),\quad \boldsymbol\lambda=(\lambda_1,\dots,\lambda_m).
$$

**第二步**：由 $\nabla L=\boldsymbol 0$ 求驻点 $(\boldsymbol x_0,\boldsymbol\lambda_0)$：
$$
\frac{\partial L}{\partial x_i}=\frac{\partial f}{\partial x_i}+\sum_{k=1}^{m}\lambda_k\frac{\partial \varphi_k}{\partial x_i}=0,\quad i=1,\dots,n;
$$
$$
\frac{\partial L}{\partial \lambda_k}=\varphi_k(\boldsymbol x)=0,\quad k=1,\dots,m.
$$

**⭐ 约束规格（constraint qualification）**：在驻点 $\boldsymbol x_0$ 处要求
$$
\boxed{\;\operatorname{rank}\!\left(\dfrac{\partial \varphi_k}{\partial x_i}(\boldsymbol x_0)\right)_{m\times n}=m,\;}
$$
即 $m$ 个约束的梯度 $\nabla\varphi_1,\dots,\nabla\varphi_m$ 在 $\boldsymbol x_0$ 处**线性无关**。

> **说明**：对约束组取微分
> $$\sum_{i=1}^{n}\frac{\partial\varphi_k}{\partial x_i}\,\mathrm{d}x_i=0,\quad k=1,\dots,m,$$
> 在秩为 $m$ 时，可由隐函数定理设 $\bar{\boldsymbol x}=(x_{m+1},\dots,x_n)$ 为自由变量，前 $m$ 个变量由约束确定为 $x_i=x_i(\bar{\boldsymbol x})$，$i=1,\dots,m$。若秩条件失效，Lagrange 必要条件可能"漏掉"真正的条件极值点，需单独考察。

### 6. ⭐ 充分条件（Hesse 矩阵判别）

对每个 Lagrange 驻点 $(\boldsymbol x_0,\boldsymbol\lambda_0)$，**固定 $\boldsymbol\lambda=\boldsymbol\lambda_0$**，定义
$$
\Phi(\boldsymbol x)=L(\boldsymbol x,\boldsymbol\lambda_0)=f(\boldsymbol x)+\sum_{k=1}^{m}\lambda_{0,k}\,\varphi_k(\boldsymbol x).
$$
计算 $\Phi$ 在 $\boldsymbol x_0$ 处的 Hesse 矩阵
$$
H(\boldsymbol x_0)=\left(\frac{\partial^2 L}{\partial x_i\,\partial x_j}(\boldsymbol x_0,\boldsymbol\lambda_0)\right)_{n\times n}.
$$

**判别准则**：

| $H(\boldsymbol x_0)$ | 结论 |
|------|------|
| **正定** | $\boldsymbol x_0$ 为**条件极小值点** |
| **负定** | $\boldsymbol x_0$ 为**条件极大值点** |
| **不定** | 需在切空间上限制后再判别 |

> **精细判别（bordered Hessian）**：更精确地，应看 $H(\boldsymbol x_0)$ 在约束切空间
> $$T_{\boldsymbol x_0}S=\{\boldsymbol h\in\mathbb R^n:\nabla\varphi_k(\boldsymbol x_0)\cdot\boldsymbol h=0,\,k=1,\dots,m\}$$
> 上限制后的正定/负定性。但这里给出的强条件（$H$ 在整个 $\mathbb R^n$ 上正定/负定）已足以保证条件极值。

**充分性证明思路**：对 $\Phi$ 在 $\boldsymbol x_0$ 处 Taylor 展开（注意 $\nabla\Phi(\boldsymbol x_0)=\boldsymbol 0$）：
$$
\Phi(\boldsymbol x_0+\boldsymbol h)-\Phi(\boldsymbol x_0)=\tfrac{1}{2}\boldsymbol h^{\mathrm T}H(\boldsymbol x_0)\boldsymbol h+o(\|\boldsymbol h\|^2).
$$
对 $\boldsymbol x_0+\boldsymbol h\in S$，有 $\varphi_k(\boldsymbol x_0+\boldsymbol h)=\varphi_k(\boldsymbol x_0)=0$，故
$$
f(\boldsymbol x_0+\boldsymbol h)-f(\boldsymbol x_0)=\Phi(\boldsymbol x_0+\boldsymbol h)-\Phi(\boldsymbol x_0)=\tfrac{1}{2}\boldsymbol h^{\mathrm T}H(\boldsymbol x_0)\boldsymbol h+o(\|\boldsymbol h\|^2).
$$
若 $H(\boldsymbol x_0)$ 正定，记 $a=\min_{\|\boldsymbol h\|=1}\boldsymbol h^{\mathrm T}H(\boldsymbol x_0)\boldsymbol h>0$，则
$$
\boldsymbol h^{\mathrm T}H(\boldsymbol x_0)\boldsymbol h\ge a\|\boldsymbol h\|^2,
$$
$$
f(\boldsymbol x_0+\boldsymbol h)-f(\boldsymbol x_0)\ge \|\boldsymbol h\|^2\!\left(\tfrac{a}{2}+o(1)\right)>0
$$
当 $\|\boldsymbol h\|$ 充分小时成立。故 $\boldsymbol x_0$ 为条件极小值点。负定情形类似。$\square$

### 7. Lagrange 乘数法的求解流程（总结）

1. **建模**：写出目标 $f$ 与约束 $\varphi_k$，验证 $m<n$。
2. **构造**：$L=f+\sum_{k}\lambda_k\varphi_k$。
3. **求驻点**：解 $\nabla L=\boldsymbol 0$（共 $n+m$ 个方程，$n+m$ 个未知数）。
4. **验秩**：检查 $\operatorname{rank}(\partial\varphi_k/\partial x_i)=m$。秩亏的点须单列考察。
5. **判别**：
   - 实际问题（紧集 + 连续 + 唯一驻点）：直接由实际意义判定；
   - 一般情形：计算 $H(\boldsymbol x_0)$ 看正定/负定；
   - $H$ 不定时改用 bordered Hessian 或直接比较函数值。

### 8. 例题

**例 4.6**　求函数 $f(x,y,z)=xyz$ 在条件 $x+y+z=a\;(x,y,z>0,\,a>0)$ 下的极大值。

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

---

## 学习要点小结

1. **二元 Taylor 公式**：算子形式 $\bigl(\Delta x\partial_x+\Delta y\partial_y\bigr)^k f$ 是关键记忆点。
2. **Hesse 矩阵**：$H_f=[f_{x_ix_j}]$，是判断多元函数极值的核心工具。
3. **极值判别三步**：求驻点 → 算 Hesse 矩阵 → 看正定/负定。
4. **二元 $AC-B^2$ 判别表**必须烂熟。
5. **闭区域上最值**：内部驻点 + 边界极值 + 不可导点，全部比较。
6. **有约束极值两条路**：
   - 能消元 → 化为无约束（如教材例 4.5 Heron 公式）；
   - 不能消元 → Lagrange 乘数法。
7. **Lagrange 乘数法的本质**：约束极值点处 $\nabla f$ 与各 $\nabla \varphi_k$ 线性相关，对应 Lagrange 函数 $L=f+\sum\lambda_k\varphi_k$ 的驻点。
8. **正则性条件不可忽略**：必要条件层面需 $\varphi_y\ne 0$（二元）或一般情形下约束 Jacobi 矩阵满秩（$\operatorname{rank}=m$）。
9. **充分条件**：固定 $\boldsymbol\lambda=\boldsymbol\lambda_0$ 得 $\Phi(\boldsymbol x)$，看其 Hesse 矩阵的正定/负定性；不定时用 bordered Hessian 或在切空间限制。
10. **几何解释**：
    - 二元：$f$ 的等值线与约束曲线相切；
    - 三元：$f$ 的等值面与约束曲面相切。
11. 实际问题中，若解唯一且最值显然存在，可直接断定该解即为最值点（如盒子表面积问题）。
12. **方法推广层次**（本节）：2 元 1 约束 → 3 元 1 约束 → 3 元 2 约束 → $n$ 元 $m$ 约束，统一思想是"约束 + 隐函数 → 化无约束 → 必要条件 → 梯度线性相关 → Lagrange 乘数"。

---

> **参考**：本节内容综合教材 §5.4 正文，并补充了《工科数学分析基础（第三版）》课堂笔记中关于：
> - 化无约束法 + Heron 公式例 4.5；
> - 三元单约束 / 三元双约束的隐函数推导；
> - $n$ 元 $m$ 约束情形的约束规格条件（rank 条件）；
> - 条件极值的 Hesse 矩阵充分性判别及证明。
