# 教材补充：检验的幂、p 值与现代检验方法（对应教材第10章）

> 来源：《统计学完全教程》(All of Statistics, L. Wasserman) 第10章。
> 对应笔记：第8章 假设检验（p57-p65）。
> 定位：笔记讲假设检验的概念、两类错误、U/t/χ²/F 检验的**操作**；本节补教材的**形式化体系（power、size、level）、p 值的严格定义与 Uniform 性质、Wald 检验、Pearson χ²、置换检验、似然比检验、多重检验（Bonferroni/FDR）**——特别是**置换检验和 FDR** 是笔记完全没有的现代工具。

## 目录

- [一、 形式化：拒绝域、power、size](#一形式化拒绝域powersize)
- [二、 Wald 检验：最通用的渐近检验](#二wald-检验最通用的渐近检验)
- [三、 检验 ⟺ 置信区间；统计显著 ≠ 科学显著](#三检验--置信区间统计显著--科学显著)
- [四、 p 值的严格定义与 Uniform(0,1) 性质](#四p-值的严格定义与-uniform01-性质)
- [五、 Pearson χ² 检验（多项数据）](#五pearson-χ²-检验多项数据)
- [六、 置换检验（非参数、精确）](#六置换检验非参数精确)
- [七、 似然比检验 LRT](#七似然比检验-lrt)
- [八、 多重检验：Bonferroni 与 FDR](#八多重检验bonferroni-与-fdr)
- [九、 拟合优度检验](#九拟合优度检验)
- [十、 附录：Neyman-Pearson 引理与 t 检验](#十附录neyman-pearson-引理与-t-检验)
- [本节重点](#本节重点)

---

## 一、 形式化：拒绝域、power、size

把参数空间分成 $\Theta_0$ 与 $\Theta_1$，检验 $H_0:\theta\in\Theta_0$ vs $H_1:\theta\in\Theta_1$。

- **拒绝域** $R\subset\mathcal X$：$X\in R$ 拒绝 $H_0$；通常 $R=\{X:\ T(X)>c\}$（$T$ 检验统计量、$c$ 临界值）。
- **两类错误**：$H_0$ 真却拒绝 = **I 型错误**；$H_1$ 真却保留 = **II 型错误**。
- **Power 函数**：$\beta(\theta)=\mathbb P_\theta(X\in R)$（每个 $\theta$ 下拒绝的概率）。
- **Size（显著性水平）**：$\alpha=\sup_{\theta\in\Theta_0}\beta(\theta)$——$H_0$ 内最大的 I 型错误概率；size ≤ α 的检验称 **level α** 检验。
- **简单假设**（$\theta=\theta_0$）vs **复合假设**（$\theta>\theta_0$ 等）；单侧/双侧检验。

**例**：$X_1,\dots,X_n\sim N(\mu,\sigma^2)$，$\sigma$ 已知，$H_0:\mu\le0$ vs $H_1:\mu>0$，拒绝域 $\bar X>c$。Power 函数 $\beta(\mu)=1-\Phi\!\left(\frac{\sqrt n(c-\mu)}{\sigma}\right)$ 随 $\mu$ 递增，size=$\beta(0)$，令其等于 $\alpha$ 解得 $c=\frac{\sigma\Phi^{-1}(1-\alpha)}{\sqrt n}$——即拒绝 $\sqrt n(\bar X-0)/\sigma>z_\alpha$。

## 二、 Wald 检验：最通用的渐近检验

**定义（Wald 检验）**：$\hat\theta$ 是 $\theta$ 的估计、$\widehat{\text{se}}$ 是估计标准误，检验 $H_0:\theta=\theta_0$ vs $H_1:\theta\ne\theta_0$：
$$W=\frac{\hat\theta-\theta_0}{\widehat{\text{se}}},\qquad \text{拒绝 } H_0\iff |W|>z_{\alpha/2}$$
**定理 10.4**：渐近下 Wald 检验的 size 恰为 $\alpha$（因为 $H_0$ 下 $W\leadsto N(0,1)$）。

**Power（定理 10.6）**：真值 $\theta^*\ne\theta_0$ 时，
$$\beta(\theta^*)\approx1-\Phi\!\left(\frac{\theta_0-\theta^*}{\text{se}}+z_{\alpha/2}\right)+\Phi\!\left(\frac{\theta_0-\theta^*}{\text{se}}-z_{\alpha/2}\right)$$
两因素：$\theta^*$ 离 $\theta_0$ 越远 power 越大；样本量越大（se 越小）power 越大。

**典型应用（都只需 plug-in 估计 + 标准误）**：
- **两比例**：$X\sim\text{Binomial}(m,p_1)$、$Y\sim\text{Binomial}(n,p_2)$，$\hat\delta=\hat p_1-\hat p_2$，$\widehat{\text{se}}=\sqrt{\frac{\hat p_1(1-\hat p_1)}{m}+\frac{\hat p_2(1-\hat p_2)}{n}}$；
- **配对比较（paired）**：$D_i=X_i-Y_i$（同一测试集），$\hat\delta=\bar D$，$\widehat{\text{se}}=S_D/\sqrt n$；
- **两均值**：$\hat\delta=\bar X-\bar Y$，$\widehat{\text{se}}=\sqrt{S_1^2/m+S_2^2/n}$；
- **两中位数**：标准误用 Bootstrap 求（第8章）。

> Wald 检验把"检验"问题统一成了"估计+标准误"问题——凡是能算 $\hat\theta\pm\widehat{\text{se}}$ 的都能检验。

## 三、 检验 ⟺ 置信区间；统计显著 ≠ 科学显著

**定理 10.10**：size α 的 Wald 检验拒绝 $H_0:\theta=\theta_0$ **当且仅当** $\theta_0\notin C=(\hat\theta-z_{\alpha/2}\widehat{\text{se}},\ \hat\theta+z_{\alpha/2}\widehat{\text{se}})$。

**重要警示**：
1. **统计显著 ≠ 科学/实际显著**——大样本下很小的效应也会"显著"；
2. **置信区间比检验信息量大**（既看是否含 $\theta_0$，也看区间离 $\theta_0$ 多远）；
3. 教材建议：**只在有明确假设要检验时才用检验**，很多时候估计+置信区间更合适。

## 四、 p 值的严格定义与 Uniform(0,1) 性质

**定义（定理 10.12）**：若检验形式为"$T(X^n)\ge c_\alpha$ 时拒绝"，则
$$p\text{-value}=\sup_{\theta\in\Theta_0}\mathbb P_\theta\big(T(X^n)\ge T(x^n)\big)$$
简单 $H_0:\theta=\theta_0$ 时即 $p=\mathbb P_{\theta_0}(T\ge t_{\rm obs})$。口语化：**p 值是 $H_0$ 下观测到"与当前一样或更极端"统计量的概率**。

**Wald 检验的 p 值**：$p=\mathbb P_{\theta_0}(|W|>|w|)\approx2\Phi(-|w|)$（$w$ 为观测值）。

**定理 10.14（重要性质）**：若检验统计量连续，则 $H_0$ 下 **p 值 ~ Uniform(0,1)**。因此：$H_0$ 真时 p 值像均匀随机数；$H_1$ 真时 p 值分布向 0 集中。也正因如此，拒绝 $p<\alpha$ 的 I 型错误率恰为 $\alpha$。

**两个警示**：
1. 大 p 值**不是** $H_0$ 成立的强证据——可能只是检验 power 低；
2. **p 值不是 $\mathbb P(H_0|\text{data})$**（那是贝叶斯量，第11章）。

## 五、 Pearson χ² 检验（多项数据）

$X=(X_1,\dots,X_k)\sim\text{Multinomial}(n,p)$，检验 $H_0:p=p_0$：
$$T=\sum_{j=1}^{k}\frac{(X_j-np_{0j})^2}{np_{0j}}=\sum_{j=1}^{k}\frac{(X_j-E_j)^2}{E_j}$$
**定理 10.17**：$H_0$ 下 $T\leadsto\chi^2_{k-1}$，拒绝 $T>\chi^2_{k-1,\alpha}$，$p=\mathbb P(\chi^2_{k-1}>t)$。

**例（孟德尔豌豆）**：$n=556$，$p_0=(9/16,3/16,3/16,1/16)$，观测 $(315,101,108,32)$：$T=0.47<\chi^2_{3,0.05}=7.815$，$p=0.93$——不拒绝（数据不违背孟德尔理论）。

## 六、 置换检验（非参数、精确）

两独立样本 $X_1,\dots,X_m\sim F_X$、$Y_1,\dots,Y_n\sim F_Y$，检验 $H_0:F_X=F_Y$。**不需要大样本理论，精确**。

**原理**：$H_0$ 下，给定数据值的顺序，观测被均匀随机地分配给两组——所以**把所有 $N!$ 种置换都试一遍，每种等可能**。置换分布：$\mathbb P_0(T=t_j)=1/N!$。

**p 值**：$p=\mathbb P_0(T>t_{\rm obs})=\frac1{N!}\sum_j I(T_j>t_{\rm obs})$（$T$ 大拒绝时）。

**算法**：① 算观测统计量 $t_{\rm obs}$；② 随机打乱数据算 $T$；③ 重复 $B$ 次；④ $p=\frac{\#\{T_j\ge t_{\rm obs}\}}{B}$。

**例**：数据 $(1,9,3)$，$T=|\bar X-\bar Y|=2$，6 种置换给 $\{2,2,7,7,5,5\}$，$p=4/6$。

> 大样本下与渐近检验结论接近；**小样本时最有用**（如基因表达数据 2,638 个基因逐个检验中位数组间差异，$p=0.045$）。

## 七、 似然比检验 LRT

检验 $H_0:\theta\in\Theta_0$ vs $H_1:\theta\notin\Theta_0$，统计量
$$\Lambda=2\log\frac{\sup_{\theta\in\Theta}\ell(\theta)}{\sup_{\theta\in\Theta_0}\ell(\theta)}=2\log\frac{\ell(\hat\theta)}{\ell(\hat\theta_0)}$$
（$\hat\theta$ 无约束 MLE，$\hat\theta_0$ 限制在 $\Theta_0$ 内的 MLE。）

**定理 10.22**：$H_0$ 下 $\Lambda\leadsto\chi^2_{r-q}$，自由度 $r-q$ = **全参数空间维数 − 限制空间维数**。

**例（孟德尔豌豆，LRT 版）**：$\Lambda=2\sum_jX_j\log(\hat p_j/p_{0j})=0.48$，自由度为 $3-0=3$，$p=\mathbb P(\chi^2_3>0.48)=0.92$——与 Pearson χ² 结论一致（大样本下两者通常相近）。

## 八、 多重检验：Bonferroni 与 FDR

做 $m$ 个检验（如 2,638 个基因），各以 level $\alpha$ 检验 → **至少一个假阳性的概率远超 $\alpha$**（多重检验问题）。

**Bonferroni 法**：$p_i<\alpha/m$ 才拒绝 $H_{0i}$。定理 10.24：假阳性总数概率 ≤ $\alpha$。缺点：**保守**（例：$\alpha=0.05$，$m=2638$ 时阈值 $0.05/2638=1.9\times10^{-5}$）。

**FDR（Benjamini–Hochberg，1995）**：控制**错误发现率**——被拒绝中"假阳性比例"的期望 $\text{FDR}=\mathbb E(\text{FDP})\le\alpha$。

**BH 算法**：
1. 排序 p 值 $p_{(1)}\le\cdots\le p_{(m)}$；
2. 找最大 $i$ 使 $p_{(i)}\le\frac{i\alpha}{m}$（独立时系数 $c_m=1$；一般 $c_m=\sum_{j=1}^m\frac1j$）；
3. 阈值 $T=p_{(\hat i)}$，拒绝所有 $p_i\le T$。

**例**：10 个检验 p 值有序，$\alpha=0.05$：Bonferroni 阈值 $0.005$ 拒绝前 2 个；BH 找到 $i=5$（$p_{(5)}=0.0122\le5\times0.005=0.025$）拒绝前 5 个。

## 九、 拟合优度检验

检验数据是否来自参数模型 $\mathcal F=\{f(x;\theta)\}$：把实轴分成 $k$ 个区间，$p_j(\theta)=\int_{I_j}f$，用多项似然估计 $\hat\theta$，统计量
$$Q=\sum_{j=1}^{k}\frac{(N_j-n\hat p_j)^2}{n\hat p_j}\leadsto\chi^2_{k-1-s}\quad(\text{自由度=区间数−参数数−1})$$
警示：不拒绝 ≠ 模型正确（可能 power 不够）；不能把 $\hat\theta$ 换成 MLE 直接套 $\chi^2_{k-1}$（Chernoff–Lehmann，1954）。

## 十、 附录：Neyman-Pearson 引理与 t 检验

**Neyman–Pearson 引理（简单对简单）**：$H_0:\theta=\theta_0$ vs $H_1:\theta=\theta_1$，似然比
$$T=\frac{\ell(\theta_1)}{\ell(\theta_0)}=\frac{\prod f(x_i;\theta_1)}{\prod f(x_i;\theta_0)}$$
取临界值 $k$ 使 $\mathbb P_{\theta_0}(T>k)=\alpha$，则该检验是**所有 size α 检验中 power 最大**的（最优势检验）。这是 LRT 的理论源头。

**t 检验（附录）**：$X_1,\dots,X_n\sim N(\mu,\sigma^2)$（$\mu,\sigma$ 均未知），$H_0:\mu=\mu_0$：
$$T=\frac{\sqrt n(\bar X_n-\mu_0)}{S_n}\ \text{在 }H_0\text{ 下精确服从 }t_{n-1}$$
拒绝 $|T|>t_{n-1,\alpha/2}$。大样本时 $t_{n-1}\approx N(0,1)$，与 Wald 检验基本一致；小样本且正态假设成立时用 t 更准。

---

## 本节重点

> - **power/size/level**：$\beta(\theta)=P_\theta(\text{拒绝})$；$\alpha=\sup_{\Theta_0}\beta$。
> - **Wald 检验**：$W=(\hat\theta-\theta_0)/\widehat{\text{se}}$，拒绝 $|W|>z_{\alpha/2}$——估计+标准误即可检验（两比例/配对/两均值/两中位数）。
> - **检验 ⟺ 置信区间**：拒绝 $H_0$ ⟺ $\theta_0\notin\hat\theta\pm z\widehat{\text{se}}$；统计显著 ≠ 科学显著。
> - **p 值**：$H_0$ 下观测到更极端值的概率；连续统计量下 $H_0$ 时 p~Uniform(0,1)；不是 $P(H_0|\text{data})$。
> - **Pearson χ²**：$\sum(X_j-E_j)^2/E_j\sim\chi^2_{k-1}$（多项拟合检验）。
> - **置换检验**：非参数、精确，小样本神器：p=打乱数据后统计量超过观测值的比例。
> - **LRT**：$\Lambda=2\log\frac{\ell(\hat\theta)}{\ell(\hat\theta_0)}\sim\chi^2_{r-q}$。
> - **多重检验**：Bonferroni（$p<\alpha/m$，保守）；**FDR/BH**（控制假阳性比例，$p_{(i)}\le i\alpha/m$）。
> - **NP 引理**：简单对简单时似然比检验最优；t 检验是大样本 Wald 的小样本正态版本。
