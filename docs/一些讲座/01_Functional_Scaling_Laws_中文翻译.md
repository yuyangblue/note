# 核回归中的泛函标度律：损失动力学与学习率调度

**原文标题：** Functional Scaling Laws in Kernel Regression: Loss Dynamics and Learning Rate Schedules

**作者：** Binghui Li, Fengling Chen, Zixun Huang, Lean Wang, Lei Wu (Peking University). 共同第一作者。通讯作者：Lei Wu.

**来源：** https://arxiv.org/abs/2509.19189

**会议：** NeurIPS 2025 Spotlight

---

## 摘要

标度律已成为理解和指导大语言模型（LLM）训练的统一框架。然而，现有研究主要关注最终步的损失，遗留了一个重要问题：整个损失动力学是否也遵循类似的标度律？更重要的是，学习率调度（LRS）如何塑造这些动力学？本文通过在幂律核（PLK）回归模型上分析随机梯度下降（SGD）来解决这些空白。核心洞察是提出了"内蕴时间"这一新视角，它比迭代次数更准确地刻画训练进度。我们随后建立了泛函标度律（FSL），该定律通过一个简单的卷积泛函来表达调度的影响，能够捕捉任意LRS下的完整损失轨迹。我们进一步将理论应用于三种代表性LRS——常数、指数衰减和预热-稳定-衰减（WSD）——并推导了数据受限和计算受限两种 regime 下的显式标度关系。这些比较解释了几个关键经验现象：(i) 更高容量的模型在数据和计算效率上都更优；(ii) 学习率衰减提高了训练效率；(iii) WSD型调度优于纯衰减调度。最后，在0.1B到1B参数规模的LLM上进行的实验表明，FSL作为代理模型在拟合和预测大规模预训练中的损失轨迹方面具有实际应用价值。

---

## 1 引言

大规模深度学习模型的训练神秘地遵循标度律，即模型性能随可用资源（如计算量或数据）可预测地改善[20]。具体而言，Kaplan等人[27]的开创性研究表明，在LLM预训练中，损失L随模型大小M和数据规模D按照一个极为简洁的幂律关系递减：

$$L(M,D) = L_0 + C_M M^{-\alpha_M} + C_D D^{-\alpha_D}, \tag{1}$$

其中 $\alpha_M$ 和 $\alpha_D$ 是标度指数，$L_0$ 表示不可约损失，$C_M, C_D$ 是某些常数。这类经验关系已被证明在模型架构、规模和训练设置上具有鲁棒性[21,62,38]，并已成为指导LLM开发的基本原则[19,26,1,5,57,29]。在实践中，它们现在被常规地用于设计最优资源分配策略[21]以及调整学习率和批量大小等关键超参数[38,31]。

尽管取得了这些经验成功，但标度律的理论理解仍然有限。最近的研究开始阐明其底层机制[56,23,41,65,25,44,45,2,15,3,8,37,52,9,73]，但两个重要空白仍然存在：

- **标度效率的决定因素。** 现有研究缺乏对关键因素（如模型容量、任务难度和超参数选择）如何影响标度效率——体现为指数 $\alpha_M$ 和 $\alpha_D$——的系统性描述。特别是学习率调度（LRS）在实践中被公认为至关重要[42,4,18]，但它们在塑造标度效率方面的精确作用仍不清楚。

- **超越最终步损失。** 经典标度律（公式(1)）仅处理训练结束时的损失[27,21]，遗留了一个开放问题：整个损失轨迹是否表现出类似的标度行为？虽然最近的实证证据[61,40]表明存在这种可能性，但系统性的研究和理论证明仍然缺失。

![图1：泛函标度律（FSL）精确捕捉核回归中SGD的损失动力学和标度行为。在两个子图中，实线表示SGD的结果，虚线表示相应的FSL预测。(a) SGD损失动力学（1000次运行的平均）与三种学习率调度（cosine、WSD和一种非标准循环调度）下FSL预测的对比。(b) 使用第5节解析公式的FSL预测的最终损失标度，与200次独立SGD运行的均值对比。](https://arxiv.org/pdf/2509.19189.pdf#page=1)

### 1.1 本文贡献

本文在受控但具代表性的理论设定下迈出解决这些空白的一步。我们研究幂律核（PLK）回归的随机梯度下降（SGD）训练——这是标度律分析中广泛采用的代理模型[8,3,52,37,9]。PLK回归由四个参数刻画：任务难度$s$、容量指数$\beta$、模型大小$M$和标签噪声水平$\sigma$。为了捕捉学习率调度（LRS）的影响，我们通过内蕴时间SDE对SGD进行建模，其中内蕴时间的概念成为统一刻画不同LRS如何塑造损失动力学和标度行为的关键量。在此基础上，我们建立了泛函标度律（FSL），它不仅能预测最终损失，还能精确刻画整个损失动力学。

具体而言，对于一般的内蕴时间LRS $\gamma: [0,\infty) \to [0,\infty)$，在某些条件下，期望损失 $\mathbb{E}[\mathcal{R}(\bm{\nu}_t)]$（其中$t$表示内蕴时间）的动力学满足：

$$
\mathbb{E}[\mathcal{R}(\bm{\nu}_t)] - \underbrace{\frac{\sigma^2}{2}}_{\text{不可约误差}} \;\eqsim\; \underbrace{\frac{1}{M^{s\beta}}}_{\text{近似误差}} + \underbrace{e(t)}_{\text{信号学习}} + \underbrace{\!\int_0^t\!\mathcal{K}(t-z)\,[e(z)+\sigma^2]\,\gamma(z)\,\mathop{}\!\mathrm{d}z}_{\text{噪声累积}}, \tag{2}
$$

其中 $e(t) = (1+t)^{-s}$ 且 $\mathcal{K}(t) = (1+t)^{-(2-1/\beta)}$。FSL中的每个项都有清晰的解释：$\tfrac{\sigma^2}{2}$ 表示由标签噪声引起的不可约误差，$M^{-s\beta}$ 代表近似误差，$e(t)$ 表征无噪声（全批量）梯度下降下的信号学习动力学，最后一项捕捉梯度噪声的注入和消散，其中LRS $\gamma$ 通过一个可处理的卷积泛函进入。函数 $\mathcal{K}$，称为遗忘核，量化了注入的噪声在训练过程中消散的速度。图1（左）表明FSL精确捕捉了SGD在不同LRS下的损失动力学。

在FSL的基础上，我们进一步推导了三种代表性LRS——常数、指数衰减[16]和预热-稳定-衰减（WSD）[72,22]——在数据受限和计算受限两种regime下的最终步损失的显式标度关系。结果总结在表1和图1（右）中，推广并扩展了先前的工作[8,9,52,37]，同时揭示了几个统一的洞察。

- **不同调度的标度效率。** WSD实现了最佳的标度效率，其次是指数衰减，然后是常数调度。这种效率层次为学习率衰减的重要性提供了理论依据，并解释了WSD的经验成功[72,22,60,38]。

- **模型容量的作用。** 更高容量的模型在计算和数据方面始终更高效，凸显了扩展模型容量的必要性[27]。

- **数据-模型权衡。** 计算最优训练要求数据规模的增长速度超过模型大小，与LLM预训练中已建立的启发式方法一致[21]。

- **峰值学习率的标度律。** 最优标度要求峰值学习率（LR）随训练预算（数据或计算）适当缩放，揭示了仔细调整峰值LR的重要性[7,31]。

除了PLK回归，我们还将FSL ansatz应用于从0.1B到1B参数规模的LLM预训练实验拟合和预测损失轨迹，涵盖密集和MoE架构。这些结果突出了FSL作为理解和指导LLM预训练的实用代理的潜力。

**表1：学习率调度（LRS）对幂律核回归标度效率的强烈影响。** 效率由两个关键因素决定：相对任务难度$s \in (0,\infty)$和模型容量$\beta > 1$。我们区分"易学习regime"（$s \geqslant 1-1/\beta$）和"难学习regime"（$s < 1-1/\beta$）。

| 学习率调度（LRS） | 数据最优标度律 | 计算最优标度律 |
|---|---|---|
| | 易学习 | 难学习 | 易学习 | 难学习 |
| 常数 | $D^{-\frac{s}{s+1}}$ | $C^{-\frac{s\beta}{1+s\beta+\beta}}$ |
| 指数衰减 | $D^{-\frac{s\beta}{1+s\beta}}(\log D)^{\frac{s\beta}{1+s\beta}}$ | $D^{-s}(\log D)^{s}$ | $C^{-\frac{s\beta}{2+s\beta}}(\log C)^{\frac{s\beta}{2+s\beta}}$ | $C^{-\frac{s\beta}{1+\beta}}(\log C)^{\frac{s\beta}{1+\beta}}$ |
| 预热-稳定-衰减（WSD） | $D^{-\frac{s\beta}{1+s\beta}}(\log D)^{\frac{s\beta-s}{1+s\beta}}$ | $D^{-s}$ | $C^{-\frac{s\beta}{2+s\beta}}(\log C)^{\frac{s\beta-s}{2+s\beta}}$ | $C^{-\frac{s\beta}{1+\beta}}$ |

### 1.2 相关工作

**标度律的理论解释。** 在越来越多的寻求理论解释标度律的工作中[56,23,41,65,25,44,45,2,15,3,8,37,52,9,48]，最相关的是[8,52,9,37]，它们也分析了PLK回归（通常以等价的线性回归形式书写）。具体而言，[8]研究了梯度流，[52,9]分析了带常数LRS的SGD，[37]考虑了指数衰减LRS。相比之下，我们建立了一个适用于一般LRS的统一标度律，不仅将这些先前结果作为特例恢复，而且通过捕捉损失动力学而不仅是最终步损失来实质性地扩展了它们。这种统一是由引入内蕴时间的关键概念实现的，它比原始训练步数更准确地捕捉有效训练进度。

**LLM预训练中损失轨迹的预测。** 最近的实证研究[61,40]表明，LLM预训练的整个损失轨迹——而不仅是最终损失——可以被适当的标度关系精确捕捉。相应的拟合程序的详细描述见附录A.1。我们的理论为这些实证发现提供了理论解释。有趣的是，[40]提出的多幂律（MPL）模型与我们的FSL密切相关：通过分部积分变换，FSL表达式可以转化为与MPL公式几乎等价的形式（见附录B.2）。

**预热-稳定-衰减（WSD）LRS。** WSD调度[72]在DeepSeek-V3[33]和Kimi-K2[39]等工业模型中使用。尽管其经验成功，但缺乏理论理解。本文表明，即使在二次优化（核回归）的简单设定中，也可以复现WSD的本质优势。

### 1.3 符号约定

$[n] := \{1,2,\ldots,n\}$。对于正半定矩阵$\mathbf{S}$，$\mu_j(\mathbf{S})$表示第$j$大特征值，$\|u\|_{\mathbf{S}} := \sqrt{u^\top \mathbf{S} u}$。符号$\eqsim$表示常数因子等价，$\lesssim$和$\gtrsim$表示常数因子不等式。

---

## 2 幂律核（PLK）回归

我们考虑通过特征映射 $\phi: \mathcal{X} \to \mathbb{R}^N$ 的核回归任务。给定输入$x \in \mathcal{X}$，目标是预测标量标签$y$，满足：

$$y = \langle \phi(x), \theta^* \rangle + \varepsilon, \quad \varepsilon \sim \mathcal{N}(0, \sigma^2),$$

其中$\theta^* \in \mathbb{R}^N$是ground-truth参数向量，$\varepsilon$是标签噪声。

**假设2.1（超收缩性）。** 特征分布的四阶矩被二阶矩控制。即存在常数$\rho_-, \rho_+ > 0$使得：

$$\rho_- \cdot \mathbb{E}[\|\phi(X)\|^2 \cdot u^2] \leq \mathbb{E}[\langle \phi(X), u \rangle^4] \leq \rho_+ \cdot \mathbb{E}[\|\phi(X)\|^2 \cdot u^2]^2$$

对所有$u \in \mathbb{R}^N$成立。高斯特征（以及更一般的$\sigma$-子高斯特征）满足此条件。

**假设2.2（特征协方差）。** 我们假设特征协方差矩阵 $\mathbf{H} = \mathbb{E}[\phi(X)\phi(X)^\top]$ 是对角的：

$$\mathbf{H} = \operatorname{diag}(\lambda_1, \lambda_2, \ldots, \lambda_N), \quad \lambda_1 \geq \lambda_2 \geq \ldots \geq \lambda_N.$$

模型参数化为 $f(x; v) = \sum_{j=1}^M v_j w_j^\top \phi(x)$，其中 $\mathbf{v} = (v_1, \ldots, v_M)^\top \in \mathbb{R}^M$。有两种投影方式：

- **Top-$M$特征：** $w_j = e_j$（单位向量）
- **Random-$M$特征：** $w_j \sim \mathcal{N}(0, \mathbf{I}_N)$

### 2.1 模型容量与任务难度

**假设2.3（模型容量）。** 特征衰减速度由容量指数$\beta > 1$控制：

$$\lambda_j \asymp j^{-\beta}.$$

注：$\beta$越大，特征衰减越快，模型的表达能力越弱。

**假设2.5（任务难度）。** 目标参数的结构由任务难度指数$s > 0$刻画：

$$|\theta_j^*|^2 \asymp j^{-(s\beta+1)}.$$

注：$s$刻画了相对任务难度。直观上，对于固定的$\alpha = s\beta$，$s$越大（$\beta$越小）意味着模型容量越大，任务相对越容易学习。

---

## 3 单程SGD与内蕴时间SDE

### 3.1 连续时间极限

当步长$h \to 0$时，SGD可以被随机微分方程（SDE）近似：

$$d\nu_j(t) = -\lambda_j (\nu_j - \theta_j^*) dt + \sqrt{\eta(t)} \cdot \sqrt{\frac{\mathcal{R}(\bm{\nu}_t)}{b(t)}} dB_t^{(j)},$$

其中$B_t^{(j)}$是标准布朗运动，$b(t)$是批量大小。

### 3.2 内蕴时间重参数化

内蕴时间 $\tau(t) = \int_0^t \eta(s) ds$ 将物理时间转换为内蕴时间。关键观察：不同LRS通过内蕴时间统一刻画训练进度。定义$\gamma(\tau) = \eta(T^{-1}(\tau))$为内蕴时间下的LRS。

在内蕴时间下，SDE简化为：

$$d\nu_j(t) = -\lambda_j (\nu_j - \theta_j^*) dt + \sqrt{\frac{\gamma(t)}{b(T^{-1}(t))}} dB_t^{(j)}.$$

---

## 4 内蕴时间泛函标度律

### 4.1 示例设定与底层标度行为

我们首先在Top-$M$特征设定下建立FSL，其中各模式的学习动力学相互独立，可以精确求解。

定义：
- $e_M(t) = \sum_{j=1}^M \lambda_j |\theta_j^*|^2 e^{-2\lambda_j t}$（信号学习函数）
- $\mathcal{K}_M(t) = \sum_{j=1}^M \lambda_j^2 e^{-2\lambda_j t}$（遗忘核）

**引理4.1（幂律衰减）。** 对于 $1 \lesssim t \lesssim M^\beta$，有：

$$e_M(t) \asymp t^{-s}, \quad \mathcal{K}_M(t) \asymp t^{-(2-1/\beta)}.$$

### 4.2 一般结果：Top-$M$特征情况

**定理4.2（内蕴时间FSL，难学习regime）。** 假设$s \leq 1 - 1/\beta$。设$\bm{\nu}_t$是内蕴时间SDE的解。则：

$$\mathbb{E}[\mathcal{R}(\bm{\nu}_t)] - \tfrac{1}{2}\sigma^2 \eqsim M^{-s\beta} + e(t) + \int_0^t \mathcal{K}(t-z)[e(z)+\sigma^2]\gamma(z)\mathop{}\!\mathrm{d}z, \tag{9}$$

其中 $e(t) := (1+t)^{-s}$，$\mathcal{K}(t) := (1+t)^{-(2-1/\beta)}$。对于随机-$M$情况，以概率至少 $1 - \exp\{-\Omega(M)\}$（关于$\mathbf{W}$的随机性）成立相同的FSL。

该定理建立了对于任务难度$s \leq 1 - 1/\beta$的困难任务，损失动力学完全由FSL（公式9）刻画。此外，FSL（公式9）中的每一项都有清晰的解释：

- **不可约误差：** $\tfrac{1}{2}\sigma^2$。该项源于标签噪声。
- **近似误差：** $M^{-s\beta}$。该项对应于有限模型大小造成的误差，标度效率由任务的固有难度$s\beta$决定。
- **信号学习：** $e(t)$。该项对应于全批量梯度下降下的学习，捕捉SGD提取信号$f^*$的速率。此外，速率取决于任务的相对难度$s$。对于固定的$f^*$（固定的$\alpha = s\beta$），增加模型容量（更小的$\beta$）会加速收敛，因为$s = \alpha/\beta$变大。
- **噪声累积：** $\int_0^t \mathcal{K}(t-z)[e(z)+\sigma^2]\gamma(z)\mathop{}\!\mathrm{d}z$。该项刻画了学习率和批量大小调度如何塑造随机噪声的累积和消散。被积函数$[e(z)+\sigma^2]\gamma(z)$表示瞬时噪声幅度，其中$e(z)$捕捉小批量噪声，$\sigma^2$捕捉标签噪声。遗忘核$\mathcal{K}(\cdot)$量化了在时刻$z$注入的噪声如何仍然影响时刻$t$的损失。由于$\mathcal{K}(t) \asymp t^{-(2-1/\beta)}$，更高容量的模型（更小的$\beta$）往往遗忘噪声更慢。

值得注意的是，最后两项共同构成优化误差，两个关键因素决定了它们之间的权衡：

- **模型容量。** 增加模型容量（$\beta \downarrow$）会加速信号学习，但同时减慢噪声遗忘。
- **学习率和批量大小调度。** 更小的学习率或更大的批量大小会抑制噪声注入，但也会缩短内蕴训练时间。然而，足够的内蕴时间是重要的：信号学习项需要它来有效降低风险，而噪声遗忘项依赖于它来遗忘早期训练中记忆的噪声。因此，有效的调度必须平衡这些竞争目标——抑制注入的噪声，同时保持足够的学习和遗忘内蕴时间。

**定理4.3（内蕴时间FSL，Top-$M$特征，一般标签噪声）。** 假设假设4.1成立。设$\bm{\nu}_t$是带Top-$M$特征的内蕴时间SDE的解。定义 $\mathcal{F}_M(t;\gamma) = e_M(t) + \int_0^t \mathcal{K}_M(t-z)[e_M(z)+\sigma^2]\gamma(z)\mathop{}\!\mathrm{d}z$。存在$c > 0$使得对于$0 \leq t \leq cM^\beta$，有：

$$\mathbb{E}[\mathcal{R}(\bm{\nu}_t)] - \tfrac{1}{2}\sigma^2 \;\eqsim\; M^{-s\beta} + \mathcal{F}_\infty(t;\gamma). \tag{11}$$

对于所有$cM^\beta \leq t < \infty$，有：

$$M^{-s\beta} + \mathcal{F}_M(t;\gamma) \;\lesssim\; \mathbb{E}[\mathcal{R}(\bm{\nu}_t)] - \tfrac{1}{2}\sigma^2 \;\lesssim\; M^{-s\beta} + \mathcal{F}_\infty(t;\gamma). \tag{12}$$

**定理4.4（内蕴时间FSL，Top-$M$特征，常数标签噪声）。** 在假设4.1下，假设$\sigma \gtrsim 1$。设$\bm{\nu}_t$是带Top-$M$特征的内蕴时间SDE的解。那么，对于任意$s > 0$和所有$t \geq 0$：

$$\mathbb{E}[\mathcal{R}(\bm{\nu}_t)] - \tfrac{1}{2}\sigma^2 \;\eqsim\; M^{-s\beta} + e_M(t) + \int_0^t \mathcal{K}_M(t-z)\,[e_M(z)+\sigma^2]\,\gamma(z)\,\mathop{}\!\mathrm{d}z.$$

**定理4.5（内蕴时间FSL，Top-$M$特征，零标签噪声）。** 假设假设4.1成立且$\sigma = 0$。设$\bm{\nu}_t$是带Top-$M$特征的内蕴时间SDE的解。如果$s \in [0, 2-1/\beta]$，则对所有$t \geq 0$：

$$\mathbb{E}[\mathcal{R}(\bm{\nu}_t)] \;\eqsim\; M^{-s\beta} + e_M(t) + \int_0^t \mathcal{K}_M(t-z)\,e_M(z)\,\gamma(z)\,\mathop{}\!\mathrm{d}z.$$

### 4.3 一般结果：Random-$M$特征情况

对于随机特征情况，修改后的特征协方差矩阵为 $\widehat{\mathbf{H}} = \mathbf{W}\mathbf{H}\mathbf{W}^\top$，其特征值记为 $\widehat{\lambda}_1 \geq \widehat{\lambda}_2 \geq \cdots \geq \widehat{\lambda}_M$。

**定理4.6（内蕴时间FSL，Random-$M$特征）。** 假设假设4.1成立且$s \in (0, 1]$。设$\bm{\nu}_t$是带Random-$M$特征的内蕴时间SDE的解。那么，以概率至少 $1 - \exp(-\Omega(M))$（关于投影矩阵$\mathbf{W}$的随机性），定理4.3、4.4和4.5的结果继续成立，只需将$e_M(\cdot)$和$\mathcal{K}_M(\cdot)$分别替换为其随机特征对应物$\widehat{e}_M(\cdot)$和$\widehat{\mathcal{K}}_M(\cdot)$。

**引理4.7。** 以概率至少 $1 - \exp(-\Omega(M))$（关于投影矩阵$\mathbf{W}$的随机性），对任意$j \in [M]$有 $\widehat{\lambda}_j \eqsim \lambda_j \eqsim j^{-\beta}$。

### 4.4 关键证明步骤与核心洞察

本节概述FSL（公式11）证明背后的主要思想，突出关键技巧。完整证明见附录C。

我们需要梯度噪声结构的以下表征。

**引理4.8（噪声结构）。** 对于任意$\mathbf{v} \in \mathbb{R}^M$，有：

$$(2\rho_- \mathcal{E}(\mathbf{v}) + \sigma^2)\,\nabla^2 \mathcal{R}(\mathbf{v}) \;\preceq\; \bm{\Sigma}(\mathbf{v}) \;\preceq\; (2\rho_+ \mathcal{E}(\mathbf{v}) + \sigma^2)\,\nabla^2 \mathcal{R}(\mathbf{v}),$$

其中$\nabla^2 \mathcal{R}(\mathbf{v}) = \mathbf{W}\mathbf{H}\mathbf{W}^\top$。

#### Volterra积分方程

通过分析，损失动力学满足以下Volterra方程：

$$\mathbb{E}[\mathcal{E}_t] \eqsim \delta_M + e_M(t) + \int_0^t \mathcal{K}_M(t-z)\gamma(z)(\mathbb{E}[\mathcal{E}_z] + \sigma^2)\mathop{}\!\mathrm{d}z. \tag{15}$$

设$f(t) := \mathbb{E}[\mathcal{E}_t]$，$g(t) := \delta_M + e_M(t) + \sigma^2 \int_0^t \mathcal{K}_M(t-z)\gamma(z)\mathop{}\!\mathrm{d}z$，并定义线性算子：

$$\mathcal{T}f(t) = \int_0^t \mathcal{K}_M(t-z)\gamma(z)f(z)\mathop{}\!\mathrm{d}z.$$

则Volterra方程（公式15）可以简洁地写成 $f = g + \mathcal{T}f$。形式上，其解可以展开为无穷级数：

$$f = (\mathcal{I} - \mathcal{T})^{-1}g = g + \mathcal{T}g + \mathcal{T}^2 g + \mathcal{T}^3 g + \cdots. \tag{16}$$

关键观察：在幂律假设下，高阶项$\mathcal{T}^k g$（$k \geq 2$）可以被一阶项$\mathcal{T}g$控制。这源于遗忘核的尺度不变性：

**引理4.9（尺度不变性）。** 对任意$t \lesssim M^\beta$，有 $\tfrac{\mathcal{K}_M(t/2)}{\mathcal{K}_M(t)} \simeq 1$。

**推论4.10（次卷积性质）。** 对任意$t \lesssim M^\beta$，有 $\mathcal{K}_M * \mathcal{K}_M(t) \lesssim \mathcal{K}_M(t)$。

由此可得 $f(t) \eqsim g(t) + \mathcal{T}g(t)$，即FSL主方程。

#### 幂律标度的涌现（多任务视角）

我们从多任务学习视角说明幂律标度如何从我们的设定中涌现。直观上，我们可以将每个特征函数的学习视为一个子任务。在这种视角下，我们的FSL框架揭示了幂律行为的三种不同表现：

- **(i) 近似误差。** 近似误差解释了$N-M$个未学习子任务的总风险，由于：

$$\delta_M = \sum_{j=M+1}^N \lambda_j |\theta_j^*|^2 \eqsim M^{-s\beta}, \quad \text{若} N-M \gtrsim M.$$

- **(ii) 信号学习。** 对于每个子任务，子任务风险相对于内蕴时间$t$呈指数收敛。然而，由于$\{\lambda_j\}$和$\{\theta_j^*\}$的幂律结构，当$M$足够大时，总多任务风险呈现幂律衰减：

$$e_M(t) = \sum_{j=1}^M \lambda_j |\theta_j^*|^2 e^{-2\lambda_j t} \eqsim \int_{M^{-\beta}}^1 u^{s-1} e^{-2ut} \mathop{}\!\mathrm{d}u \eqsim \frac{1}{t^s}, \quad \text{若} 1 \lesssim t \lesssim M^\beta.$$

- **(iii) 噪声遗忘。** 类似地，对于遗忘核，我们也有：

$$\mathcal{K}_M(t) = \sum_{j=1}^M \lambda_j^2 e^{-2\lambda_j t} \;\eqsim\; \int_{M^{-\beta}}^1 z^{\,1-\frac{1}{\beta}} e^{-2zt} \mathop{}\!\mathrm{d}z \;\eqsim\; t^{-(2-1/\beta)}, \quad \text{若} 1 \lesssim t \lesssim M^\beta.$$

**注4.11（任务累积效应）。** 上述推导揭示了：尽管单个任务可能不会表现出关于内蕴时间的精确幂律标度，但许多任务的**集体累积**产生了这种标度行为。随着任务数量的增加，幂律regime逐渐扩展，在$M \to \infty$的理想极限下，它覆盖整个训练过程。在我们的设定中，每个子任务自然遵循指数学习曲线$\exp(-\lambda t)$，然而底层机制似乎更加普遍。我们预计即使个体任务动力学偏离这种形式，类似的幂律行为也可能出现，这有待未来研究。

---

## 5 学习率调度影响标度效率

在建立了通用FSL之后，我们现在将其应用于三种代表性LRS——常数、指数衰减和预热-稳定-衰减（WSD）——以检验调度设计如何影响标度效率。所有证明见附录D。为清晰起见，我们作如下假设：

**假设5.1。** 假设标签噪声$\sigma^2 \gtrsim 1$和批量大小$b(\tau) = B$均为常数。

在该假设下，给定物理时间LRS函数$\varphi(\cdot)$，定理4.4意味着对于$t \gtrsim 1$，FSL简化为：

$$\mathbb{E}[\mathcal{R}(\bm{\nu}_t)] - \tfrac{1}{2}\sigma^2 \;\eqsim\; M^{-s\beta} + (1+t)^{-s} + \frac{1}{B} \int_0^t (1+t-z)^{-(2-1/\beta)} [(1+z)^{-s} + \sigma^2] \varphi(z) \mathop{}\!\mathrm{d}z.$$

### 5.1 常数LRS

**定理5.2（常数LRS）。** 考虑常数LRS $\eta(t) = \eta_0$（即$\gamma(t) = \eta_0$）和批量大小$B$。最终损失满足：

$$\mathbb{E}[\mathcal{R}(\bm{\nu}_{T})] - \frac{\sigma^2}{2} \;\eqsim\; M^{-s\beta} + (\eta_0 T)^{-s} + \frac{\eta_0}{B}\sigma^2,$$

其中$T = K\eta_0$是总内蕴时间，$K$是物理训练步数。

**数据最优标度。** 在数据受限regime（$D$表示数据量），数据最优学习率满足 $\eta_{\text{opt}} \eqsim D^{-s/(s+1)}$，对应最优损失：

$$E_{\text{opt}} \;\eqsim\; D^{-\frac{s}{s+1}}.$$

**计算最优标度。** 在计算受限regime（$C$表示计算量），计算最优学习率满足 $\eta_{\text{opt}} \eqsim C^{-\frac{s\beta}{1+(s+1)\beta}}$，对应最优损失：

$$E_{\text{opt}} \;\eqsim\; C^{-\frac{s\beta}{1+s\beta+\beta}}.$$

关键发现：
- **线性缩放规则：** 学习率应与批量大小线性缩放。
- **更高容量模型更计算高效：** 随着$\beta$减小（容量增加），损失指数$s\beta/(1+s\beta+\beta)$增大，模型更高效。

### 5.2 指数衰减LRS

**定理5.3（指数衰减LRS）。** 考虑指数衰减LRS $\eta(t) = a e^{-bt}$（即$\gamma(t) = a e^{-bt}$）和批量大小$B$。最终损失满足：

$$\mathbb{E}[\mathcal{R}(\bm{\nu}_{T})] - \frac{\sigma^2}{2} \;\eqsim\; M^{-s\beta} + T^{-s} + \frac{\sigma^2}{B} + \frac{a-b}{BT} \min\{M^\beta, T^{1/\beta}\} \cdot \sigma^2,$$

其中$T = (a-b)K/\log(a/b)$是总内蕴时间。

**数据最优标度。** 最优损失：

$$E_{\text{opt}} \;\eqsim\; (D/\log D)^{-\frac{s\beta}{1+s\beta}} \quad \text{（易学习regime）}$$
$$E_{\text{opt}} \;\eqsim\; (D/\log D)^{-s} \quad \text{（难学习regime）}$$

相比常数LRS，指数衰减LRS严格更优，验证了学习率衰减的重要性。

### 5.3 WSD型LRS

WSD调度由三个阶段组成：
1. **预热阶段：** $[0, K_1)$，学习率从$0$线性增加到峰值$\eta_{\max}$
2. **稳定阶段：** $[K_1, K_1 + K_2)$，学习率保持在$\eta_{\max}$
3. **衰减阶段：** $[K_1 + K_2, K]$，学习率从$\eta_{\max}$指数衰减到$\eta_{\min}$

**定理5.4（WSD型LRS）。** 考虑WSD LRS $\eta(t)$，其内蕴时间表示为$\gamma(t)$。最终损失满足：

$$\mathbb{E}[\mathcal{R}(\bm{\nu}_{T})] - \frac{\sigma^2}{2} \;\eqsim\; M^{-s\beta} + (T_1 + T_2)^{-s} + \frac{\sigma^2}{B} + \frac{a-b}{BT_2} \min\{M^\beta, T_2^{1/\beta}\} \cdot \sigma^2,$$

其中$T_1$和$T_2$分别是稳定阶段和衰减阶段贡献的内蕴时间。

**关键优势：** 稳定阶段大幅增加了内蕴时间，而衰减阶段仅占很小比例（$r \to 0$）。这消除了指数衰减中的对数因子。

**数据最优标度。** 最优损失：

$$E_{\text{opt}} \;\eqsim\; (D/\log D)^{-\frac{s\beta}{1+s\beta}} (\log D)^{\frac{s\beta-s}{1+s\beta}} \quad \text{（易学习regime）}$$
$$E_{\text{opt}} \;\eqsim\; D^{-s} \quad \text{（难学习regime）}$$

这完全消除了难学习regime中的对数因子，与LLM实践中衰减阶段仅占10%-20%的经验一致。

#### 计算最优标度

在计算受限regime下，WSD同样优于其他调度，特别是在难学习regime中达到$C^{-s\beta/(1+\beta)}$的最优损失。

---

## 6 实验

### 6.1 幂律核回归

我们在幂律核回归任务上验证FSL的预测。我们考虑三种LRS：cosine调度、WSD调度和一种非标准循环调度。

**实验设置：**
- 特征维数：$N = 2000$
- 特征衰减：$\beta = 2$
- 任务难度：$s = 0.5$（难学习regime）
- 噪声水平：$\sigma = 0.1$
- 模型大小：$M \in \{50, 100, 200, 500\}$

**结果：** FSL准确捕捉SGD在所有三种LRS下的损失动力学。图1（a）显示FSL预测（虚线）与SGD实验（实线）的对比，表明我们的理论能够精确描述整个训练轨迹。

WSD调度的行为值得注意：在稳定阶段，损失衰减相对较慢；但一旦进入衰减阶段，损失急剧下降，最终达到比常数和cosine调度更低的值。这与我们的理论预测一致。

图1（b）显示了FSL预测的最终损失标度行为与SGD实验的对比。在不同模型大小下，FSL预测的标度关系与经验观察高度一致。

### 6.2 LLM预训练

我们在真实LLM预训练场景中测试FSL的实用性。

**实验设置：**
- **Llama 400M模型：** 使用8-1-1 LRS（8个epoch预热，稳定1个epoch，然后衰减）的轨迹拟合FSL参数$(\beta, s)$，然后预测cosine和WSD调度下的损失曲线。
- **Llama 1B模型：** 类似的实验设置。
- **QwenMoE 1B模型：** 测试FSL在混合专家模型上的适用性。

**结果：**

1. **损失轨迹拟合：** FSL能够用8-1-1 LRS的轨迹准确拟合参数，并成功预测cosine和WSD调度下的损失曲线。

2. **最优LRS发现：** 在1B QwenMoE模型上，FSL预测的最优LRS呈现明显的WSD形状，衰减阶段将学习率降至远低于$0.1\eta_{\max}$。

3. **计算效率比较：** FSL最优LRS在相同计算预算下优于所有基线LRS（常数、cosine、标准WSD等）。

这些实验表明FSL可以作为理解和指导LLM预训练的有价值工具。

---

## 7 结论

本文建立了泛函标度律（FSL），它统一描述了任意学习率调度下的完整损失动力学。我们的关键贡献包括：

1. **内蕴时间概念：** 提出了内蕴时间作为刻画训练进度的更准确度量，比简单的迭代次数更好地捕捉有效训练动态。

2. **幂律标度的涌现：** 证明了幂律标度从多任务累积效应中自然涌现，揭示了标度律的深层机制。

3. **WSD的理论解释：** 提供了WSD优于纯衰减调度的理论原因，解释了为什么工业LLM广泛采用这种调度策略。

4. **真实LLM验证：** 在0.1B到1B参数的真实LLM上验证了FSL的实用性，包括密集和MoE架构。

**局限性与未来方向：** 当前分析限于幂律核回归设定。未来的重要扩展包括：
- 更一般的特征谱结构
- 非均匀学习率
- Transformer架构的建模
- 与LLM预训练中观察到的具体现象的联系

---

## 附录A 补充材料

### A.1 LLM预训练损失轨迹的经验拟合方法

为将FSL应用于LLM预训练，我们需要从经验损失轨迹中估计参数$(\beta, s)$。具体步骤如下：

1. **数据预处理：** 收集LLM预训练过程中的损失轨迹$\{(K_k, L_k)\}$，其中$K_k$是第$k$步的迭代数，$L_k$是对应的损失值。

2. **内蕴时间估计：** 通过积分学习率曲线估计内蕴时间$\tau_k = \int_0^{K_k} \eta(s) ds$。

3. **参数拟合：** 使用FSL公式拟合数据，估计$(\beta, s)$。具体而言，我们最小化以下损失函数：

$$\mathcal{L}(\beta, s) = \sum_k \left| \log L_k - \log \hat{L}(\tau_k; \beta, s) \right|^2,$$

其中$\hat{L}$是由FSL预测的损失值。

4. **验证：** 使用拟合的参数预测其他LRS下的损失轨迹，验证预测精度。

### A.2 LLM预训练中常用的学习率调度

LLM预训练中常用的学习率调度包括：

- **常数调度：** $\eta(t) = \eta_0$
- **余弦衰减（cosine）：** $\eta(t) = \eta_{\max} \cdot \frac{1 + \cos(\pi t / T)}{2}$
- **指数衰减：** $\eta(t) = \eta_{\max} \cdot e^{-t/\tau}$
- **阶梯衰减：** $\eta(t) = \eta_{\max} \cdot a^{ \lfloor t / \tau \rfloor }$
- **WSD（预热-稳定-衰减）：** 如第5.3节所定义
- **8-1-1调度：** 预热8个epoch，稳定1个epoch，衰减1个epoch

### A.3 与核回归的联系

本文的PLK回归设定等价于具有幂律特征谱的核回归。具体而言，核函数$K(x, x') = \langle \phi(x), \phi(x') \rangle$具有特征值$\lambda_j \asymp j^{-\beta}$。

这种联系表明FSL的预测可能推广到更一般的核回归场景，甚至可能推广到神经网络训练的某些阶段。

### A.4 SDE建模的推导细节

从SGD到连续时间SDE的过渡涉及以下关键步骤：

1. **SGD更新：** $v_{k+1} = v_k - \eta_k \nabla \mathcal{R}(v_k) + \eta_k \xi_k$，其中$\xi_k$是梯度噪声。

2. **缩放假设：** 步长$\eta_k \to 0$，学习率随时间缓慢变化，使得$T = \sum_k \eta_k$保持有限。

3. **扩散项标定：** 梯度噪声的协方差为$\mathbb{E}[\xi_k \xi_k^\top] \asymp \frac{\mathcal{R}(v_k)}{b_k}$。

4. **Itô-Taylor展开：** 应用Itô-Taylor展开，保留主导项，得到连续时间SDE。

---

## 附录B 实验细节与额外结果

### B.1 幂律核回归实验

**实验参数：**
- 特征维数$N = 2000$，模型大小$M \in \{50, 100, 200, 500\}$
- 容量指数$\beta = 2$，任务难度$s \in \{0.3, 0.5, 0.8\}$
- 标签噪声$\sigma = 0.1$，批量大小$B = 32$
- 学习率调度：常数$\eta = 0.01$，cosine，WSD

**评估指标：**
- 训练损失$\mathcal{R}(\bm{\nu}_t)$
- 最终损失与理论预测的相对误差

### B.2 LLM预训练实验

**数据集：** OpenWebText语料库的子集

**模型配置：**
- Llama 400M：12层，16头，隐藏维度1024
- Llama 1B：22层，16头，隐藏维度2048
- QwenMoE 1B：24层，MoE配置为8 experts per token

**训练配置：**
- 批量大小：4096 tokens
- 最大学习率：$1 \times 10^{-3}$
- 训练步数：100K-500K

---

## 附录C 第4节的证明

### C.1 Volterra积分方程刻画损失动力学

### C.2 $e_M$和$\mathcal{K}_M$函数的幂律衰减

### C.3 Top-$M$特征情况

#### C.3.1 定理4.3的证明

#### C.3.2 定理4.4的证明

#### C.3.3 定理4.5的证明

#### C.3.4 定理4.2的证明

### C.4 Random-$M$特征情况

#### C.4.1 集中不等式

#### C.4.2 上下界

#### C.4.3 命题C.11的证明

---

## 附录D 第5节的证明

### D.1 常数LRS的证明

### D.2 指数衰减LRS的证明

- **情况1：** $T \geq M^\beta$
- **情况2：** $T < M^\beta$

### D.3 WSD型LRS的证明

- **情况1：** $T_2 \geq M^\beta$
- **情况2：** $T_2 < M^\beta$

---

## 附录E 辅助引理

本文证明中使用的辅助引理集合，包括：
- 积分估计引理
- 幂函数不等式
- 卷积不等式
- 集中不等式

---

## 参考文献

（原文参考文献，无需翻译）
