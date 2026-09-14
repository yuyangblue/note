# 教材补充：MLE 的渐近理论与充分统计量（对应教材第9章）

> 来源：《统计学完全教程》(All of Statistics, L. Wasserman) 第9章。
> 对应笔记：第7章 参数估计（p49-p56）。
> 定位：笔记讲矩估计、MLE、无偏性/有效性/相合性、区间估计的**计算**；本节补教材的核心增量——**Fisher 信息、MLE 的渐近正态与最优性、Delta 方法（参数版）、多参数模型、充分统计量与指数族**。这些是"为什么 MLE 好"的理论依据。

## 目录

- [一、 参数兴趣与烦扰参数](#一参数兴趣与烦扰参数)
- [二、 MLE 的五个基本性质](#二mle-的五个基本性质)
- [三、 Score 函数与 Fisher 信息](#三score-函数与-fisher-信息)
- [四、 MLE 的渐近正态性（核心定理）](#四mle-的渐近正态性核心定理)
- [五、 MLE 的最优性：效率与 ARE](#五mle-的最优性效率与-are)
- [六、 Delta 方法（参数推断版）](#六delta-方法参数推断版)
- [七、 多参数模型：Fisher 信息矩阵](#七多参数模型fisher-信息矩阵)
- [八、 参数 Bootstrap](#八参数-bootstrap)
- [九、 充分统计量：因子分解与 Rao-Blackwell](#九充分统计量因子分解与-rao-blackwell)
- [十、 指数族](#十指数族)
- [十一、 数值求 MLE：Newton-Raphson 与 EM](#十一数值求-mlenewton-raphson-与-em)
- [本节重点](#本节重点)

---

## 一、 参数兴趣与烦扰参数

$\theta=(\theta_1,\dots,\theta_k)$，若只关心某个函数 $T(\theta)$，则 $T(\theta)$ 叫**参数兴趣**，其余是**烦扰参数**。
例：$X\sim N(\mu,\sigma^2)$，关心"超过1的人口比例" $T=\mathbb P(X>1)=1-\Phi\!\left(\frac{1-\mu}{\sigma}\right)$——是 $(\mu,\sigma)$ 的复合函数。

## 二、 MLE 的五个基本性质

设 $\theta^*$ 为真值，$\hat\theta_n$ 为 MLE（假设正则条件——$f(x;\theta)$ 的光滑性条件成立）：

1. **一致**：$\hat\theta_n\xrightarrow{p}\theta^*$；
2. **等变（equivariant）**：$g(\hat\theta_n)$ 是 $g(\theta)$ 的 MLE（定理9.14：MLE 与变换可交换）；
3. **渐近正态**：$(\hat\theta_n-\theta^*)/\widehat{\text{se}}\leadsto N(0,1)$；
4. **渐近最优（有效）**：所有"良态"估计量中 MLE 渐近方差最小；
5. 近似 Bayes 估计（第11章）。

> 注意：这些性质只在**模型假设正确**时成立；模型错了 MLE 可能很差。正则条件破坏时（如 Uniform$(0,\theta)$ 支撑依赖参数）部分性质仍成立但推导不同。

## 三、 Score 函数与 Fisher 信息

**Score 函数**：
$$s(X;\theta)=\frac{\partial}{\partial\theta}\log f(X;\theta)$$
**性质（引理9.31）**：$\mathbb E_\theta\big(s(X;\theta)\big)=0$（对 $\int f=1$ 两边求导）。

**Fisher 信息**：
$$I_n(\theta)=\sum_{i=1}^{n}V_\theta\big(s(X_i;\theta)\big)=nI(\theta)$$
且有简便公式（二阶导）：
$$I(\theta)=-\mathbb E_\theta\!\left(\frac{\partial^2}{\partial\theta^2}\log f(X;\theta)\right)$$
**直觉**：对数似然在真值处的"曲率"越大，参数越容易被数据锁定，信息越多、方差越小。

**例**：Bernoulli——$s=\frac{x-p}{p}-\frac{1-x}{1-p}$，$I(p)=\frac1{p(1-p)}$；Poisson——$I(\lambda)=1/\lambda$；$N(\theta,\sigma^2)$（$\sigma^2$ 已知）——$I(\theta)=1/\sigma^2$。

## 四、 MLE 的渐近正态性（核心定理）

**定理 9.18（MLE 渐近正态）**：
$$\frac{\hat\theta_n-\theta}{\text{se}}\leadsto N(0,1),\qquad \text{se}=\frac{1}{\sqrt{nI(\theta)}}$$
且把 $\text{se}$ 换成**估计标准误** $\widehat{\text{se}}=\frac{1}{\sqrt{nI(\hat\theta_n)}}$ 结论仍成立。

**推论（MLE 置信区间，定理9.19）**：
$$C_n=\Big(\hat\theta_n\pm z_{\alpha/2}\,\widehat{\text{se}}\Big),\qquad \mathbb P_\theta(\theta\in C_n)\to1-\alpha$$
95% 区间即 $\hat\theta\pm2\widehat{\text{se}}$（民意调查"±2个点"的来源）。

**例（Bernoulli）**：$\hat p=\bar X_n$，$\widehat{\text{se}}=\sqrt{\frac{\hat p(1-\hat p)}{n}}$，区间 $\hat p\pm z_{\alpha/2}\sqrt{\hat p(1-\hat p)/n}$。

**证明骨架（附录）**：score 展开 + CLT + 大数定律：
$$\sqrt n(\hat\theta-\theta)=\frac{n^{-1/2}\sum s(X_i;\theta)}{-n^{-1}\sum \frac{\partial^2}{\partial\theta^2}\log f(X_i;\theta)}\leadsto\frac{N(0,I(\theta))}{I(\theta)}=N\!\left(0,\frac1{I(\theta)}\right)$$

## 五、 MLE 的最优性：效率与 ARE

**渐近相对效率（ARE）**：两个估计量 $T_n,U_n$ 满足 $\sqrt n(T_n-\theta)\leadsto N(0,t^2)$、$\sqrt n(U_n-\theta)\leadsto N(0,u^2)$，则
$$\text{ARE}(U,T)=\frac{t^2}{u^2}$$
**例**：$N(\theta,\sigma^2)$ 中 MLE $\bar X$ 与样本中位数的 ARE：$\text{ARE}(\hat\theta_{\text{med}},\bar X)=\frac{2}{\pi}\approx0.63$——**用中位数等于只用约 63% 的数据**。

**定理 9.23**：MLE 在所有良态估计量中渐近方差最小（**有效/渐近最优**）。证明框架是 Cramér–Rao 下界：$V(\hat\theta)\ge\frac1{nI(\theta)}$，MLE 渐近达到下界。

> 代价：最优性依赖模型正确。第12章决策理论再一般化。

## 六、 Delta 方法（参数推断版）

**定理 9.24**：$T=g(\theta)$（$g$ 可导，$g'(\theta)\ne0$），则 $g(\hat\theta_n)$ 是 $T$ 的 MLE 且
$$\sqrt n\big(g(\hat\theta_n)-g(\theta)\big)\leadsto N\!\left(0,\ \frac{[g'(\theta)]^2}{I(\theta)}\right)$$
置信区间：$g(\hat\theta_n)\pm z_{\alpha/2}\,\widehat{\text{se}}$，其中 $\widehat{\text{se}}=\frac{|g'(\hat\theta_n)|}{\sqrt{nI(\hat\theta_n)}}$。

**例（logit）**：$\psi=\log\frac{p}{1-p}$，$g'(p)=\frac1{p(1-p)}$，$\widehat{\text{se}}(\hat\psi)=\frac1{\sqrt{n\hat p(1-\hat p)}}\cdot\frac{1}{\hat p(1-\hat p)}\cdot$…（照公式代）。
**例（log σ）**：$N(\mu,\sigma^2)$，$\mu$ 已知，$\psi=\log\sigma$：$\hat\psi=\log\hat\sigma_n$，$\widehat{\text{se}}=1/\sqrt{2n}$，95% 区间 $\hat\psi\pm2/\sqrt{2n}$。

## 七、 多参数模型：Fisher 信息矩阵

$\theta=(\theta_1,\dots,\theta_k)$，**Fisher 信息矩阵**：
$$I_n(\theta)=-\mathbb E_\theta[H],\qquad H_{jk}=\frac{\partial^2}{\partial\theta_j\partial\theta_k}\log f(X;\theta)$$
**定理 9.27**：
$$\hat\theta_n\approx N\!\big(\theta,\ I_n^{-1}(\hat\theta_n)\big)$$
- $\widehat{\text{se}}_j=\sqrt{\text{对角元 }[I_n^{-1}]_{jj}}$；
- $\widehat{\text{Cov}}(\hat\theta_j,\hat\theta_k)\approx[I_n^{-1}]_{jk}$。

**多元 Delta 方法（定理9.28）**：$T=g(\theta)$，梯度 $\nabla g$，则
$$\widehat{\text{se}}(g(\hat\theta))=\sqrt{(\nabla g)^{\mathsf T}\,\hat I_n^{-1}\,(\nabla g)}$$
**例**：$N(\mu,\sigma^2)$，$T=\sigma/\mu$：$\widehat{\text{se}}=\sqrt{\frac{\hat\sigma^2}{n\hat\mu^2}+\frac{\hat\sigma^4}{2n\hat\mu^4}}$（梯度代入）。

## 八、 参数 Bootstrap

与非参数 Bootstrap 唯一区别：**从 $f(x;\hat\theta_n)$ 抽样**（而非从 $\widehat F_n$），$\hat\theta_n$ 用 MLE 或矩估计。
优点：比 Delta 方法省事；缺点：没有解析公式。例：$\hat\psi=\hat\sigma/\hat\mu$ 的标准误可直接模拟。

> 习题10的深刻对比：$\text{Uniform}(0,\theta)$ 中 $\hat\theta=X_{(n)}$，参数 Bootstrap 的 $P(\hat\theta^*=\hat\theta)=0$，而非参数 Bootstrap $P(\hat\theta^*=\hat\theta)=1-(1-1/n)^n\approx0.632$——**非参数 Bootstrap 对"极值型"估计量失效**（重抽样样本最大值几乎必等于原样本最大值）。

## 九、 充分统计量：因子分解与 Rao-Blackwell

**定义（两种等价的）**：
- 教材版本：若 $\frac{f(x^n;\theta)}{f(y^n;\theta)}=c$（与 $\theta$ 无关）当且仅当 $T(x^n)=T(y^n)$，则 $T$ 充分；
- 常用版本：**给定 $T=t$ 时数据分布与 $\theta$ 无关**。

**因子分解定理（定理9.40，最实用）**：
$$T\ \text{充分}\iff f(x^n;\theta)=g\big(T(x^n),\theta\big)\,h(x^n)$$
即：联合密度能拆成"只含 $T$ 和 $\theta$ 的部分"×"与 $\theta$ 无关的部分"。

**例**：Bernoulli：$T=\sum X_i$ 充分（$f=p^T(1-p)^{n-T}$）；$N(\mu,\sigma^2)$：$T=(\bar X,S)$ 最小充分；Poisson：$T=\sum X_i$。$T=X_1$ 不充分；$(\sum X_i,X_1)$ 充分但不最小。

**Rao–Blackwell 定理（定理9.42）**：$\hat\theta$ 是估计量、$T$ 充分，则
$$\tilde\theta=\mathbb E(\hat\theta|T)\ \text{的 MSE 不比 }\hat\theta\ \text{大}$$
即**好估计应只依赖充分统计量**。例：$\hat\theta=X_1$ 改进为 $\tilde\theta=\frac1n\sum X_i$。

## 十、 指数族

**单参数指数族**：
$$f(x;\theta)=h(x)\,e^{\eta(\theta)T(x)-B(\theta)}$$
- $T(X)$ 是**自然充分统计量**；样本时 $\sum_iT(X_i)$ 充分；
- 改写为自然参数形式：$f(x;\eta)=h(x)e^{\eta T(x)-A(\eta)}$；
- **矩生成**：$\mathbb E(T(X))=A'(\eta)$，$V(T(X))=A''(\eta)$。

**覆盖的分布**：Poisson（$\eta=\log\theta$）、Binomial、Bernoulli、正态、Gamma——都是指数族；**Uniform$(0,\theta)$ 不是指数族**（$T=X_{(n)}\ne\sum T(X_i)$，支撑依赖参数）。

## 十一、 数值求 MLE：Newton-Raphson 与 EM

- **Newton–Raphson**：$\theta_{j+1}=\theta_j-\ell'(\theta_j)/\ell''(\theta_j)$（多元：$\theta_{j+1}=\theta_j-H^{-1}\nabla\ell$）。初值常用矩估计。
- **EM 算法（期望最大化）**：似然难最大化，但引入**隐变量/缺失数据** $Z$ 后完整数据似然易最大化：
  - E 步：计算 $Q(\theta|\theta^j)=\mathbb E\big(\log f(y^n,z^n;\theta)\big|y^n,\theta^j\big)$；
  - M 步：$\theta^{j+1}=\arg\max_\theta Q(\theta|\theta^j)$。
  - 性质：每次迭代似然不降（$\ell(\theta^{j+1})\ge\ell(\theta^j)$，用 KL 距离证明）。
  - **例（两正态混合）**：$f(y)=\frac12\phi(y;\mu_0,1)+\frac12\phi(y;\mu_1,1)$。E 步算 $\tau_i=\mathbb P(Z_i=1|y^n,\theta^j)=\frac{\phi(y_i;\mu_1^j,1)}{\phi(y_i;\mu_1^j,1)+\phi(y_i;\mu_0^j,1)}$；M 步 $\mu_0^{j+1}=\frac{\sum(1-\tau_i)y_i}{\sum(1-\tau_i)}$、$\mu_1^{j+1}=\frac{\sum\tau_i y_i}{\sum\tau_i}$。

---

## 本节重点

> - **Fisher 信息** $I(\theta)=-E[\partial^2\log f/\partial\theta^2]$；$I_n=nI$。
> - **MLE 渐近正态**：$\hat\theta\approx N(\theta,1/[nI(\theta)])$；区间 $\hat\theta\pm z_{\alpha/2}\widehat{\text{se}}$。
> - **MLE 最优**：方差达 Cramér–Rao 下界；ARE 例：中位数/均值 $=2/\pi\approx0.63$。
> - **等变性**：$g(\hat\theta)$ 是 $g(\theta)$ 的 MLE。
> - **Delta 方法**：$\widehat{\text{se}}(g(\hat\theta))=\frac{|g'(\hat\theta)|}{\sqrt{nI(\hat\theta)}}$；多元用梯度+信息矩阵。
> - **参数 Bootstrap**：从 $f(x;\hat\theta)$ 重抽样；对极值统计量，非参数 Bootstrap 失效（$P(\hat\theta^*=\hat\theta)\approx0.632$）。
> - **充分统计量**：因子分解定理；Rao–Blackwell：$E(\hat\theta|T)$ 不增 MSE。
> - **指数族**：$f=h\,e^{\eta T-B}$，$E(T)=A'(\eta)$；Bernoulli/二项/Poisson/正态/Gamma 都是，Uniform$(0,\theta)$ 不是。
> - **EM**：E 步算隐变量后验，M 步最大化完整似然；似然单调不降。
