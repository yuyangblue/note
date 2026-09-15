# 《统计学完全教程》第5章 收敛（下）：中心极限定理与 Delta 方法 - 笔记

> **参考来源**：课本第 5 章 5.4–5.5 节（中心极限定理、Delta 方法）；**视频主讲：MIT 6.041SC**（BV1JZhFzYEXH 上集）L19（上 p191–p197：中心极限定理与二项正态近似）；**讲义参考：MIT 18.600 Lecture 31**（本地 `原始材料\MIT18.600\Lecture31.pdf`：中心极限定理；Delta 方法不在 18.600 范围）；18.650 视频无对应集；补充讲义 CMU 36-705 Lec6（随机阶记号、Lyapunov CLT）。

## 目录
- [1. 核心概念](#1-核心概念)
- [2. 中心极限定理 CLT](#2-中心极限定理-clt)
- [3. Berry-Esseen 界](#3-berry-esseen-界)
- [4. Delta 方法](#4-delta-方法)
- [5. 随机阶记号](#5-随机阶记号)
- [6. 例题](#6-例题)
- [7. 本节重点](#7-本节重点)

---

## 1. 核心概念

第 5 章下半部分给出**渐近正态**的两个主定理：CLT（均值近似正态）和 Delta 方法（均值的函数也近似正态）。统计推断（置信区间、检验、p 值）几乎全部建立在"$\sqrt{n}(\hat\theta_n - \theta) \leadsto N(0, \sigma^2)$"这一范式上。

---

## 2. 中心极限定理 CLT

**定理 5.8（中心极限定理）**：$X_1, \cdots, X_n$ 为 IID，$\mu = \mathbb{E}(X_i)$，$\sigma^2 = \mathbb{V}(X_i)$（$0 < \sigma^2 < \infty$），则：

$$\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \leadsto N(0,1)$$

即对任意实数 $x$：

$$P\left(\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \le x\right) \to \Phi(x) = \int_{-\infty}^x \frac{1}{\sqrt{2\pi}}e^{-u^2/2}du$$

**等价表述**：$\bar{X}_n \approx N(\mu, \sigma^2/n)$，或 $\sum_{i=1}^n X_i \approx N(n\mu, n\sigma^2)$。

**证明思路（MGF 法）**：设 $\phi$ 为 $X_i$ 的 MGF（在 0 附近存在）。$Y_i = (X_i - \mu)/\sigma$，$M_{Y}(t) = \phi(t/\sigma)e^{-\mu t/\sigma}$，$M_Y(0) = 0$，$M_Y'(0) = 0$，$M_Y''(0) = 1$。$\bar{X}_n$ 标准化的 MGF：

$$M_n(t) = \left[M_Y\left(\frac{t}{\sqrt{n}}\right)\right]^n$$

对 $M_Y(t/\sqrt{n})$ 做二阶泰勒展开：$M_Y\left(\frac{t}{\sqrt{n}}\right) = 1 + \frac{t^2}{2n} + o\left(\frac{1}{n}\right)$，因此 $M_n(t) \to e^{t^2/2}$ = $N(0,1)$ 的 MGF。由 MGF 收敛 → 分布收敛，得证。

> **白话解读**：**不管 $X_i$ 是什么分布**（只要二阶矩存在），标准化后的样本均值都收敛到标准正态。$n$ 越大，$\bar{X}_n$ 越像 $N(\mu, \sigma^2/n)$。这就是"正态分布无处不在"的原因——大量独立小效应的叠加必正态。这正是第 18 讲之前 Wasserman 说的"CLT 是统计推断的心脏"。

**例 5.9**：$X_1, \cdots, X_n \sim \text{Bernoulli}(p)$，$\hat p_n = \bar{X}_n$，$\sigma^2 = p(1-p)$：

$$\frac{\sqrt{n}(\hat p_n - p)}{\sqrt{p(1-p)}} \leadsto N(0,1), \quad \text{即} \quad \hat p_n \approx N\left(p, \frac{p(1-p)}{n}\right)$$

**例 5.10**：$X \sim \text{Poisson}(n)$（均值=方差=$n$），$X = \sum_{i=1}^n Y_i$（$Y_i \sim \text{Poisson}(1)$ 独立）：

$$\frac{X - n}{\sqrt{n}} \leadsto N(0,1), \quad X \approx N(n, n)$$

> **白话解读**：泊松（参数 $n$ 很大时）可用正态近似——均值 $n$、方差 $n$。这是"大数目的稀有事件计数 ≈ 正态"的体现。

---

## 3. Berry-Esseen 界

CLT 只给"极限"，不回答"$n$ 多大才够"。Berry-Esseen 给出**收敛速度**：

**定理 5.11**：$X_1, \cdots, X_n$ 为 IID，$\mu = \mathbb{E}(X_i)$，$\sigma^2 = \mathbb{V}(X_i)$，$\gamma = \mathbb{E}|X_i - \mu|^3 < \infty$。设 $Z_n = \frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma}$，$F_n$ 为其 CDF，则：

$$\sup_x |F_n(x) - \Phi(x)| \le \frac{33\gamma}{4\sigma^3\sqrt{n}}$$

> **白话解读**：CLT 近似的误差以 $O(1/\sqrt{n})$ 衰减，常数由三阶绝对矩 $\gamma$ 决定。**偏态/厚尾分布（$\gamma$ 大）需要更大的 $n$** 才能让正态近似可靠。$\sqrt{n}$ 速率的直觉：标准化幅度是 $1/\sqrt{n}$，误差自然也是这个量级。

---

## 4. Delta 方法

### 4.1 单变量 Delta 方法

**定理 5.12（Delta 方法）**：$Y_n$ 满足 $\sqrt{n}(Y_n - \theta) \leadsto N(0, \sigma^2)$，$g$ 在 $\theta$ 处可导且 $g'(\theta) \ne 0$，则：

$$\sqrt{n}(g(Y_n) - g(\theta)) \leadsto N(0, \sigma^2(g'(\theta))^2)$$

**证明思路**：对 $g(Y_n)$ 在 $\theta$ 处泰勒展开：$g(Y_n) = g(\theta) + g'(\theta)(Y_n - \theta) + \text{余项}$。余项是 $o_p(Y_n - \theta) = o_p(1/\sqrt{n})$，乘以 $\sqrt{n}$ 消失（需要 $g'(\theta) \ne 0$）。再用 Slutsky 定理整理。

> **白话解读**：**"均值的函数 ≈ 均值处的函数 + 斜率×误差"**——一阶泰勒近似把问题线性化。$g$ 是光滑函数时，$g(\bar{X}_n) \approx N(g(\mu),\ (g'(\mu))^2 \sigma^2/n)$。方差乘上"斜率平方"。
>
> **用途**：$\hat\theta = 1/\bar{X}$、$e^{\hat\theta}$、$\log \hat\theta$、$\hat p(1-\hat p)$ 等估计量的渐近分布都能由 Delta 方法得到。

### 4.2 多变量 Delta 方法

**定理 5.14（多变量版本）**：$\nabla g$ 为梯度（在 $\theta$ 处取值），$Y_n$ 满足 $\sqrt{n}(Y_n - \theta) \leadsto N(0, \Sigma)$，则：

$$\sqrt{n}(g(Y_n) - g(\theta)) \leadsto N(0,\ \nabla g(\theta)^T\Sigma\nabla g(\theta))$$

**证明思路**：多变量泰勒展开 $g(y) = g(\theta) + \nabla g(\theta)^T(y-\theta) + \text{余项}$，余项 $= o(\|y - \theta\|)$，处理同上。

> **白话解读**：方差变成"梯度转置 × 协方差矩阵 × 梯度"（二次型）。$g$ 的每个分量方向上的不确定性按梯度权重累加。**估计多个参数的函数**（如比例差 $g(p_1,p_2) = p_1 - p_2$）时用这个版本。

---

## 5. 随机阶记号

**定义 5.16（随机阶）**：

$$Y_n = O_p(a_n) \iff \frac{Y_n}{a_n} \xrightarrow{P} 0 \text{ 的补集情形：对任意 } \epsilon \text{ 存在 } M_\epsilon \text{ 使 } P\left(\left|\frac{Y_n}{a_n}\right| > M_\epsilon\right) < \epsilon \text{（最终有界）}$$

$$Y_n = o_p(a_n) \iff \frac{Y_n}{a_n} \xrightarrow{P} 0$$

**例 5.17**：$\sqrt{n}(\bar{X}_n - \mu) = O_p(1)$——CLT 说它依分布收敛到 $N(0,\sigma^2)$（分布有界）；$\bar{X}_n - \mu = o_p(1)$——WLLN 说它依概率趋于 0；$\bar{X}_n - \mu = O_p(n^{-1/2})$。

> **白话解读**：$O_p$ 表示"数量级不会超过 $a_n$"（概率意义下的有界），$o_p$ 表示"比 $a_n$ 小得多"（除以 $a_n$ 后趋于 0）。这是渐近论证的"速记语言"——Delta 方法证明里的"余项是 $o_p$ 的所以能扔"就是用它表达。

---

## 6. 例题

**例 1（比例估计的 CLT）**：$n = 100$，$X_i \sim \text{Bernoulli}(0.5)$，$\hat p = \bar{X}$。$\hat p \approx N(0.5, 0.25/100)$，$P(|\hat p - 0.5| \le 0.1) \approx \Phi(2) - \Phi(-2) \approx 0.95$。

**例 2（Delta 方法：$g(x) = 1/x$）**：$X_i \sim \text{Exp}(\beta)$，$\bar{X}_n \approx N(\beta, \beta^2/n)$，$g'(x) = -1/x^2$，$g'(\beta) = -1/\beta^2$：

$$\sqrt{n}\left(\frac{1}{\bar{X}_n} - \frac{1}{\beta}\right) \leadsto N\left(0,\ \frac{\beta^2}{\beta^4}\right) = N\left(0,\ \frac{1}{\beta^2}\right)$$

**例 3（Delta 方法：$g(x) = \log x$）**：$g'(x) = 1/x$：

$$\sqrt{n}(\log \bar{X}_n - \log \mu) \leadsto N\left(0, \frac{\sigma^2}{\mu^2}\right)$$

**例 4（方差稳定变换思路）**：选择 $g$ 使渐近方差常数（与 $\theta$ 无关），如对泊松 $X \approx N(\lambda, \lambda)$，取 $g(x) = \sqrt{x}$（$g'(\lambda) = 1/(2\sqrt\lambda)$），渐近方差 $= \lambda \cdot \frac{1}{4\lambda} = 1/4$——**开方变换稳定泊松方差**。

**例 5（多变量 Delta：比例差）**：$\hat p_1, \hat p_2$ 独立（样本量 $n_1, n_2$），$g(p_1, p_2) = p_1 - p_2$，$\nabla g = (1, -1)$：

$$\hat p_1 - \hat p_2 \approx N\left(p_1 - p_2,\ \frac{p_1(1-p_1)}{n_1} + \frac{p_2(1-p_2)}{n_2}\right)$$

---

## 7. 本节重点

> **本节重点**：
> - **CLT**：$\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \leadsto N(0,1)$，即 $\bar{X}_n \approx N(\mu, \sigma^2/n)$——任何分布（二阶矩有限）的均值近似正态；MGF 泰勒展开证明。
> - Berry-Esseen：误差 $\le \frac{33\gamma}{4\sigma^3\sqrt{n}}$——偏态厚尾需要更大 $n$。
> - **Delta 方法**：$\sqrt{n}(g(Y_n) - g(\theta)) \leadsto N(0, \sigma^2(g'(\theta))^2)$；多变量版本用梯度二次型 $\nabla g^T\Sigma\nabla g$。
> - 随机阶：$O_p$（数量级有界）、$o_p$（相对 $a_n$ 可忽略）；$\bar{X}_n - \mu = O_p(n^{-1/2})$。
> - **常见坑**：$g'(\theta) = 0$ 时 Delta 方法失效（退化，需要二阶展开）；CLT 要求 $\sigma < \infty$；正态近似在小 $n$ + 强偏态时误差大（Berry-Esseen）。
