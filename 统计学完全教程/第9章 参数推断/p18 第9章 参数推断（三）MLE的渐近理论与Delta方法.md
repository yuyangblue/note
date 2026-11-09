# 《统计学完全教程》第9章 参数推断（三）：MLE 的渐近理论与 Delta 方法 - 笔记

> **参考来源**：课本第 9 章 9.5、9.7–9.12 节与附录 9.13.1（证明）；**18.650 视频**（B站合集 `BV1hp4y1i77w` 分P p05：MLE 相合性/渐近正态/最优性；p06 末尾：Delta 方法；课件 `03_Lectures4-5_Maximum_Likelihood.pdf`、`04_Lecture6_Method_of_Moments.pdf`，逐字稿 Lec5/Lec6）；**CMU 36-705 Lecture Notes 15–16**（渐近理论、MLE 最优性，桌面 `All of Statistics 统计部分\01_主线_Wasserman_36-705_Fall2020\LectureNotes\`，对照表见 `统计学完全教程/原始材料/CMU36-705_课程资源与章节对照.md`）。

## 目录

- [[#1. 核心概念]]
- [[#2. Kullback–Leibler 散度与可识别性]]
- [[#3. MLE 的相合性]]
- [[#4. 得分函数与 Fisher 信息]]
- [[#5. 渐近正态与置信区间]]
- [[#6. 最优性与渐近相对效率]]
- [[#7. Delta 方法]]
- [[#8. 多参数模型]]
- [[#9. 参数 Bootstrap]]
- [[#10. 检验假设条件]]
- [[#11. 例题]]
- [[#12. 本节重点]]

---

## 1. 核心概念

p16 给出了 MLE 的五条性质（总览见 [[统计学完全教程/第9章 参数推断/p16 第9章 参数推断（一）矩估计与极大似然.md#5.1 五条主要性质（9.4 节）|p16 §5.1]]）。本篇回答三个递进的问题，并给出证明：

1. $\widehat{\theta}_n$ 收敛到真值吗？——**相合性**（§3），靶子是 KL 散度（§2）；
2. $\widehat{\theta}_n$ 的分布近似是什么？——**渐近正态**（§5），工具是得分函数与 Fisher 信息（§4）；
3. 有没有更好的估计量？——**最优性**（§6），答案：正则条件下没有。

整套理论都是**渐近**的（$n \to \infty$），依赖第 5 章的全部工具：大数定律（[[统计学完全教程/第5章 收敛与极限/p13 第5章 收敛（上）收敛类型与大数定律.md#5. 强大数定律|p13 §5]]）、CLT（[[统计学完全教程/第5章 收敛与极限/p14 第5章 收敛（下）中心极限定理与Delta方法.md#2. 中心极限定理 CLT|p14 §2]]）、Slutsky（[[统计学完全教程/第5章 收敛与极限/p13 第5章 收敛（上）收敛类型与大数定律.md#3. 收敛的关系|p13 §3]]）与 Delta 方法（[[统计学完全教程/第5章 收敛与极限/p14 第5章 收敛（下）中心极限定理与Delta方法.md#4. Delta 方法|p14 §4]]）。

## 2. Kullback–Leibler 散度与可识别性

**定义**：两个 PDF $f, g$ 的 **Kullback–Leibler 散度**

$$D(f,g) = \int f(x)\log\frac{f(x)}{g(x)}\,dx \qquad (9.6)$$

可证 $D(f,g) \ge 0$ 且 $D(f,f) = 0$。注意：$D$ **不对称**（$D(f,g) \ne D(g,f)$），所以形式上不是距离——课本脚注明确说它只是"类距离"。

**概念（可识别性）**：记 $D(\theta,\psi) \equiv D(f(x;\theta), f(x;\psi))$。称模型 $\mathfrak{F}$ **可识别**（identifiable），如果 $\theta \ne \psi$ 蕴涵 $D(\theta,\psi) > 0$——不同的参数值对应**不同的分布**。此后默认模型可识别。

**动机**：可识别性是相合性的最低要求——如果两个参数值给出同一个分布，数据根本无法区分它们，任何估计量都谈不上收敛到"真值"。

## 3. MLE 的相合性

**思路（整个证明只做一件事：说明对数似然的平均值的最大点收敛到真值）**。设 $\theta_*$ 为真值。最大化 $\ell_n(\theta)$ 等价于最大化

$$M_n(\theta) = \frac{1}{n}\left(\ell_n(\theta) - \ell_n(\theta_*)\right)$$

（减去常数 $\ell_n(\theta_*)$ 不改变最大点。）由大数定律，$M_n(\theta)$ 逐点收敛到

$$\int \log\frac{f(x;\theta_*)}{f(x;\theta)}f(x;\theta_*)\,dx \ =\ -D(\theta_*, \theta)$$

而 $-D(\theta_*,\theta)$ 在 $\theta = \theta_*$ 处取唯一最大值 0（可识别性保证别处严格小于 0）。所以**最大点应当被"吸"到 $\theta_*$**——这就是相合性的全部直觉。

要把"逐点收敛"升级成"最大点收敛"，还需要两块拼图（定理 9.13 的条件）：

- **一致收敛**：$\sup_\theta \lvert M_n(\theta) - M(\theta)\rvert \xrightarrow{P} 0$——否则逐点收敛可能漏掉最大点在两线之间的窄缝里溜走；
- **可识别 + $M(\theta)$ 表现良好**：对每个 $\varepsilon > 0$，$\sup_{\lvert\theta - \theta_*\rvert \ge \varepsilon} M(\theta) < M(\theta_*)$——真值的坑是全局最深的。

**定理 9.13**：上述两条成立时，MLE $\widehat{\theta}_n \xrightarrow{P} \theta_*$。

> [!note]- 证明骨架（课本附录 9.13.1）
> 由 $\widehat{\theta}_n$ 是最大点，$M_n(\widehat{\theta}_n) \ge M_n(\theta_*)$，于是
> $$M(\theta_*) - M(\widehat{\theta}_n) = \underbrace{\left[M_n(\widehat{\theta}_n) - M(\widehat{\theta}_n)\right]}_{\text{一致性控制}} + \underbrace{\left[M(\theta_*) - M_n(\theta_*)\right]}_{\to 0} \le 2\sup_\theta \lvert M_n(\theta) - M(\theta)\rvert \xrightarrow{P} 0$$
> 即 $M(\widehat{\theta}_n) \xrightarrow{P} M(\theta_*)$。任给 $\varepsilon > 0$，取 $\delta > 0$ 使 $\lvert\theta-\theta_*\rvert \ge \varepsilon$ 时 $M(\theta) \le M(\theta_*) - \delta$，则
> $$\mathbb{P}\left(\lvert\widehat{\theta}_n - \theta_*\rvert > \varepsilon\right) \le \mathbb{P}\left(M(\widehat{\theta}_n) < M(\theta_*) - \delta\right) \to 0$$
>
> ∎

注意（正则条件失效则结论失效，CMU L15 的例子）：取 $Y_{i1}, Y_{i2} \sim N(\mu_i, \sigma^2)$ 并强制 $\mu_1 = \mu_2$（参数落在更大家族的边界上），MLE 变成 $\widehat{\sigma}^2 = \frac{1}{4n}\sum_i (Y_{i1} - Y_{i2})^2$，期望只有真值的一半——**不相合**。同 p16 例 9.12 一样，这类反例都出在正则条件被破坏的地方。

## 4. 得分函数与 Fisher 信息

**定义 9.16（得分函数）**：

$$s(X;\theta) = \frac{\partial \log f(X;\theta)}{\partial \theta} \qquad (9.9)$$

**定义（Fisher 信息）**：

$$I_n(\theta) = \sum_{i=1}^n \mathbb{V}_\theta\left(s(X_i;\theta)\right) \qquad (9.10)$$

$n=1$ 时记 $I(\theta)$。

**引理 9.31**：$\mathbb{E}_\theta\left[s(X;\theta)\right] = 0$，从而 $\mathbb{V}_\theta(s) = \mathbb{E}_\theta(s^2)$。

> [!note]- 证明
> 归一化 $1 = \int f(x;\theta)\,dx$ 两边对 $\theta$ 求导（积分号下求导）：
> $$0 = \int \frac{\partial f(x;\theta)}{\partial\theta}dx = \int \frac{\partial f / \partial\theta}{f}\,f(x;\theta)\,dx = \int s(x;\theta)f(x;\theta)\,dx = \mathbb{E}_\theta\,s(X;\theta)$$
>
> ∎

**定理 9.17**：$I_n(\theta) = n\,I(\theta)$，且有第二种算法

$$I(\theta) = -\mathbb{E}_\theta\left(\frac{\partial^2 \log f(X;\theta)}{\partial\theta^2}\right) \qquad (9.11)$$

**动机（Fisher 信息在测什么）**：得分是"对数似然对 $\theta$ 的斜率"；在真值处斜率期望为零（引理 9.31），但它的**波动幅度**取决于数据对 $\theta$ 有多敏感——数据越能"暴露"参数（比如 $\sigma$ 越小、分布越尖），得分方差越大，Fisher 信息越大。期望为 0 意味着它是均值为零的噪声项，这正是 §5 证明里分子是 CLT 对象的原因。

## 5. 渐近正态与置信区间

**定理 9.18（MLE 的渐近正态）**：令 $\text{se} = \sqrt{\mathbb{V}(\widehat{\theta}_n)}$，在适当的正则条件下：

1. $\text{se} \approx \sqrt{1/I_n(\theta)}$ 且 $\dfrac{\widehat{\theta}_n - \theta}{\text{se}} \rightsquigarrow N(0,1)$；
2. 用估计值 $\widehat{\text{se}} = \sqrt{1/I_n(\widehat{\theta}_n)}$ 替换后 $\dfrac{\widehat{\theta}_n - \theta}{\widehat{\text{se}}} \rightsquigarrow N(0,1)$ 仍成立。

即 $\widehat{\theta}_n \approx N(\theta, \widehat{\text{se}}^2)$。

> [!note]- 证明思路（课本附录 9.13.1；每步用了哪个工具要认出来）
> **先展开**：MLE 是驻点，$\ell'(\widehat{\theta}) = 0$；在 $\theta$ 处一阶泰勒展开 $0 \approx \ell'(\theta) + (\widehat{\theta}-\theta)\ell''(\theta)$，整理得
> $$\sqrt{n}(\widehat{\theta} - \theta) = \frac{-\frac{1}{\sqrt{n}}\sum_i Y_i}{\frac{1}{n}\sum_i \Lambda_i} = \frac{\text{TOP}}{\text{BOTTOM}}$$
> 其中 $Y_i = \partial\log f(X_i;\theta)/\partial\theta$（即得分，期望 0、方差 $I(\theta)$），$\Lambda_i = -\partial^2 \log f(X_i;\theta)/\partial\theta^2$（期望 $I(\theta)$）。
> **再分而治之**：分子由 **CLT** 收敛到 $N(0, I(\theta))$；分母由**大数定律**收敛到 $I(\theta)$；两式相除由 **Slutsky**（定理 5.5(e)）得 $\sqrt{n}(\widehat{\theta}-\theta) \rightsquigarrow N(0, 1/I(\theta))$。
> **最后换掉真值**：$I(\theta)$ 连续时 $I(\widehat{\theta}) \xrightarrow{P} I(\theta)$，再用一次 Slutsky 得第 2 条。∎

**定理 9.19（渐近置信区间）**：令

$$C_n = \left(\widehat{\theta} - z_{\alpha/2}\,\widehat{\text{se}},\ \widehat{\theta} + z_{\alpha/2}\,\widehat{\text{se}}\right)$$

则 $\mathbb{P}_\theta(\theta \in C_n) \to 1 - \alpha$。

> [!note]- 证明
> 令 $Z \sim N(0,1)$：
> $$\mathbb{P}_\theta(\theta \in C_n) = \mathbb{P}_\theta\left(-z_{\alpha/2} \le \frac{\widehat{\theta} - \theta}{\widehat{\text{se}}} \le z_{\alpha/2}\right) \to \mathbb{P}(-z_{\alpha/2} < Z < z_{\alpha/2}) = 1-\alpha$$
> 第一步只是移项，第二步用定理 9.18 第 2 条。∎

$\alpha = 0.05$ 时 $z_{\alpha/2} = 1.96 \approx 2$，所以 $\widehat{\theta} \pm 2\widehat{\text{se}}$ 是常用的渐近 95% 置信区间——报纸上"民意测验精确到一个百分点、95% 正确"就是这个区间的白话版（置信区间的正确解读见 [[统计学完全教程/第6章 模型统计推断与学习/p15 第6章 模型统计推断与学习.md#5.2 置信区间的正确解释（课本重点纠错）|p15 §5.2]]，枢轴量的思想见 [[统计学完全教程/第6章 模型统计推断与学习/p15 第6章 模型统计推断与学习.md#5.3 基于正态的置信区间|p15 §5.3]]）。

三个标准例子（都从 $\ell''$ 出发，练"算 $I$"的手感）：

- **例 9.20（Bernoulli）**：$\ell''$ 路线给出 $I(p) = \dfrac{1}{p(1-p)}$，于是 $\widehat{\text{se}} = \left\{\dfrac{\widehat{p}(1-\widehat{p})}{n}\right\}^{1/2}$，95% 区间 $\widehat{p}_n \pm 2\sqrt{\widehat{p}_n(1-\widehat{p}_n)/n}$。
- **例 9.21（正态，$\sigma^2$ 已知）**：$s(X;\theta) = (X-\theta)/\sigma^2$，$s' = -1/\sigma^2$，$I(\theta) = 1/\sigma^2$；由定理 9.18 $\overline{X}_n \approx N(\theta, \sigma^2/n)$——本例正态近似**精确成立**而非渐近。
- **例 9.22（Poisson）**：$\widehat{\lambda} = \overline{X}_n$，$I(\lambda) = 1/\lambda$，$\widehat{\text{se}} = \sqrt{\widehat{\lambda}_n/n}$，$1-\alpha$ 区间 $\widehat{\lambda}_n \pm z_{\alpha/2}\sqrt{\widehat{\lambda}_n/n}$。

## 6. 最优性与渐近相对效率

**动机（一个具体比较）**：$X_1,\cdots,X_n \sim N(\theta,\sigma^2)$ 时 MLE 是 $\overline{X}_n$，另一个合理估计是样本中位数 $\widetilde{\theta}_n$。两者都相合，但

$$\sqrt{n}(\overline{X}_n - \theta) \rightsquigarrow N(0, \sigma^2), \qquad \sqrt{n}(\widetilde{\theta}_n - \theta) \rightsquigarrow N\left(0, \sigma^2\frac{\pi}{2}\right)$$

中位数收敛到正确的值，但方差比 MLE 大 $\pi/2 \approx 1.57$ 倍。

**概念（渐近相对效率）**：设两个估计量 $T_n, U_n$ 满足 $\sqrt{n}(T_n - \theta) \rightsquigarrow N(0,t^2)$、$\sqrt{n}(U_n - \theta) \rightsquigarrow N(0,u^2)$，定义

$$\text{ARE}(U, T) = \frac{t^2}{u^2}$$

即 $U$ 相对 $T$ 的**渐近相对效率**。正态例子里 $\text{ARE}(\text{中位数}, \text{MLE}) = 2/\pi \approx 0.64$：用中位数相当于只用了一小部分数据的信息。

**定理 9.23**：若 $\widehat{\theta}_n$ 是 MLE，$\widetilde{\theta}_n$ 是任何其他估计量，则（渐近意义下）

$$\mathbb{V}(\widetilde{\theta}_n) \ \gtrsim\ \mathbb{V}(\widehat{\theta}_n)$$

即 MLE 渐近方差最小，称 MLE **有效**（efficient）或**渐近最优**。

注意两条边界，都是考点：

- 这一切**以模型正确为前提**：模型错了 MLE 未必最优（本节例题 2 的 (e) 问就是模型错时估计量收敛到错误靶子的例子）；
- 定理的精确表述比"MLE 方差最小"微妙（课本脚注明说细节复杂），更一般的 optimality 理论在第 12 章决策论（对应 CMU 讲义 L14）。

## 7. Delta 方法

现在处理关注参数：$T = g(\theta)$，$g$ 光滑。MLE 的同变性（p16 定理 9.14）给出 $\widehat{T} = g(\widehat{\theta})$；问题变成：$\widehat{T}$ 的分布是什么？

**定理 9.24（Delta 方法）**：若 $g$ 可微且 $g'(\theta) \ne 0$，则

$$\frac{\widehat{T} - \tau}{\widehat{\text{se}}(\widehat{T})} \rightsquigarrow N(0,1), \qquad \widehat{\text{se}}(\widehat{T}) = \left\lvert g'(\widehat{\theta})\right\rvert \widehat{\text{se}} \qquad (9.15)$$

其中 $\tau = g(\theta)$。由此构造渐近 $1-\alpha$ 置信区间 $\widehat{T} \pm z_{\alpha/2}\,\widehat{\text{se}}(\widehat{T})$。

**思路**：对 $g$ 做一阶泰勒展开 $g(\widehat{\theta}) \approx g(\theta) + g'(\theta)(\widehat{\theta} - \theta)$——渐近正态的估计量乘常数、加常数后仍是渐近正态，方差按 $(g')^2$ 缩放。（单变量 Delta 方法的完整推导见 [[统计学完全教程/第5章 收敛与极限/p14 第5章 收敛（下）中心极限定理与Delta方法.md#4.1 单变量 Delta 方法|p14 §4.1]]，这里只是把它用到 MLE 上并配上 Fisher 信息。）

- **例 9.25（logit）**：$X_1,\cdots,X_n \sim \text{Bernoulli}(p)$，$\psi = g(p) = \log\frac{p}{1-p}$（对数几率）。$g'(p) = \frac{1}{p(1-p)}$，$\widehat{\psi} = \log\frac{\widehat{p}}{1-\widehat{p}}$，则 $\widehat{\text{se}}(\widehat{\psi}) = \frac{1}{\sqrt{n\,\widehat{p}(1-\widehat{p})}}$，95% 区间 $\widehat{\psi} \pm \dfrac{2}{\sqrt{n\widehat{p}(1-\widehat{p})}}$。
- **例 9.26（log 方差）**：$X_1,\cdots,X_n \sim N(\mu,\sigma^2)$，$\mu$ 已知。$\widehat{\sigma}^2 = \frac{1}{n}\sum(X_i-\mu)^2$，$I(\sigma) = 2/\sigma^2$（对 $\log f$ 求 $\sigma$ 的两阶导可得），$\widehat{\text{se}} = \sigma/\sqrt{2n}$。取 $\psi = g(\sigma) = \log\sigma$，$g' = 1/\sigma$，则 $\widehat{\text{se}}(\widehat{\psi}) = \frac{1}{\sqrt{2n}}$，95% 区间 $\widehat{\psi} \pm \frac{2}{\sqrt{2n}}$——区间长度与数据完全无关，因为对数刻度把尺度参数的误差"标准化"了。

## 8. 多参数模型

$\theta = (\theta_1,\cdots,\theta_k)$，$\widehat{\theta} = (\widehat{\theta}_1,\cdots,\widehat{\theta}_k)$ 为 MLE，$\ell_n(\theta) = \sum_i \log f(X_i;\theta)$。记 $H_{ij} = \partial^2 \log f / \partial\theta_i \partial\theta_j$，定义 **Fisher 信息矩阵**

$$I_n(\theta) = -\begin{pmatrix} \mathbb{E}_\theta(H_{11}) & \cdots & \mathbb{E}_\theta(H_{1k}) \\ \vdots & \ddots & \vdots \\ \mathbb{E}_\theta(H_{k1}) & \cdots & \mathbb{E}_\theta(H_{kk}) \end{pmatrix}$$

**定理 9.27**：正则条件下 $\widehat{\theta} \approx N(\theta, I_n(\theta)^{-1})$（即 $\sqrt{n}(\widehat{\theta}-\theta) \rightsquigarrow N(0, I(\theta)^{-1})$）。第 $j$ 个分量的标准误 $se_j = \sqrt{I_n^{-1}(j,j)}$（$I_n^{-1}$ 的第 $j$ 个对角元开方），近似协方差 $\text{Cov}(\widehat{\theta}_j, \widehat{\theta}_k) \approx I_n^{-1}(j,k)$。

注意：多参数情形方差和协方差**一起**由 $I_n^{-1}$ 给出——参数之间的相关性藏在矩阵的非对角元里，这是单参数公式 $\text{se} = 1/\sqrt{I_n}$ 的正确推广。

**定理 9.28（多参数 Delta 方法）**：设 $T = g(\theta_1,\cdots,\theta_k)$，梯度 $\nabla g = \left(\frac{\partial g}{\partial\theta_1},\cdots,\frac{\partial g}{\partial\theta_k}\right)^T$ 在 $\theta$ 处非零。$\widehat{T} = g(\widehat{\theta})$ 满足

$$\frac{\widehat{T} - \tau}{\widehat{\text{se}}(\widehat{T})} \rightsquigarrow N(0,1), \qquad \widehat{\text{se}}(\widehat{T}) = \sqrt{(\nabla g)^T\, I_n^{-1}(\widehat{\theta})\, \nabla g} \qquad (9.20)$$

（多变量 Delta 方法的一般形式见 [[统计学完全教程/第5章 收敛与极限/p14 第5章 收敛（下）中心极限定理与Delta方法.md#4.2 多变量 Delta 方法|p14 §4.2]]。）

**例 9.29（变异系数）**：$X_1,\cdots,X_n \sim N(\mu,\sigma^2)$，$T = g(\mu,\sigma) = \sigma/\mu$（课本把这题的 Fisher 信息矩阵留作习题 8）。推导：

> [!note]- 解答（自行推导，全链条可验证）
> 由 $\log f = -\log\sigma - \frac{(x-\mu)^2}{2\sigma^2} - \frac{1}{2}\log 2\pi$：
> $$I(\mu,\sigma) = \begin{pmatrix} 1/\sigma^2 & 0 \\ 0 & 2/\sigma^2 \end{pmatrix} \qquad\Longrightarrow\qquad I^{-1} = \begin{pmatrix} \sigma^2 & 0 \\ 0 & \sigma^2/2 \end{pmatrix}$$
> 梯度 $\nabla g = \left(-\dfrac{\sigma}{\mu^2},\ \dfrac{1}{\mu}\right)^T$，代入定理 9.28（多参数 Delta 用 $I_n^{-1} = I^{-1}/n$）：
> $$\text{se}(\widehat{\tau}) = \sqrt{\frac{1}{n}\left(\frac{\sigma^4}{\mu^4} + \frac{\sigma^2}{2\mu^2}\right)} = \frac{1}{\sqrt{n}}\sqrt{\tau^4 + \frac{\tau^2}{2}}, \qquad \tau = \frac{\sigma}{\mu}$$
> 标准误自己也是参数的函数——实操中代入 $\widehat{\mu},\widehat{\sigma}$。

## 9. 参数 Bootstrap

参数模型下，标准误与置信区间也可以用 Bootstrap 估计——唯一的改动是**抽样来源**：

| 方法 | 从哪里抽 |
|---|---|
| 非参数 Bootstrap（第 8 章，笔记未写） | 经验分布 $\widehat{F}_n$ |
| **参数 Bootstrap** | 模型密度 $f(x;\widehat{\theta}_n)$（$\widehat{\theta}_n$ 可取 MLE 或矩估计） |

**例 9.30（续例 9.29）**：求 $\tau = \sigma/\mu$ 的 Bootstrap 标准误：模拟 $X_1^*,\cdots,X_n^* \sim N(\widehat{\mu},\widehat{\sigma}^2)$，算 $\widehat{\mu}^* = n^{-1}\sum X_i^*$、$\widehat{\sigma}^{2*} = n^{-1}\sum(X_i^* - \widehat{\mu}^*)^2$、$\widehat{\tau}^* = \widehat{\sigma}^*/\widehat{\mu}^*$；重复 $B$ 次得 $\widehat{\tau}_1^*,\cdots,\widehat{\tau}_B^*$，取标准误

$$\text{se}_{boot} = \sqrt{\frac{1}{B}\sum_{b=1}^B\left(\widehat{\tau}_b^* - \frac{1}{B}\sum_{b'}\widehat{\tau}_{b'}^*\right)^2}$$

**两种方法的分工**（课本原话归纳）：Bootstrap 比 Delta 方法**容易得多**（不用手算梯度与信息矩阵）；Delta 方法的优势是给出**闭式表达式**，便于看误差如何随参数变化。两者互补，不是替代。

## 10. 检验假设条件

既然整套推断建立在"数据来自参数模型"上，就该检查这个假设。两条路：

- **非正式**：看图。直方图明显双峰，正态假设就该存疑；
- **正式**：拟合优度检验（goodness-of-fit test），见课本 10.5 节（第 10 章，对应 18.650 p07–p09 与 CMU 讲义 L16 尾–L18）。

## 11. 例题

**例 1（Uniform(0,θ) 的 MLE 相合性，课本习题 4）**
$X_1,\cdots,X_n \sim \text{Unif}(0,\theta)$，MLE $\widehat{\theta} = X_{(n)} = \max\{X_1,\cdots,X_n\}$。证明 $\widehat{\theta}$ 相合。

> [!note]- 解答
> 对任意 $\varepsilon > 0$（取 $0 < \varepsilon < \theta$）：
> $$\mathbb{P}\left(\lvert\widehat{\theta} - \theta\rvert > \varepsilon\right) = \mathbb{P}(X_{(n)} < \theta - \varepsilon) = \mathbb{P}(X_1 < \theta-\varepsilon, \cdots, X_n < \theta-\varepsilon) = \left(\frac{\theta-\varepsilon}{\theta}\right)^n \to 0$$
> 第二个等号用独立性、第三个等号用 $\mathbb{P}(X_i < c) = c/\theta$。结论：依概率收敛，$\widehat{\theta}$ 相合。
> 注意这是 p16 例 9.12 的续篇：正则条件失效的模型里 MLE 仍可能相合（定理 9.13 只是充分条件），但收敛**速度**变了——$((\theta-\varepsilon)/\theta)^n$ 是指数速度，比通常的 $1/\sqrt{n}$ 快得多，$\sqrt{n}(\widehat{\theta}-\theta)$ 的极限分布退化，定理 9.18 的正态近似在这里不成立。

**考点**：[[#3. MLE 的相合性|相合性]]、[[统计学完全教程/第5章 收敛与极限/p13 第5章 收敛（上）收敛类型与大数定律.md#2.1 依概率收敛|依概率收敛]]

**例 2（MLE vs 矩估计的效率对决，课本习题 6）**
$X_1,\cdots,X_n \sim N(\theta,1)$。令 $Y_i = \mathbb{1}(X_i > 0)$，$\psi = \mathbb{P}(Y_1 = 1)$。(a) 求 $\psi$ 的 MLE $\widehat{\psi}$ 及其 Delta 方法标准误；(b) $\widehat{\psi} = \frac{1}{n}\sum Y_i$ 也是相合估计，求渐近相对效率 $\text{ARE}(\widehat{\psi}, \widehat{\psi})$；(c) 若数据其实不正态，$\overline{\psi}$ 收敛到什么？

> [!note]- 解答
> (a) $\psi = \mathbb{P}(X > 0) = \Phi(\theta)$，由同变性 $\widehat{\psi} = \Phi(\overline{X}_n)$。Delta 方法：$g(\theta) = \Phi(\theta)$，$g'(\theta) = \phi(\theta)$（标准正态密度），$I(\theta) = 1$，故 $\text{se}(\widehat{\psi}) = \phi(\theta)/\sqrt{n}$，估计为 $\phi(\overline{X}_n)/\sqrt{n}$。
> (b) $\overline{\psi} = \frac{1}{n}\sum Y_i$ 是 IID 均值，CLT 给 $\sqrt{n}(\overline{\psi} - \psi) \rightsquigarrow N(0, \psi(1-\psi))$，即 $u^2 = \psi(1-\psi)$；而 MLE 的 $t^2 = \phi(\theta)^2$。于是
> $$\text{ARE}(\overline{\psi}, \widehat{\psi}) = \frac{\phi(\theta)^2}{\psi(1-\psi)}$$
> 在 $\theta = 0$ 处：$\psi = 1/2$，$\phi(0) = 1/\sqrt{2\pi}$，ARE $= \frac{1/(2\pi)}{1/4} = \frac{2}{\pi} \approx 0.64$——与中位数对 MLE 的效率比完全相同（$Y_i = \mathbb{1}(X_i>0)$ 恰是中位数的数据压缩版）。
> (c) 若 $X_i$ 的真实分布是 $F \ne N(\theta,1)$，则 $\widehat{\psi} = \Phi(\overline{X}_n)$ 收敛到 $\Phi(\mathbb{E}_F X)$，一般不等于真实的 $\mathbb{P}_F(X>0)$——**MLE 收敛到了错误的靶子**；而 $\overline{\psi}$ 由大数定律仍收敛到真实的 $\mathbb{P}_F(X>0)$。模型错了，"渐近最优"的 MLE 可以输给笨办法：定理 9.23 的前提是模型正确。

**考点**：[[#6. 最优性与渐近相对效率|ARE]]、[[#7. Delta 方法|Delta 方法]]、[[#5. 渐近正态与置信区间|渐近正态]]

**例 3（两处理的比较，课本习题 7）**
$n_1$ 人接受处理 1，$n_2$ 人接受处理 2；有效人数 $X_1 \sim \text{Bin}(n_1,p_1)$、$X_2 \sim \text{Bin}(n_2,p_2)$（独立）。$\psi = p_1 - p_2$。(a) 求 MLE；(b) 求 Fisher 信息矩阵；(c) 用多参数 Delta 方法求 $\widehat{\psi}$ 的渐近标准误；(d) $n_1 = n_2 = 200$、$X_1 = 160$、$X_2 = 148$，给出 90% 置信区间。

> [!note]- 解答
> (a) 同变性 + 各自的 MLE：$\widehat{p}_1 = X_1/n_1$、$\widehat{p}_2 = X_2/n_2$，$\widehat{\psi} = \widehat{p}_1 - \widehat{p}_2$。
> (b) 两组独立，对数似然可加，Fisher 信息矩阵是对角的：
> $$I(p_1,p_2) = \begin{pmatrix} \dfrac{n_1}{p_1(1-p_1)} & 0 \\ 0 & \dfrac{n_2}{p_2(1-p_2)} \end{pmatrix} \qquad\Longrightarrow\qquad I^{-1} = \begin{pmatrix} \dfrac{p_1(1-p_1)}{n_1} & 0 \\ 0 & \dfrac{p_2(1-p_2)}{n_2} \end{pmatrix}$$
> (c) $\nabla g = (1, -1)^T$，代入定理 9.28：
> $$\text{se}(\widehat{\psi}) = \sqrt{\frac{p_1(1-p_1)}{n_1} + \frac{p_2(1-p_2)}{n_2}}$$
> (d) $\widehat{p}_1 = 0.8$、$\widehat{p}_2 = 0.74$、$\widehat{\psi} = 0.06$；$\text{se} = \sqrt{0.0008 + 0.000962} \approx 0.042$。$z_{0.05} = 1.645$，90% 区间
> $$0.06 \pm 1.645 \times 0.042 = 0.06 \pm 0.069 \approx (-0.01,\ 0.13)$$
> 区间包含 0——在这个置信水平下没有证据表明两种处理有效比例不同。

**考点**：[[#8. 多参数模型|Fisher 信息矩阵]]、[[#8. 多参数模型|多参数 Delta 方法]]、[[#5. 渐近正态与置信区间|渐近置信区间]]

**例 4（三种方法估同一个标准误，课本习题 9 的骨架）**
$X_1,\cdots,X_n \sim N(\mu,1)$，$T = e^\mu$。比较 Delta 方法、参数 Bootstrap、非参数 Bootstrap 三条路给 $\widehat{T} = e^{\overline{X}}$ 配标准误。

> [!note]- 解答
> - **Delta 方法**：$g'(\mu) = e^\mu$，$I(\mu) = 1$，$\text{se}(\widehat{T}) = e^\mu/\sqrt{n}$，代入 $\widehat{\mu}$ 得 $e^{\overline{X}}/\sqrt{n}$——闭式，一步出；
> - **参数 Bootstrap**：从 $N(\widehat{\mu},1)$ 抽 $B$ 组样本，每组算 $\widehat{T}^* = e^{\overline{X}^*}$，取标准差；
> - **非参数 Bootstrap**：从经验分布 $\widehat{F}_n$（即对原数据有放回重抽）做同样的事。
> 三者在大样本下应给出接近的答案；课本这题还要求把 Bootstrap 直方图与真实抽样分布（模拟获得）叠着比——教材的结论方向是 Bootstrap 直方图通常比单一的正态近似更贴近真实分布，代价是计算量。

**考点**：[[#7. Delta 方法|Delta 方法]]、[[#9. 参数 Bootstrap|参数 Bootstrap]]、[[统计学完全教程/第9章 参数推断/p16 第9章 参数推断（一）矩估计与极大似然.md#5.2 同变性|同变性]]

## 12. 本节重点

> **本节重点**：
> - 相合性证明的主线：最大化 $\ell_n$ ⟺ 最大化 $M_n$，LLN 把 $M_n$ 压到 $-D(\theta_*,\theta)$，可识别性保证最大点唯一，一致收敛堵住"窄缝溜走"；正则条件失效（支撑依赖参数、参数在边界上）时不相合。
> - 得分函数期望为 0（归一化求导）；Fisher 信息 = 得分的方差 = $-\mathbb{E}(\ell'')$，衡量数据暴露参数的能力；$I_n = nI$。
> - 渐近正态的证明 = 分子 CLT + 分母 LLN + Slutsky；由此得 $\widehat{\theta} \pm z_{\alpha/2}\widehat{\text{se}}$，$\widehat{\text{se}} = 1/\sqrt{nI(\widehat{\theta})}$。
> - MLE 渐近有效（方差最小），但**以模型正确为前提**；ARE 量化两个相合估计量的效率差（中位数 vs 均值是 $2/\pi$）。
> - 关注参数 $T = g(\theta)$：同变性给点估计，Delta 方法给标准误 $\lvert g'(\widehat{\theta})\rvert\,\widehat{\text{se}}$；多参数版本 $I_n^{-1}$ 整矩阵进公式。
> - 参数 Bootstrap 从 $f(x;\widehat{\theta})$ 抽样（非参数版从 $\widehat{F}_n$ 抽）；Bootstrap 易算、Delta 有闭式，互补使用。
> - **常见坑**：忘给 ARE 写前提（模型正确）；多参数时只取 $I_n^{-1}$ 对角元而忽略协方差；对正则条件失效的模型（Uniform、边界参数）硬套定理 9.18 的正态近似。

---
