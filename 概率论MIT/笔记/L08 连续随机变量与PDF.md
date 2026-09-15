# L08 连续随机变量与概率密度函数 - 笔记

> **参考来源**
> - 视频：B站 6.041SC 上集 BV1JZhFzYEXH，**p80–p88**（L08.1 课程概览 ~ L08.9 正态概率计算）
> - 讲义：Lecture 8（L08.pdf，20 页；含答案版 L08AS.pdf）
> - 教材：《Introduction to Probability》第 2 章 2.4–2.6

## 目录
- [1. 核心概念](#1-核心概念)
- [2. 公式与定义](#2-公式与定义)
- [3. 关键性质](#3-关键性质)
- [4. 例题](#4-例题)
- [5. 本节重点](#5-本节重点)

---

## 1. 核心概念

### 1.1 PDF：连续世界的"概率律"
对连续随机变量，单点概率恒为 0，改用**概率密度函数**描述：
$$P(a \le X \le b) = \int_a^b f_X(x)\, dx$$
- $f_X(x) \ge 0$，$\int_{-\infty}^{\infty} f_X(x)\, dx = 1$；
- $f_X(x) \cdot \delta \approx P(x \le X \le x+\delta)$（$f$ 是"单位长度上的概率"）。

### 1.2 期望与方差（连续版）
$$E[X] = \int_{-\infty}^{\infty} x f_X(x)\, dx, \qquad E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x)\, dx$$

### 1.3 CDF：统一离散与连续
$$F_X(x) = P(X \le x)$$
连续时 $F_X(x) = \int_{-\infty}^x f_X(t)\,dt$，离散时 $F_X(x) = \sum_{k \le x} p_X(k)$。

---

## 2. 公式与定义

### 2.1 三种核心连续分布

| 分布 | 参数 | PDF | 均值 | 方差 |
|---|---|---|---|---|
| 连续均匀 | $a<b$ | $\frac{1}{b-a}$（$a\le x\le b$） | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ |
| 指数 | $\lambda>0$ | $\lambda e^{-\lambda x}$（$x\ge0$） | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |
| 正态 | $\mu,\sigma^2$ | $\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ |

补充（$0,\dots,n$ 离散均匀的连续类比）：连续均匀 $[a,b]$ 方差 $\frac{(b-a)^2}{12}$；离散 $a,\dots,b$ 方差 $\frac{1}{12}(b-a)(b-a+2)$。

### 2.2 标准正态
$N(0,1)$：$f_X(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$，$E[X]=0$，$\text{var}(X)=1$；CDF 无闭合形式，用表查 $\Phi(z)$。

### 2.3 正态的线性性
$X \sim N(\mu, \sigma^2)$，$Y = aX + b$ ⇒ $Y \sim N(a\mu + b, a^2\sigma^2)$。
标准化：$Y = (X-\mu)/\sigma \sim N(0,1)$。

### 2.4 CDF 通用性质
非递减；$x\to\infty$ 时趋于 1；$x\to-\infty$ 时趋于 0。

---

## 3. 关键性质

- **指数分布无记忆性**：$P(X > t+s \mid X > t) = P(X > s)$——剩余寿命分布与已用时间无关（见 L09 详讲）；
- **方差性质**（连续版同样成立）：$\text{var}(aX+b) = a^2\text{var}(X)$，$\text{var}(X) = E[X^2]-(E[X])^2$；
- 正态的重要性：中心极限定理的主角 + 大量微小独立噪声叠加的模型（应用普遍）。

---

## 4. 例题

### 例 1：均匀分布的均值方差
$X \sim U[a,b]$：
- $E[X] = \int_a^b x \cdot \frac{1}{b-a} dx = \frac{a+b}{2}$；
- $E[X^2] = \int_a^b x^2 \frac{dx}{b-a} = \frac{a^2+ab+b^2}{3}$；
- $\text{var}(X) = \frac{a^2+ab+b^2}{3} - \frac{(a+b)^2}{4} = \frac{(b-a)^2}{12}$。

### 例 2：指数分布的均值
$f_X(x) = \lambda e^{-\lambda x}$（$x\ge0$）：
- $E[X] = \int_0^\infty x\lambda e^{-\lambda x}dx = \frac{1}{\lambda}$（分部积分）；
- $E[X^2] = \frac{2}{\lambda^2}$ ⇒ $\text{var}(X) = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}$。

### 例 3：正态概率计算
- 设 $X \sim N(2, 9)$（$\mu=2,\sigma=3$），求 $P(X \le 5)$；
- 标准化：$P\left(Z \le \frac{5-2}{3}\right) = \Phi(1) \approx 0.8413$；
- 一般步骤：先把关注事件写成标准正态的形式，再查表。

---

## 5. 本节重点

> **本节重点**：
> - PDF 是密度（积分得概率）、单点概率为 0；$\int f = 1$；期望/期望值法则换积分。
> - 均匀/指数/正态三兄弟的 PDF、均值、方差要背熟。
> - 正态线性性：$aX+b \sim N(a\mu+b, a^2\sigma^2)$；标准化 $Z=(X-\mu)/\sigma$ 后查表。
> - CDF 定义与单调性；离散与连续统一。
> - **常见坑**：① 把 $f_X(x)$ 当概率（可能大于 1）；② 指数分布只对 $x \ge 0$ 定义；③ 正态查表前忘记标准化（$\sigma$ 在分母）。
