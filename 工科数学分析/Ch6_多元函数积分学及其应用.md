# 第六章 多元函数积分学及其应用

## §6.1 多元积分的概念与性质

### 6.1.1 物体质量

设物体 $\Omega$ 的密度函数 $f$ 连续，求质量 $M$。

**分割**：将 $\Omega$ 分成 $n$ 个小部分 $\Omega_i\ (1\leq i\leq n)$，得分割 $T=\{\Omega_i\}$。

**近似**：任取 $P_i\in\Omega_i$，因 $f$ 在 $\Omega$ 连续，故当 $\Omega_i$ 的度量（直径）$\Delta\Omega_i$ 充分小时，$f(P)\approx f(P_i),\ P\in\Omega_i$。

$\Omega_i$ 的质量 $M_i\approx f(P_i)\Delta\Omega_i$

**求和**：$M=\sum M_i\approx\sum_{i=1}^n f(P_i)\Delta\Omega_i$

**取极限**：当 $||T||=\max_{1\leq i\leq n}\Omega_i$ 的直径 $\to 0$ 时

$$M=\lim_{||T||\to 0}\sum_{i=1}^n f(P_i)\Delta\Omega_i$$

### 6.1.2 多元积分的概念

若有界的几何体 $\Omega$ 可求长、面积、体积……则称它**可度量**。

**定理 A**：有界几何体 $\Omega$ 可度量 $\Longleftrightarrow\ \Omega$ 的边界的度量为 $0$。

| 几何体 | 边界 |
|--------|------|
| 线段 $[a,b]$ | $\{a,b\}$ |
| 平面图形 | 曲线 |
| 立体 | 曲面 |

**定义**：设 $\Omega$ 是有界几何体，它是可度量的，再设 $f$ 是 $\Omega$ 上的有界函数。任取 $\Omega$ 的分割 $T=\{\Omega_i\}$ 以及介点集 $\{P_i\}$，当分割细度 $||T||=\max_{1\leq i\leq n}\Omega_i$ 的直径 $\to 0$ 时，若极限

$$\lim_{||T||\to 0}\sum_{i=1}^n f(P_i)\Delta\Omega_i=J$$

存在，则称 $f$ 在 $\Omega$ 上**可积**，称 $J$ 为 $f$ 在 $\Omega$ 上的积分，记为 $J=\int_\Omega f(P)\,d\Omega$。

各类积分形式：

1. 若 $\Omega=[a,b]$ 且 $f$ 是 $\Omega$ 上的一元函数，则 $\int_\Omega f(P)\,d\Omega=\int_a^b f(x)\,dx$（**定积分**）。
2. 若 $\Omega$ 是平面有界闭域 $D$ 且 $f$ 是 $D$ 上的二元函数，则 $\int_\Omega f(P)\,d\Omega=\iint_D f(x,y)\,d\sigma$（**二重积分**）。
3. 若 $\Omega$ 是 $\mathbb{R}^3$ 中有界闭域（立体）且 $f$ 是 $\Omega$ 上的三元函数，则 $\int_\Omega f(P)\,d\Omega=\iiint_\Omega f(x,y,z)\,dV$（**三重积分**）。
4. 若 $\Omega$ 是有界可求长曲线 $\Gamma$ 且 $f$ 是 $\Gamma$ 上的二元函数或三元函数，则 $\int_\Omega f(P)\,d\Omega=\int_\Gamma f(x,y)\,ds$ 或 $\int_\Gamma f(x,y,z)\,ds$（**曲线积分**）。
5. 若 $\Omega$ 是曲面 $S$ 且 $f$ 是 $S$ 上的三元函数，则 $\int_\Omega f(P)\,d\Omega=\iint_S f(x,y,z)\,dS$（**曲面积分**）。

### 6.1.3 积分的存在条件和性质

**1. 存在条件**：设 $\Omega$ 是有界闭域且可度量，则下列函数在 $\Omega$ 上可积：
- (1) 连续函数；
- (2) 不连续点集度量为 $0$。

**2. 线性性质**：$\int_\Omega [k_1f(P)+k_2g(P)]\,d\Omega=k_1\int_\Omega f(P)\,d\Omega+k_2\int_\Omega g(P)\,d\Omega$。

**3. 区域可加性**：设 $\Omega=\Omega_1\cup\Omega_2$，且 $\Omega_1,\Omega_2$ 内部不相交，则
$$\int_\Omega f(P)\,d\Omega=\int_{\Omega_1}f(P)\,d\Omega+\int_{\Omega_2}f(P)\,d\Omega$$

**4. 积分不等式**：
- (1) 若 $f(P)\leq g(P),\ P\in\Omega$，则 $\int_\Omega f(P)\,d\Omega\leq\int_\Omega g(P)\,d\Omega$；
- (2) $\left|\int_\Omega f(P)\,d\Omega\right|\leq\int_\Omega |f(P)|\,d\Omega$；
- (3) 若 $m\leq f(P)\leq M,\ \forall P\in\Omega$，则 $m\Delta\Omega\leq\int_\Omega f(P)\,d\Omega\leq M\Delta\Omega$，其中 $\Delta\Omega$ 为 $\Omega$ 的度量。

**5. 中值定理**：设 $\Omega$ 为可度量的有界闭域，$f$ 在 $\Omega$ 连续，则存在 $\xi\in\Omega$ 使 $\int_\Omega f(P)\,d\Omega=f(\xi)\Delta\Omega$。

---

**$\Omega$ 可度量**：以平面情形为例，平面图形的面积。

设 $P$ 是平面有界图形，存在矩形 $R\supset P$，用平行于坐标轴的直线网将 $P$ 分割，此时 $T$ 的网眼——小闭矩形可分为三类：
- ① $\Delta_i$ 中全为 $P$ 内点；
- ② $\Delta_i$ 中全为 $P$ 外点；
- ③ $\Delta_i$ 中含 $P$ 的边界点。

**定义**：
- 内和 $s_P(T)$ = ①类小矩形面积之和。若不存在则定义 $s_P(T)=0$。
- 外和 $S_P(T)$ = ①③类小矩形面积之和。

则内和 $s_P(T)\leq$ 矩形 $R$ 的面积，外和 $S_P(T)\geq s_P(T)$。

**定义**：
- 内面积 $\underline{I}_P=\sup_T s_P(T)$
- 外面积 $\bar{I}_P=\inf_T S_P(T)$

若 $\underline{I}_P=\bar{I}_P=I_P$，则称 $P$ 可求面积，称 $I_P$ 为 $P$ 的面积。

**定理 $a_1$**：平面有界图形可求面积 $\Longleftrightarrow$ 对任何 $\varepsilon>0$，存在直线网 $T$ 使 $S_P(T)-s_P(T)<\varepsilon$。

**推论 1**：平面有界图形 $P$ 的面积为 $0$ $\Longleftrightarrow\ \bar{I}_P=0$，即 $\forall\varepsilon>0$，存在直线网 $T$，使 $S_P(T)<\varepsilon$，或存在有限个小矩形覆盖 $P$，面积之和 $<\varepsilon$。

**定理 $a_2$**：平面有界图形 $P$ 可求面积 $\Longleftrightarrow\ P$ 的边界面积为 $0$。

**定理 $a_3$**：若曲线 $K$ 是 $[a,b]$ 上的连续函数 $f(x)$ 图像，则 $K$ 的面积为 $0$。

**推论 2**：参数方程 $x=\varphi(t),\ y=\psi(t),\ \alpha\leq t\leq\beta$ 所表示的光滑曲线（$\varphi'(t),\psi'(t)$ 连续且 $\varphi'^2(t)+\psi'^2(t)\neq 0$），$K$ 的面积为 $0$。

**推论 3**：平面上分段光滑曲线围成的有界闭区域可求面积。

**注**：存在不可求面积的平面有界图形，例如
$$P=\{(x,y)\mid x,y\in[0,1]\cap\mathbb{Q}\}$$

事实上，对任何直线网 $T$，因 $P$ 中点都为边界点，故含 $P$ 中点的小矩形均为③类，从而 $s_P(T)=0,\ \underline{I}_P=0$。下面证明③类小矩形全体覆盖正方形 $[0,1]\times[0,1]$，于是外面积是 $1$。

记③类小矩形的并集为 $E$，因为小矩形是闭集，所以 $E$ 是闭集。对任何 $Q(x_0,y_0)\in D$，由实数可用有理数列逼近，存在 $[0,1]$ 中的有理数列 $\{x_n\},\{y_n\}$ 使 $x_n\to x_0,\ y_n\to y_0$，从而 $(x_n,y_n)\in P$ 且 $(x_n,y_n)\to(x_0,y_0)$，说明 $Q$ 是 $P$ 的聚点。又因 $P\subset E$，所以 $Q$ 是 $E$ 的聚点，又 $E$ 是闭集，$\therefore Q\in E$，$D\subset E$。

---

## §6.2 二重积分的计算

### 6.2.1 二重积分的几何意义

任取 $D$ 的分割 $T=\{\sigma_i\}$ 以及 $\{\xi_i,\eta_i\}\in\sigma_i$，则 $\sigma_i$ 对应的曲顶柱体体积 $\Delta V_i\approx f(\xi_i,\eta_i)\Delta\sigma_i$。

于是
$$\iint_D f(x,y)\,d\sigma=\lim_{||T||\to 0}\sum_{i=1}^n f(\xi_i,\eta_i)\Delta\sigma_i$$

### 6.2.2 直角坐标系下二重积分的计算

#### 一、矩形区域 $D=[a,b]\times[c,d]$

曲顶柱体与平面 $x=x_0$ 的截面是曲边梯形，面积 $A(x_0)=\int_c^d f(x_0,y)\,dy$。

曲顶柱体体积 $V=\int_a^b A(x)\,dx=\int_a^b dx\int_c^d f(x,y)\,dy$。

**定理 A**：设 $f(x,y)$ 在 $D=[a,b]\times[c,d]$ 上可积，且对每个 $x\in[a,b]$，积分 $\int_c^d f(x,y)\,dy$ 存在，则累次积分 $\int_a^b dx\int_c^d f(x,y)\,dy$ 存在且
$$\iint_D f(x,y)\,d\sigma=\int_a^b dx\int_c^d f(x,y)\,dy$$

**分析**：令 $F(x)=\int_c^d f(x,y)\,dy$，去证 $\iint_D f(x,y)\,d\sigma=\int_a^b F(x)\,dx$。

右边 $=\lim_{\Delta x\to 0}\sum_{i=1}^n F(\xi_i)\Delta x_i\quad(\Delta x=\max_{1\leq i\leq n}\Delta x_i)$

$$=\lim_{\Delta x\to 0}\sum_{i=1}^n\int_c^d f(\xi_i,y)\,dy\cdot\Delta x_i$$

$$=\lim_{\Delta x\to 0}\sum_{i=1}^n\sum_{k=1}^m\int_{y_{k-1}}^{y_k} f(\xi_i,y)\,dy\cdot\Delta x_i$$

其中 $m_{ik}\leq f(\xi_i,y)\leq M_{ik}$，$m_{ik}=\inf_{\Delta_{ik}}f,\quad M_{ik}=\sup_{\Delta_{ik}}f$。

$$\Delta_{ik}=[x_{i-1},x_i]\times[y_{k-1},y_k]$$

$T=\{\Delta_{ik}\},\quad ||T||=\max_{i,k}\Delta_{ik}$。

$$\sum_{i=1}^n\sum_{k=1}^m m_{ik}\Delta x_i\Delta y_k\leq\square\leq\sum_{i=1}^n\sum_{k=1}^m M_{ik}\Delta x_i\Delta y_k$$

当 $||T||\to 0$ 时，左、右 $\to\iint_D f(x,y)\,d\sigma$。

**定理 B**：若 $f(x,y)$ 在 $D=[a,b]\times[c,d]$ 上连续，则
$$\iint_D f(x,y)\,d\sigma=\int_a^b dx\int_c^d f(x,y)\,dy=\int_c^d dy\int_a^b f(x,y)\,dx$$

#### 二、一般区域

通常可分为：

**X 型区域**：对任何 $x_0\in(a,b)$，直线 $x=x_0$ 与区域边界的交点最多有 $2$ 个，则此时区域可表示为
$$D:\ a\leq x\leq b,\quad y_1(x)\leq y\leq y_2(x)$$

**Y 型区域**：对任何 $y_0\in(c,d)$，直线 $y=y_0$ 与区域边界的交点至多 $2$ 个，此时 $D:\ c\leq y\leq d,\quad x_1(y)\leq x\leq x_2(y)$。

**定理 C**：若 $f(x,y)$ 在 X 型区域 $D$ 上连续，其中 $D:\ a\leq x\leq b,\quad y_1(x)\leq y\leq y_2(x)$，$y_1(x),y_2(x)$ 在 $[a,b]$ 连续，则
$$\iint_D f(x,y)\,d\sigma=\int_a^b dx\int_{y_1(x)}^{y_2(x)} f(x,y)\,dy$$

**证明**：存在矩形 $R=[a,b]\times[c,d]\supset D$。令
$$F(x,y)=\begin{cases}f(x,y),&(x,y)\in D\\ 0,&(x,y)\in R\setminus D\end{cases}$$

因 $D$ 可求面积，故 $\partial D$ 面积为 $0$。因 $f$ 在 $D$ 上连续，故 $F$ 的不连续点集 $K\subset\partial D$，从而 $K$ 的面积是 $0$。因此 $F$ 在 $R$ 上可积。于是
$$\iint_D f(x,y)\,d\sigma=\iint_R F(x,y)\,d\sigma=\int_a^b dx\int_c^d F(x,y)\,dy=\int_a^b dx\int_{y_1(x)}^{y_2(x)} f(x,y)\,dy$$

#### 三、例题

**例 2.1**：$\iint_D\left(1-\frac{x}{3}-\frac{y}{4}\right)d\sigma$，其中 $D=[-1,1]\times[-2,2]$。

解：$I=\int_{-1}^1 dx\int_{-2}^2\left(1-\frac{x}{3}-\frac{y}{4}\right)dy=\int_{-1}^1 4\left(1-\frac{x}{3}\right)dx=8$。

**例 2.2**：$\iint_D (x^2+y^2)\,d\sigma$，$D$ 由 $y=0,\ x=1$ 及 $y=x^2$ 围成。

解：$I=\int_0^1 dx\int_0^{x^2}(x^2+y^2)\,dy=\int_0^1\left(x^4+\frac{1}{3}x^6\right)dx=\frac{1}{5}+\frac{1}{21}=\frac{26}{105}$。

**例 2.3**：$\iint_D xy\,d\sigma$，其中 $D$ 由 $y^2=x$ 与 $y=x-2$ 围成。

看作 Y 型区域，不分区。

$$I=\int_{-1}^2 dy\int_{y^2}^{y+2} xy\,dx=\int_{-1}^2 y\cdot\frac{1}{2}\left[(2+y)^2-y^4\right]dy=\frac{45}{8}$$

**例 2.4**：$\iint_D \frac{\sin x}{x}\,d\sigma$，其中 $D$ 由 $y=x$ 和 $y=x^2$ 围成。

$$I=\int_0^1 dx\int_{x^2}^x \frac{\sin x}{x}\,dy=\int_0^1\frac{\sin x}{x}(x-x^2)\,dx=\int_0^1(1-x)\sin x\,dx$$

---

### 分部积分的列表算法

$$\int u v^{(n+1)}\,dx=\int u\,dv^{(n)}=uv^{(n)}-\int u'v^{(n)}\,dx$$

递推展开可得列表法：

| 求导（$u$ 及其各阶导数） | 积分（$v^{(n+1)}$ 及其各阶积分） | 符号 |
|:---:|:---:|:---:|
| $u$ | $v^{(n+1)}$ | $+$ |
| $u'$ | $v^{(n)}$ | $-$ |
| $u''$ | $v^{(n-1)}$ | $+$ |
| $u'''$ | $v^{(n-2)}$ | $-$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $u^{(n)}$ | $v'$ | $(-1)^n$ |
| $u^{(n+1)}$ | $v$ | $(-1)^{n+1}$（再积分） |

对角线相乘，最后一行同列相乘再积分。

**e.g.** $\displaystyle\int x^4 e^x\,dx$：

列表：
- $x^4\ \to\ 4x^3\ \to\ 12x^2\ \to\ 24x\ \to\ 24\ \to\ 0$
- $e^x\ \to\ e^x\ \to\ e^x\ \to\ e^x\ \to\ e^x\ \to\ e^x$

原式 $=e^x(x^4-4x^3+12x^2-24x+24)+C$。

**e.g.** $\displaystyle\int x^3\sin x\,dx$：

列表：
- $x^3\ \to\ 3x^2\ \to\ 6x\ \to\ 6\ \to\ 0$
- $\sin x\ \to\ -\cos x\ \to\ -\sin x\ \to\ \cos x\ \to\ \sin x$

$=\cos x(-x^3+6x)+\sin x(3x^2-6)+C$。

**e.g.** $\displaystyle\int_0^1(1-x)\sin x\,dx$：

列表：
- $1-x\ \to\ -1\ \to\ 0$
- $\sin x\ \to\ -\cos x\ \to\ -\sin x$

$=\left[(1-x)(-\cos x)-\sin x\right]_0^1=1-\sin 1$。

---

**例**：$\iint_D\left(xy^3+x^3ye^{x^2+y^2}\right)d\sigma$，其中 $D$ 由 $y=x,\ y=-1,\ x=1$ 围成。

解：令 $D_1=\triangle OAB,\ D_2=\triangle OBC$。

$xy^3$ 在 $D_1$ 上关于 $x$ 是奇函数；$x^3y$ 在 $D_2$ 上关于 $y$ 是奇函数。

$$\iint_D xy^3e^{x^2+y^2}\,d\sigma=\iint_{D_1}+\iint_{D_2}=0$$

由对称性 $\displaystyle\iint_D x^2y^2\,d\sigma=2\iint_{D_2}x^2y^2\,d\sigma=\cdots=2\int_0^1 x^2\,dx\times\int_0^1 y^2\,dy=\frac{2}{9}$。

---

**例 2.** 交换累次积分的顺序

$$I=\int_{-2}^0 dy\int_0^{\frac{2+y}{2}}f(x,y)\,dx+\int_0^2 dy\int_0^{\frac{2-y}{2}}f(x,y)\,dy$$

解：$I=\iint_D f(x,y)\,d\sigma=\int_0^1 dx\int_{2x-2}^{2-2x}f(x,y)\,dy$。

---

### 6.2.3 极坐标系下二重积分的计算

$$\iint_D f(x,y)\,d\sigma=\lim_{||T||\to 0}\sum_{i=1}^n f(\xi_i,\eta_i)\Delta\sigma_i$$

使用 $r=\text{const},\ \theta=\text{const}$ 分割区域 $D$。

$$\Delta\sigma=\frac{1}{2}\left[(r+\Delta r)^2\Delta\theta-r^2\Delta\theta\right]=r\Delta r\Delta\theta+\frac{1}{2}(\Delta r)^2\Delta\theta$$

当 $|\Delta r|,|\Delta\theta|$ 充分小，$\Delta\sigma\approx r\Delta r\Delta\theta$。

于是
$$\iint_D f(x,y)\,d\sigma=\iint_\Delta f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$$

其中 $\Delta$ 是 $D$ 在 $r$-$\theta$ 平面内的对应区域。

#### 1. 原点在 $D$ 外

**$\theta$ 形区域**：$\theta=\theta_0$ 与 $D$ 的边界交点至多 $2$ 个，此时 $\Delta:\ \alpha\leq\theta\leq\beta,\ r_1(\theta)\leq r\leq r_2(\theta)$。

$$\iint_D f(x,y)\,d\sigma=\int_\alpha^\beta d\theta\int_{r_1(\theta)}^{r_2(\theta)}f(r\sin\theta,r\cos\theta)\,r\,dr$$

**$r$ 形区域**：$r=r_0$ 与 $D$ 的边界交点至多 $2$ 个，此时 $\Delta:\ r_1\leq r\leq r_2,\ \theta_1(r)\leq\theta\leq\theta_2(r)$。

$$\iint_D f(x,y)\,d\sigma=\int_{r_1}^{r_2}dr\int_{\theta_1(r)}^{\theta_2(r)}f(r\cos\theta,r\sin\theta)\,r\,d\theta$$

#### 2. 原点在 $D$ 内

此时 $\Delta:\ 0\leq\theta\leq 2\pi,\ 0\leq r\leq r(\theta)$，其中 $r=r(\theta)$ 是 $D$ 的边界曲线的极坐标方程。

$$\iint_D f(x,y)\,d\sigma=\int_0^{2\pi}d\theta\int_0^{r(\theta)}f(r\cos\theta,r\sin\theta)\,r\,dr$$

#### 3. 原点在 $D$ 边界上

此时 $\Delta:\ \alpha\leq\theta\leq\beta,\ 0\leq r\leq r(\theta)$。

$$\iint_D f(x,y)\,d\sigma=\int_\alpha^\beta d\theta\int_0^{r(\theta)}f(r\cos\theta,r\sin\theta)\,r\,dr$$

---

**例 2.7**：$\iint_D (x^2+y^2)\,d\sigma$，$D:\ a^2\leq x^2+y^2\leq b^2$。

解：$I=\iint_\Delta r^2\cdot r\,dr\,d\theta=\int_0^{2\pi}d\theta\int_a^b r^3\,dr=2\pi\cdot\frac{b^4-a^4}{4}$。

**例 2.8**：求由
$$\begin{cases}x^2+y^2+z^2\leq 4a^2\\x^2+y^2\leq 2ay\end{cases}$$
确定的立体的体积。

解：$V=4V_1=4\int_0^{\frac{\pi}{2}}d\theta\int_0^{2a\sin\theta}\sqrt{4a^2-r^2}\,r\,dr$

$$=2\int_0^{\frac{\pi}{2}}d\theta\int_0^{2a\sin\theta}\sqrt{4a^2-r^2}\,d(r^2)=\cdots=\frac{32a^3}{3}\left(\frac{\pi}{2}-\frac{2}{3}\right)$$

**例 2.9**：将累次积分 $I=\int_0^1 dx\int_{1-x}^{\sqrt{1-x^2}}f(x^2+y^2)\,dy$ 化为极坐标系的累次积分。

解：$D:\ 0\leq x\leq 1,\ 1-x\leq y\leq\sqrt{1-x^2}$。

$AB:\ x+y=1\xrightarrow[\substack{x=r\cos\theta\\y=r\sin\theta}}]{} r=\frac{1}{\sin\theta+\cos\theta}$

$\widehat{AB}:\ y=\sqrt{1-x^2}\longrightarrow r=1,\ 0\leq\theta\leq\frac{\pi}{2}$。

$$I=\int_0^{\frac{\pi}{2}}d\theta\int_{\frac{1}{\sin\theta+\cos\theta}}^1 f(r^2)\,r\,dr$$

---

**例 2.10**：$\iint_D e^{-(x^2+y^2)}\,d\sigma$，$D:\ x^2+y^2\leq R^2$。

解：$I=\int_0^{2\pi}d\theta\int_0^R e^{-r^2}r\,dr=\pi\left(1-e^{-R^2}\right)$。

**应用于 Gauss 积分**：$\displaystyle\int_0^{+\infty}e^{-x^2}\,dx=\frac{\sqrt{\pi}}{2}$。

$$I^2=\lim_{R\to+\infty}\left(\int_0^R e^{-x^2}dx\right)^2=\lim_{R\to+\infty}\int_0^R e^{-x^2}dx\int_0^R e^{-y^2}dy$$

$$=\lim_{R\to+\infty}\iint_{[0,R]^2}e^{-(x^2+y^2)}dx\,dy,\quad D=[0,R]\times[0,R]$$

利用圆进行放缩：令 $B_r=\{(x,y)\mid x^2+y^2\leq r^2,\ x,y\geq 0\}$。

则 $B_R\subset D\subset B_{\sqrt{2}R}$。

$$\frac{\pi}{4}\left(1-e^{-R^2}\right)=\iint_{B_R}e^{-(x^2+y^2)}dxdy\leq\square\leq\iint_{B_{\sqrt{2}R}}e^{-(x^2+y^2)}dxdy=\frac{\pi}{4}\left(1-e^{-2R^2}\right)\to\frac{\pi}{4}$$

$$\therefore\ \lim_{R\to\infty}\square=\frac{\pi}{4},\quad\therefore\ I=\frac{\sqrt{\pi}}{2}$$

**例 2.11**：$\iint_D x^2\,d\sigma$，$D:\ x^2+y^2=R^2$ 与 $y=-x$ 围成的右上半区域。

解：$I=\iint_D x^2\,d\sigma=\iint_D y^2\,d\sigma$（由对称性）。

$$I=\frac{1}{2}\iint_D(x^2+y^2)\,d\sigma=\frac{1}{2}\int_{-\frac{\pi}{4}}^{\frac{3\pi}{4}}d\theta\int_0^R r^3\,dr=\frac{\pi R^4}{8}$$

---

**EX**：
1. $\displaystyle\iint_D(\sin^2x+\cos^2y)\,d\sigma$，其中 $D=[0,1]\times[0,1]$。
   $$I=\iint_D(\sin^2y+\cos^2x)\,d\sigma=\frac{1}{2}\iint_D 2\,d\sigma=1$$
2. $\displaystyle\iint_D\left(\frac{x^2}{a^2}+\frac{y^2}{b^2}\right)d\sigma$，$a\neq b$，$D:\ x^2+y^2\leq 1$。

   依然关于 $x,y$ 对称：
   $$I=\iint_D\left(\frac{x^2}{a^2}+\frac{y^2}{b^2}\right)d\sigma=\iint_D\left(\frac{y^2}{a^2}+\frac{x^2}{b^2}\right)d\sigma$$
   $$=\frac{1}{2}\left(\frac{1}{a^2}+\frac{1}{b^2}\right)\iint_D(x^2+y^2)\,d\sigma=\frac{1}{2}\left(\frac{1}{a^2}+\frac{1}{b^2}\right)\int_0^{2\pi}d\theta\int_0^1 r^3\,dr=\frac{\pi}{4}\left(\frac{1}{a^2}+\frac{1}{b^2}\right)$$

---

### 6.2.4 曲线坐标下二重积分的计算

（= 二重积分的变量代换）

**例**：$\displaystyle\iint_D e^{\frac{x-y}{x+y}}dxdy$，令 $u=x-y,\ v=x+y$。

变换 $T:\ u=u(x,y),\ v=v(x,y)$，其中 $(x,y)\in D,\ (u,v)\in\Delta$。

若下列条件满足：
1. $u(x,y),v(x,y)\in C^1(\Delta)$（一阶偏导连续）；
2. Jacobi 行列式 $\displaystyle\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}u_x&u_y\\v_x&v_y\end{vmatrix}\neq 0,\ \forall(x,y)\in D$；
3. 变换 $T:\ D\to\Delta$ 是一对一的（$xOy$ 平面 $\to$ $uOv$ 平面）。

则称变换 $T$ 为**正则变换**。

**① 正则变换** $T:\ D\to\Delta$ 有唯一逆变换 $T^{-1}:\ \Delta\to D$。

由隐函数组定理，对每个点 $P\in\Delta$，方程组
$$\begin{cases}F(x,y,u,v)=u(x,y)-u=0\\G(x,y,u,v)=v(x,y)-v=0\end{cases}$$
唯一确定定义在邻域 $U(P)$ 上的函数组
$$\begin{cases}x=x(u,v)\\y=y(u,v)\end{cases}$$
从而唯一确定局部逆变换 $T^{-1}(u,v)=(x,y)$。由唯一性，对任何 $p,q\in\Delta$，在 $U(p)\cap U(q)$ 上，$(x,y)$ 相同，$\therefore$ 它们可拼成完整逆变换。

**② 逆变换** $T^{-1}$ 也是正则变换。

设 $T:\ u=f(x,y),\ v=g(x,y)$，则 $T^{-1}:\ x=\varphi(u,v),\ y=\psi(u,v)$。

则 $u=f(\varphi(u,v),\psi(u,v)),\ v=g(\varphi(u,v),\psi(u,v))$。

或写成 $T\circ T^{-1}(u,v)=(u,v),\ T\circ T^{-1}=id_\Delta$。

求导得 $\begin{pmatrix}u_x&u_y\\v_x&v_y\end{pmatrix}\begin{pmatrix}x_u&x_v\\y_u&y_v\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$。

于是 $\displaystyle\frac{\partial(u,v)}{\partial(x,y)}\cdot\frac{\partial(x,y)}{\partial(u,v)}=1$。

---

**EX2. 证明**：
1. 若 $f(x,y)$ 连续，则原像 $f^{-1}[a,b]=\{(x,y)\mid a<f(x,y)<b\}$ 是开集。
2. 设映射 $T:\ \Delta\to D,\ (u,v)\to(x,y)$ 连续。若 $V\subset D$ 是开集，则原像 $T^{-1}(V)=\{P\mid T(P)\in V\}$ 是开集。
3. 设 (2) 中的函数组 $x=x(u,v),\ y=y(u,v)\in C^1(\Delta)$ 且 $\displaystyle\frac{\partial(x,y)}{\partial(u,v)}\neq 0$，则 $T:\ \Delta\to D$ 将边界变成边界，内部变成内部。

**证明**：(1)(2) 依连续性、开集的定义。

函数 $f$ 连续 $\Longleftrightarrow\ \{x\mid f(x)>c\}$ 与 $\{x\mid f(x)<c\}$ 是开集。

(3) 当 $\displaystyle\frac{\partial(x,y)}{\partial(u,v)}\neq 0$ 时，由隐函数组定理，映射 $T:\ \Delta\to D$ 存在逆映射 $T^{-1}:\ D\to\Delta$，它们都连续且一对一。

若 $P\in\partial\Delta$ 为边界点，$q=T(P)\in D$ 是内点，则存在邻域 $U(q)\subset D$，于是 $U(P)=T^{-1}(U(q))$ 是开集，$P$ 为 $\Delta$ 的内点，矛盾。

若 $P\in\Delta$ 是内点，但 $q=T(P)\in\partial D$ 是边界点，则 $P\in T^{-1}(q)$ 且存在邻域 $U(P)\subset\Delta$，于是 $U(q)=T(U(P))=(T^{-1})^{-1}(U(P))$ 是开集，矛盾。

---

**逆变换** $T^{-1}:\ \Delta\to D$。

$uOv$ 平面内，直线 $v=v_0,\ v=v_0+\Delta v,\ u=u_0,\ u=u_0+\Delta u$。

映射到 $xOy$ 平面内，曲线 $r=r(u,v_0),\ r=r(u,v_0+\Delta v),\ r=r(u_0,v),\ r=r(u_0+\Delta u,v)$。

于是 $uOv$ 平面内矩形 $P_0P_1P_2P_3\xrightarrow{T^{-1}}$ $xOy$ 平面内曲边四边形 $Q_0Q_1Q_2Q_3$。

当 $|\Delta u|,|\Delta v|$ 充分小时：

$\Delta\sigma=S_{Q_0Q_1Q_2Q_3}\approx\|\overrightarrow{Q_0Q_1}\times\overrightarrow{Q_0Q_2}\|$

$\overrightarrow{Q_0Q_1}=r(u_0+\Delta u,v_0)-r(u_0,v_0)=r_u(u_0,v_0)\Delta u+o(\Delta u)$

$\overrightarrow{Q_0Q_2}=r(u_0,v_0+\Delta v)-r(u_0,v_0)=r_v(u_0,v_0)\Delta v+o(\Delta v)$

$\Delta\sigma\approx\|r_u(u_0,v_0)\Delta u\times r_v(u_0,v_0)\Delta v+o(\cdots)\|$

$\approx\|r_u(u_0,v_0)\times r_v(u_0,v_0)\|\cdot|\Delta u\cdot\Delta v|$

$$d\sigma=\|r_u\times r_v\|\,du\,dv$$

$$r_u\times r_v=\left(0,0,\frac{\partial(x,y)}{\partial(u,v)}\right)$$

$$d\sigma=\left|\frac{\partial(x,y)}{\partial(u,v)}\right|du\,dv$$

$$\iint_D f(x,y)\,d\sigma=\iint_\Delta f(x(u,v),y(u,v))\left|\frac{\partial(x,y)}{\partial(u,v)}\right|du\,dv$$

---

**例 2.12**：$\iint_D(y-x)\,d\sigma$，$D$ 由 $y=x+1,\ y=x-3,\ y=-\frac{1}{3}x+5,\ y=-\frac{1}{3}x+\frac{5}{3}$ 围成。

解：令 $u=y-x,\ v=y+\frac{1}{3}x$，则 $u\in[-3,1],\ v\in[\frac{5}{3},5]$。

$$\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}-1&1\\\frac{1}{3}&1\end{vmatrix}=-\frac{4}{3},\quad\frac{\partial(x,y)}{\partial(u,v)}=-\frac{3}{4}$$

$$I=\iint_\Delta u\cdot\frac{3}{4}\,du\,dv=\int_{-3}^1\frac{3}{4}u\,du\int_{\frac{5}{3}}^5 dv=-\frac{48}{5}$$

**EX3**：$\displaystyle\iint_D e^{\frac{x-y}{x+y}}d\sigma$，$D$ 由 $x=0,\ y=0$ 及 $x+y=1$ 围成。

解：$u=x-y,\ v=x+y$，则 $x=\frac{u+v}{2},\ y=\frac{v-u}{2}$。

$x=0\Rightarrow u+v=0$；$y=0\Rightarrow v=u$；$x+y=1\Rightarrow v=1$。

$$\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}1&-1\\1&1\end{vmatrix}=2,\quad\therefore\ \frac{\partial(x,y)}{\partial(u,v)}=\frac{1}{2}$$

$$I=\frac{1}{2}\iint_\Delta e^{\frac{u}{v}}du\,dv=\frac{1}{2}\int_0^1 dv\int_{-v}^v e^{\frac{u}{v}}du=\frac{e-e^{-1}}{4}$$

**例 13**：$\displaystyle\iint_D\sqrt{xy}\,d\sigma$，$D$ 由 $xy=1,\ xy=2,\ y=x,\ y=4x\ (x,y>0)$ 围成。

解：令 $u=xy,\ v=\frac{y}{x}$，则 $u\in[1,2],\ v\in[1,4]$。

$$\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}y&x\\-\frac{y}{x^2}&\frac{1}{x}\end{vmatrix}=\frac{2y}{x}=2v,\quad\frac{\partial(x,y)}{\partial(u,v)}=\frac{1}{2v}$$

$$I=\iint_\Delta\frac{\sqrt{u}}{2v}\,du\,dv=\int_1^4\frac{dv}{2v}\int_1^2\sqrt{u}\,du=\frac{(2\sqrt{2}-1)\ln 2}{3}$$

---

**注**：极坐标变换 $T:\ \square\to\mathbb{R}^2$。

$x=r\cos\theta,\ y=r\sin\theta,\ 0\leq r<+\infty,\ 0\leq\theta\leq 2\pi$。

从带状区域到全平面的满射。

$\displaystyle\frac{\partial(x,y)}{\partial(r,\theta)}=r$。变换 $T$ 在原点和正实轴上非一对一。

$$\iint_D f(x,y)\,d\sigma=\iint_\Delta f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$$

1. $xOy$ 平面上圆域 $D:\ x^2+y^2\leq R^2$，对应 $rO\theta$ 平面矩形区域 $\Delta=[0,R]\times[0,2\pi]$。

   在 $D$ 中剔除：
   - (a) 小圆盘 $x^2+y^2<\varepsilon^2$（原点邻域）；
   - (b) 圆心角为 $\varepsilon$ 的扇环 $ABB'A'$。

   余下部分为 $D_\varepsilon$。此时 $T:\ \Delta_\varepsilon\to D_\varepsilon$ 是一对一、正则，且在 $\Delta_\varepsilon$ 上 $\displaystyle\frac{\partial(x,y)}{\partial(r,\theta)}=r>0$。

   $$\iint_{D_\varepsilon}f(x,y)\,d\sigma=\iint_{\Delta_\varepsilon}f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$$

   由可加性，左右两边当 $\varepsilon\to 0^+$ 时趋于相同极限。

2. $D$ 为一般有界闭域，则存在充分大的 $R>0$ s.t. $D\subset B_R=\{(x,y)\mid x^2+y^2\leq R^2\}$。

   令
   $$F(x,y)=\begin{cases}f(x,y),&(x,y)\in D\\0,&(x,y)\in B_R\setminus D\end{cases}$$

   它在 $B_R\setminus D$ 上的不连续点集 $E\subset\partial D$，面积为 $0$。从而 $F$ 在 $B_R$ 可积。
   $$\iint_{B_R}F(x,y)\,dxdy=\iint_{\Delta}F(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$$
   $$=\iint_D f(x,y)\,dxdy=\iint_\Delta f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$$

**广义极坐标变换**：$x=ar\cos\theta,\ y=br\sin\theta$。

$$\frac{\partial(x,y)}{\partial(r,\theta)}=\begin{vmatrix}a\cos\theta&-ar\sin\theta\\b\sin\theta&br\cos\theta\end{vmatrix}=abr$$

$$\iint_D f(x,y)\,dxdy=\iint_\Delta f(ar\cos\theta,br\sin\theta)\,abr\,dr\,d\theta$$

**例 2.14**：$\iint_D x^2\,d\sigma$，$D:\ \frac{x^2}{4}+\frac{y^2}{9}\leq 1$。

解：$x=2r\cos\theta,\ y=3r\sin\theta,\ r\geq 0,\ 0\leq\theta\leq 2\pi$。

$$I=\iint_\Delta (2r\cos\theta)^2\cdot 6r\,dr\,d\theta=\int_0^{2\pi}\cos^2\theta\,d\theta\int_0^1 24r^3\,dr=6\pi$$

**EX4**：求椭球 $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}\leq 1$ 的体积。

解：令 $x=ar\cos\theta,\ y=br\sin\theta$，则 $r^2+\frac{z^2}{c^2}=1$，$z^2=c^2(1-r^2)$。

第一卦限 $V_1=c\iint_D\sqrt{1-r^2}\,d\sigma=c\int_0^{\frac{\pi}{2}}d\theta\int_0^1\sqrt{1-r^2}\,abr\,dr=\frac{\pi abc}{6}$。

$$V=8V_1=\frac{4}{3}\pi abc$$

---

## §6.3 三重积分

### 6.3.1 三重积分化为累次积分

#### 1. 截面法

已知平行截面质量求立体质量。

对每个 $z\in[p,q]$ 有截面 $D(z)$，则
$$\iiint_V f(x,y,z)\,dV=\int_p^q dz\iint_{D(z)}f(x,y,z)\,dxdy\quad\text{（先二后一）}$$

特别地，当 $f(x,y,z)=z$ 时，
$$\iiint_V z\,dV=\int_p^q zA(z)\,dz$$
其中 $A(z)$ 是截面 $D(z)$ 的面积。

#### 2. 投影法

将 $V$ 投影至 $xOy$ 平面得区域 $D$。

特征：$\forall (x,y)\in D,\ z_1(x,y)\leq z\leq z_2(x,y)$。

因此
$$\iiint_V f(x,y,z)\,dV=\iint_D dxdy\int_{z_1(x,y)}^{z_2(x,y)}f(x,y,z)\,dz\quad\text{（先一后二）}$$

---

**例 3.1**：$\iiint_V xyz\,dV$，其中 $V$ 由平面 $x=0,\ y=0,\ z=0,\ x+y+z=1$ 围成。

解：截面法。对 $z\in[0,1]$，截面 $D(z):\ x+y\leq 1-z,\ x,y\geq 0$。

于是
$$I=\int_0^1 z\,dz\iint_{D(z)}xy\,dxdy=\cdots=\frac{1}{720}$$

**例 3.2**：$\iiint_V z\,dV$，其中 $V:\ x^2+y^2+z^2\leq R^2,\ z\geq 0$。

解：将 $V$ 投影到 $xOy$ 平面得区域 $D:\ x^2+y^2\leq R^2$。

$$I=\iint_D dxdy\int_0^{\sqrt{R^2-x^2-y^2}}z\,dz=\iint_D\frac{1}{2}(R^2-x^2-y^2)\,dxdy$$

$$=\frac{1}{2}\int_0^{2\pi}d\theta\int_0^R(R^2-r^2)r\,dr=\frac{1}{4}\pi R^4$$

**例 3.3**：$\iiint_V z^2\,dV$，其中 $V:\ \frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}\leq 1$。

解：截面法。对每个 $z\in[-c,c]$，截面 $D(z):\ \frac{x^2}{a^2}+\frac{y^2}{b^2}\leq 1-\frac{z^2}{c^2}$。

$A(z)=\pi ab\left(1-\frac{z^2}{c^2}\right)$。

$$I=\int_{-c}^c z^2 A(z)\,dz=\int_{-c}^c z^2\pi ab\left(1-\frac{z^2}{c^2}\right)dz=\frac{4}{15}\pi abc^3$$

**例 3.4**：$\iiint_V(x+y+z)\,dV$，$x^2+y^2\leq z\leq\sqrt{2-x^2-y^2}$。

解：两个曲面交线在 $xOy$ 平面投影为圆周 $x^2+y^2=1$。

因为 $V$ 关于 $yOz$ 平面对称，$f=x$ 是奇函数，所以 $\iiint_V x\,dV=0$。类似地 $\iiint_V y\,dV=0$。

于是
$$I=\iiint_V z\,dV=\iint_D dxdy\int_{x^2+y^2}^{\sqrt{2-x^2-y^2}}z\,dz$$

$$=\iint_D\frac{1}{2}\left[2-x^2-y^2-(x^2+y^2)^2\right]dxdy$$

$$=\frac{1}{2}\int_0^{2\pi}d\theta\int_0^1(2-r^2-r^4)r\,dr=\frac{7\pi}{12}$$

---

### 6.3.2 柱坐标与球坐标下三重积分的计算

#### 1. 三重积分的变量代换

取正则变换 $u=u(x,y,z),\ v=v(x,y,z),\ w=w(x,y,z)$，$(x,y,z)\in V,\ (u,v,w)\in V'$。

在此变换下，点 $P_0(x_0,y_0,z_0)$ 可用三个曲面的交点确定：
$$\begin{cases}u(x,y,z)=u(x_0,y_0,z_0)=u_0\\v(x,y,z)=v(x_0,y_0,z_0)=v_0\\w(x,y,z)=w(x_0,y_0,z_0)=w_0\end{cases}$$

在 $Ouvw$ 空间中，用曲面族 $u=c_1,\ v=c_2,\ w=c_3$ 分割 $V'$，体积微元 $dV'=du\,dv\,dw$。

$$\mathbf{r}=(x(u,v,w),\ y(u,v,w),\ z(u,v,w))$$

$$\frac{\partial(x,y,z)}{\partial(u,v,w)}=\begin{vmatrix}x_u&x_v&x_w\\y_u&y_v&y_w\\z_u&z_v&z_w\end{vmatrix}$$

$$\iiint_V f(x,y,z)\,dV=\iiint_{V'}f(x(u,v,w),\cdots)\left|\frac{\partial(x,y,z)}{\partial(u,v,w)}\right|du\,dv\,dw$$

#### 2. 柱坐标

$V\xrightarrow{\text{投影}} D\xrightarrow{\text{极坐标}}\Delta$

取变换 $x=r\cos\theta,\ y=r\sin\theta,\ z=z$。

$0\leq r<+\infty,\ 0\leq\theta\leq 2\pi,\ -\infty<z<+\infty$。

$$\frac{\partial(x,y,z)}{\partial(r,\theta,z)}=\begin{vmatrix}\cos\theta&-r\sin\theta&0\\\sin\theta&r\cos\theta&0\\0&0&1\end{vmatrix}=r$$

当 $r>0,\ 0\leq\theta<2\pi$ 时为正则变换。

$$\iiint_V f(x,y,z)\,dV=\iiint_\Delta f(r\cos\theta,r\sin\theta,z)\,r\,dr\,d\theta\,dz$$

**例 3.5**：$\iiint_V z\,dV$，其中 $V$ 是曲面 $z=x^2+y^2$，圆柱面 $x^2+y^2=2y$ 与平面 $z=0$ 所围成区域（抛物面之外，$xOy$ 之上）。

解：$I=\iint_D dxdy\int_0^{x^2+y^2}z\,dz=\iint_D\frac{1}{2}(x^2+y^2)^2\,dxdy$

$$=\int_0^\pi d\theta\int_0^{2\sin\theta}\frac{1}{2}r^4\cdot r\,dr=\frac{1}{2}\int_0^\pi d\theta\frac{(2\sin\theta)^6}{6}$$

$$=\frac{32}{3}\int_0^\pi\sin^6\theta\,d\theta=\frac{32}{3}\cdot\frac{\pi}{2}\cdot\frac{5!!}{6!!}=\frac{5\pi}{3}$$

**例 3.6**：$\iiint_V(x^3y^2+z)\,dV$，$V$ 由 $z=x^2+y^2$ 和 $z=4$ 围成。

解：$V$ 关于 $yOz$ 平面对称，$x^3y^2$ 是 $x$ 的奇函数。

$$I=\iiint_V z\,dV=\iint_D dxdy\int_{x^2+y^2}^4 z\,dz$$

$$=\iint_\Delta\frac{1}{2}(16-r^4)r\,dr\,d\theta=\int_0^{2\pi}d\theta\int_0^2\left(8r-\frac{1}{2}r^5\right)dr=\frac{64\pi}{3}$$

**例 3.7**：$I=\iiint_V\sqrt{x^2+y^2}\,dV$，$V$ 是 $z=x^2+y^2$ 与 $z=4$ 围成。

解：$I=\int_0^{2\pi}d\theta\int_0^2 dr\int_{r^2}^4 r\cdot r\,dz=\frac{128\pi}{15}$。（别忘了 Jacobian 是 $r$）

---

#### 3. 球坐标

$x=r\sin\varphi\cos\theta,\ y=r\sin\varphi\sin\theta,\ z=r\cos\varphi$。

$$\frac{\partial(x,y,z)}{\partial(r,\varphi,\theta)}=\begin{vmatrix}\sin\varphi\cos\theta&r\cos\varphi\cos\theta&-r\sin\varphi\sin\theta\\\sin\varphi\sin\theta&r\cos\varphi\sin\theta&r\sin\varphi\cos\theta\\\cos\varphi&-r\sin\varphi&0\end{vmatrix}=r^2\sin\varphi$$

$\varphi\in[0,\pi],\ \theta\in[0,2\pi],\ r\in[0,+\infty)$。

$$\iiint_V f(x,y,z)\,dV=\iiint_{V'}f(r\sin\varphi\cos\theta,r\sin\varphi\sin\theta,r\cos\varphi)\,r^2\sin\varphi\,dr\,d\varphi\,d\theta$$

$$dV=r^2\sin\varphi\,dr\,d\varphi\,d\theta$$

**例 3.8**：$V:\ x^2+y^2+z^2=2az\ (a>0)$ 和锥面（以 $z$ 轴为对称轴，顶角 $2\alpha$）围成。

解：$V=\int_0^{2\pi}d\theta\int_0^\alpha d\varphi\int_0^{2a\cos\varphi}r^2\sin\varphi\,dr=\frac{4\pi a^3}{3}(1-\cos^4\alpha)$。

**例 3.9**：$I=\iiint_V z^2\,dV$，$V=\{(x,y,z)\mid r\leq R,\ x^2+y^2+(z-R)^2\leq R^2\}$。

解：
1. $I=\int_0^{2\pi}d\theta\int_0^{\frac{\sqrt{3}R}{2}}dr\int_{R-\sqrt{R^2-r^2}}^{\sqrt{R^2-r^2}}z^2\,dz=\frac{59}{480}\pi R^5$。
2. 球坐标分成两部分 $I_1+I_2$：
   $$I_1=\int_0^{2\pi}d\theta\int_0^{\frac{\pi}{3}}\cos^2\varphi\sin\varphi\,d\varphi\int_0^R r^4\,dr=\frac{2}{5}\pi R^5\cdot\frac{7}{24}$$
   $$I_2=\int_0^{2\pi}d\theta\int_{\frac{\pi}{3}}^{\frac{\pi}{2}}\cos^2\varphi\sin\varphi\,d\varphi\int_0^{2R\cos\varphi}r^4\,dr=\frac{2}{5}\pi R^5\cdot\frac{1}{96}$$
   $$I_1+I_2=\frac{59}{480}\pi R^5$$
3. 截面法：$I=\int_0^{\frac{R}{2}}z^2\,dz\iint_{D_1(z)}d\sigma+\int_{\frac{R}{2}}^R z^2\,dz\iint_{D_2(z)}d\sigma=\cdots=\frac{59}{480}\pi R^5$。

**例 3.10**：$\iiint_V(x+y+z)\cos^2(x+y+z)^2\,dV$（被积函数可能为 $(x+y+z)\cos[(x+y+z)^2]$），其中 $V:\ 0\leq x+y\leq 1,\ 0\leq x-z\leq 1,\ 0\leq x+y+z\leq 1$。

解：取 $u=x-y,\ v=x-z,\ w=x+y+z$，则

$$\frac{\partial(u,v,w)}{\partial(x,y,z)}=\begin{vmatrix}1&-1&0\\1&0&-1\\1&1&1\end{vmatrix}=3,\quad\frac{\partial(x,y,z)}{\partial(u,v,w)}=\frac{1}{3}$$

$$I=\iiint w\cos(w^2)\cdot\frac{1}{3}\,du\,dv\,dw=\frac{1}{3}\int_0^1 du\int_0^1 dv\int_0^1 w\cos(w^2)\,dw=\frac{1}{6}\sin 1$$

---

## §6.4 含参变量积分（与反常重积分）

曲顶柱体体积，以曲面 $z=f(x,y)$ 为顶。

1. **底为矩形区域** $R=[a,b]\times[c,d]$，截面面积 $A(x)=\int_c^d f(x,y)\,dy$，体积 $V=\int_a^b A(x)\,dx=\int_a^b dx\int_c^d f(x,y)\,dy$。
2. **底为有界闭域** $G$，截面面积 $A(x)=\int_{c(x)}^{d(x)}f(x,y)\,dy$，体积 $V=\int_a^b A(x)\,dx=\int_a^b dx\int_{c(x)}^{d(x)}f(x,y)\,dy$。

   令 $y=c(x)+t(d(x)-c(x))=\xi(x,t)$，则
   $$A(x)=\int_0^1 f(x,\xi(x,t))(d(x)-c(x))\,dt=\int_0^1 g(x,t)\,dt$$

---

### 一、含参变量的正常积分

设 $f(x,y)$ 定义在矩形区域 $R=[a,b]\times[c,d]$。

若对每个 $x\in[a,b]$，函数 $\varphi(y)=f(x,y)$ 在 $[c,d]$ 上可积，则定义函数
$$I(x)=\int_c^d f(x,y)\,dy\quad (*)$$

设 $f(x,y)$ 定义在区域 $G$ 上，其中 $G:\ a\leq x\leq b,\ c(x)\leq y\leq d(x)$。

$c(x),d(x)$ 在 $[a,b]$ 连续，若对每个 $x\in[a,b]$，函数 $\varphi(y)=f(x,y)$ 在 $[c(x),d(x)]$ 可积，定义函数
$$F(x)=\int_{c(x)}^{d(x)}f(x,y)\,dy\quad (**)$$

函数 $(*)$ 与 $(**)$ 称为定义在 $[a,b]$ 上的**含参变量的积分**。

**定理 4.1（连续性）**：若 $f(x,y)$ 在矩形区域 $[a,b]\times[c,d]$ 上连续，则函数 $I(x)=\int_c^d f(x,y)\,dy$ 在 $[a,b]$ 上连续，$J(y)=\int_a^b f(x,y)\,dx$ 在 $[c,d]$ 上连续。

$$\lim_{x\to x_0}I(x)=I(x_0)=\int_c^d f(x_0,y)\,dy=\int_c^d\lim_{x\to x_0}f(x,y)\,dy$$

**证**：设 $x,x+\Delta x\in[a,b]$，则
$$I(x+\Delta x)-I(x)=\int_c^d[f(x+\Delta x,y)-f(x,y)]\,dy$$

依条件 $f(x,y)$ 在 $[a,b]\times[c,d]$ 上一致连续，对任何 $\varepsilon>0$，存在 $\delta>0$，使 $(x_1,y_1),(x_2,y_2)\in[a,b]\times[c,d]$ 且 $|x_1-x_2|<\delta,\ |y_1-y_2|<\delta$ 时，有 $|f(x_1,y_1)-f(x_2,y_2)|<\varepsilon$。

于是当 $|\Delta x|<\delta$ 时，
$$|I(x+\Delta x)-I(x)|\leq\int_c^d|f(x+\Delta x,y)-f(x,y)|\,dy\leq\varepsilon(d-c)$$

**定理 4.4**：设 $f(x,y)$ 定义在区域 $G$ 上，连续，其中 $G:\ [a,b]\times[c(x),d(x)]$，$c(x),d(x)$ 在 $[a,b]$ 连续，则 $F(x)=\int_{c(x)}^{d(x)}f(x,y)\,dy$ 在 $[a,b]$ 也连续。

**证明**：令 $y=c(x)+t(d(x)-c(x))$，则 $dy=(d(x)-c(x))dt$。
$$F(x)=\int_0^1 f(x,\xi(x,t))(d(x)-c(x))\,dt=\int_0^1 g(x,t)\,dt$$
因为 $f(x,y)$ 在 $G$ 上连续，所以 $g(x,t)$ 在 $[a,b]\times[0,1]$ 上连续，因此由连续性定理 $F(x)$ 在 $[a,b]$ 上连续。

---

**EX1**：$\displaystyle\lim_{\alpha\to 0}\int_\alpha^{1+\alpha}\frac{dx}{1+x^2+\alpha^2}$

**解**：因为 $\alpha,1+\alpha$ 在 $\mathbb{R}$ 上连续，$\frac{1}{1+x^2+\alpha^2}$ 在 $\mathbb{R}$ 上连续，由连续性定理 $I(\alpha)=\int_\alpha^{1+\alpha}\frac{dx}{1+x^2+\alpha^2}$ 在 $\mathbb{R}$ 上连续，从而在 $\alpha=0$ 连续，因此
$$\text{原式}=\int_0^1\frac{dx}{1+x^2}=\arctan x\Big|_0^1=\frac{\pi}{4}$$

**方法二**：$I(\alpha)=\frac{1}{\sqrt{1+\alpha^2}}\arctan\frac{x}{\sqrt{1+\alpha^2}}\Big|_\alpha^{1+\alpha}=\frac{\theta_1-\theta_2}{\sqrt{1+\alpha^2}}$

其中 $\theta_1=\arctan\frac{1+\alpha}{\sqrt{1+\alpha^2}},\ \theta_2=\arctan\frac{\alpha}{\sqrt{1+\alpha^2}}$。

$$\lim_{\alpha\to 0}I(\alpha)=\lim_{\alpha\to 0}\frac{\theta_1-\theta_2}{\sqrt{1+\alpha^2}}=\frac{\pi}{4}$$

---

**定理 4.2（可微性）**：设 $f(x,y),\ f_x(x,y)$ 在矩形区域 $R=[a,b]\times[c,d]$ 上连续，则 $I(x)=\int_c^d f(x,y)\,dy$ 在 $[a,b]$ 上可微，且
$$\frac{d}{dx}\int_c^d f(x,y)\,dy=\int_c^d f_x(x,y)\,dy$$

**证**：设 $x,x+\Delta x\in[a,b]$，则
$$\frac{I(x+\Delta x)-I(x)}{\Delta x}=\int_c^d\frac{f(x+\Delta x,y)-f(x,y)}{\Delta x}\,dy=\int_c^d f_x(x+\theta\Delta x,y)\,dy\quad(\theta\in[0,1])$$

因 $f_x$ 连续，由连续性定理，$\displaystyle\lim_{\Delta x\to 0}\frac{I(x+\Delta x)-I(x)}{\Delta x}=\int_c^d f_x(x,y)\,dy$。

---

**定理 4.2（可微性——变限情形）**：设 $f(x,y),\ f_x(x,y)$ 在矩形区域 $R=[a,b]\times[p,q]$ 上连续，$c(x),d(x)$ 为定义在 $[a,b]$ 上，值域 $\subset[p,q]$ 的可微函数，则
$$F(x)=\int_{c(x)}^{d(x)}f(x,y)\,dy$$
在 $[a,b]$ 可微，且
$$F'(x)=\int_{c(x)}^{d(x)}f_x(x,y)\,dy+f(x,d(x))d'(x)-f(x,c(x))c'(x)$$

**证明**：$F(x)$ 是复合函数，它由 $H(x,c,d)=\int_c^d f(x,y)\,dy$，$c=c(x),\ d=d(x)$ 合成。于是
$$F'(x)=\frac{\partial H}{\partial x}+\frac{\partial H}{\partial c}\frac{dc}{dx}+\frac{\partial H}{\partial d}\frac{dd}{dx}=\int_c^d f_x(x,y)\,dy-f(x,c(x))c'(x)+f(x,d(x))d'(x)$$

---

**EX2**：$\displaystyle\int_0^1\frac{\ln(1+x)}{1+x^2}\,dx=?$

**解**：令 $\varphi(\alpha)=\int_0^1\frac{\ln(1+\alpha x)}{1+x^2}\,dx$，则 $\varphi(0)=0,\ \varphi(1)=I$。

且 $\varphi(\alpha)$ 在矩形区域 $[0,1]\times[0,1]$ 上满足可微性定理的条件。

于是
$$\varphi'(\alpha)=\int_0^1\frac{x}{(1+\alpha x)(1+x^2)}\,dx$$

$$=\int_0^1\frac{1}{1+\alpha^2}\left(\frac{\alpha}{1+x^2}+\frac{x}{1+x^2}-\frac{\alpha}{1+\alpha x}\right)dx$$

$$=\frac{1}{1+\alpha^2}\left(\alpha\cdot\frac{\pi}{4}+\frac{1}{2}\ln 2-\ln(1+\alpha)\right)$$

因此
$$I=\varphi(1)-\varphi(0)=\int_0^1\varphi'(\alpha)\,d\alpha=\frac{\pi}{8}\ln(1+\alpha^2)\Big|_0^1+\frac{\ln 2}{2}\arctan\alpha\Big|_0^1-J$$

$2J=\frac{\pi}{4}\ln 2$，$\displaystyle I=\frac{\pi}{8}\ln 2$。

---

$$I(x)=\int_c^d f(x,y)\,dy,\quad J(y)=\int_a^b f(x,y)\,dx$$

分别在 $[a,b],\ [c,d]$ 积分，得：
$$\int_a^b dx\int_c^d f(x,y)\,dy=\int_c^d dy\int_a^b f(x,y)\,dx$$

同一个曲顶柱体体积。

**定理 4.3（积分次序交换）**：若二元函数 $f(x,y)$ 在 $R=[a,b]\times[c,d]$ 上连续，则
$$\int_a^b dx\int_c^d f(x,y)\,dy=\int_c^d dy\int_a^b f(x,y)\,dx$$

**证明**：任取 $u\in[a,b]$，令 $I_1(u)=\int_a^u dx\int_c^d f(x,y)\,dy,\ I_2(u)=\int_c^d dy\int_a^u f(x,y)\,dx$。

$I_1(a)=I_2(a)=0$，下面证 $I_1'(u)=I_2'(u)$。

$I_1'(u)=\int_c^d f(u,y)\,dy$。

记 $\int_a^u f(x,y)\,dx=H(u,y)$，则 $I_2(u)=\int_c^d H(u,y)\,dy$。

依条件 $H(u,y)$ 与 $H_u(u,y)=f(u,y)$ 在 $R$ 上连续。

其中 $H(u,u)$ 连续是因为
$$H(u+\Delta u,y+\Delta y)-H(u,y)=\int_u^{u+\Delta u}f(x,y+\Delta y)\,dx-\int_a^u f(x,y)\,dx$$

$$=\int_a^{u+\Delta u}(f(x,y+\Delta y)-f(x,y))\,dx+\int_u^{u+\Delta u}f(x,y)\,dx$$

$|\square|\leq\varepsilon(b-a)+M|\Delta u|\to 0$。

由可微性定理
$$I_2'(u)=\int_c^d H_u(u,y)\,dy=\int_c^d f(u,y)\,dy=I_1'(u)$$

---

**例 4.2**：求 $I=\displaystyle\int_0^1\frac{x^b-x^a}{\ln x}\,dx\ (b>a>0)$。

**解**：$x^b-x^a=\int_a^b\frac{d(x^y)}{dy}\,dy=\int_a^b x^y\ln x\,dy$。

$$\frac{x^b-x^a}{\ln x}=\int_a^b x^y\,dy$$

$I=\int_0^1 dx\int_a^b x^y\,dy$，又 $x^y$ 在 $[0,1]\times[a,b]$ 上连续。

由积分次序交换：
$$I=\int_a^b dy\int_0^1 x^y\,dx=\ln\frac{b+1}{a+1}$$

---

### 二、含参变量的反常积分——欧拉积分

#### 1. Beta 函数

$$B(p,q)=\int_0^1 x^{p-1}(1-x)^{q-1}\,dx\quad\text{（第一类 Euler 积分）}$$

**定义域**：$B(p,q)=\int_0^{\frac{1}{2}}+\int_{\frac{1}{2}}^1 x^{p-1}(1-x)^{q-1}\,dx$。

当 $x\to 0^+$ 时，$x^{p-1}(1-x)^{q-1}\sim x^{p-1}$，当 $p>0$ 时，$I_1$ 收敛。

$x\to 1^-$ 时，$x^{p-1}(1-x)^{q-1}\sim(1-x)^{q-1}$，当 $q>0$ 时，$I_2$ 收敛。

因此 $B(p,q)$ 定义域为 $(0,+\infty)\times(0,+\infty)$。

**1. 连续性**：$B(p,q)$ 在 $(0,+\infty)\times(0,+\infty)$ 上连续。

**2. 对称性**：$B(p,q)=B(q,p),\ p,q>0$。

$$B(p,q)\xlongequal{1-x=t}\int_0^1(1-t)^{p-1}t^{q-1}\,dt=\int_0^1 t^{q-1}(1-t)^{p-1}\,dt=B(q,p)$$

**3. 递推公式**：
$$B(p,q)=\int_0^1(1-x)^{q-1}\frac{1}{p}\,d(x^p)\quad(q>1)$$

$$=(1-x)^{q-1}\frac{x^p}{p}\Big|_0^1-\int_0^1(q-1)(1-x)^{q-2}(-1)\frac{x^p}{p}\,dx$$

$$=\frac{q-1}{p}\int_0^1 x^p(1-x)^{q-2}\,dx$$

$$x^p(1-x)^{q-2}=x^{p-1}[1-(1-x)](1-x)^{q-2}=x^{p-1}(1-x)^{q-2}-x^{p-1}(1-x)^{q-1}$$

$$\therefore\ B(p,q)=\frac{q-1}{p}B(p,q-1)-\frac{q-1}{p}B(p,q)$$

$$\therefore\ B(p,q)=\frac{q-1}{p+q-1}B(p,q-1)\quad(p>0,q>1)$$

$$=\frac{(p-1)(q-1)}{(p+q-1)(p+q-2)}B(p-1,q-1)\quad(p,q>1)$$

**4. 其他表示**：

(1) 令 $x=\cos^2\varphi$，得 $dx=2\cos\varphi(-\sin\varphi)\,d\varphi$。
$$B(p,q)=2\int_0^{\frac{\pi}{2}}(\cos\varphi)^{2p-1}(\sin\varphi)^{2q-1}\,d\varphi$$

(2) 令 $x=\frac{1}{1+t}$，得
$$B(p,q)=\int_0^{+\infty}\frac{t^{q-1}}{(1+t)^{p+q}}\,dt=\left(\int_0^1+\int_1^{+\infty}\right)\frac{t^{q-1}}{(1+t)^{p+q}}\,dt$$

对第二个积分令 $t=\frac{1}{u}$，得 $\int_1^{+\infty}\frac{t^{q-1}}{(1+t)^{p+q}}\,dt=\int_0^1\frac{u^{p-1}}{(1+u)^{p+q}}\,du$。

于是
$$B(p,q)=\int_0^1\frac{x^{p-1}+x^{q-1}}{(1+x)^{p+q}}\,dx$$
