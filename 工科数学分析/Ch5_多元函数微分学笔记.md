# 第5章 多元函数微分学及其应用

---

## §5.3.5 高阶偏导数与高阶全微分

### 1. 高阶偏导数

$$\frac{\partial}{\partial y}\left(\frac{\partial z}{\partial x}\right) = \frac{\partial^2 z}{\partial x \partial y} = f_{xy} / f_{12}$$

**Ex 12.** 求 $z = e^{x+2y}$ 的所有二阶偏导。

$$\frac{\partial z}{\partial x} = e^{x+2y}, \quad \frac{\partial z}{\partial y} = 2e^{x+2y}$$

$$\frac{\partial^2 z}{\partial x^2} = e^{x+2y}, \quad \frac{\partial^2 z}{\partial x \partial y} = 2e^{x+2y}$$

$$\frac{\partial^2 z}{\partial y^2} = 4e^{x+2y}, \quad \frac{\partial^2 z}{\partial y \partial x} = 2e^{x+2y}$$

**Ex 13.** 求 $z = \arctan\frac{y}{x}$ 的所有二阶偏导。

$$\frac{\partial z}{\partial x} = \frac{-\frac{y}{x^2}}{1+\frac{y^2}{x^2}} = -\frac{y}{x^2+y^2}, \quad \frac{\partial z}{\partial y} = \frac{\frac{1}{x}}{1+\left(\frac{y}{x}\right)^2} = \frac{x}{x^2+y^2}$$

$$\frac{\partial^2 z}{\partial x^2} = \frac{2xy}{(x^2+y^2)^2}, \quad \frac{\partial^2 z}{\partial x \partial y} = -\frac{x^2+y^2-2y^2}{(x^2+y^2)^2} = \frac{y^2-x^2}{(x^2+y^2)^2}$$

$$\frac{\partial^2 z}{\partial y^2} = -\frac{2xy}{(x^2+y^2)^2}, \quad \frac{\partial^2 z}{\partial y \partial x} = \frac{x^2+y^2-2x^2}{(x^2+y^2)^2} = \frac{y^2-x^2}{(x^2+y^2)^2}$$

**问：** $z_{yx} \equiv z_{xy}$？不一定。

**例：**
$$f(x,y) = \begin{cases} xy\frac{x^2-y^2}{x^2+y^2}, & x^2+y^2 \neq 0 \\ 0, & x^2+y^2 = 0 \end{cases}$$

$$f_x(x,y) = \begin{cases} \frac{y(x^4-y^4+4x^2y^2)}{(x^2+y^2)^2}, & x^2+y^2 \neq 0 \\ 0, & x^2+y^2 = 0 \end{cases}$$

$$f_y(x,y) = \begin{cases} \frac{x(x^4-y^4-4x^2y^2)}{(x^2+y^2)^2}, & x^2+y^2 \neq 0 \\ 0, & x^2+y^2 = 0 \end{cases}$$

$$f_{xy}(0,0) = \lim_{\Delta y \to 0} \frac{f_x(0,\Delta y)-f_x(0,0)}{\Delta y} = \lim_{\Delta y \to 0} \frac{-\Delta y}{\Delta y} = -1$$

$$f_{yx}(0,0) = \lim_{\Delta x \to 0} \frac{f_y(\Delta x,0)-f_y(0,0)}{\Delta x} = \lim_{\Delta x \to 0} \frac{\Delta x}{\Delta x} = 1$$

**定理**（$z_{xy}=z_{yx}$ 相等的充分条件）：若 $f_{xy}$ 和 $f_{yx}$ 在 $(x_0,y_0)$ 都连续，则 $f_{xy}(x_0,y_0) = f_{yx}(x_0,y_0)$。

**Ex 14.** 若 $z = x \cdot f\left(2x, \frac{y}{x}\right)$，其中 $f(u,v)$ 的二阶偏导数连续，求 $z_{xy}$。

**解：**

① $z \to z_x \to z_{xy}$

$$z_x = f + x\left(2f_1 - \frac{y}{x^2}f_2\right) = f + 2x f_1 - \frac{y}{x}f_2$$

$$z_{xy} = \frac{2y}{x}f_2 + 2x f_{12} \cdot \frac{1}{x} - \frac{1}{x}f_2 - \frac{y}{x}f_{22} \cdot \frac{1}{x} = 4y f_{12} - \frac{2y^2}{x^2}f_{22}$$

② $z \to z_y \to z_{yx} \to z_{xy}$

$$z_y = x \cdot \left(f_2 \cdot \frac{1}{x}\right) = 2y f_2$$

$$z_{yx} = 2y\left[f_{21} \cdot 2 + f_{22}\left(-\frac{y}{x^2}\right)\right] = 4y f_{21} - \frac{2y^2}{x^2}f_{22} = z_{xy}$$

### 2. 高阶全微分

设 $z = f(x,y)$ 的二阶偏导数都连续。

则 $dz = f_x dx + f_y dy$，其中 $x,y$ 与它们的微分 $dx, dy$ 互相独立。

固定 $dx, dy$，将 $dz$ 作为 $x,y$ 的函数。

定义二阶微分 $d^2z = d(dz)$。

对自变量 $dx, dy$，$d(dx)=d(dy)=0$。此时

$$d^2z = d(f_x dx + f_y dy) = f_{xx}dx^2 + f_{yy}dy^2 + 2f_{xy}dxdy$$

---

## §5.3.6 由一个方程确定隐函数的微分法

设 $F(x,y)=0$。隐函数存在条件的分析：

其一：存在点 $P_0(x_0,y_0)$ 使 $F(x_0,y_0)=0$。集合 $\Gamma = \{(x,y)\in \mathbb{R}^2 \mid F(x,y)=0\}$ 非空。

它是曲面 $z=F(x,y)$ 与平面 $z=0$ 的交线。

令 $\Phi(x,y,z) = F(x,y) - z$，则梯度 $\nabla\Phi = (F_x, F_y, -1)$。

与等值面 $\Phi=0$（即曲面 $z=F(x,y)$）正交。

设光滑曲线 $\gamma(t) = (x(t), y(t), z(t))$ 是曲面 $z=F(x,y)$ 上通过点 $Q_0(x_0,y_0,0)$，由 $\Phi(x(t),y(t),z(t)) \equiv 0$ 得

$$0 = \Phi_x \frac{dx}{dt} + \Phi_y \frac{dy}{dt} + \Phi_z \frac{dz}{dt}$$

切向量 $\frac{d\gamma}{dt} \perp \nabla\Phi$。

过 $Q_0$ 且垂直于 $\nabla\Phi(Q_0)$ 的曲面称为曲面 $z=F(x,y)$ 在 $Q_0$ 的**切平面**。

它的方程为

$$0 = \nabla\Phi(Q_0) \cdot (x-x_0, y-y_0, z-z_0) = F_x(P_0)(x-x_0) + F_y(P_0)(y-y_0) - (z-z_0)$$

对 $Q_0(x_0,y_0,0)$ 有 $F_x(P_0)(x-x_0) + F_y(P_0)(y-y_0) - z = 0$。

其二：$\nabla\Phi(P_0) \neq (0,0)$，否则曲面 $z=F(x,y)$ 过点 $Q_0$ 的切平面为 $z=0$。此时曲面 $z=F(x,y)$ 与平面 $z=0$ 相切于 $Q_0$，这可能导致交集 $\Gamma$ 不是一条曲线而是单点。

其三：若要求 $y=y(x)$ 可微，则 $F$ 可微时，由 $F(x,y(x)) \equiv 0$ 及链式法则

$$F_x + F_y \frac{dy}{dx} = 0$$

若 $F_y(x_0,y_0) \neq 0$，则 $\left.\frac{dy}{dx}\right|_{x=x_0} = -\frac{F_x(x_0,y_0)}{F_y(x_0,y_0)}$。

**定理 3.6**（隐函数的存在唯一性、可微性）

设 (i) $F(x,y)$ 在区域 $D$ 上连续，$P_0(x_0,y_0)$ 为 $D$ 的内点。

(ii) $F(x_0,y_0)=0$ —— 初始条件。

(iii) $F_y(x_0,y_0) \neq 0$；

(iv) $F_y(x,y)$ 在 $D$ 内连续。

(iii)(iv) $\Rightarrow$ 存在某邻域 $U(P_0)$ 使 $F_y|_{U(P_0)} \neq 0$。不妨设 $F_y > 0$。

对某个固定的 $x$，若 $F(x,y)=0$，且 $(x,y) \in U(P_0)$ 则 $y$ 唯一。

则在点 $P_0$ 的某邻域 $U(P_0) \subset D$ 内，方程 $F(x,y)=0$ 唯一确定一个函数 $y=f(x)$，$x \in (x_0-\alpha, x_0+\alpha)$ 使得：

1° $f(x_0)=y_0$。当 $x \in (x_0-\alpha, x_0+\alpha)$ 时 $(x,f(x)) \in U(P_0)$，$F(x,f(x))=0$。

2° $f(x)$ 在 $(x_0-\alpha, x_0+\alpha)$ 上连续，若 $F(x,y)$ 在 $D$ 内连续，则 $f(x)$ 可导且导数连续。

只证明 $F_x, F_y$ 在 $D$ 内都连续的情形。

考虑初值问题 $\frac{dy}{dx} = -\frac{F_x(x,y)}{F_y(x,y)}$，$y(x_0)=y_0$。

因为 $-\frac{F_x(x,y)}{F_y(x,y)}$ 在 $P_0$ 附近连续，由 ODE 存在性定理，上述问题必有 $f(x)$ 满足。

$$\frac{d}{dx}[F(x,y(x))] = F_x + F_y \cdot \frac{dy}{dx} = 0$$

说明 $F(x,y(x)) \equiv F(x_0,y(x_0)) = F(x_0,y_0) = 0$。

类似地，由三元方程 $F(x,y,z)=0$ 确定二元隐函数 $z=f(x,y)$ 可微。

代入方程得 $F(x,y,f(x,y)) \equiv 0$。

取微分 $F_x dx + F_y dy + F_z dz = 0$

当 $F_z \neq 0$ 时，$dz = -\frac{F_x}{F_z}dx - \frac{F_y}{F_z}dy$。

**例 3.25.** 设方程 $e^z + xyz = e$ 确定函数 $z=z(x,y)$，求 $z_x, z_y, z_{xy}$。

**解：** 对原方程取微分得 $0 = d(e^z) + d(xyz)$。

$$dz = -\frac{yz\,dx + xz\,dy}{e^z+xy} = e^z dz + yz\,dx + xz\,dy + xy\,dz$$

$$z_x = -\frac{yz}{e^z+xy}, \quad z_y = -\frac{xz}{e^z+xy}$$

因此

$$z_{xy} = -\frac{z + y z_y}{e^z+xy} + yz \cdot \frac{e^z z_y + x}{(e^z+xy)^2}$$

$$= -\frac{z}{\square} - \frac{y}{\square}\left(\frac{-xz}{\square}\right) + \frac{yz e^z}{\square^2}\left(-\frac{xz}{\square}\right) + \frac{xyz}{\square^2}$$

$$= -\frac{z}{\square} + \frac{2xyz}{\square^2} - \frac{xyz^2 e^z}{\square^3}$$

---

## §5.4 多元函数的 Taylor 公式与极值

### §5.4.1 中值定理

设 $f(x,y)$ 在凸区域 $D \subset \mathbb{R}^2$ 上可微，则对 $D$ 中任意两点 $(x_0,y_0), (x_0+\Delta x, y_0+\Delta y)$，一定存在 $\theta \in (0,1)$ 使

$$f(x_0+\Delta x, y_0+\Delta y) - f(x_0,y_0) = f_x(x_0+\theta\Delta x, y_0+\theta\Delta y)\Delta x + f_y(x_0+\theta\Delta x, y_0+\theta\Delta y)\Delta y$$

**证：** $\varphi(t) = f(x_0+t\Delta x, y_0+t\Delta y)$ 在 $[0,1]$ 可微。

由 Lagrange 中值定理，存在 $\theta \in (0,1)$，使

$$\varphi(1)-\varphi(0) = \varphi'(\theta) = f_x(x_0+\theta\Delta x, y_0+\theta\Delta y)\Delta x + f_y(x_0+\theta\Delta x, y_0+\theta\Delta y)\Delta y$$

**EX1** 设 $f(x,y)$ 的二阶偏导数连续，写出一元函数 $\Phi(t) = f(x_0+t\Delta x, y_0+t\Delta y)$ 在 $t=0$ 的二阶 Taylor 公式（带 Peano）。

**解：** 依条件 $\Phi(t)$ 的二阶导数连续，则

$$\Phi(t) = \Phi(0) + \Phi'(0)t + \frac{1}{2}\Phi''(0)t^2 + o(t^2)$$

其中 $\Phi'(t) = f_x \Delta x + f_y \Delta y$

$$\Phi''(t) = (f_{xx}\Delta x + f_{xy}\Delta y)\Delta x + (f_{yx}\Delta x + f_{yy}\Delta y)\Delta y$$

$$= f_{xx}\Delta x^2 + f_{yy}\Delta y^2 + 2f_{xy}\Delta x \Delta y$$

$$= (\Delta x \quad \Delta y) \begin{pmatrix} f_{xx} & f_{xy} \\ f_{xy} & f_{yy} \end{pmatrix} \begin{pmatrix} \Delta x \\ \Delta y \end{pmatrix}$$

令 $x_0 = (x_0,y_0)$，$\Delta x = (\Delta x, \Delta y)$，则 $f(x_0+\Delta x) = f(x_0) + \langle \nabla f(x_0), \Delta x \rangle + \frac{1}{2} \Delta x \cdot H_f(x_0) \cdot (\Delta x)^T + o(\|\Delta x\|^2)$

$H_f = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{xy} & f_{yy} \end{pmatrix}|_{x_0}$（Hesse 矩阵）

对自变量 $x,y$ 的一阶微分 $dx, dy$ 有 $dx=\Delta x, dy=\Delta y$。

于是上式可写成

$$f(x_0+dx, y_0+dy) = f(x_0,y_0) + dz + \frac{1}{2}d^2z + o(dx^2+dy^2)$$

**例 4.1** 设 $z=z(x,y)$ 是由方程 $z^3 - 2xz + y = 0$ 确定的隐函数，且 $z(1,1)=1$。求 $z(x,y)$ 在点 $(1,1)$ 处的二阶 Taylor 带 Peano。

**注：** 将 $x=1, y=1$ 代入原方程 $0 = z^3 - 2z + 1 = (z-1)(z^2+z-1)$

三个实根 $z=1, \frac{-1\pm\sqrt{5}}{2}$。

**方法1：** 原方程两边取微分得 $3z^2 dz - 2(z\,dx + x\,dz) + dy = 0$。

解出 $dz = \frac{2z\,dx - dy}{3z^2 - 2x}$。

则 $z_x = \frac{2z}{3z^2-2x}$，$z_y = -\frac{1}{3z^2-2x}$。

$z_x(1,1)=2$，$z_y(1,1)=-1$，$z(1,1)=1$。

$$z_{xx} = \frac{-2(3z^2+2x)z_x}{\square^2}, \quad z_{xy} = \frac{-2(3z^2+2x)z_y}{\square^2}, \quad z_{yy} = \frac{6z\,z_y}{\square^2}$$

$x=y=z=1$ 时 $z_{xx}=-16$，$z_{xy}=10$，$z_{yy}=-6$。

因此 $z(1+x, 1+y) = 1 + 2x - y + \frac{1}{2}(-16x^2 + 20xy - 6y^2) + o(x^2+y^2)$。

**方法二：** 对原方程取微分得 $3z^2 dz - 2(z\,dx + x\,dz) + dy = 0$。

$$(3z^2-2x)dz - 2z\,dx + dy = 0$$

由 $z(1,1)=1$ 得 $dz|_{(1,1,1)} = 2dx - dy$。

再取微分 $0 = d(3z^2-2x)dz + (3z-2x)d^2z - 2\,dz\,dx$

$$= 6z(dz)^2 + (3z-2x)d^2z - 4\,dz\,dx$$

于是 $d^2z|_{(1,1)} = 4dx(2dx-dy) - 6(2dx-dy)^2 = -16(dx)^2 + 20dx\,dy - 6(dy)^2$。

---

### §5.4.2 无约束极值、最值

#### 1. 无约束极值

设 $f$ 定义在点 $P_0$ 的某邻域 $U(P_0)$ 内，若 $\forall P \in U(P_0)$ 都有 $f(P) \leq f(P_0)$，则称 $f$ 在 $P_0$ 取**极大值**。

设 $f(x,y)$ 在 $P_0(x_0,y_0)$ 取极值，则对任何实数 $h$，两个一元函数

$$\varphi(t) = f(x_0+th, y_0), \quad \psi(t) = f(x_0, y_0+th)$$

均在 $t=0$ 取极值。由 Fermat 引理，$\varphi'(0) = f_x(x_0,y_0) \cdot h = 0$，$\psi'(0) = f_y(x_0,y_0)h = 0$。

由 $h$ 的任意性，$f_x(x_0,y_0) = f_y(x_0,y_0) = 0$。

**定理 4.3**（极值的必要条件） 设 $f$ 在点 $x_0$ 的一阶偏导数都存在，若 $f$ 在 $x_0$ 取极值，则 $\nabla f(x_0) = 0$。

（为何不取 $\Phi(t) = f(x_0+th, y_0+tk)$ 其中 $t,k$ 任意？$\Phi(t)$ 要求可微，$\varphi(t)$ 和 $\psi(t)$ 只要求偏导数存在。）

满足 $\nabla f = 0$ 的点叫做**驻点**（stable point）。

极值点一定是驻点，驻点不一定是极值点，例如鞍点。

由 Taylor 公式：$f(x_0+\Delta x) - f(x_0) = \langle \nabla f(x_0), \Delta x \rangle + \frac{1}{2}(\Delta x)^T H_f(x_0) \Delta x + o(\|\Delta x\|)$

若 $x_0$ 是驻点，则 $f(x_0+\Delta x) - f(x_0) = \frac{1}{2}(\Delta x)^T H_f(x_0) \Delta x + o(\|\Delta x\|)$。

**定理 4.4**（极值的充分条件） 设 $f(x_0)$ 在 $U(x_0)$ 内二阶偏导数连续，$x_0$ 是驻点，$H_f(x_0)$ 是 $x_0$ 点的 Hesse 矩阵 $\left(\frac{\partial^2 f}{\partial x_i \partial x_j}(x_0)\right)_{n\times n}$。

若 Hesse 矩阵是正定（负定）的，则 $f(x_0)$ 为极小（大）值。

因为 Hesse 矩阵是实对称矩阵，存在实正交矩阵 $Q$，使得

$$Q^T H_f(x_0) Q = \text{diag}\{\lambda_1, \lambda_2, \dots, \lambda_n\}$$

其中 $\lambda_1, \dots, \lambda_n$ 是 $H_f(x_0)$ 的实特征值。

令 $\Delta x = Qy$，则 $\Delta z = \frac{1}{2}y^T(Q^T H_f(x_0)Q)y + o(\|y\|^2) = \frac{1}{2}y^T \text{diag}\{\lambda_i\} y + o(\|y\|^2)$。

记 $y = (y_1, y_2, \dots, y_n)^T$，$\Delta z = \frac{1}{2}\sum_{i=1}^n \lambda_i y_i^2 + o(\sum_{i=1}^n y_i^2)$。

对二元函数 $f(x,y)$，记 $A = f_{xx}(x_0)$，$B = f_{xy}(x_0)$，$C = f_{yy}(x_0)$，$H_f(x_0) = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$。

$AC-B^2 = \lambda_1\lambda_2$，$A+C = \lambda_1+\lambda_2$。

- **正定：** (1) $A>0$ 且 $AC-B^2>0$，$x_0$ 为极小值点。
- **负定：** (1) $A<0$ 且 $AC-B^2>0$，$x_0$ 为极大值点。
- **不定：** (3) $AC-B^2<0$，$x_0$ 不是极值点。
- (4) $AC-B^2=0$，无法依据定理 4.4 判定。

**例：** $f(x,y)=x^2$，$f_x=2, f_{xx}=2, f_{xy}=0, f_{yy}=0$，$AC-B^2=0$，原点 $(0,0)$ 是极小值点。

$g(x,y)=x^2+y$，$(0,0)$ 不是极值点，$A=2, B=C=0$，$AC-B^2=0$。

**例 4.2** 求 $f(x,y) = x^3 + y^3 + 3xy$ 的极值。

**解：** 先求驻点 $f_x = 3x^2 + 3y = 0$，$f_y = 3y^2 + 3x = 0$。

求出驻点 $P_1(0,0)$，$P_2(-1,-1)$。

再求二阶偏导 $f_{xx}=6x$，$f_{xy}=3$，$f_{yy}=6y$。

$H_f(P_1) = \begin{pmatrix} 0 & 3 \\ 3 & 0 \end{pmatrix}$，$H_f(P_2) = \begin{pmatrix} -6 & 3 \\ 3 & -6 \end{pmatrix}$。

$P_1$ 非，$P_2$ 为极大值点，$f(P_2)=1$ 是极大值。

**例 4.3** 求 $f(x,y) = 2x^2 - 3xy^2 + y^4$ 的极值点。

**解：** $f_x = 4x - 3y^2$，$f_y = -6xy + 4y^3$。

$f_x = f_y = 0 \Rightarrow$ 唯一驻点 $(0,0)$。

$f_{xx}=4$，$f_{xy}=-6y$，$f_{yy}=-6x+12y^2$。

$f_{xx}(0,0)=4$，$f_{xy}(0,0)=f_{yy}(0,0)=0$。

$A=4, B=C=0$，$AC-B^2=0$。

又因为 $f(x,y)-f(0,0) = (2x-y^2)(x-y^2) = \begin{cases} >0 & x>y^2 \text{ 或 } x<y^2/2 \\ <0 & \frac{1}{2}y^2 < x < y^2 \end{cases}$

$\therefore f(0,0)=0$ 不是极值。

**EX2** 求方程 $2x^2+y^2+z^2+2xy-2x-2y-4z+4=0$ 所确定的隐函数 $z=z(x,y)$ 的极值。

**解：** 两边取微分 $4x\,dx + 2y\,dy + 2z\,dz + 2x\,dy + 2y\,dx - 2\,dx - 2\,dy - 4\,dz = 0$。

$$(4x+2y-2)dx + (2y+2x-2)dy + (2z-4)dz = 0$$

$$dz = \frac{(1-2x-y)dx + (1-x-y)dy}{z-2}$$

$$z_x = \frac{1-2x-y}{z-2}, \quad z_y = \frac{1-x-y}{z-2}$$

驻点 $(0,1)$，$z=1$ 或 $3$。在 $(0,1,1)$ 和 $(0,1,3)$ 附近确定 $z=z(x,y)$。

再取微分 $(4dx+2dy)dx + (2dy+2dx)dy + 2dz^2 + (2z-4)d^2z = 0$。

代入 $dz=0$，$0 = 4dx^2 + 4dxdy + 2dy^2 + (2z-4)d^2z$。

$$d^2z = \frac{2dx^2 + 4dxdy + dy^2}{2-z}$$

$$z_{xx} = \frac{2}{2-z}, \quad z_{xy} = \frac{2}{2-z}, \quad z_{yy} = \frac{1}{2-z}$$

当 $x=0, y=1, z=1$：$A=2, C=1, B=1$，$AC-B^2=1$ 极小。

当 $x=0, y=1, z=3$：$A=-2, C=-1, B=-1$，$AC-B^2=1$ 极大。

#### 2. 最大值、最小值

有界闭域上的连续函数可取到最大值与最小值。它们可能在区域内部取到（极值），也可能在区域的边界取到。

**例 4.4** 求 $f(x,y) = x^2 + 2x^2y + y^2$ 在圆域 $D = \{(x,y) \mid x^2+y^2 \leq 1\}$ 上的最值。

**解：** $f_x = 2x + 4xy$，$f_y = 2x^2 + 2y$。驻点 $P_1(0,0)$，$P_2(\frac{1}{2}, -\frac{1}{2})$，$P_3(-\frac{1}{2}, -\frac{1}{2})$。

$f(P_1)=0$，$f(P_2)=f(P_3)=\frac{1}{4}$。

边界上 $x^2+y^2=1$，$f(x,y) = 1 + 2(1-y^2)y = \varphi(y)$，定义在 $y \in [-1,1]$。

由 $\varphi'(y) = 2-6y^2=0$，$y = \pm\frac{1}{\sqrt{3}}$ 以及 $\varphi(\pm\frac{1}{\sqrt{3}}) = 1 \pm \frac{4\sqrt{3}}{9}$。

比较：$\max_D f = 1 + \frac{4\sqrt{3}}{9}$，$\min_D f = 0$。

**EX 3** 证明：圆的外切三角形中，等边三角形面积最小。

**证：** 设圆的半径为 $a$，$S = a^2(\tan\frac{\alpha}{2} + \tan\frac{\beta}{2} + \tan\frac{\gamma}{2})$。

$\alpha+\beta+\gamma=2\pi$，$0<\alpha,\beta,\gamma<\pi$。

$= a^2(\tan\frac{\alpha}{2} + \tan\frac{\beta}{2} - \tan\frac{\alpha+\beta}{2})$。

$S$ 的定义域 $0<\alpha,\beta<\pi$，$\alpha+\beta>\pi$，即 $\triangle ABC$ 不含边。

$$S_\alpha = \frac{a^2}{2}\left(\sec^2\frac{\alpha}{2} - \sec^2\frac{\alpha+\beta}{2}\right), \quad S_\beta = \frac{a^2}{2}\left(\sec^2\frac{\beta}{2} - \sec^2\frac{\alpha+\beta}{2}\right)$$

以及 $0<\frac{\alpha}{2}, \frac{\beta}{2}<\frac{\pi}{2}$，$\cos\frac{\alpha}{2}=\cos\frac{\beta}{2}=-\cos\frac{\alpha+\beta}{2}$ 有一解 $\alpha=\beta=\frac{2\pi}{3}$。

$A = S_{\alpha\alpha} = 4\sqrt{3}a^2$，$B = S_{\alpha\beta} = 2\sqrt{3}a^2$，$C = S_{\beta\beta} = 4\sqrt{3}a^2$，$A>0$，$AC-B^2>0$。

$\therefore S$ 在 $(\frac{2\pi}{3}, \frac{2\pi}{3})$ 取极小值 $3\sqrt{3}a^2$。

下证 $\min_D S = 3\sqrt{3}a^2$。

其一，$S$ 在 $D$ 上连续，但 $D$ 不是有界闭域，$S$ 在 $D$ 上处处有偏导数。

其二，$S$ 在 $\triangle ABC$ 的边界附近的值 $\to 3\sqrt{3}a^2$。

$AC$：当 $\alpha+\beta \to \pi+0$ 时，由 $0<\frac{\alpha}{2}, \frac{\beta}{2}<\frac{\pi}{2}$ 知 $S > \frac{a^2}{2}(-\tan\frac{\alpha+\beta}{2}) \to +\infty$。

$AB, BC$：$\alpha \to \pi-0$ 时，由 $0<\frac{\alpha}{2}, \frac{\beta}{2}<\frac{\pi}{2}$ 以及 $\frac{\alpha+\beta}{2}<\pi$ 知 $S > \frac{a^2}{2}\tan\frac{\alpha}{2} \to +\infty$。

由 $\beta=\pi-\delta, \alpha=\pi-\delta, \alpha+\beta=\pi+\delta$ 围成 $\triangle A_1B_1C_1$。

则 $D = \triangle A_1B_1C_1 \cup (\text{int}\triangle ABC - \triangle A_1B_1C_1) = D_1 \cup (D-D_1)$。

其中 $\triangle A_1B_1C_1$ 是有界闭域且存在 $\delta>0$ s.t. $S|_{D-D_1} > 6\sqrt{3}a^2$。

于是 $\min_D S = \min_{D_1} S$ 在 $D_1$ 内点 $(\frac{2}{3}\pi, \frac{2}{3}\pi)$ 取到。

因此 $\min_D S = S(\frac{2}{3}\pi, \frac{2}{3}\pi) = 3\sqrt{3}a$。

---

### §5.4.3 有约束极值：Lagrange 乘数法

#### 1. 一个约束条件

二元函数 $z=f(x,y)$ 目标函数，约束条件 $g(x,y)=0$。

设方程 $g(x,y)=0$ 确定某隐函 $y=y(x)$，$g_y(P_0) \neq 0$。

若极值在 $P_0$ 取到，则 $z=f(x,y(x))$ 在 $x=x_0$ 处取到极值。

$$\frac{dz}{dx} = f_x + f_y \frac{dy}{dx} = 0, \quad \frac{d}{dx}g(x,y(x)) = g_x + g_y \frac{dy}{dx} = 0$$

$\nabla f \cdot \nabla g \perp (1, \frac{dy}{dx})$（曲线 $y=y(x)$ 的切向量），$\nabla f \parallel \nabla g$。

因此存在常数 $\lambda_0$ 使 $\nabla f(P_0) = \lambda_0 \nabla g(P_0)$，$g(P_0)=0$ （*2）

引入变量 $\lambda$ 以及函数 $L(x,y,\lambda) = f(x,y) - \lambda g(x,y)$ （*3）

$\because L_x = f_x - \lambda g_x$，$L_y = f_y - \lambda g_y$，$L_\lambda = -g$。

$\therefore$（*2）等价于 $\nabla L(P_0) = 0$ （*4）

若 $P_0(x_0,y_0)$ 为条件极值点，则 $(x_0,y_0,\lambda_0)$ 为 $L(x,y,\lambda)$ 的驻点。

该方法称为**拉格朗日乘数法**。条件极值 $\to$ 无条件极值。

若约束集 $\{(x,y)\mid g(x,y)=0\}$ 是有界闭集则条件极值一定存在。

设 $g_x, g_y$ 在 $D$ 上不全为 $0$。求出拉格朗日函数（*3）的驻点，以及相应函数，再取最大或最小。

**EX 4.** 设 $x^2+xy+y^2=1$，求 $2x+3y$ 最大值。

**解：** 令 $L(x,y,\lambda) = 2x+3y - \lambda(x^2+xy+y^2-1)$

$$\nabla L = 0 \Rightarrow \begin{cases} L_x = 2 - \lambda(2x+y) = 0 & \text{①} \\ L_y = 3 - \lambda(x+2y) = 0 & \text{②} \\ L_\lambda = -(x^2+xy+y^2-1) = 0 \end{cases}$$

①② $\Rightarrow$ $\begin{cases} x = \pm\frac{1}{\sqrt{21}} \\ y = \pm\frac{4}{\sqrt{21}} \end{cases}$ 代入得 $\lambda = \dots$

$(2x+3y)_{\max} = \frac{14}{\sqrt{21}}$

#### 三元函数极值

$u=f(x,y,z)$，$g(x,y,z)=0$。

若极值在点 $P_0(x_0,y_0,z_0)$ 处取到。

$g(x,y,z)=0$，$g_z \neq 0 \Rightarrow$ 隐 $z=z(x,y)$。

$g(x,y,z(x,y))=0$ 求偏导得 $g_x + g_z z_x = 0$，$g_y + g_z z_y = 0$。

$\nabla g \perp (1,0,z_x)=\vec{v_1}$，$\nabla g \perp (0,1,z_y)=\vec{v_2}$。

$\nabla g \parallel \vec{v_1} \times \vec{v_2} = (-z_x, -z_y, 1) = \vec{v_3}$。

因为 $u=f(x,y,z(x,y))$ 在 $Q_0(x_0,y_0)$ 取极值

$u_x = f_x + f_z \cdot z_x = 0$，$u_y = f_y + f_z \cdot z_y = 0$。

$\nabla f \perp \vec{v_1}$，$\nabla f \perp \vec{v_2} \Rightarrow \nabla f \parallel \vec{v_3}$。

说明 $\nabla f(P_0) \parallel \nabla g(P_0)$。令 $L(x,y,z,\lambda) = f(x,y,z) - \lambda g(x,y,z)$。

则条件极值 $\Rightarrow \nabla L = 0 \Leftrightarrow \nabla f - \lambda \nabla g = 0$，$g=0$。

**例 4.8** 设 $x,y,z>0$，$xyz=V$，求 $u=xy+2yz+2zx$ 的 min。

令 $L(x,y,z,\lambda) = xy+2yz+2zx - \lambda(xyz-V)$

$$\nabla L = 0 \Rightarrow \begin{cases} L_x = y+2z-\lambda yz = 0 & \text{①} \\ L_y = x+2z-\lambda xz = 0 & \text{②} \\ L_z = 2y+2x-\lambda xy = 0 & \text{③} \\ L_\lambda = V-xyz = 0 & \text{④} \end{cases}$$

①$\times$x - ②$\times$y：$2z(x-y)=0 \Rightarrow x=y$

③$\times$y - ①$\times$z：$xy-2zx=0 \Rightarrow y=2z$

代入④ $V = 2z^3$，$z = \sqrt[3]{\frac{V}{2}}$，$\therefore u = 12z^2 = 6\left(\frac{V}{2}\right)^{\frac{2}{3}}$。

**EX** 设 $x,y,z>0$ 证明 $xyz \leq \left(\frac{x+y+z}{3}\right)^3$。

**证：** $u=xyz$，$x+y+z=a>0$。

令 $L(x,y,z) = xyz - \lambda(x+y+z-a)$

$$\nabla L = 0 \Rightarrow \begin{cases} L_x = yz-\lambda = 0 \\ L_y = xz-\lambda = 0 \\ L_z = xy-\lambda = 0 \\ L_\lambda = -(x+y+z-a) = 0 \end{cases} \Rightarrow x=y=z=\frac{a}{3}, \quad u=\left(\frac{a}{3}\right)^3$$

约束集 $S: \{(x,y,z)\mid x+y+z=a, x,y,z>0\}$ 为 $\triangle ABC$。

为有界闭域，$u=xyz$ 在 $S$ 上连续，可取到最大值与最小值。

最小值在 $\partial S$ 上，$u=0$，$\therefore$ 最大值在内部，$\therefore$ 最大值为 $\left(\frac{a}{3}\right)^3$。

#### 2. 两个约束条件

$u=f(x,y,z)$，$g(x,y,z)=0$，$h(x,y,z)=0$。

设方程组 $\begin{cases} g(\cdot)=0 \\ h(\cdot)=0 \end{cases}$ 确定隐函数组 $x=x(z), y=y(z)$。

若 $u=f(x(z),y(z),z)$ 取极值，则 $\frac{du}{dz} = f_x \frac{dx}{dz} + f_y \frac{dy}{dz} + f_z = 0$，$(f_x,f_y,f_z) \cdot (\frac{dx}{dz}, \frac{dy}{dz}, 1) = 0$。

即 $\nabla f \perp \vec{T}$（曲线切向量）。将 $x=x(z), y=y(z)$ 代入约束条件得

$0 = g(x(z),y(z),z)$ 求导 $\Rightarrow g_x \frac{dx}{dz} + g_y \frac{dy}{dz} + g_z = 0$。

$0 = h(x(z),y(z),z)$ 求导 $\Rightarrow h_x \frac{dx}{dz} + h_y \frac{dy}{dz} + h_z = 0$。

$\therefore \nabla f, \nabla g, \nabla h \perp \vec{T}$，存在常数 $\lambda, \mu$ s.t. $\nabla f + \lambda \nabla g + \mu \nabla h = 0$。

令 $L(x,y,z,\lambda,\mu) = f(x,y,z) + \lambda g(x,y,z) + \mu h(x,y,z)$，$\nabla L = 0$。

**EX 5.** 求 $u=x^2+y^2+z^2$ 在约束条件 $\begin{cases} \frac{x^2}{4}+\frac{y^2}{5}+\frac{z^2}{25}=1 \\ z=x+y \end{cases}$ 下的最值。

**解：** $L(x,y,z,\lambda,\mu) = x^2+y^2+z^2 - \lambda\left(\frac{x^2}{4}+\frac{y^2}{5}+\frac{z^2}{25}-1\right) - \mu(x+y-z)$

$$\nabla L = 0 \Rightarrow \begin{cases} L_x = 2x - \frac{1}{2}\lambda x - \mu = 0 & \text{①} \\ L_y = 2y - \frac{2}{5}\lambda y - \mu = 0 & \text{②} \\ L_z = 2z - \frac{2}{25}\lambda z + \mu = 0 & \text{③} \\ L_\lambda = 1 - \frac{x^2}{4} - \frac{y^2}{5} - \frac{z^2}{25} = 0 & \text{④} \\ L_\mu = z - x - y = 0 & \text{⑤} \end{cases}$$

①$\times$x + ②$\times$y + ③$\times$z $\Rightarrow 2(x^2+y^2+z^2) - \lambda\left(\frac{x^2}{4}+\frac{y^2}{5}+\frac{z^2}{25}\right) - \mu(x+y-z) = 0$。

结合④⑤ $x^2+y^2+z^2=\lambda$。

由①②③ $x = \frac{\mu}{2-\frac{1}{2}\lambda}$，$y = \frac{\mu}{2-\frac{2}{5}\lambda}$，$z = \frac{\mu}{2-\frac{2}{25}\lambda}$。代入⑤

$$\frac{1}{2-\frac{1}{2}\lambda} + \frac{1}{2-\frac{2}{5}\lambda} + \frac{1}{2-\frac{2}{25}\lambda} = 0$$

$\lambda = 10 / \frac{75}{17}$。

**Another method.** From ①②③ 视 $x,y,z,\mu$ 为未知数，$\lambda$ 为系数，线性方程组有非零解：

$$\begin{vmatrix} 2-\frac{1}{2}\lambda & & -1 \\ & 2-\frac{2}{5}\lambda & -1 \\ & & 2-\frac{2}{25}\lambda & 1 \\ 1 & 1 & -1 & 0 \end{vmatrix} = (2-\frac{1}{2}\lambda)(2-\frac{2}{5}\lambda+2-\frac{2}{25}) - (-1)(2-\frac{2}{5}\lambda)(2-\frac{2}{25}\lambda)$$

$$= 12 - \frac{98}{25}\lambda + \frac{34}{125}\lambda^2$$

#### 3. 一般情形

$$\begin{cases} u = f(x), x = (x_1, x_2, \dots, x_n) \in \mathbb{R}^n \\ \varphi_k(x) = 0, \quad 1 \leq k \leq m < n \end{cases}$$

(1) 写出拉格朗日函数 $L(x,\lambda) = f(x) + \lambda_1\varphi_1(x) + \lambda_2\varphi_2(x) + \dots + \lambda_m\varphi_m(x)$。

由 $\nabla L = 0$ 求出全部驻点 $(x_0, \lambda_0)$。

其中 $x_0 = (x_{0,1}, x_{0,2}, \dots, x_{0,n})$，$\lambda_0 = (\lambda_{0,1}, \lambda_{0,2}, \dots, \lambda_{0,m})$。

并要求 $\text{rank}\left(\frac{\partial\varphi_k}{\partial x_i}\right)_{m\times n} = m$。

对方程组 $\varphi_k(x)=0$，$1\leq k \leq m$ 取微分得

$$\frac{\partial\varphi_1}{\partial x_1}dx_1 + \dots + \frac{\partial\varphi_1}{\partial x_m}dx_m + \frac{\partial\varphi_1}{\partial x_{m+1}}dx_{m+1} + \dots + \frac{\partial\varphi_1}{\partial x_n}dx_n = 0$$

$$\vdots$$

$$\frac{\partial\varphi_m}{\partial x_1}dx_1 + \dots + \frac{\partial\varphi_m}{\partial x_m}dx_m + \frac{\partial\varphi_m}{\partial x_{m+1}}dx_{m+1} + \dots + \frac{\partial\varphi_m}{\partial x_n}dx_n = 0$$

设 $\tilde{x} = (x_{m+1}, \dots, x_n)$ 且由约束条件确定隐函数组

$x_1 = x_1(\tilde{x}), \dots, x_m = x_m(\tilde{x})$。

#### (3) 条件极值的充分条件

对 $L$ 的每个驻点，计算 $\Phi(x) = L(x,\lambda_0)$ 在点 $x_0$ 处的 Hesse 矩阵

$H(x_0) = \left(\frac{\partial^2 L}{\partial x_i \partial x_j}(x_0,\lambda_0)\right)_{n\times n}$。若 $H(x_0)$ 正（负）定，则 $x_0$ 为条件极小（大）值点。

**证：** 注意到 $\nabla\Phi(x) = \nabla f(x) + \lambda_{0,1}\nabla\varphi_1(x) + \dots + \lambda_{0,m}\nabla\varphi_m(x)$，$\nabla\Phi(x_0)=0$。

定义约束集 $S = \{x \in \mathbb{R}^n \mid \varphi_k(x)=0, \quad 1\leq k \leq m\}$。

在 $S$ 上 $f(x) = \Phi(x)$。设 $x, x+h \in S$，则 $f(x+h)-f(x) = \Phi(x+h)-\Phi(x)$。

$$= \nabla\Phi(x) \cdot h + \frac{1}{2}h^T H(x) h + o(\|h\|^2)$$

$$f(x_0+h)-f(x_0) = \frac{1}{2}h^T H(x_0)h + o(\|h\|^2)$$

当 $H(x_0)$ 是正定矩阵时 $\alpha = \min_{\|h\|=1} h^T H(x_0)h > 0$。

此时 $h^T H(x_0)h \geq \alpha \|h\|^2$。于是 $f(x_0+h)-f(x_0) \geq \|h\|^2\left(\frac{\alpha}{2}+o(1)\right) \geq 0$。

**EX 6** 求方程 $2x^2+y^2+z^2+2xy-2x-2y-4z+4=0$ 确定的隐函数的极值。

**解：** $u=f(x,y,z)=z$，$g(x,y,z)=0$。

令 $L(x,y,z,\lambda) = z + \lambda g(x,y,z)$

$$\nabla L = 0 \Rightarrow \begin{cases} L_x = \lambda(4x+2y-2) = 0 \\ L_y = \lambda(2y+2x-2) = 0 \\ L_z = 1 + \lambda(2z-4) = 0 \end{cases} \Rightarrow x=0, y=1 \text{ 代入原方程 } z=1, \lambda=\frac{1}{2}; \quad z=3, \lambda=-\frac{1}{2}$$

$L_{xx}=4\lambda$，$L_{yy}=2\lambda$，$L_{zz}=2\lambda$。

$L_{xy}=2\lambda$，$L_{xz}=0$，$L_{yz}=0$。

① $L(x,y,z,\frac{1}{2})$ 在 $(0,1,1)$ 的 Hesse 为 $\begin{pmatrix} 2 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ 正定，$z(0,1)=1$ 是极小值。

② $L(x,y,z,-\frac{1}{2})$ 在 $(0,1,3)$ 的 Hesse 为 $\begin{pmatrix} -2 & -1 & 0 \\ -1 & -1 & 0 \\ 0 & 0 & -1 \end{pmatrix}$ 负定，$z(0,1)=3$ 是极大值。

---

### 蜂房问题

利用切割"翻折"，在每个角切一个三棱锥翻上去。

（图示：六棱柱切割示意图）

---

## §5.5 多元向量值函数的导数与微分

$n$ 元向量值函数 $f: A \subset \mathbb{R}^n \to \mathbb{R}^m$

$$f(x) = (f_1(x), f_2(x), \dots, f_m(x)), \quad x \in A$$

**极限：** 设 $a=(a_1,a_2,\dots,a_m) \in \mathbb{R}^m$，定义 $\lim_{x\to x_0} f(x) = a \Leftrightarrow \lim_{x\to x_0} f_i(x) = a_i, \forall i \in \{1,\dots,m\}$。

若 $\lim_{x\to x_0} f(x) = f(x_0)$，则称向量值函数 $f$ 在 $x=x_0$ 连续。

### §5.5.1 一元向量值函数

对 $f(x) = (f_1(x), f_2(x), \dots, f_m(x))$，定义导数 $f'(x_0) = (f_1'(x_0), f_2'(x_0), \dots, f_m'(x_0))$。

定义二阶导数 $f''(x_0) = (f_1''(x_0), f_2''(x_0), \dots, f_m''(x_0))$。

若存在向量 $a=(a_1,a_2,\dots,a_m)$，使 $f(x_0+\Delta x) = f(x_0) + a \cdot \Delta x + o(\Delta x)$，则称 $f$ 在 $x=x_0$ 处可微。

$f$ 在 $x_0$ 处微分 $df(x_0) = a\,dx$。

**定理** $f(x)=(f_1(x),\dots,f_m(x))$ 在 $x_0$ 可微 $\Leftrightarrow$ $\forall f_i(x)$ 在 $x=x_0$ 可微。

### §5.5.2 二元向量值函数

$$f(x_1,x_2) = (f_1(x_1,x_2), \dots, f_m(x_1,x_2))$$

若每个 $f_i$ 都在 $x_0=(x_{0,1}, x_{0,2})$ 可微，则称 $f$ 在 $x_0$ 可微。

也称 $f$ 在 $x_0$ 可导，并称

$$df(x_0) = \begin{pmatrix} df_1(x_0) \\ \vdots \\ df_m(x_0) \end{pmatrix} = \begin{pmatrix} \frac{\partial f_1}{\partial x_1}(x_0)dx_1 + \frac{\partial f_1}{\partial x_2}(x_0)dx_2 \\ \vdots \\ \frac{\partial f_m}{\partial x_1}(x_0)dx_1 + \frac{\partial f_m}{\partial x_2}(x_0)dx_2 \end{pmatrix}$$

$$= \begin{pmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} \\ \vdots & \vdots \\ \frac{\partial f_m}{\partial x_1} & \frac{\partial f_m}{\partial x_2} \end{pmatrix}_{m\times 2} \begin{pmatrix} dx_1 \\ dx_2 \end{pmatrix}_{2\times 1}$$ 为 $f$ 在 $x_0$ 的微分。

称 $A = \begin{pmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} \\ \vdots & \vdots \\ \frac{\partial f_m}{\partial x_1} & \frac{\partial f_m}{\partial x_2} \end{pmatrix}_{x=x_0}$ 为 $f$ 在 $x_0$ 的导数（**Jacobi 矩阵**）。

$$df(x_0) = A \begin{pmatrix} dx_1 \\ dx_2 \end{pmatrix} = Df(x_0)\,dx$$

**定理 5.2.** $f: U(x_0) \subset \mathbb{R}^n \to \mathbb{R}^m$，$f$ 在 $x_0$ 可微的充分条件是每个 $\frac{\partial f_i}{\partial x_j}$ 在 $x_0$ 连续。

### §5.5.3 微分运算法则

#### 1. 链式法则

设 $(u,v) \xrightarrow{f} (x_1,x_2) \xrightarrow{g} (y_1,y_2)$，$f,g$ 都可微。

则 $g\circ f$ 也可微，且 $D(g\circ f) = Dg \cdot D(f)$。

$$\begin{pmatrix} \frac{\partial y_1}{\partial u} & \frac{\partial y_1}{\partial v} \\ \frac{\partial y_2}{\partial u} & \frac{\partial y_2}{\partial v} \end{pmatrix} = \begin{pmatrix} \frac{\partial y_1}{\partial x_1}\frac{\partial x_1}{\partial u} + \frac{\partial y_1}{\partial x_2}\frac{\partial x_2}{\partial u} & \frac{\partial y_1}{\partial x_1}\frac{\partial x_1}{\partial v} + \frac{\partial y_1}{\partial x_2}\frac{\partial x_2}{\partial v} \\ \frac{\partial y_2}{\partial x_1}\frac{\partial x_1}{\partial u} + \frac{\partial y_2}{\partial x_2}\frac{\partial x_2}{\partial u} & \frac{\partial y_2}{\partial x_1}\frac{\partial x_1}{\partial v} + \frac{\partial y_2}{\partial x_2}\frac{\partial x_2}{\partial v} \end{pmatrix} = \begin{pmatrix} \frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} \\ \frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2} \end{pmatrix} \begin{pmatrix} \frac{\partial x_1}{\partial u} & \frac{\partial x_1}{\partial v} \\ \frac{\partial x_2}{\partial u} & \frac{\partial x_2}{\partial v} \end{pmatrix}$$

(4) $f: \mathbb{R} \to \mathbb{R}^3$，$g: \mathbb{R} \to \mathbb{R}^3$ 都可微。

则向量积 $f\times g$ 可微，且 $D(f\times g) = Df \times g + f \times Dg$。

**Pf(4)：** 设 $f=(f_1,f_2,f_3)$，$g=(g_1,g_2,g_3)$，则 $f\times g = \begin{vmatrix} i & j & k \\ f_1 & f_2 & f_3 \\ g_1 & g_2 & g_3 \end{vmatrix} = \begin{vmatrix} f_2 & f_3 \\ g_2 & g_3 \end{vmatrix}i + \begin{vmatrix} f_3 & f_1 \\ g_3 & g_1 \end{vmatrix}j + \begin{vmatrix} f_1 & f_2 \\ g_1 & g_2 \end{vmatrix}k$。

$$D(f\times g) = D\begin{vmatrix} f_2 & f_3 \\ g_2 & g_3 \end{vmatrix}i + D\begin{vmatrix} f_3 & f_1 \\ g_3 & g_1 \end{vmatrix}j + D\begin{vmatrix} f_1 & f_2 \\ g_1 & g_2 \end{vmatrix}k$$

$$= D(f_2g_3 - f_3g_2)i + \square j + \square k$$

$$= (f_2'g_3 + f_2g_3' - f_3'g_2 - f_3g_2')i + \dots$$

$$= \begin{vmatrix} f_2' & f_3' \\ g_2 & g_3 \end{vmatrix}i + \begin{vmatrix} f_3' & f_1' \\ g_3 & g_1 \end{vmatrix}j + \begin{vmatrix} f_1' & f_2' \\ g_1 & g_2 \end{vmatrix}k + \begin{vmatrix} f_2 & f_3 \\ g_2' & g_3' \end{vmatrix}i + \begin{vmatrix} f_3 & f_1 \\ g_3' & g_1' \end{vmatrix}j + \begin{vmatrix} f_1 & f_2 \\ g_1' & g_2' \end{vmatrix}k$$

$$= D(f)\times g + f\times D(g)$$

---

## §5.5.4 由方程组确定隐函数组及其微分法

设方程组 $F(x,y,u,v)=0$，$G(x,y,u,v)=0$ 由它们确定两个定义在 $D \subset \mathbb{R}^2$ 上的函数 $u=u(x,y)$ 和 $v=v(x,y)$，称为由它们确定的**隐函数组**。

设 $F,G,u,v$ 都可微，对 $F,G$ 取微分得

$$\begin{cases} F_x dx + F_y dy + F_u du + F_v dv = 0 \\ G_x dx + G_y dy + G_u du + G_v dv = 0 \end{cases}$$

$$\begin{cases} F_u du + F_v dv = -F_x dx - F_y dy \\ G_u du + G_v dv = -G_x dx - G_y dy \end{cases}$$

为了解出 $du, dv$，需要 $\frac{\partial(F,G)}{\partial(u,v)} = \begin{vmatrix} F_u & F_v \\ G_u & G_v \end{vmatrix} \neq 0$。

称为 $F,G$ 关于 $u,v$ 的 **Jacobi 行列式**。

**定理 5.5**（隐函数组存在定理）

(i) 设 $F(x,y,u,v)$ 和 $G(x,y,u,v)$ 在区域 $V \subseteq \mathbb{R}^4$ 上连续，$P_0(x_0,y_0,u_0,v_0)$ 为 $V$ 的内点。

(ii) $F(P_0)=G(P_0)=0$。

(iii) $F,G$ 在 $V$ 内有连续的一阶偏导数。

(iv) 在 $P_0$ 处，$\frac{\partial(F,G)}{\partial(u,v)} \neq 0$。

则在 $P_0$ 的某个邻域内，方程组 $\begin{cases} F=0 \\ G=0 \end{cases}$ 唯一确定一个定义在 $Q_0(x_0,y_0)$ 的某邻域 $U(P_0)$ 内的隐函数组 $\begin{cases} u=u(x,y) \\ v=v(x,y) \end{cases}$。

s.t. 1° $u_0=f(x_0,y_0)$，$v_0=g(x_0,y_0)$ 且 $(x,y) \in U(Q_0)$ 时

$$\begin{cases} F(x,y,f(x,y),g(x,y)) \equiv 0 \\ G(x,y,f(x,y),g(x,y)) \equiv 0 \end{cases}$$

2° 在 $U(Q_0)$ 内，$u=f(x,y)$，$v=g(x,y)$ 有连续一阶偏导数，且 $du, dv$ 满足方程组

$$\begin{cases} F_u du + F_v dv = -F_x dx - F_y dy \\ G_u du + G_v dv = -G_x dx - G_y dy \end{cases}$$

**EX 1.** 讨论方程组 $\begin{cases} F(x,y,u,v) = u^2+v^2-x^2-y^2 = 0 \\ G(x,y,u,v) = -u+v-xy+1 = 0 \end{cases}$ 在 $P_0(1,1,1,1)$ 附近确定怎样的隐函数组并求一阶微分（求 $u,v$ 在点 $(1,1)$ 处的一阶微分）。

**解：** $F(P_0)=G(P_0)=0$；$F,G$ 在 $\mathbb{R}^4$ 内有一阶连续偏导数。

$$\begin{pmatrix} F_u & F_v & F_x & F_y \\ G_u & G_v & G_x & G_y \end{pmatrix}_{P_0} = \begin{pmatrix} 2u & 2v & -2x & -2y \\ -1 & 1 & -y & -x \end{pmatrix}_{P_0} = \begin{pmatrix} 2 & 2 & -2 & -2 \\ -1 & 1 & -1 & -1 \end{pmatrix}$$

因为 $\left.\frac{\partial(F,G)}{\partial(u,v)}\right|_{P_0} = 4$，所以可以确定 $u=u(x,y)$，$v=v(x,y)$。

对 $\begin{cases} F \\ G \end{cases}$ 取微分 $\begin{cases} 2u\,du + 2v\,dv = 2x\,dx + 2y\,dy \\ -du + dv = y\,dx + x\,dy \end{cases}$

$$\Rightarrow \begin{cases} du = \frac{(2x+2y)\,dx + (2x+2y)\,dy}{2(u+v)} \\ dv = \frac{(2x-2y)\,dx + (2y-2x)\,dy}{2(u+v)} \end{cases}$$

---

## §5.6 多元函数微分学在几何问题中的应用

### §5.6.1 空间曲线的切线与法平面

#### 1. 曲线的参数方程

平面曲线：$\begin{cases} x=x(t) \\ y=y(t) \end{cases}$，$\alpha \leq t \leq \beta$

空间曲线：$\begin{cases} x=x(t) \\ y=y(t) \\ z=z(t) \end{cases}$，$\alpha \leq t \leq \beta$

$\vec{r}(t) = (x(t), y(t), z(t))$。

#### 2. 简单曲线与有向曲线

若对任何 $t_1, t_2 \in (\alpha,\beta)$，$t_1 \neq t_2$，有 $r(t_1) \neq r(t_2)$，即 $r: (\alpha,\beta) \to \mathbb{R}^3$ 是单射，曲线不自交，则称之为**简单曲线**。

若还有 $r(\alpha)=r(\beta)$，则称之为**简单闭曲线**。

对已选定的参数 $t$ 的曲线 $\Gamma$，规定 $t$ 增加的方向为正向，规定了方向的曲线称为**有向（定向）曲线**。

例如 $xOy$ 平面内的圆周 $r(t)=(\cos t, \sin t, 0)$，$t$ 从 $0$ 到 $2\pi$ 是正向曲线。

#### 3. 空间曲线的切线与法平面（法平面 $\perp$ 切线）

**(1)** 设空间简单曲线 $\Gamma$ 的参数方程为 $r=r(t)=(x(t), y(t), z(t))$，$\alpha \leq t \leq \beta$。

其中 $r(t)$ 在 $[\alpha,\beta]$ 可导，其导数记为 $\dot{r}(t)=(\dot{x}(t), \dot{y}(t), \dot{z}(t))$ 且设 $\dot{r}(t) \neq 0$。

下面讨论 $\Gamma$ 在 $P_0(x(t_0), y(t_0), z(t_0))$ 处的切线。

取动点 $P=r(t_0+\Delta t)$ 有割线 $P_0P$。

当 $P \to P_0$ 时，割线 $P_0P$ 的极限定义为 $\Gamma$ 在 $P_0$ 的切线。

割线方向：$\vec{P_0P}$，$\Delta r = (\Delta x, \Delta y, \Delta z)$。

$$\Delta r = (\Delta x, \Delta y, \Delta z) = (x(t_0+\Delta t)-x(t_0), y(t_0+\Delta t)-y(t_0), z(t_0+\Delta t)-z(t_0))$$

$$\frac{\Delta r}{\Delta t} = \left(\frac{\Delta x}{\Delta t}, \frac{\Delta y}{\Delta t}, \frac{\Delta z}{\Delta t}\right)$$

当 $\Delta t \to 0$，$\lim_{\Delta t \to 0} \frac{\Delta r}{\Delta t} = \dot{r}(t_0) = (\dot{x}(t_0), \dot{y}(t_0), \dot{z}(t_0))$ —— **切方向（向量）**。

它指向参数 $t$ 增加的方向。

对 $r=(x,y,z)$，$dr=(dx,dy,dz)=(\dot{x}(t)dt, \dot{y}(t)dt, \dot{z}(t)dt) = \dot{r}(t)\,dt$。

说明 $(dx,dy,dz)$ 也是切方向，当 $dt>0$ 时指向 $t$ 增加的方向。

因此曲线 $\Gamma$ 在 $P_0$ 切线方程为

$$\frac{x-x_0}{\dot{x}(t_0)} = \frac{y-y_0}{\dot{y}(t_0)} = \frac{z-z_0}{\dot{z}(t_0)}$$

其中 $x_0=x(t_0), y_0=y(t_0), z_0=z(t_0)$。

**法平面**过点 $P_0$ 且垂直于切线，其方程为

$$\dot{x}(t_0)(x-x_0) + \dot{y}(t_0)(y-y_0) + \dot{z}(t_0)(z-z_0) = 0$$

**(2)** 曲线 $\Gamma$ 是两个曲面 $\begin{cases} F(x,y,z)=0 \\ G(x,y,z)=0 \end{cases}$ 的交线 （*）

设（*）在点 $P_0(x_0,y_0,z_0)$ 满足隐函数组定理的条件。

其中 $J(P_0) = \left.\frac{\partial(F,G)}{\partial(x,y)}\right|_{P_0} \neq 0$，则（*）在 $P_0$ 附近唯一确定隐函数组 $\begin{cases} x=x(z) \\ y=y(z) \end{cases}$。

且 $\begin{cases} F_x dx + F_y dy = -F_z dz \\ G_x dx + G_y dy = -G_z dz \end{cases}$，解出

$$\frac{dx}{dz} = \frac{1}{J}\begin{vmatrix} -F_z & F_y \\ -G_z & G_y \end{vmatrix} = \frac{1}{J}\frac{\partial(F,G)}{\partial(y,z)}$$

$$\frac{dy}{dz} = \frac{1}{J}\begin{vmatrix} F_x & -F_z \\ G_x & -G_z \end{vmatrix} = \frac{1}{J}\frac{\partial(F,G)}{\partial(z,x)}$$

曲线 $\Gamma$ 在 $P_0$ 附近有参数表示 $\vec{r}(z) = (x(z), y(z), z)$，$\vec{r}'(z) = (\dot{x}(z), \dot{y}(z), 1)$。

过点 $P_0$ 的切线的方程

$$\frac{x-x_0}{\frac{dx}{dz}(z_0)} = \frac{y-y_0}{\frac{dy}{dz}(z_0)} = \frac{z-z_0}{1}$$

即 $\frac{x-x_0}{A} = \frac{y-y_0}{B} = \frac{z-z_0}{C}$。

其中 $A = \left.\frac{\partial(F,G)}{\partial(y,z)}\right|_{P_0}$，$B = \left.\frac{\partial(F,G)}{\partial(z,x)}\right|_{P_0}$，$C = \left.\frac{\partial(F,G)}{\partial(x,y)}\right|_{P_0}$。

法平面方程 $A(x-x_0) + B(y-y_0) - C(z-z_0) = 0$。

**Another way：** 曲面 $S_1: F(x,y,z)=0$，曲面 $S_2: G(x,y,z)=0$。

$\Gamma = S_1 \cap S_2$。对上述两式取微分

$$\begin{cases} F_x dx + F_y dy + F_z dz = 0 = \nabla F \cdot dr \quad \therefore \nabla F \perp dr \\ G_x dx + G_y dy + G_z dz = 0 = \nabla G \cdot dr \quad \therefore \nabla G \perp dr \end{cases}$$

于是切向量 $dr \parallel \nabla F \times \nabla G = (A,B,C)$。

**例 6.2** 求曲线 $\begin{cases} 2x^2+y^2+z^2=45 \\ x^2+2y^2=z \end{cases}$ 在 $P_0(-2,1,6)$ 处的切线及法平面方程。

**解：** 因为 $\nabla F(P_0) = (4x, 2y, 2z)|_{P_0} = (-8, 2, 12)$。

$\nabla G(P_0) = (2x, 4y, -1)|_{P_0} = (-4, 4, -1)$。

切线方向 $dr \parallel \nabla F(P_0) \times \nabla G(P_0) = (-50, -56, -24)$。

切线方程 $\frac{x+2}{25} = \frac{y-1}{28} = \frac{z-6}{12}$。

法平面：$25(x+2) + 28(y-1) + 12(z-6) = 0$。

---

### §5.6.2 弧长

#### 1. 定义与计算

**定义 6.1**（弧长）设简单曲线 $\Gamma = \widehat{AB}$ 的参数方程为 $r(t)=(x(t), y(t), z(t))$，$\alpha \leq t \leq \beta$。

其中 $A=r(\alpha)$，$B=r(\beta)$。在 $\Gamma$ 上从 $A$ 到 $B$ 引入分点，折线长度为 $S_n = \sum_{i=1}^n \|P_{i-1}P_i\|$。

称 $T=\{P_i\}$ 为曲线 $\Gamma$ 的一个分割，$d=\max_{1\leq i\leq n} \|P_{i-1}P_i\|$ 称为细度。

若对任意分割，和式极限 $\lim_{d\to 0} S_n = \lim_{d\to 0} \sum_{i=1}^n \|P_{i-1}P_i\| = S$ 且与分割 $T$ 的选取无关，则称上述极限值 $S$ 为曲线 $\Gamma$ 的弧长，此时称 $\Gamma$ 是**可求长曲线**。

注：不可求长曲线例子（分形）。

**定理 6.1.** 设在 $[\alpha,\beta]$ 上 $r(t)$ 连续且 $\dot{r}(t) \neq 0$，则曲线 $\Gamma=r(t)$ 是可求长曲线。

且长度为 $S = \int_\alpha^\beta \|\dot{r}(t)\| dt = \int_\alpha^\beta \sqrt{(\dot{x}(t))^2 + (\dot{y}(t))^2 + (\dot{z}(t))^2}\,dt$。

**证：** 对 $1 \leq i \leq n$，设 $P_i=r(t_i)$。

$$\|P_{i-1}P_i\|^2 = (x(t_i)-x(t_{i-1}))^2 + (y(t_i)-y(t_{i-1}))^2 + (z(t_i)-z(t_{i-1}))^2$$

依条件，由 Lagrange 中值定理分别存在 $\xi_i, \eta_i, \zeta_i \in [t_{i-1}, t_i]$ s.t.

$$x(t_i)-x(t_{i-1}) = \dot{x}(\xi_i)\Delta t_i$$

$$y(t_i)-y(t_{i-1}) = \dot{y}(\eta_i)\Delta t_i$$

$$z(t_i)-z(t_{i-1}) = \dot{z}(\zeta_i)\Delta t_i$$

于是 $\|P_{i-1}P_i\| = \sqrt{\dot{x}^2(\xi_i) + \dot{y}^2(\eta_i) + \dot{z}^2(\zeta_i)}\,\Delta t_i$。

$$S_n = \sum_{i=1}^n \sqrt{\dot{x}^2(\xi_i) + \dot{y}^2(\eta_i) + \dot{z}^2(\zeta_i)}\,\Delta t_i$$

$$= \sum_{i=1}^n \|\dot{r}(\tau_i)\|\Delta t_i + \sigma, \quad \tau_i \in (t_{i-1}, t_i)$$

其中 $\sigma = \sum_{i=1}^n \left(\sqrt{\dot{x}^2(\xi_i) + \dot{y}^2(\eta_i) + \dot{z}^2(\zeta_i)} - \sqrt{\dot{x}^2(\tau_i) + \dot{y}^2(\tau_i) + \dot{z}^2(\tau_i)}\right)\Delta t_i$。

$$\leq \sum_{i=1}^n \sqrt{[\dot{x}(\xi_i)-\dot{x}(\tau_i)]^2 + [\dot{y}(\eta_i)-\dot{y}(\tau_i)]^2 + [\dot{z}(\zeta_i)-\dot{z}(\tau_i)]^2}\,\Delta t_i$$

下证 $\lim_{d\to 0} \sigma = 0$。

因为 $\dot{r}(t)$ 在 $[\alpha,\beta]$ 上连续，且 $\dot{r}(t) \neq 0$，所以存在常数 $m>0$，s.t. $\sqrt{\dot{x}^2(\xi_i)+\dot{y}^2(\eta_i)+\dot{z}^2(\zeta_i)^2} \geq m$，$\|P_{i-1}P_i\| \geq m\,\Delta t_i$。

令 $\Delta t = \max_{1\leq i\leq n} \Delta t_i$，则 $\Delta t \leq \frac{d}{m}$。当 $d \to 0$ 时，$\Delta t \to 0$。

依条件 $\dot{x}(t), \dot{y}(t), \dot{z}(t)$ 在 $[\alpha,\beta]$ 连续 $\to$ 一致连续。

对任何 $\varepsilon>0$，存在 $\delta>0$，当 $t, t' \in [\alpha,\beta]$ 且 $|t-t'|<\delta$ 时，

有 $|\dot{x}(t)-\dot{x}(t')|<\varepsilon$，$|\dot{y}(t)-\dot{y}(t')|<\varepsilon$，$|\dot{z}(t)-\dot{z}(t')|<\varepsilon$。

当 $d < m\delta$ 时，$\Delta t < \frac{d}{m} < \delta$，此时 $\xi_i, \eta_i, \zeta_i, \tau_i \in [t_{i-1}, t_i]$。

所以 $\sigma \leq \sum_{i=1}^n \sqrt{3\varepsilon^2}\,\Delta t_i = \sqrt{3}\varepsilon \sum_{i=1}^n \Delta t_i = \sqrt{3}\varepsilon(\beta-\alpha)$。

因此 $\lim_{d\to 0} S_n = \lim_{d\to 0} \sum_{i=1}^n \|\dot{r}(\tau_i)\|\Delta t_i + 0 = \int_\alpha^\beta \|\dot{r}(t)\|\,dt$。

#### 2. 弧微分与自然参数

因为 $dS = \sqrt{(dx)^2+(dy)^2+(dz)^2}$，所以用弧长 $S$ 为参数时

$$\frac{dr}{dS} = \left(\frac{dx}{dS}, \frac{dy}{dS}, \frac{dz}{dS}\right)$$

是单位切向量，设它与 $x$ 轴、$y$ 轴、$z$ 轴正方向的夹角分别为 $\alpha, \beta, \gamma$，则

$$\frac{dr}{dS} = (\cos\alpha, \cos\beta, \cos\gamma)$$

$$dx = \cos\alpha\,dS, \quad dy = \cos\beta\,dS, \quad dz = \cos\gamma\,dS$$

**例 6.5.** 求螺旋线 $\begin{cases} x = a\cos\theta \\ y = a\sin\theta \\ z = k\theta \end{cases}$ 一个螺距 $(0 \leq \theta \leq 2\pi)$ 之间的长度。

**解：** $\dot{r}(\theta) = (-a\sin\theta, a\cos\theta, k)$。

$\|\dot{r}(\theta)\| = \sqrt{a^2+k^2}$。

弧长 $S = \int_0^{2\pi} \|\dot{r}(\theta)\|\,d\theta = 2\pi\sqrt{a^2+k^2}$。

---

### §5.6.3 曲面的切平面和法线

#### 1. 曲面的参数方程

球面的参数方程：设 $P(x,y,z)$ 为球面上一点，在 $xOy$ 平面投影为 $M(x,y,0)$。

$$P(\|OP\|\sin\varphi\cos\theta, \|OP\|\sin\varphi\sin\theta, \|OP\|\cos\varphi), \quad \varphi \in [0,\pi], \theta \in [0,2\pi]$$

$\varphi$ 取长度是纬线，$\theta$ 取长度是经线。

一般地，曲面 $S$ 的参数方程 $r(u,v) = (x(u,v), y(u,v), z(u,v))$，$(u,v) \in \Delta$。

$r: \Delta \subset \mathbb{R}^2 \to \mathbb{R}^3$。

#### 2. 曲面上的曲线表示

在曲面 $S$ 上，考虑两类曲线：

① $v=v_0$，$u$ 变化，称为 $u$ 曲线。

② $u=u_0$，$v$ 变化，称为 $v$ 曲线。

它们的切向量分别为 $r_u = (x_u, y_u, z_u)$，$r_v = (x_v, y_v, z_v)$。

#### 3. 曲面的切平面与法线

设曲面 $S$ 的参数方程为 $r(u,v) = (x(u,v), y(u,v), z(u,v))$，$(u,v) \in \Delta$。

其中 $r(u,v)$ 在 $\Delta$ 上连续，在点 $(u_0,v_0) \in \Delta$ 可微。

过曲面 $S$ 上任一点 $r_0 = r(u_0,v_0)$ 的任一光滑曲线 $\Gamma$ 的参数方程为 $r = r(u(t), v(t))$，$t \in I$。

其中 $u(t_0)=u_0$，$v(t_0)=v_0$。在上式中对 $t$ 求导得

$$\dot{r}(t_0) = r_u(u_0,v_0)\dot{u}(t_0) + r_v(u_0,v_0)\dot{v}(t_0)$$

右端是切向量 $r_u(u_0,v_0)$ 与 $r_v(u_0,v_0)$ 的线性组合。

若 $r_u \times r_v|_{(u_0,v_0)} \neq 0$，说明 $r_u(u_0,v_0)$ 与 $r_v(u_0,v_0)$ 不共线。

从而可张成一个平面 $\Pi$，称之为曲面 $S$ 在正则点 $r_0$ 的**切平面**。

它的法向量为

$$r_u \times r_v = \begin{vmatrix} i & j & k \\ x_u & y_u & z_u \\ x_v & y_v & z_v \end{vmatrix} = (A, B, C)$$

其中 $A = \left.\frac{\partial(y,z)}{\partial(u,v)}\right|_{(u_0,v_0)}$，$B = \left.\frac{\partial(z,x)}{\partial(u,v)}\right|_{(u_0,v_0)}$，$C = \left.\frac{\partial(x,y)}{\partial(u,v)}\right|_{(u_0,v_0)}$。

切平面方程为 $A(x-x_0) + B(y-y_0) + C(z-z_0) = 0$。

法线方程

$$\frac{x-x_0}{A} = \frac{y-y_0}{B} = \frac{z-z_0}{C}$$

若 $r_u=(x_u,y_u,z_u)$，$r_v=(x_v,y_v,z_v)$ 在 $\Delta$ 内连续，称曲面**光滑**。

对曲面 $F(x,y,z)=0$，设在点 $P_0(x_0,y_0,z_0)$ 处满足隐函数定理的条件。

$F_z(P_0) \neq 0$，隐函数 $z=z(x,y)$，曲面 $S: r(x,y)=(x,y,z(x,y))$。

$r_x = (1, 0, z_x) = (1, 0, -\frac{F_x}{F_z})$，$r_y = (0, 1, z_y) = (0, 1, -\frac{F_y}{F_z})$。

$$r_x \times r_y = \begin{vmatrix} i & j & k \\ 1 & 0 & -\frac{F_x}{F_z} \\ 0 & 1 & -\frac{F_y}{F_z} \end{vmatrix} = \left(\frac{F_x}{F_z}, \frac{F_y}{F_z}, 1\right)$$

法向量 $\vec{n} = (F_x, F_y, F_z) = \nabla F$。

切平面方程 $F_x(P_0)(x-x_0) + F_y(P_0)(y-y_0) + F_z(P_0)(z-z_0) = 0$。

法线方程

$$\frac{x-x_0}{F_x(P_0)} = \frac{y-y_0}{F_y(P_0)} = \frac{z-z_0}{F_z(P_0)}$$

**例 6.8** 求曲面 $\begin{cases} x = u\cos v \\ y = u\sin v \\ z = av \end{cases}$ 在 $u=\sqrt{2}, v=\frac{\pi}{4}$ 处的切平面与法线方程。

**解：** $r = (u\cos v, u\sin v, av)$

$$r_u = (\cos v, \sin v, 0), \quad u=\sqrt{2}, \quad r_u = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0\right)$$

$$r_v = (-u\sin v, u\cos v, a), \quad v=\frac{\pi}{4}, \quad r_v = (-1, 1, a)$$

$$\therefore r_u \times r_v|_{(\sqrt{2}, \frac{\pi}{4})} = \begin{vmatrix} i & j & k \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\ -1 & 1 & a \end{vmatrix} = \left(\frac{a}{\sqrt{2}}, -\frac{a}{\sqrt{2}}, \sqrt{2}\right) \parallel (a, -a, 2)$$

取法向量 $n=(a, -a, 2)$。切平面 $a(x-1) - a(y-1) + 2(z-\frac{\pi}{4}a) = 0$。

$$ax - ay + 2z = \frac{\pi}{2}a$$

**EX 1** 环面的参数方程。考虑 $yOz$ 平面上的圆周 $C: (y-a)^2+z^2=b^2$。

其中 $a>b>0$。该曲面绕 $z$ 轴一周形成环面，求曲面方程。

**解：** ① 圆周 $C$ 的参数方程为 $y=a+b\cos u$，$z=b\sin u$，$u \in [0,2\pi]$。

$$\begin{cases} z = b\sin u \\ x = r\cos v = (a+b\cos u)\cos v \\ y = r\sin v = (a+b\cos u)\sin v \end{cases}$$

$0 \leq u \leq 2\pi$，$0 \leq v \leq 2\pi$。

**EX 2** **Mobius 带**：矩形一组对边反向粘合。

细杆的两种旋转的合成，绕自身中心和绕 $z$ 轴。

开始时细杆 $L$ 占据 $\{(a, 0, u) \mid |u| \leq l\}$。

细杆中点 $C$ 绕 $xOy$ 面上的圆周 $x^2+y^2=a^2$ 逆时针。

细杆绕 $C$ 自转 s.t. $L$ 与 $z$ 轴所在平面与 $xOy$ 面垂直。

且当 $C$ 转 $\theta$ 角时，细杆绕 $C$ 转 $\frac{\theta}{2}$ 角。

细杆端点 $z = u\cos\frac{\theta}{2}$，$|u| \leq l$。

$x = OP'\cos\theta = (a+u\sin\frac{\theta}{2})\cos\theta$，$\theta \in [0, 2\pi]$。

$y = OP'\sin\theta = (a+u\sin\frac{\theta}{2})\sin\theta$。

---

## §5.7 空间曲线的曲率与挠率

### §5.7.1 Frenet 标架

设曲线 $\Gamma$ 的自然参数方程为 $r=r(s)$。

一般参数方程为 $r=r(t)$。

求导：$\frac{dr}{ds}=r'$，$\frac{d^2r}{ds^2}=r''$。

$\frac{dr}{dt}=\dot{r}$，$\frac{d^2r}{dt^2}=\ddot{r}$。

#### 1. 切线与法平面

与曲线 $\Gamma: r=r(s)$ 正向一致的单位切向量 $T(s) = r'(s)$。

$dr=(dx,dy,dz)$，$ds^2 = dx^2+dy^2+dz^2 = \|dr\|^2$。

$\|dr/ds\|=1$，$\therefore r'(s)$ 是单位切向量。

于是 $\Gamma$ 在点 $r(s_0)$ 的切线方程为 $\rho - r(s_0) = \lambda r'(s_0)$。

法平面方程 $[\rho - r(s_0)] \cdot r'(s_0) = 0$。

#### 2. 主法线和次法线

因为 $\|r'(s)\|=1 = \langle r'(s), r'(s) \rangle$。

对 $s$ 求导 $0 = r''(s) \cdot r'(s) + r'(s) \cdot r''(s) = 2r'(s)\cdot r''(s)$。

$\Rightarrow r'(s) \perp r''(s)$，$r'(s) \times r''(s) \neq 0$。

称 $N(s_0) = \frac{r''(s_0)}{\|r''(s_0)\|}$ 为曲线 $\Gamma$ 在 $r'(s_0)$ 的**主法向量**。

对应法线为主法线。

记 $B(s_0) = T(s_0) \times N(s_0)$ 为曲线 $\Gamma$ 在 $r'(s_0)$ 的**次法向量**。

$B(s)$ 与 $N(s)$ 张成法平面。

#### 3. 密切平面

过曲线 $\Gamma$ 上的点 $r(s_0)$ 的平面有无穷多个，欲知 which 与 $\Gamma$ 最贴近。

当 $\Gamma$ 为空间曲线时，考虑 $r(s_0)$ 邻近点 $r(s_0+\Delta s)$。

到上述平面的距离，设 $\Sigma$ 是过 $r(s_0)$ 的平面，其单位法向量 $n$。则 $r(s_0+\Delta s)$ 到平面 $\Sigma$ 的距离

$$d = \lambda = n \cdot (r(s_0+\Delta s) - r(s_0))$$

由 Taylor 公式

$$r(s_0+\Delta s) - r(s_0) = r'(s_0)\Delta s + \frac{1}{2}r''(s_0)(\Delta s)^2 + o((\Delta s)^2)$$

于是 $d = n \cdot r'(s_0)\Delta s + n \cdot r''(s_0)\frac{(\Delta s)^2}{2} + o((\Delta s)^2)$。

① 若 $\Sigma$ 不含切线，则 $n \cdot r'(s_0) \neq 0$。
