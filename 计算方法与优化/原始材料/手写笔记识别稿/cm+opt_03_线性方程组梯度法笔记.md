# 线性方程组与梯度法（最速下降法 SD 与共轭梯度法 CG）笔记

> 来源：手写笔记 `cm+opt_线性方程祖梯度法.pdf`（共 9 页）。
> 本笔记逐页忠实转录原文内容与批注，公式保持原样；（红）/（蓝）标注原文颜色批注。

---

## 第 1 页

### 2.3 梯度法

### 1. 等价变分问题

**（蓝）** $kx = b$ 弹簧受力问题，弹性能 $\tfrac{1}{2}kx^2$，外力做功 $-b\cdot x$。

**（蓝）** 力平衡方程：$kx = b$；能量最小化方程：$\dfrac{dE}{dx} = 0$

$$
\Longleftrightarrow\quad
E = \tfrac{1}{2}kx^2 - b\cdot x
\ \longrightarrow\ \frac{dE}{dx} = 0
\ \longrightarrow\ kx - b = 0
\quad (\min E)
$$

设 $A\in\mathbb{R}^{n\times n}$，$A$ 正定，向量 $\vec{b} = (b_1, b_2, \cdots, b_n)^{\mathsf T}$，$\vec{x} = (x_1, x_2, \cdots, x_n)^{\mathsf T}$。

则对方程组 $A\vec{x} = \vec{b}$，考虑二次函数

$$
\varphi(\vec{x}) = \tfrac{1}{2}\vec{x}^{\mathsf T} A\vec{x} - \vec{b}^{\mathsf T}\vec{x}
= \tfrac{1}{2}\sum_{ij} a_{ij}x_ix_j - \sum_i b_ix_i .
$$

此时 $\varphi(\vec{x})$ 有以下性质：

**(1)** $\forall\,\vec{x}\in\mathbb{R}^n$，$\varphi(\vec{x})$ 的梯度

$$
\nabla\varphi(\vec{x}) = A\vec{x} - \vec{b}.
$$

**(2)** $\forall\,\vec{x},\vec{\eta}\in\mathbb{R}^n,\ \alpha\in\mathbb{R}$，

$$
\varphi(\vec{x}+\alpha\vec{\eta})
= \varphi(\vec{x}) + \alpha\,(A\vec{x} - \vec{b})^{\mathsf T}\vec{\eta}
+ \tfrac{1}{2}\,\vec{\eta}^{\mathsf T} A\vec{\eta}\cdot\alpha^2 .
$$

**证明 (1)**：

$$
\nabla\varphi(\vec{x}) = \Big(\frac{\partial\varphi}{\partial x_1},\ \frac{\partial\varphi}{\partial x_2},\ \cdots,\ \frac{\partial\varphi}{\partial x_n}\Big)^{\mathsf T}
$$

$$
\frac{\partial\varphi}{\partial x_k}
= \frac{\partial}{\partial x_k}\Big(\tfrac{1}{2}\textstyle\sum_{ij} a_{ij}x_ix_j - \sum_i b_ix_i\Big)
= \tfrac{1}{2}\frac{\partial}{\partial x_k}\Big(\sum_{ij}a_{ij}x_ix_j\Big) - \frac{\partial}{\partial x_k}\Big(\sum_i b_ix_i\Big)
$$

$$
= \tfrac{1}{2}\sum_{ij} a_{ij}\,\frac{\partial}{\partial x_k}(x_ix_j) - \sum_i b_i\,\frac{\partial x_i}{\partial x_k}
$$

$$
= \tfrac{1}{2}\sum_{ij} a_{ij}\big(x_j\delta_{ik} + x_i\delta_{jk}\big) - \sum_j b_j\delta_{jk}
$$

$$
= \tfrac{1}{2}\sum_j a_{kj}x_j + \tfrac{1}{2}\sum_i a_{ik}x_i - b_k
$$

$$
= \sum_j a_{kj}x_j - b_k = (A\vec{x} - \vec{b})_k
\ \Longrightarrow\ \nabla\varphi(\vec{x}) = A\vec{x} - \vec{b}.
$$

**（红）☆** 如 $g(x_1, x_2) = x_1$：$\dfrac{\partial g}{\partial x_1} = 1$，$\dfrac{\partial g}{\partial x_2} = 0$ $\Longrightarrow$ $\dfrac{\partial x_i}{\partial x_k} = \delta_{ik}$。

**证明 (2)**：

$$
\varphi(\vec{x}+\alpha\vec{\eta})
= \tfrac{1}{2}(\vec{x}+\alpha\vec{\eta})^{\mathsf T}A(\vec{x}+\alpha\vec{\eta}) - \vec{b}^{\mathsf T}(\vec{x}+\alpha\vec{\eta})
$$

$$
= \tfrac{1}{2}\vec{x}^{\mathsf T}A\vec{x} + \tfrac{1}{2}\alpha\vec{\eta}^{\mathsf T}A\vec{x} + \tfrac{1}{2}\alpha\vec{x}^{\mathsf T}A\vec{\eta} + \tfrac{1}{2}\alpha^2\vec{\eta}^{\mathsf T}A\vec{\eta} - \vec{b}^{\mathsf T}\vec{x} - \alpha\vec{b}^{\mathsf T}\vec{\eta}
$$

$$
= \varphi(\vec{x}) + \alpha\,(A\vec{x})^{\mathsf T}\vec{\eta} - \alpha\cdot\vec{b}^{\mathsf T}\vec{\eta} + \tfrac{1}{2}\alpha^2\cdot\vec{\eta}^{\mathsf T}A\vec{\eta}
$$

$$
= \varphi(\vec{x}) + (A\vec{x} - \vec{b})^{\mathsf T}\vec{\eta}\cdot\alpha + \tfrac{1}{2}\vec{\eta}^{\mathsf T}A\vec{\eta}\cdot\alpha^2
$$

（蓝）末式 $\tfrac{1}{2}\vec{\eta}^{\mathsf T}A\vec{\eta}$ 处旁注「$\longrightarrow a$」（二次项系数）。

**（红）** $\vec{x}^{\mathsf T}A\vec{\eta} = x_j\,a_{ij}\,\eta_i$。

**（蓝）** 若给定 $\vec{x},\vec{\eta}$，则 $\varphi(\vec{x}+\alpha\vec{\eta}) = c + b\cdot\alpha + a\cdot\alpha^2 = g(\alpha)$。

（图示：过 $\vec{x}$ 与 $\vec{x}+\alpha\vec{\eta}$ 两点的虚线，方向向量为 $\vec{\eta}$。）

---

## 第 2 页

**(3)**

$$
\varphi(\vec{x}^*) = \tfrac{1}{2}(\vec{x}^*)^{\mathsf T}A\vec{x}^* - \vec{b}^{\mathsf T}\vec{x}^*
= -\tfrac{1}{2}\vec{b}^{\mathsf T}\vec{x}^*
= -\tfrac{1}{2}(\vec{x}^*)^{\mathsf T}A\vec{x}^*
$$

考虑 $\vec{x}\ne\vec{x}^*$，取 $\vec{y} = \vec{x} - \vec{x}^*$：

$$
\varphi(\vec{x}) = \varphi(\vec{x}^* + \vec{y})
= \varphi(\vec{x}^*) + (A\vec{x}^* - \vec{b})^{\mathsf T}\cdot\vec{y}\cdot 1 + \tfrac{1}{2}\vec{y}^{\mathsf T}A\vec{y}\cdot 1
$$

$$
= \varphi(\vec{x}^*) + \tfrac{1}{2}(\vec{x} - \vec{x}^*)^{\mathsf T}A(\vec{x} - \vec{x}^*)
$$

$$
\Longrightarrow\ \varphi(\vec{x}) - \varphi(\vec{x}^*) = \tfrac{1}{2}(\vec{x} - \vec{x}^*)^{\mathsf T}A(\vec{x} - \vec{x}^*) \ge 0
\qquad\blacksquare
$$

**定理**：设 $A$ 正定，则 $\vec{x}^*$ 为 $A\vec{x} = \vec{b}$ 的解 $\Longleftrightarrow$ $\vec{x}^*$ 满足 $\varphi(\vec{x}^*) = \min_{\vec{x}}\varphi(\vec{x})$。

**（蓝）** 求解线性方程组（正定）$\Longleftrightarrow$ 求解变分最小值问题。$\downarrow$ 找到 $\varphi(\vec{x})$ 的最小值。

**线性搜索算法**：基于一系列 $f(x_k)$，使 $f(x_k)$ 逐渐趋于 $\min\varphi(\vec{x})$。

设已知 $\vec{x}_k\in\mathbb{R}^n$，选择非零向量 $\vec{p}_k\in\mathbb{R}^n$ 作为搜索方向。

在 $\vec{x}_k + \alpha\vec{p}_k$ 中找到 $\alpha_k$ 使

$$
\varphi(\vec{x}_k + \alpha_k\vec{p}_k) = \min_\alpha \varphi(\vec{x}_k + \alpha\vec{p}_k)
$$

此时

$$
\varphi(\vec{x}_k + \alpha\vec{p}_k)
= \varphi(\vec{x}_k) + \alpha\,(A\vec{x}_k - \vec{b})^{\mathsf T}\vec{p}_k + \tfrac{1}{2}\alpha^2\,\vec{p}_k^{\mathsf T}A\vec{p}_k
$$

$$
\Longrightarrow\ \frac{\partial\varphi}{\partial\alpha} = 0 = (A\vec{x}_k - \vec{b})^{\mathsf T}\vec{p}_k + \alpha\,\vec{p}_k^{\mathsf T}A\vec{p}_k
$$

$$
\Longrightarrow\ \alpha = \frac{(\vec{b} - A\vec{x}_k)^{\mathsf T}\vec{p}_k}{\vec{p}_k^{\mathsf T}A\vec{p}_k}\ \longrightarrow\ \alpha_k
$$

$$
\Longrightarrow\ \varphi(\vec{x}_k + \alpha_k\vec{p}_k) = \varphi(\vec{x}_k) - \frac{\big[(\vec{b} - A\vec{x}_k)^{\mathsf T}\vec{p}_k\big]^2}{2\,\vec{p}_k^{\mathsf T}A\vec{p}_k}
$$

定义残差 $\vec{r}_k = \vec{b} - A\vec{x}_k$（旁注：$\downarrow A(\vec{x}^* - \vec{x}_k)$），

$$
\alpha_k = \frac{\vec{r}_k^{\mathsf T}\cdot\vec{p}_k}{\vec{p}_k^{\mathsf T}A\vec{p}_k}
$$

$$
\vec{r}_k = \vec{b} - A\vec{x}_k = \vec{b} - A(\vec{x}_{k-1} + \alpha_{k-1}\vec{p}_{k-1})
= (\vec{b} - A\vec{x}_{k-1}) - \alpha_{k-1}A\vec{p}_{k-1}
= \vec{r}_{k-1} - \alpha_{k-1}A\vec{p}_{k-1}
\quad\longrightarrow\ \text{残差方程}
$$

$$
\Longrightarrow\ \vec{p}_{k-1}^{\mathsf T}\cdot\vec{r}_k
= \vec{p}_{k-1}^{\mathsf T}\cdot\vec{r}_{k-1} - \alpha_{k-1}\,\vec{p}_{k-1}^{\mathsf T}A\vec{p}_{k-1}
= \vec{p}_{k-1}^{\mathsf T}\vec{r}_{k-1} - \frac{\vec{r}_{k-1}^{\mathsf T}\cdot\vec{p}_{k-1}}{\vec{p}_{k-1}^{\mathsf T}A\vec{p}_{k-1}}\cdot\vec{p}_{k-1}^{\mathsf T}A\vec{p}_{k-1} = 0
$$

---

## 第 3 页

### 2. 最速下降法（Steepest Descent, SD）

搜索方向：取 $\vec{x}_k$ 点处下降最快方向为搜索方向。$\vec{p}$ 为负梯度方向，对于 $\nabla\varphi = A\vec{x}_k - \vec{b}$ $\Longrightarrow$ $-\nabla\varphi(\vec{x}_k) = \vec{b} - A\vec{x}_k$

$$
\Longrightarrow\ \vec{p}_k = \vec{r}_k/|\vec{r}_k|
$$

此时

$$
\alpha_k = \frac{\vec{r}_k\cdot\vec{r}_k/|\vec{r}_k|}{\vec{r}_k^{\mathsf T}/|\vec{r}_k|\cdot A\cdot\vec{r}_k/|\vec{r}_k|}
= \frac{\vec{r}_k^{\mathsf T}\cdot\vec{r}_k}{\vec{r}_k^{\mathsf T}A\vec{r}_k}\cdot|\vec{r}_k|
$$

$$
\vec{x}_{k+1} = \vec{x}_k + \alpha_k\cdot\vec{p}_k
= \vec{x}_k + \frac{\vec{r}_k^{\mathsf T}\cdot\vec{r}_k}{\vec{r}_k^{\mathsf T}A\vec{r}_k}\cdot\vec{r}_k
$$

**（蓝）** 可以不对搜索方向归一：$\vec{p}_k = \vec{r}_k$，

$$
\alpha_k = \frac{\vec{r}_k^{\mathsf T}\cdot\vec{r}_k}{\vec{r}_k^{\mathsf T}A\vec{r}_k},
\qquad
\vec{x}_{k+1} = \vec{x}_k + \alpha_k\cdot\vec{p}_k
= \vec{x}_k + \frac{\vec{r}_k^{\mathsf T}\cdot\vec{r}_k}{\vec{r}_k^{\mathsf T}A\vec{r}_k}\cdot\vec{r}_k
$$

**SD 基本算法：**

```
选取 x ∈ Rⁿ, k = 0, err = 1
while (k ≤ N_max) and (err > ε):
    r_k = b − A·x_k
    α_k = r_k^T·r_k / r_k^T·A·r_k
    x_{k+1} = x_k + α_k·r_k
    k = k + 1
    err = ‖r_k‖
```

### 最速下降法收敛性

**引理 1**：若 $A$ 正定，$A$ 特征值为 $0 < \lambda_1 \le \lambda_2 \le \cdots \le \lambda_n$，$P(\lambda)$ 为一多项式，则

$$
\|P(A)\vec{x}\|_A \le \max_i |P(\lambda_i)|\cdot\|\vec{x}\|_A,
\qquad \vec{x}\in\mathbb{R}^n .
$$

※ $\|\vec{x}\|_A = \sqrt{\vec{x}^{\mathsf T}A\vec{x}}$。

**证明**：

$$
\|P(A)\vec{x}\|_A = \sqrt{\vec{x}^{\mathsf T}\,P(A)\,A\,P(A)\,\vec{x}}
$$

考虑 $A$ 关于 $\lambda_i$ 的特征向量 $\vec{e}_i$，设 $\vec{x} = \sum_i \beta_i\vec{e}_i$。

---

## 第 4 页

（接上页）

$$
\vec{x}^{\mathsf T}P(A)\,A\,P(A)\vec{x}
= \Big(\sum_i \beta_i\vec{e}_i\Big)^{\mathsf T}P(A)\,A\,P(A)\Big(\sum_i \beta_i\vec{e}_i\Big)
= \sum_i \lambda_i\beta_i^2\,P^2(\lambda_i)
\le \max_i P^2(\lambda_i)\cdot\sum_i \beta_i^2\lambda_i
$$

由于

$$
\vec{x}^{\mathsf T}A\vec{x} = \Big(\sum_i\beta_i\vec{e}_i\Big)^{\mathsf T}A\Big(\sum_i\beta_i\vec{e}_i\Big) = \sum_i \beta_i^2\lambda_i
$$

$$
\Longrightarrow\ \|P(A)\vec{x}\|_A \le \max_i |P(\lambda_i)|\cdot\|\vec{x}\|_A
$$

**定理**：最速下降法生成的 $\vec{x}_k$ 有

$$
\|\vec{x}_k - \vec{x}^*\|_A \le \Big(\frac{\lambda_n - \lambda_1}{\lambda_n + \lambda_1}\Big)^{k}\,\|\vec{x}_0 - \vec{x}^*\|_A .
$$

**证明**：由已知

$$
\|\vec{x}_k - \vec{x}^*\|_A^2 = (\vec{x}_k - \vec{x}^*)^{\mathsf T}A(\vec{x}_k - \vec{x}^*)
$$

$$
= \vec{x}_k^{\mathsf T}A\vec{x}_k - \vec{x}_k^{\mathsf T}A\vec{x}^* - (\vec{x}^*)^{\mathsf T}A\vec{x}_k + (\vec{x}^*)^{\mathsf T}A\vec{x}^*
= f(\vec{x}_k) + f(\vec{x}^*)^{\mathsf T}A\vec{x}^*
$$

（$f(\vec{x}_k)$ 下有着重线。）

$$
\le f(\vec{x}_{k-1} + \alpha\vec{p}_{k-1}) + (\vec{x}^*)^{\mathsf T}A\vec{x}^*
$$

（旁注：☆ $\vec{x}_k = \vec{x}_{k-1} + \alpha_{k-1}\vec{p}_{k-1}$；$\alpha_{k-1} = \arg\min_\alpha f(\vec{x}_{k-1} + \alpha\vec{p}_{k-1})$。）

$$
= (\vec{x}_{k-1} + \alpha\vec{p}_{k-1} - \vec{x}^*)^{\mathsf T}A(\vec{x}_{k-1} + \alpha\vec{p}_{k-1} - \vec{x}^*)
$$

$$
\Longrightarrow\ \|\vec{x}_k - \vec{x}^*\|_A \le \|\vec{x}_{k-1} + \alpha(\vec{b} - A\vec{x}_{k-1}) - \vec{x}^*\|_A
$$

$$
= \|\vec{x}_{k-1} + \alpha(A\vec{x}^* - A\vec{x}_{k-1}) - \vec{x}^*\|_A
= \|(I - \alpha A)(\vec{x}_{k-1} - \vec{x}^*)\|_A
$$

$$
\le \max_i |1 - \alpha\lambda_i|\cdot\|\vec{x}_{k-1} - \vec{x}^*\|_A
\qquad\text{①}\quad (\text{由引理 1，取 } P(\lambda) = 1-\alpha\lambda)
$$

由于 $\alpha$ 是可取任意值：

$$
\|\vec{x}_k - \vec{x}^*\|_A \le \min_\alpha \max_i |1-\alpha\lambda_i|\cdot\|\vec{x}_{k-1} - \vec{x}^*\|_A
$$

**（红）※** $\max_i|1-\alpha\lambda_i| = \max\{|1-\alpha\lambda_1|,\ |1-\alpha\lambda_n|\}$（附示意图）

$$
\min_\alpha \max_i |1-\alpha\lambda_i| = \min_\alpha \max\{|1-\alpha\lambda_1|,\ |1-\alpha\lambda_n|\}
= \frac{\lambda_n - \lambda_1}{\lambda_n + \lambda_1}
\qquad\text{②}
$$

① + ② $\Longrightarrow$

$$
\|\vec{x}_k - \vec{x}^*\|_A \le \frac{\lambda_n - \lambda_1}{\lambda_n + \lambda_1}\,\|\vec{x}_{k-1} - \vec{x}^*\|_A
\le \cdots \le \Big(\frac{\lambda_n - \lambda_1}{\lambda_n + \lambda_1}\Big)^{k}\|\vec{x}_0 - \vec{x}^*\|_A
$$

---

## 第 5 页

### 3. 共轭梯度法（Conjugate Gradient, CG）

改进 SD 收敛速度 $\longrightarrow$ 改变搜索方向 $\vec{p}_k$。

**（蓝）** 回顾线搜索：

$$
\vec{x}_{k+1} = \vec{x}_k + \alpha_k\vec{p}_k
= \vec{x}_{k-1} + \alpha_{k-1}\vec{p}_{k-1} + \alpha_k\vec{p}_k
= \cdots = \vec{x}_0 + \alpha_0\vec{p}_0 + \alpha_1\vec{p}_1 + \cdots + \alpha_k\vec{p}_k
= \vec{x}_0 + \sum_{i=0}^{k}\alpha_i\vec{p}_i
$$

设 $\vec{x}_0 = \vec{0}\ \Longrightarrow\ \vec{x}_{k+1} = \sum_{i=0}^{k}\alpha_i\vec{p}_i \in \mathrm{Span}\{\vec{p}_0, \vec{p}_1, \cdots, \vec{p}_k\}$。

**（红）** 即 $\vec{x}_{k+1}$ 属于由 $\vec{p}_0, \vec{p}_1, \cdots, \vec{p}_k$ 共 $k+1$ 个向量所张成的空间；$\vec{x}_k$——由 $\vec{p}_0, \vec{p}_1, \cdots, \vec{p}_{k-1}$ 共 $k$ 个向量——。

**（红）※** 若 $\vec{p}_0 = (1,0,0,0)^{\mathsf T}$，$\vec{p}_1 = (1,1,0,0)^{\mathsf T}$，$\vec{p}_2 = (1,1,1,0)^{\mathsf T}$，

$$
\vec{x}_0 = (1,2,4,0)^{\mathsf T} \in \mathrm{Span}\{\vec{p}_0, \vec{p}_1, \vec{p}_2\}
$$

若进一步设 $\vec{p}_3 = (2,2,1,0)^{\mathsf T}$，

$$
\vec{x}_0 = (4,3,1,0)^{\mathsf T} \in \mathrm{Span}\{\vec{p}_0, \vec{p}_1, \vec{p}_2, \vec{p}_3\}
$$

若设 $\vec{x} = \vec{y} + \alpha\vec{p}_k$，其中 $\vec{y}\in\mathrm{Span}\{\vec{p}_0, \vec{p}_1, \cdots, \vec{p}_{k-1}\}$（旁注「$k$ 个.」），则

$$
\varphi(\vec{x}) = \varphi(\vec{y} + \alpha\vec{p}_k)
= \varphi(\vec{y}) + \alpha\,(A\vec{y} - \vec{b})^{\mathsf T}\cdot\vec{p}_k + \tfrac{1}{2}\alpha^2\cdot\vec{p}_k^{\mathsf T}A\vec{p}_k
$$

$$
= \varphi(\vec{y}) + \alpha\cdot(A\vec{y})^{\mathsf T}\cdot\vec{p}_k + \tfrac{1}{2}\alpha^2\cdot\vec{p}_k^{\mathsf T}A\vec{p}_k - \alpha\cdot\vec{b}^{\mathsf T}\vec{p}_k
$$

$$
\min_{\vec{x}\in\mathrm{Span}\{\vec{p}_0,\cdots,\vec{p}_k\}}\varphi(\vec{x})
= \min_{\substack{\vec{y}\in\mathrm{Span}\{\vec{p}_0,\cdots,\vec{p}_{k-1}\}\\ \alpha\in\mathbb{R}}}
\big(\varphi(\vec{y}) + \alpha(A\vec{y})^{\mathsf T}\vec{p}_k + \tfrac{1}{2}\alpha^2\vec{p}_k^{\mathsf T}A\vec{p}_k - \alpha\vec{b}^{\mathsf T}\vec{p}_k\big)
$$

（红批注：$\varphi(\vec{y})$ 下标「与 $\alpha$ 无关」；$\alpha(A\vec{y})^{\mathsf T}\vec{p}_k$ 下标「$\alpha,\vec{y}$ 耦合」；末两项下标「与 $\vec{y}$ 无关」。）

**（红）※** 针对 $\vec{x}$ 的 2 个变量 $\alpha, \vec{y}$ 的最小化问题，转化为逐个变量 $\alpha, \vec{y}$ 求解。

若设计 $\vec{p}_k$ 使 $(A\vec{y})^{\mathsf T}\vec{p}_k = 0$，则最小化问题更容易，$\forall\,\vec{y}\in\mathrm{Span}\{\vec{p}_0, \cdots, \vec{p}_{k-1}\}$。

**问题**：如何找到 $\vec{p}_k$，$\forall\,\vec{y}\in\mathrm{Span}\{\vec{p}_0, \cdots, \vec{p}_{k-1}\}$，使 $(A\vec{y})^{\mathsf T}\vec{p}_k = 0$？

---

## 第 6 页

$$
(A\vec{y})^{\mathsf T}\vec{p}_k = \vec{y}^{\mathsf T}(A\vec{p}_k)
= \big(\beta_0\vec{p}_0 + \beta_1\vec{p}_1 + \cdots + \beta_{k-1}\vec{p}_{k-1}\big)^{\mathsf T}\cdot A\vec{p}_k
$$

$$
= \beta_0\vec{p}_0^{\mathsf T}A\vec{p}_k + \beta_1\vec{p}_1^{\mathsf T}A\vec{p}_k + \cdots + \beta_{k-1}\vec{p}_{k-1}^{\mathsf T}A\vec{p}_k = 0,\quad \forall\,\beta_i\in\mathbb{R}
$$

$$
\Longrightarrow\ \vec{p}_i^{\mathsf T}A\vec{p}_k = 0,\quad \forall\, i\in\{0, 1, 2, \cdots, k-1\}
$$

**定义**：若 $A$ 正定，且 $\mathbb{R}^n$ 中向量组 $\{\vec{p}_0, \cdots, \vec{p}_{n-1}\}$ 满足 $\vec{p}_j^{\mathsf T}A\vec{p}_i = 0\ (i\ne j)$，则称 $\{\vec{p}_0, \cdots, \vec{p}_{n-1}\}$ 为 **A-共轭向量组**；$\vec{p}_j^{\mathsf T}A\vec{p}_i = 0\ (i\ne j)$ 称 **A-共轭**。

**（红）※** 若 $A = I$：$\vec{p}_j^{\mathsf T}A\vec{p}_i = \vec{p}_j^{\mathsf T}\vec{p}_i = 0$。

若 $A = C^{\mathsf T}C$：$\vec{p}_j^{\mathsf T}A\vec{p}_i = \vec{p}_j^{\mathsf T}C^{\mathsf T}C\vec{p}_i = (C\vec{p}_j)^{\mathsf T}\cdot(C\vec{p}_i) = 0$（$C\vec{p}_j$、$C\vec{p}_i$ 下有下划线）。

### 构造 $\vec{p}_k$ 的方法

由于 $\vec{p}_{k-1}^{\mathsf T}\cdot\vec{r}_k = 0$，假设

$$
\vec{p}_k = \vec{r}_k + \beta_{k-1}\cdot\vec{p}_{k-1}
$$

（红 ※：$\vec{p}_k = m\cdot\vec{r}_k + n\cdot\vec{p}_{k-1}$，若 $m = 0$，$\vec{p}_k\parallel\vec{p}_{k-1}$。）

此时由 $\vec{p}_{k-1}^{\mathsf T}A\vec{p}_k = 0$：

$$
\Longrightarrow\ \vec{p}_{k-1}^{\mathsf T}A(\vec{r}_k + \beta_{k-1}\cdot\vec{p}_{k-1}) = 0
\ \Longrightarrow\ \beta_{k-1} = -\frac{\vec{r}_k^{\mathsf T}A\vec{p}_{k-1}}{\vec{p}_{k-1}^{\mathsf T}A\vec{p}_{k-1}}
$$

基于此关系得到的 $\{\vec{p}_k\}$ 及相应的 $\{\vec{x}_k\}$ 满足：

$$
(1)\ \vec{r}_i^{\mathsf T}\cdot\vec{r}_j = 0\ (i\ne j);\qquad
(2)\ \vec{p}_i^{\mathsf T}A\vec{p}_j = 0\ (i\ne j)
\qquad \text{※取 } \vec{p}_0 = \vec{r}_0
$$

---

## 第 7 页

### 共轭梯度法

给定 $\vec{x}_k$，计算残差 $\vec{r}_k$，得到

$$
\beta_{k-1} = -\frac{\vec{r}_k^{\mathsf T}A\vec{p}_{k-1}}{\vec{p}_{k-1}^{\mathsf T}A\vec{p}_{k-1}}
$$

进一步计算

$$
\vec{p}_k = \vec{r}_k + \beta_{k-1}\cdot\vec{p}_{k-1}
\qquad
\text{（红 ※：} \min_{\vec{y},\alpha}\varphi(\vec{y},\alpha)\text{）}
$$

对于 $\alpha$ 变量计算

$$
\arg\min_\alpha\big(\tfrac{1}{2}\alpha^2\cdot\vec{p}_k^{\mathsf T}A\vec{p}_k - \alpha\cdot\vec{b}^{\mathsf T}\vec{p}_k\big)
= \min_{\vec{y}} g_1(\vec{y}) + \min_{\alpha} g_2(\alpha)
$$

（红：末式下有下划线。）

得到

$$
\alpha_k = \frac{\vec{b}^{\mathsf T}\cdot\vec{p}_k}{\vec{p}_k^{\mathsf T}A\vec{p}_k}
$$

计算得

$$
\vec{x}_{k+1} = \vec{x}_k + \alpha_k\cdot\vec{p}_k
$$

**（红）※** 经典线搜索中

$$
\alpha_k = \frac{(\vec{b} - A\vec{x}_k)^{\mathsf T}\cdot\vec{p}_k}{\vec{p}_k^{\mathsf T}A\vec{p}_k}\ \longrightarrow\ \text{①}
$$

$$
= \frac{\vec{b}^{\mathsf T}\cdot\vec{p}_k}{\vec{p}_k^{\mathsf T}A\vec{p}_k} - \underbrace{\Big(\frac{\vec{x}_k^{\mathsf T}A\vec{p}_k}{\vec{p}_k^{\mathsf T}A\vec{p}_k}\Big)}_{\text{圈出，}\to 0}
$$

$$
\Big\downarrow\ \vec{x}_0 = \vec{0}
$$

$$
\vec{x}_k\in\mathrm{Span}\{\vec{p}_0, \cdots, \vec{p}_{k-1}\}
$$

$$
\Big\downarrow
$$

$\vec{x}_k$ 与 $\vec{p}_k$ $A$-共轭。

**CG 算法流程：**

```
选取 x ∈ Rⁿ, k = 0, err = 1
计算 r = b − A·x, p = r
while (k ≤ N_max) and (err > ε):
    α_k = r_k^T·r_k / p_k^T·A·p_k          （红 ※：q = A·p_k）
    x_{k+1} = x_k + α_k·p_k                 （↓ q）
    r_{k+1} = r_k − α_k·A·p_k  → q
    β_k = r_{k+1}^T·r_{k+1} / r_k^T·r_k     （圈出）
    p_{k+1} = r_{k+1} + β_k·p_k
    k = k + 1
end
```

**（红）※** 残差方程 $\vec{r}_{k+1} = \vec{r}_k - \alpha_k A\vec{p}_k$ $\Longrightarrow$ $A\vec{p}_k = \tfrac{1}{\alpha_k}(\vec{r}_k - \vec{r}_{k+1})$。

---

## 第 8 页

$$
\beta_k = -\frac{\vec{r}_{k+1}^{\mathsf T}A\vec{p}_k}{\vec{p}_k^{\mathsf T}A\vec{p}_k}
= -\frac{\vec{r}_{k+1}^{\mathsf T}\big(\tfrac{1}{\alpha_k}(\vec{r}_k - \vec{r}_{k+1})\big)}{\vec{p}_k^{\mathsf T}\big(\tfrac{1}{\alpha_k}(\vec{r}_k - \vec{r}_{k+1})\big)}
$$

$$
= -\frac{\vec{r}_{k+1}^{\mathsf T}\cdot\vec{r}_k - \vec{r}_{k+1}^{\mathsf T}\cdot\vec{r}_{k+1}}{\vec{p}_k^{\mathsf T}\cdot\vec{r}_k - \vec{p}_k^{\mathsf T}\cdot\vec{r}_{k+1}}
= \frac{\vec{r}_{k+1}^{\mathsf T}\cdot\vec{r}_{k+1}}{\vec{p}_k^{\mathsf T}\cdot\vec{r}_k}
$$

（红注：分子第一项 $\vec{r}_{k+1}^{\mathsf T}\vec{r}_k$ 与分母第二项 $\vec{p}_k^{\mathsf T}\vec{r}_{k+1}$ 处标「$\to 0$」。）

$$
= \frac{\vec{r}_{k+1}^{\mathsf T}\cdot\vec{r}_{k+1}}{(\vec{r}_k + \beta_{k-1}\cdot\vec{p}_{k-1})^{\mathsf T}\cdot\vec{r}_k}
= \frac{\vec{r}_{k+1}^{\mathsf T}\cdot\vec{r}_{k+1}}{\vec{r}_k^{\mathsf T}\cdot\vec{r}_k}
$$

CG 中：

- 第一步找到 $\mathrm{Span}\{\vec{p}_0\}$ 中最优点：$\vec{x}_1 = \arg\min_{\vec{x}\in\Omega_0}\varphi(\vec{x})$，$\Omega_0$，$\dim\Omega_0 = 1$
- 第二步找到 $\mathrm{Span}\{\vec{p}_0, \vec{p}_1\}$ 中最优点：$\vec{x}_2 = \arg\min_{\vec{x}\in\Omega_1}\varphi(\vec{x})$，$\Omega_1$，$\dim\Omega_1 = 2$
- 第三步 $\cdots$ $\mathrm{Span}\{\vec{p}_0, \vec{p}_1, \vec{p}_2\}$ $\cdots$：$\vec{x}_3 = \arg\min_{\vec{x}\in\Omega_2}\varphi(\vec{x})$，$\Omega_2$，$\dim\Omega_2 = 3$
- $\vdots$
- 第 $n$ 步 $\cdots$ $\mathrm{Span}\{\vec{p}_0, \cdots, \vec{p}_{n-1}\}$ $\cdots$：$\vec{x}_n = \arg\min_{\vec{x}\in\Omega_{n-1}}\varphi(\vec{x})$，$\Omega_{n-1}$，$\dim(\Omega_{n-1}) = n$　※ $\vec{x}_n = \vec{x}^*$

※ $\Omega_0 \subset \Omega_1 \subset \Omega_2 \subset \Omega_3 \subset \cdots \subset \Omega_{n-1}$

**定理**：利用 CG 得到的 $\vec{x}_k$ 满足

$$
\|\vec{x}_k - \vec{x}^*\|_A \le 2\Big(\frac{\sqrt{\kappa_2} - 1}{\sqrt{\kappa_2} + 1}\Big)^{k}\|\vec{x}_0 - \vec{x}^*\|_A,
\qquad \text{其中 } \kappa_2 = \|A\|_2\cdot\|A^{-1}\|_2 .
$$

※ $\kappa_2 = \dfrac{\lambda_n}{\lambda_1}$。

对比 SD 的 $\Big(\dfrac{1-\lambda_n/\lambda_1}{1+\lambda_n/\lambda_1}\Big)^{k}$。

---

## 第 9 页

### 预优化 CG（预条件化 CG）

CG 收敛速度取决于 $A$ 的 2-条件数。

原问题 $A\vec{x} = \vec{b}$ $\Longrightarrow$ $A'\vec{x} = \vec{b}'$，使 $\mathrm{Cond}(A') \ll \mathrm{Cond}(A)$。
