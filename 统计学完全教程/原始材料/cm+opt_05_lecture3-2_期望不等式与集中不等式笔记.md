# 工科概率论与数理统计 · Lecture 3-2 笔记
## 期望不等式与正态尾界 / 集中不等式与有限样本保证

> 来源：讲义 `lecture_3_2(1).pdf`（武汉大学，授课教师：刘常钰，2026—2027 学年，共 67 页）。
> 本笔记按幻灯片顺序忠实转录全部内容与页面结论，公式保持原样。

---

# 3.4 期望不等式与正态尾界

## 分布未知，还能控制尾概率吗？

**现实处境**：精确分布常常未知，但往往知道一部分信息：非负性、均值、方差。目标：只用这些信息，给尾概率一个对所有满足条件的分布都成立的上界。

| 已知信息 | 不等式 | 形式 | 衰减速度 |
|---|---|---|---|
| 只知道 $Y\ge 0$ 与均值 $\mathbb{E}Y$ | **Markov 不等式** | $\mathbb{P}(Y\ge t)\le \dfrac{\mathbb{E}Y}{t},\quad t>0$ | 上界按 $1/t$ 衰减 |
| 再知道方差 $\mathrm{Var}(X)=\sigma^2$ | **Chebyshev 不等式** | $\mathbb{P}(\lvert X-\mu\rvert\ge t)\le\dfrac{\sigma^2}{t^2},\quad t>0$ | 上界按 $1/t^2$ 衰减 |

若还知道**独立、有界**等信息，可得到更紧的**指数型上界**（Hoeffding、Bernstein、Chernoff 等），后续不等式部分继续。

> **掌握的信息越多，能换来的尾概率上界通常越紧。**

## Cauchy–Schwarz 不等式

**定理（Cauchy–Schwarz）**
条件：$\mathbb{E}[X^2]<\infty$，$\mathbb{E}[Y^2]<\infty$。则

$$
\big|\mathbb{E}[XY]\big|\ \le\ \mathbb{E}|XY|\ \le\ \sqrt{\mathbb{E}[X^2]\,\mathbb{E}[Y^2]}
$$

**等号条件**：$|\mathbb{E}[XY]|$ 版取等 $\iff Y = cX$ a.s.；$\mathbb{E}|XY|$ 版取等 $\iff |Y| = c|X|$ a.s.（$c\ge 0$）。

**应用：相关系数**（$0<\mathrm{Var}X, \mathrm{Var}Y<\infty$）

对 $U = X - \mathbb{E}X$，$V = Y - \mathbb{E}Y$ 用定理：

$$
|\rho_{XY}| = \frac{|\mathrm{Cov}(X,Y)|}{\sqrt{\mathrm{Var}X\,\mathrm{Var}Y}} \le 1，
\quad \text{且 } |\rho_{XY}| = 1 \iff Y = aX + b\ \text{a.s.}，\ a\ne 0.
$$

### Cauchy–Schwarz 不等式：判别式证明

1. **退化情形**：若 $\mathbb{E}[X^2]=0$，则 $X=0$ a.s.，两边都为 $0$。下设 $\mathbb{E}[X^2]>0$。
2. **构造恒非负的二次函数**：对任意实数 $\lambda$：

$$
0 \le \mathbb{E}[(Y-\lambda X)^2] = \mathbb{E}[Y^2] - 2\lambda\,\mathbb{E}[XY] + \lambda^2\,\mathbb{E}[X^2]
$$

3. **判别式 $\le 0$**：关于 $\lambda$ 的二次函数恒非负，所以

$$
4(\mathbb{E}[XY])^2 - 4\,\mathbb{E}[X^2]\,\mathbb{E}[Y^2] \le 0
$$

4. **等号条件**：等号成立 $\iff$ 存在 $\lambda$ 使 $\mathbb{E}[(Y-\lambda X)^2] = 0$，即 $Y = \lambda X$ a.s.。

## 课堂题 A

**背景与已知**：某学习算法用 $n$ 个训练样本得到预测器，它在一个新样本上的预测误差记为随机变量 $R_n$（可正可负）。

- 已知：$\mathbb{E}[R_n^2] \le 4/n$（均方误差上界）。
- **不假设** $R_n$ 服从正态或任何具体分布。

**问题**

1. 用 Cauchy–Schwarz 给出平均绝对误差 $\mathbb{E}|R_n|$ 的上界。
2. 对任意 $\varepsilon>0$，给出尾概率 $\mathbb{P}(|R_n|\ge\varepsilon)$ 的上界。

**本题需要的公式**

- Cauchy–Schwarz（$\mathbb{E}U^2,\mathbb{E}V^2<\infty$）：$\quad\mathbb{E}|UV| \le \sqrt{\mathbb{E}[U^2]\,\mathbb{E}[V^2]}$
- Markov（$Y\ge 0,\ a>0$）：$\quad\mathbb{P}(Y\ge a) \le \dfrac{\mathbb{E}Y}{a}$

**提示**：① 取 $V\equiv 1$；② 先把事件改写成非负变量 $R_n^2$ 的事件。

### 课堂题 A 解答

**① 平均绝对误差**

取 $U = |R_n|$、$V\equiv 1$：$\mathbb{E}[U^2] = \mathbb{E}[R_n^2]\le 4/n<\infty$，$\mathbb{E}[V^2]=1$，条件满足。

$$
\mathbb{E}|R_n| = \mathbb{E}\big(|R_n|\cdot 1\big) \le \sqrt{\mathbb{E}[R_n^2]\cdot\mathbb{E}[1^2]} \le \frac{2}{\sqrt{n}}
$$

**结论**：平均绝对误差至多 $2/\sqrt{n}$；这是对所有满足条件的分布都成立的上界，不是实际误差。

**② 尾概率**

事件改写：$\{|R_n|\ge\varepsilon\} = \{R_n^2\ge\varepsilon^2\}$；$R_n^2\ge 0$，可用 Markov。

$$
\mathbb{P}\big(|R_n|\ge\varepsilon\big) = \mathbb{P}\big(R_n^2\ge\varepsilon^2\big) \le \frac{\mathbb{E}[R_n^2]}{\varepsilon^2} \le \min\Big\{1,\ \frac{4}{n\varepsilon^2}\Big\}
$$

**结论**：取 $\min$ 是因为概率本来不超过 1；当 $n\varepsilon^2\le 4$ 时这个界没有信息。

### 课堂题 A（续）

**条件重述**：$R_n$ 为训练规模 $n$ 时的预测误差，只知 $\mathbb{E}[R_n^2]\le 4/n$，无分布假设。已得：$\mathbb{E}|R_n|\le 2/\sqrt{n}$；$\mathbb{P}(|R_n|\ge\varepsilon)\le\min\{1,\ 4/(n\varepsilon^2)\}$。

**问题**

3. $R_n$ 是否在 $L^2$、$L^1$、依概率三种意义下收敛到 0？每一种分别依据哪个结果？
4. $n = 100$ 时，平均绝对误差 $\mathbb{E}|R_n|$ 与 $\mathbb{P}(|R_n|\ge 0.5)$ 分别能保证到多少？

**定义**

- $L^2$ 收敛：$\mathbb{E}[R_n^2]\to 0$
- $L^1$ 收敛：$\mathbb{E}|R_n|\to 0$
- 依概率收敛：对每个 $\varepsilon>0$，$\mathbb{P}(|R_n|\ge\varepsilon)\to 0$

### 课堂题 A 解答 ③④

**③ 三种收敛（条件：$\mathbb{E}[R_n^2]\le 4/n$）**

- $L^2$：$\mathbb{E}[R_n^2]\le 4/n\to 0$，直接由定义。
- $L^1$：由 ①，$0\le\mathbb{E}|R_n|\le 2/\sqrt{n}\to 0$。
- 依概率：由 ②，对每个固定 $\varepsilon>0$，$\mathbb{P}(|R_n|\ge\varepsilon)\le 4/(n\varepsilon^2)\to 0$。

$$
R_n \xrightarrow{\ L^2\ } 0 \ \Longrightarrow\ R_n \xrightarrow{\ L^1\ } 0 \ \Longrightarrow\ R_n \xrightarrow{\ P\ } 0
$$

两个箭头分别由 Cauchy–Schwarz 与 Markov 证明。

**④ 代入 $n=100$，$\varepsilon=0.5$**

$$
\mathbb{E}|R_{100}| \le \frac{2}{10} = 0.2,
\qquad
\mathbb{P}\big(|R_{100}|\ge 0.5\big) \le \frac{4}{100\times 0.5^2} = 0.16
$$

**两个都是严格上界**：对任何满足 $\mathbb{E}[R_{100}^2]\le 0.04$ 的分布都成立；实际误差可能小得多。

## Jensen 不等式：先平均还是先变换

**凸函数的定义**

$g$ 定义在区间 $I$ 上；对任意 $x, y\in I$，$\theta\in[0,1]$：

$$
g\big(\theta x + (1-\theta)y\big) \le \theta g(x) + (1-\theta)g(y)
$$

常用充分判据：若 $g''(x)\ge 0$ 处处成立，则 $g$ 是凸函数（凸函数不一定二次可导）。

**定理（Jensen）**

设 $g$ 为凸函数，且相关期望存在，则

$$
g(\mathbb{E}X)\ \le\ \mathbb{E}[g(X)]
$$

（图示：凸曲线 $g$、弦 $\mathbb{E}g(X)$ 与 $g(\mathbb{E}X)$ 的位置关系，$x_1 < \mathbb{E}X < x_2$。）

> **「先平均再变换」不超过「先变换再平均」（凸函数；凹函数方向相反）**

## 课堂题 B

**背景与已知**：对一个真实标签为 1 的固定样本，随机选择一个基模型进行预测。所选模型给出的正类概率记为 $Q$，其分布为

$$
\mathbb{P}(Q = 0.2) = 1/4,\qquad \mathbb{P}(Q = 0.8) = 3/4
$$

$$
\ell(q) = -\log q,\qquad \bar{q} = \mathbb{E}[Q]
$$

其中 $\bar{q}$ 是按相同权重进行**软投票**时的集成输出。

**问题**

1. 计算 $\mathbb{E}[Q]$，并解释它在模型集成中的含义。
2. 判断 $\ell(q) = -\log q$ 的凸性，并核对 Jensen 不等式的条件。

**可用知识**

- Jensen（期望形式，$g$ 凸）：$g(\mathbb{E}[X]) \le \mathbb{E}[g(X)]$；需要确认 $Q$ 落在 $g$ 的定义域内，并且相关期望有意义。
- **凸性判别**：若 $g$ 在区间 $I$ 上二阶可导且 $g''(x)\ge 0$，则 $g$ 在 $I$ 上为凸函数。

### 解析 ①②

**第一步：计算集成概率**

| $q$ | $\mathbb{P}(Q=q)$ |
|---|---|
| 0.2 | 1/4 |
| 0.8 | 3/4 |

$$
\mathbb{E}[Q] = 0.2\times 1/4 + 0.8\times 3/4 = 0.65
$$

软投票集成输出为 $\bar{q} = 0.65$。

**第二步：核对凸性和期望条件**

$$
\ell'(q) = -1/q,\qquad \ell''(q) = 1/q^2 > 0
$$

所以 $\ell$ 在 $(0,1)$ 上**严格凸**。本题中 $Q$ 只有两个正的有限取值，因此

$$
\mathbb{E}[Q] < \infty,\qquad \mathbb{E}|\ell(Q)| < \infty
$$

> 随机选一个模型时的平均损失是 $\mathbb{E}[\ell(Q)]$；软投票集成的损失是 $\ell(\mathbb{E}[Q])$。哪一个更小？

### 解析 ③

**条件重述**：真实标签为 1；随机选择的基模型概率为 $Q$，其中 $\mathbb{P}(Q=0.2)=1/4$，$\mathbb{P}(Q=0.8)=3/4$；损失 $\ell(q) = -\log q$；集成输出 $\bar{q} = \mathbb{E}[Q]$。

**③ 使用期望形式比较**

对应关系：$X = Q$，$g = \ell$（$\ell$ 为凸函数）。由 Jensen：

$$
\ell(\mathbb{E}[Q]) \le \mathbb{E}[\ell(Q)]
$$

两边分别计算：

$$
\ell(\mathbb{E}[Q]) = -\log(0.65) \approx 0.4308
$$

$$
\mathbb{E}[\ell(Q)] = 1/4[-\log 0.2] + 3/4[-\log 0.8] \approx 0.5697
$$

在这个随机模型选择机制下，**软投票的对数损失不超过随机选择一个基模型时的平均对数损失**。

（图：$\ell(q) = -\log q$ 曲线；$q=0.2$（概率 1/4）、$q=0.8$（概率 3/4）；随机选模型的平均损失（弦上）0.5697；软投票集成的损失（曲线上）$\ell(\mathbb{E}[Q])=0.4308$；差距 $\approx 0.1389$。）

## Mills 不等式：已知正态分布时的尾界

**定理（仅对 $Z\sim N(0,1)$）**

$\varphi$ 为标准正态密度，$t>0$。单侧：

$$
\mathbb{P}(Z\ge t) \le \frac{\varphi(t)}{t}
$$

由对称性乘 2，得双侧：

$$
\mathbb{P}(|Z|\ge t) \le \frac{2\varphi(t)}{t} = \sqrt{\frac{2}{\pi}}\,\frac{e^{-t^2/2}}{t}
$$

（图示：标准正态密度，两侧尾部面积之和 $\mathbb{P}(|Z|\ge 3)\approx 0.0027$。）

> **Mills 是对本身服从正态分布的变量的严格界。CLT 只给正态近似，不能把它直接变成样本均值的严格上界。**

## 同一事件 $|Z|\ge 3$：三个数的比较

$Z\sim N(0,1)$，事件 $\{|Z|\ge 3\}$（双侧）。同一事件下比较两种上界与精确值。

| 方法 | 额外使用的信息 | 数值 | 性质 |
|---|---|---|---|
| Chebyshev | 方差 | **0.111** | 严格上界 |
| Mills | 正态密度的形状 | **0.00295** | 严格上界 |
| 标准正态表 | 完整分布 | **0.00270** | 精确概率 |

**计算**：

$$
\mathbb{P}(|Z|\ge 3) \le \frac{1}{3^2} \approx 0.111
\qquad\qquad
\mathbb{P}(|Z|\ge 3) \le \sqrt{\frac{2}{\pi}}\,\frac{e^{-4.5}}{3} \approx 0.00295
$$

## 课堂题 C：100 次正态测量的平均误差

**背景与已知**：传感器独立测量 100 次，第 $i$ 次误差 $X_i\sim N(0,4)$（均值 0、方差 4），$X_1,\cdots,X_{100}$ 相互独立。

平均误差 $\bar{X} = \dfrac{1}{100}\sum_{i=1}^{100}X_i$。目标：$\mathbb{P}(|\bar{X}|\ge 0.4)$。

**问题**

1. 写出 $\bar{X}$ 的精确分布，并把事件标准化。
2. 分别用 Chebyshev、Mills 给出上界，再查表求精确概率。

**本题需要的公式**

- 独立正态的均值仍为正态：$\quad X_i \overset{\text{iid}}{\sim} N(\mu,\sigma^2)\ \Longrightarrow\ \bar{X}\sim N\Big(\mu,\ \dfrac{\sigma^2}{n}\Big)$
- Chebyshev（方差有限）：$\quad\mathbb{P}(|\bar{X}-\mu|\ge t)\le \dfrac{\mathrm{Var}(\bar{X})}{t^2}$
- Mills（仅对 $Z\sim N(0,1)$，$z>0$）：$\quad\mathbb{P}(|Z|\ge z)\le \dfrac{2\varphi(z)}{z}$
- **标准正态表（节选）**：$\varphi$、$\Phi$ 为标准正态的密度与分布函数，$\varphi(z) = e^{-z^2/2}/\sqrt{2\pi}$。
  $\Phi(1)\approx 0.8413$，$\Phi(2)\approx 0.9772$，$\Phi(3)\approx 0.9987$；$\varphi(1)\approx 0.2420$，$\varphi(2)\approx 0.0540$，$\varphi(3)\approx 0.0044$

### 课堂题 C 解答：标准化后比较三个数

**① 精确分布与标准化（用了独立性：方差相加）**

$$
\bar{X}\sim N\Big(0,\ \frac{4}{100}\Big) = N(0,\ 0.2^2),
\qquad
Z = \frac{\bar{X}}{0.2}\sim N(0,1),
\qquad
\{|\bar{X}|\ge 0.4\} = \{|Z|\ge 2\}
$$

| 方法 | 计算 | 数值 | 性质 |
|---|---|---|---|
| Chebyshev | $\dfrac{\mathrm{Var}(\bar{X})}{0.4^2} = \dfrac{0.04}{0.16}$ | **0.25** | 严格上界 |
| Mills | $\dfrac{2\varphi(2)}{2} = \varphi(2)$ | **≈ 0.0540** | 严格上界 |
| 精确（查表） | $2[1-\Phi(2)]$ | **≈ 0.0455** | 精确概率 |

Mills 只比真实值大约 19%；Chebyshev 只用了方差，大约是 5.5 倍。

### 课堂题 C（续）③：只知道均值和方差时

**条件改变**：仍是 100 次独立测量，每次误差均值 0、方差 4，但不知道是否服从正态。目标仍为 $\mathbb{P}(|\bar{X}|\ge 0.4)$。

③ 上一页的 0.25（Chebyshev）、0.0540（Mills）、0.0455（精确值）哪些仍严格有效？CLT 能给什么？

- **Chebyshev 0.25：仍严格有效。** 它只用 $\mathrm{Var}(\bar{X}) = 4/100$；这个方差的计算用了独立（两两不相关即可），不用正态。
- **Mills 0.0540：不能直接用。** Mills 要求 $Z$ 精确服从 $N(0,1)$；一般总体下 $\bar{X}/0.2$ 只是近似正态。
- **0.0455：只剩 CLT 近似。**

$$
\mathbb{P}(|\bar{X}|\ge 0.4)\approx 2[1-\Phi(2)]\approx 0.0455
\qquad (n\to\infty \text{ 时的极限；} n=100 \text{ 时没有误差保证})
$$

> **三类结论要分清**：精确概率（需完整分布）· 严格上界（只需部分信息）· 渐近近似（需 $n$ 大，不带保证）。

## 两类工具：期望关系与尾概率

**期望 / 变换关系**

- **Cauchy–Schwarz**：$\mathbb{E}[X^2], \mathbb{E}[Y^2]<\infty$；控制乘积的平均。
- **Jensen**：$g$ 凸且期望存在；比较「先平均」与「先变换」。

**尾事件的严格上界**

- **Markov**：$Y\ge 0$，$\mathbb{E}Y<\infty$。
- **Chebyshev**：$\mathrm{Var}(X)<\infty$。
- **Mills**：变量本身 $Z\sim N(0,1)$。

---

# 3.5 集中不等式与有限样本保证

## 同一尾事件：已知信息能改进多少

独立抛公平硬币 $n=100$ 次，$X_i\overset{\text{i.i.d.}}{\sim}\mathrm{Bernoulli}(0.5)$，$\bar{X}_{100}$ 为正面比例。所求事件：$\mathbb{P}(\bar{X}_{100}\ge 0.75)$。

**Markov：只用 $\bar{X}_{100}\ge 0$ 与均值**

$$
\mathbb{P}(\bar{X}_{100}\ge 0.75) \le \frac{\mathbb{E}\bar{X}_{100}}{0.75} = \frac{0.5}{0.75} \approx 0.667
$$

严格上界，但几乎没有信息。

**Chebyshev：再用方差**

$$
\mathrm{Var}(\bar{X}_{100}) = \frac{0.25}{100} = 0.0025
$$

$$
\mathbb{P}\big(|\bar{X}_{100} - 0.5|\ge 0.25\big) \le \frac{0.0025}{0.25^2} = 0.04
$$

事件 $\bar{X}_{100}\ge 0.75$ 包含于上式事件，所以上界为 0.04。

> 两个数都对 $n=100$ **严格成立**。Chebyshev 本身只需均值与方差；但本题算 $\mathrm{Var}(\bar{X}_{100}) = 0.25/100$ 时**已用了独立性**（两两不相关即足够）。两者都还没用到「有界」；Hoeffding 将再利用每次观测的取值范围。

## 指数化之前：Markov 怎样被重复使用

**Markov 本体：非负变量 + 均值**

$$
Y\ge 0\quad\Longrightarrow\quad \mathbb{P}(Y\ge a) \le \frac{\mathbb{E}Y}{a},\qquad a>0
$$

**Chebyshev：对平方偏差用 Markov；多要了二阶矩**

$$
\mathbb{P}(|X-\mu|\ge t) = \mathbb{P}\big((X-\mu)^2\ge t^2\big) \le \frac{\mathbb{E}(X-\mu)^2}{t^2} = \frac{\mathrm{Var}(X)}{t^2}
$$

> **思考**：如果现在还知道**独立性**与**有界性**，能否选一个更适合控制大偏差的非负变换？

## 为什么要指数化：对指数偏差用 Markov

**设定**：$T = S_n - \mathbb{E}S_n$，目标是上尾概率 $\mathbb{P}(T\ge t)$。注意 $T$ 可正可负，不能直接当作非负变量。

**指数变换：对任意 $\lambda>0$**

$$
\mathbb{P}(T\ge t) = \mathbb{P}\big(e^{\lambda T}\ge e^{\lambda t}\big) \le e^{-\lambda t}\,\mathbb{E}\,e^{\lambda T}
$$

- 指数函数递增，$\lambda>0$ 时两个事件相同；$e^{\lambda T}\ge 0$，可以用 Markov。
- **代价**：必须能控制指数矩 $\mathbb{E}\,e^{\lambda T}$（它可能是无穷）。控制住并选好 $\lambda$ 后，**才可能**得到指数型尾界。

> 过渡：对独立样本和，指数把「和」变成「积」。

## Chernoff 方法（一）：事件、指数化与 Markov

流程：**事件** → **指数化** → **Markov** → 独立 → 指数矩 → 优化

**记号**：$Y_i = X_i - \mathbb{E}X_i$，$T = \sum_{i=1}^n Y_i$；$t>0$；$\lambda>0$ 是可以选择的参数。

$$
\mathbb{P}\Big(\sum_{i=1}^{n} Y_i\ge t\Big) = \mathbb{P}\big(e^{\lambda\sum_i Y_i}\ge e^{\lambda t}\big)
\qquad \begin{matrix}\textbf{递增性}\\ \lambda>0\ \text{时事件不变}\end{matrix}
$$

$$
\le e^{-\lambda t}\ \mathbb{E}\big[e^{\lambda\sum_i Y_i}\big]
\qquad \begin{matrix}\textbf{Markov}\\ \text{指数项非负：} e^{\lambda T}\ge 0\end{matrix}
$$

> 到这里还没有用到独立性：任何随机变量 $T$ 都能走到这一步。

## Chernoff 方法（二）：独立性、指数矩与参数选择

流程：事件 → 指数化 → Markov → **独立** → **指数矩** → **优化**

接上页：$\mathbb{P}(T\ge t) \le e^{-\lambda t}\,\mathbb{E}\,e^{\lambda\sum_i Y_i}$，其中 $T = \sum_i Y_i$，$\lambda>0$。

**独立性：和变成积（只有这一步需要独立）**

$$
\mathbb{E}\big[e^{\lambda\sum_i Y_i}\big]\ \longrightarrow\ \prod_{i=1}^{n}\ \mathbb{E}\ e^{\lambda Y_i}
$$

**控制每个因子，再挑最好的 $\lambda$**

若已知条件给出 $\mathbb{E}\,e^{\lambda Y_i}\le M_i(\lambda)$，每个 $\lambda>0$ 都给一个上界；取下确界是挑其中最紧的。

$$
\mathbb{P}(T\ge t) \le \inf_{\lambda>0}\bigg\{ e^{-\lambda t}\prod_{i=1}^{n} M_i(\lambda) \bigg\}
$$

> 后面三种不等式只替换 $M_i(\lambda)$ 这一格。

## 只知道范围时，怎样控制指数矩

**输入：中心化 + 取值范围**

$Y_i = X_i - \mathbb{E}X_i$，$\mathbb{E}Y_i = 0$；$a_i\le Y_i\le b_i$ a.s.，区间宽度 $w_i = b_i - a_i$。

**引理（Hoeffding）**

$$
\mathbb{E}\,e^{\lambda Y_i} \le \exp\Big(\frac{\lambda^2 w_i^2}{8}\Big),\qquad \lambda\in\mathbb{R}
$$

（图示：$e^{\lambda x}$（凸）与 $[a,b]$ 上的弦；在 $[a,b]$ 内：曲线在弦下方；$X$ 的取值范围 $[a,b]$。弦线只依赖两个端点：这是「范围」进入指数矩的入口。）

## Hoeffding（一）：把引理代入通式

流程：事件 → 指数化 → Markov → 独立 → **指数矩** → 优化

**通用骨架**

$$
\mathbb{P}(T\ge t) \le \inf_{\lambda>0}\bigg\{ e^{-\lambda t}\prod_{i=1}^{n} M_i(\lambda) \bigg\}
$$

**这一格填 Hoeffding 引理**

$$
M_i(\lambda) = \exp\bigg(\frac{\lambda^2(b_i-a_i)^2}{8}\bigg)
\qquad
X_i\in[a_i,b_i]\ \text{a.s.；中心化不改变区间宽度。}
$$

**代入后**

$$
\mathbb{P}(T\ge t) \le \inf_{\lambda>0} \exp\bigg[-\lambda t + \frac{\lambda^2}{8}\sum_{i=1}^{n}(b_i-a_i)^2\bigg]
$$

## Hoeffding（二）：优化参数，得到上尾界

流程：事件 → 指数化 → Markov → 独立 → 指数矩 → **优化**

**对 $\lambda$ 求最小值**：记 $W = \sum_{i=1}^n (b_i-a_i)^2$，要最小化指数 $-\lambda t + \lambda^2 W/8$。

$$
-t + \frac{\lambda W}{4} = 0\ \Longrightarrow\ \lambda_* = \frac{4t}{W}
$$

$$
-\lambda_* t + \frac{\lambda_*^2 W}{8} = -\frac{2t^2}{W}
$$

**定理（Hoeffding，上尾单侧）**

$$
\mathbb{P}\big(S_n - \mathbb{E}S_n\ge t\big) \le \exp\Big(-\frac{2t^2}{W}\Big)
$$

**条件**：

- $X_1,\cdots,X_n$ **相互独立**
- $X_i\in[a_i,b_i]$ a.s.，区间事先确定
- $t>0$；$W = \sum_{i=1}^{n}(b_i-a_i)^2$
- **不要求同分布，也不需要方差**

## Hoeffding：双侧界由两个单侧界相加

**条件与记号（与单侧相同）**：$X_1,\cdots,X_n$ 相互独立，$X_i\in[a_i,b_i]$ a.s.，$t>0$；$W = \sum_{i=1}^n (b_i-a_i)^2$。

$$
\{|S_n - \mathbb{E}S_n|\ge t\} = \{S_n - \mathbb{E}S_n\ge t\}\cup\{S_n - \mathbb{E}S_n\le -t\}
$$

**双侧结论**

$$
\mathbb{P}\big(|S_n - \mathbb{E}S_n|\ge t\big) \le 2\exp\Big(-\frac{2t^2}{W}\Big)
$$

## Hoeffding：样本均值形式

**从样本和到样本均值**：$X_1,\cdots,X_n$ 相互独立，同一区间 $X_i\in[a,b]$ a.s.；取 $t = n\varepsilon$，此时 $W = n(b-a)^2$。

**单侧**

$$
\mathbb{P}\big(\bar{X}_n - \mathbb{E}\bar{X}_n\ge\varepsilon\big) \le \exp\bigg(-\frac{2n\varepsilon^2}{(b-a)^2}\bigg)
$$

$$
\mathbb{P}\big(|\bar{X}_n - \mathbb{E}\bar{X}_n|\ge\varepsilon\big) \le 2\exp\bigg(-\frac{2n\varepsilon^2}{(b-a)^2}\bigg)
$$

**Bernoulli 特例**：独立 $X_i\sim\mathrm{Bernoulli}(p)$ 时 $\mathbb{E}\bar{X}_n = p$、$b-a = 1$，单侧界为 $e^{-2n\varepsilon^2}$，双侧界为 $2e^{-2n\varepsilon^2}$。

## 练习：硬币问题

**题目**：$X_1,\cdots,X_{100}$ 相互独立，均服从 $\mathrm{Bernoulli}(1/2)$；$\bar{X}_{100}$ 是这 100 次抛掷的正面比例。

求 $\mathbb{P}(\bar{X}_{100}\ge 0.75)$ 的**严格上界**。

1. 核对 Hoeffding 的条件：独立性、取值范围、中心、单侧还是双侧。
2. 分别用 Markov、Chebyshev、Hoeffding 求上界，并说明各用了哪些信息。

**三种工具：条件与公式**

- **Markov**　非负 + 均值（$Y\ge 0,\ a>0$）：$\mathbb{P}(Y\ge a)\le\dfrac{\mathbb{E}Y}{a}$
- **Chebyshev**　再加方差（$t>0$）：$\mathbb{P}(|Y - \mathbb{E}Y|\ge t)\le\dfrac{\mathrm{Var}(Y)}{t^2}$
- **Hoeffding**　独立 + 有界：$X_i$ 相互独立，$X_i\in[a,b]$（样本均值、单侧）：

$$
\mathbb{P}\big(\bar{X}_n - \mathbb{E}\bar{X}_n\ge\varepsilon\big)\le\exp\bigg(-\frac{2n\varepsilon^2}{(b-a)^2}\bigg)
$$

### 解答 ①：先核对 Hoeffding 的条件

**题目重述**：$X_1,\cdots,X_{100}$ 独立同分布 $\mathrm{Bernoulli}(1/2)$（公平硬币，正面记 1），$\bar{X}_{100}$ 为正面比例；求 $\mathbb{P}(\bar{X}_{100}\ge 0.75)$ 的严格上界。

**① 条件逐条核对**

- **独立**：各次抛掷相互独立 ✓
- **范围**：$X_i\in[0,1]$，区间事先已知，宽度 $b-a = 1$ ✓
- **中心**：$\mathbb{E}\bar{X}_{100} = 0.5$，事件 $= \{\bar{X}_{100} - 0.5\ge 0.25\}$，$\varepsilon = 0.25$
- **方向**：只问上尾 $\Longrightarrow$ **单侧**，不乘 2

**本题需要的公式**：Hoeffding（样本均值、单侧）。条件：$X_i$ 相互独立，$X_i\in[a,b]$ a.s.

$$
\mathbb{P}\big(\bar{X}_n - \mathbb{E}\bar{X}_n\ge\varepsilon\big)\le\exp\bigg(-\frac{2n\varepsilon^2}{(b-a)^2}\bigg)
$$

### 硬币问题解答 ②：同一事件的三个严格上界

Hoeffding 代入 $n=100$，$\varepsilon = 0.25$，$b-a=1$：

$$
\mathbb{P}(\bar{X}_{100}\ge 0.75)\le\exp(-2\times 100\times 0.25^2) = e^{-12.5}\approx 3.7\times 10^{-6}
$$

| 方法 | 用到的信息 | 上界 |
|---|---|---|
| Markov | 非负 + 均值 0.5 | **0.5/0.75 ≈ 0.667** |
| Chebyshev | + 方差 0.25/100（推导用了独立） | **0.04** |
| Hoeffding | 独立 + 有界 [0,1] | **≈ 3.7 × 10⁻⁶** |
| 精确（二项分布） | 完整分布 | **≈ 2.8 × 10⁻⁷** |

前三行都是对 $n=100$ **严格成立**的上界，差别来自所用信息；最后一行是精确概率。

随 $n$ 变化：Chebyshev 界 $4/n$，$n$ 翻倍只减半；Hoeffding 界 $e^{-n/8}$，$n$ 翻倍变为平方。

## Bernstein（一）：方差怎样进入指数矩

流程：事件 → 指数化 → Markov → 独立 → **指数矩** → 优化

**Markov 行（不变）**

$$
\mathbb{P}\Big(\sum_{i=1}^{n}Y_i\ge t\Big) \le e^{-\lambda t}\,\mathbb{E}\,e^{\lambda\sum_i Y_i}
$$

**这次多知道什么**

独立；$\mathbb{E}Y_i = 0$；$|Y_i|\le M$ a.s.；方差和 $\nu = \sum_{i=1}^{n}\mathrm{Var}(X_i)$。

**指数矩控制式（$0<\lambda<3/M$）**

$$
\mathbb{E}\,e^{\lambda\sum_i Y_i} \le \exp\bigg(\frac{\lambda^2\nu}{2(1 - \lambda M/3)}\bigg)
$$

## Bernstein（二）：上尾界

流程：事件 → 指数化 → Markov → 独立 → 指数矩 → **优化**

**代入，并选一个 $\lambda$**：把指数矩界代入 Markov 行，取

$$
\lambda = \frac{t}{\nu + Mt/3}
$$

它满足 $0<\lambda<3/M$，给出一个合法的上界（**不声称恰好最优**）。

**定理（Bernstein，上尾单侧）**

$$
\mathbb{P}\Big(\sum_{i=1}^{n}Y_i\ge t\Big) \le \exp\bigg[-\frac{t^2}{2(\nu + Mt/3)}\bigg]
$$

**条件**：

- $X_i$ 相互独立，$Y_i = X_i - \mathbb{E}X_i$
- $|Y_i|\le M$ a.s.（中心化后的界）
- $\nu = \sum_{i=1}^{n}\mathrm{Var}(X_i)$，$t>0$
- 下尾同理；双侧乘 2

## 判断题

**背景与已知**：抛一次公平硬币得 $B\sim\mathrm{Bernoulli}(1/2)$，然后令 $X_1 = X_2 = \cdots = X_n = B$。

（就像把同一条数据复制 $n$ 份，当作 $n$ 个样本。）

每个 $X_i\in[0,1]$，$\mathbb{E}X_i = 1/2$；$\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$。

**问题**

1. $\bar{X}_n$ 等于什么？
2. 精确计算 $\mathbb{P}(\bar{X}_n - 1/2\ge 1/4)$。

**对照用的公式**：对照：Hoeffding 的条件是 $X_1,\cdots,X_n$ **相互独立**，$X_i\in[a,b]$ a.s.；此时

$$
\mathbb{P}(\bar{X}_n - \mathbb{E}\bar{X}_n\ge\varepsilon)\le e^{-2n\varepsilon^2/(b-a)^2}
$$

### 判断题解答 ①②

**① 样本均值**

$$
\bar{X}_n = \frac{1}{n}\sum_{i=1}^{n}B = B
$$

$n$ 个「样本」只携带一次抛掷的信息。

**② 精确概率**

$$
\mathbb{P}\Big(\bar{X}_n - \frac{1}{2}\ge\frac{1}{4}\Big) = \mathbb{P}\Big(B\ge\frac{3}{4}\Big) = \mathbb{P}(B = 1) = \frac{1}{2}
$$

**结论**：对**每一个** $n$，这个概率都是 ½；增加「样本」完全没有用。

### 判断题（续）③④

**条件重述**：$X_1 = \cdots = X_n = B\sim\mathrm{Bernoulli}(1/2)$，$X_i\in[0,1]$；已得 $\bar{X}_n = B$，$\mathbb{P}(\bar{X}_n - 1/2\ge 1/4) = 1/2$。

③ 能否直接使用 Hoeffding？若硬套，会得到什么？
④ $\bar{X}_n$ 是否依概率收敛到 1/2？

**③ 不能。** $X_i$ 完全相依，违反「相互独立」。硬套得 $\exp(-2n\cdot 1/16) = e^{-n/8}$；$n\ge 6$ 时 $e^{-n/8} < 1/2$，「上界」竟小于真实概率——矛盾。

**④ 不收敛。** $|B - 1/2| = 1/2$ 恒成立，故 $\mathbb{P}(|\bar{X}_n - 1/2|\ge 1/4) = 1 \not\to 0$。

（图示：精确概率 $= 1/2$（水平线）与硬套 Hoeffding 的 $e^{-n/8}$（虚线）随 $n$ 变化；$n\ge 6$ 时「上界」低于真实概率；横轴为样本个数 $n$。）

## Chernoff 界（一）：Bernoulli 的指数矩

流程：事件 → 指数化 → Markov → 独立 → **指数矩** → 优化

**适用对象**

独立 $X_i\sim\mathrm{Bernoulli}(p_i)$（$p_i$ 可以不同）；$S = \sum_{i=1}^n X_i$，$\mu = \mathbb{E}S = \sum_{i=1}^n p_i$。

**单项指数矩：先精确，再放大**

$$
\mathbb{E}\,e^{\lambda X_i} = 1 + p_i\big(e^{\lambda} - 1\big)\ \le\ \exp\{p_i(e^{\lambda} - 1)\}
$$

（红注：不等式：用了 $1 + u\le e^u$。）

**独立求积**

$$
\mathbb{E}\,e^{\lambda S} = \prod_{i=1}^{n}\ \mathbb{E}\ e^{\lambda X_i} \le \exp\{\mu(e^{\lambda} - 1)\}
$$

## Chernoff 界（二）：乘法型上尾式

流程：事件 → 指数化 → Markov → 独立 → 指数矩 → **优化**

**代入通用方法（$\delta>0$）**

$$
\mathbb{P}\big(S\ge (1+\delta)\mu\big) \le \inf_{\lambda>0}\exp\{-\lambda(1+\delta)\mu + \mu(e^{\lambda} - 1)\}
$$

取 $e^{\lambda} = 1+\delta$，即 $\lambda = \log(1+\delta) > 0$。

**乘法型 Chernoff 上尾界（$\delta>0$）**

$$
\mathbb{P}\big(S\ge (1+\delta)\mu\big) \le \bigg[\frac{e^{\delta}}{(1+\delta)^{1+\delta}}\bigg]^{\mu}
$$

用了真实的 $p_i$，但经过一次放宽，所以仍是上界而不是精确概率。

## Chernoff 界：下尾与简化式的适用范围

**上尾**

- 乘法式原式（$\delta>0$）：

$$
\mathbb{P}\big(S\ge (1+\delta)\mu\big) \le \bigg[\frac{e^{\delta}}{(1+\delta)^{1+\delta}}\bigg]^{\mu}
$$

- 简化式（仅 $0<\delta\le 1$）：

$$
\mathbb{P}\big(S\ge (1+\delta)\mu\big) \le e^{-\mu\delta^2/3}
$$

**下尾**

- 乘法式原式（$0<\delta<1$）：

$$
\mathbb{P}\big(S\le (1-\delta)\mu\big) \le \bigg[\frac{e^{-\delta}}{(1-\delta)^{1-\delta}}\bigg]^{\mu}
$$

- 简化式（$0<\delta<1$）：

$$
\mathbb{P}\big(S\le (1-\delta)\mu\big) \le e^{-\mu\delta^2/2}
$$

> **范围和公式一起记**：上尾简化式只在 $0<\delta\le 1$ 时使用；$\delta>1$ 时回到乘法式原式。

## 练习：众包标注的错误条数

**题目**：1000 条数据各有相互独立的标注错误指示变量 $X_i\sim\mathrm{Bernoulli}(0.01)$；$S = \sum_{i=1}^{1000}X_i$ 为错误条数。求 $\mathbb{P}(S\ge 30)$ 的上界。

1. 求 $\mu$、$\delta$，并判断上尾简化式是否适用。
2. 计算 Hoeffding 上界。
3. 计算 Bernstein 与乘法型 Chernoff 上界，并比较三者。

**可用方法：输入与公式**

- **Hoeffding**　独立 + 范围 $[0,1]$：$\mathbb{P}(\bar{X} - \mathbb{E}\bar{X}\ge\varepsilon)\le e^{-2n\varepsilon^2}$
- **Bernstein**　$Y_i$ 独立，$\mathbb{E}Y_i = 0$，$|Y_i|\le M$，$\nu = \sum\mathrm{Var}(Y_i)$：

$$
\mathbb{P}\Big(\sum_i Y_i\ge t\Big)\le\exp\bigg(-\frac{t^2}{2(\nu + Mt/3)}\bigg)
$$

- **Chernoff**　独立 Bernoulli 之和 $S$，$\mu = \mathbb{E}S$，$\delta>0$：

$$
\mathbb{P}\big(S\ge (1+\delta)\mu\big)\le\bigg[\frac{e^{\delta}}{(1+\delta)^{1+\delta}}\bigg]^{\mu}
\qquad
\text{简化式（仅当 } 0<\delta\le 1\text{）：}\ \mathbb{P}\big(S\ge (1+\delta)\mu\big)\le e^{-\mu\delta^2/3}
$$

### 解答 ①②：参数与 Hoeffding

**① 参数与适用范围**

$$
\mu = 1000(0.01) = 10,\qquad \delta = \frac{30 - 10}{10} = 2 > 1
$$

$\delta>1$，所以简化式 $\exp(-\mu\delta^2/3)$ **不在保证范围内**；上尾要用乘法式原式。

**② Hoeffding（$n = 1000$，$\varepsilon = 0.02$）**

$$
\mathbb{P}\big(\bar{X} - 0.01\ge 0.02\big)\le e^{-2(1000)(0.02)^2} = e^{-0.8}\approx 0.449
$$

### 解答 ③：Bernstein 与 Chernoff

**Bernstein（$t = 20$，$\nu = 1000(0.01)(0.99) = 9.9$，$M = 0.99$）**

$$
\mathbb{P}(S - 10\ge 20)\le\exp\bigg[-\frac{20^2}{2(9.9 + 0.99\cdot 20/3)}\bigg]\approx 5.44\times 10^{-6}
$$

**乘法型 Chernoff 原式（$\mu = 10$，$\delta = 2$）**

$$
\mathbb{P}(S\ge 30)\le\bigg(\frac{e^2}{3^3}\bigg)^{10}\approx 2.36\times 10^{-6}
$$

**本题结论**：Chernoff 最小，Bernstein 接近，Hoeffding（0.449）很松——Bernoulli 概率已知，且事件在远上尾。三个数都是严格上界。

## McDiarmid 不等式：样本和之外的函数

Hoeffding 处理独立变量的**和**；这里的 $f$ **不必是和**，只看替换一个输入时 $f$ 最多变多少。

**定理（有界差分不等式）**

条件：$X_1,\cdots,X_n$ **相互独立**；只改第 $i$ 个输入，$f$ 的变化不超过 $c_i$：

$$
\sup_{x_1,\cdots,x_n,x_i'}\big|f(\cdots,x_i,\cdots) - f(\cdots,x_i',\cdots)\big| \le c_i
$$

$$
\mathbb{P}\big(|f(X) - \mathbb{E}f(X)|\ge t\big) \le 2\exp\bigg(-\frac{2t^2}{\sum_{i=1}^{n}c_i^2}\bigg)
$$

（图示：输入 $x_1, x_2, x_3', x_4, x_5$，替换 $x_3$ 后 $f$ 至多变 $c_3$；只改 $x_3$ 一个输入，$f$ 最多变 $c_3$；把所有 $c_i$ 平方后再求和。）

**检验：$f$ 为样本均值，独立 $X_i\in[0,1]$**

$$
c_i = \frac{1}{n},\qquad \sum_i c_i^2 = \frac{1}{n}
\ \Longrightarrow\
\mathbb{P}\big(|\bar{X}_n - \mathbb{E}\bar{X}_n|\ge t\big)\le 2e^{-2nt^2}
\qquad (\text{即 Hoeffding})
$$

## 模型给猫狗打分，怎样判断排得好不好？

模型已训练好，给每张图一个「像猫的程度」得分，**越高越像猫**。用新图片评估，**不重新训练**。

| 图片（真实身份） | 记号 | 猫类评分 |
|---|---|---|
| 猫 1（正例） | P1 | 0.90 |
| 猫 2（正例） | P2 | 0.60 |
| 狗 1（负例） | N1 | 0.80 |
| 狗 2（负例） | N2 | 0.50 |
| 狗 3（负例） | N3 | 0.30 |

- **正例**：真实是猫，共 m 张（本例 m = 2）
- **负例**：真实是狗，共 r 张（本例 r = 3）
- **得分**：越大越像猫；分高 ≠ 分类一定对

- 猫 1：$0.90 > 0.80$ 狗 1 → **排对 1 分**
- 猫 2：$0.60 < 0.80$ 狗 1 → **排错 0 分**

**AUC（Area Under the ROC Curve）衡量**：随机拿一只猫和一只狗，模型有多大可能把猫排在狗前面？

## 6 次配对怎样变成 AUC？

**规则**：猫分高于狗记 1，低于记 0，相同记 1/2。

| | 狗 1：0.80 | 狗 2：0.50 | 狗 3：0.30 |
|---|---|---|---|
| **猫 1：0.90** | **1**（0.90 > 0.80） | 1 | 1 |
| **猫 2：0.60** | **0**（0.60 < 0.80） | 1 | 1 |

**把 6 格加起来**

$$
\widehat{\mathrm{AUC}} = \frac{1+1+1+0+1+1}{2\times 3} = \frac{5}{6}\approx 0.833
$$

**一般写法**

$$
h_{ij} = \mathbf{1}\{s_i^{+} > s_j^{-}\} + 1/2\,\mathbf{1}\{s_i^{+} = s_j^{-}\}
$$

$$
\widehat{\mathrm{AUC}} = \frac{1}{mr}\sum_{l=1}^{m}\sum_{j=1}^{r} h_{ij},\qquad 0\le h_{ij}\le 1
$$

> 6 次猫狗配对中，5 次猫排在狗前面，所以经验 AUC = 5/6。它**不是**「5 张图片分类正确」：图片只有 5 张，比较有 6 对。

## 替换一只猫，为什么最多影响一行？

同一个固定模型；只把 **猫 2（0.60）** 换成另一张猫图 **猫 2′（0.20）**，其余 4 张不变。

| 原来 | 狗 1：0.80 | 狗 2：0.50 | 狗 3：0.30 |
|---|---|---|---|
| 猫 1：0.90 | 1 | 1 | 1 |
| 猫 2：0.60 | 0 | 1 | 1 |

经验 AUC = 5/6

| 替换猫 2 之后 | 狗 1：0.80 | 狗 2：0.50 | 狗 3：0.30 |
|---|---|---|---|
| 猫 1：0.90 | 1 | 1 | 1 |
| 猫 2′：0.20 | 0 | 0 | 0 |

经验 AUC′ = 3/6

**本次实际变化**：$\Big|\dfrac{5}{6} - \dfrac{3}{6}\Big| = \dfrac{2}{6} = \dfrac{1}{3}$（只动了第二行的 3 格）

- **换一只猫：只影响一行（r 格）**：$\quad|\Delta\widehat{\mathrm{AUC}}|\le\dfrac{r\times 1}{mr} = \dfrac{1}{m}$（本例 m = 2：上界 1/2，实际 1/3）
- **换一只狗：只影响一列（m 格）**：$\quad|\Delta\widehat{\mathrm{AUC}}|\le\dfrac{m\times 1}{mr} = \dfrac{1}{r}$（这是最坏情况的上界）

## 为什么 AUC 能用 McDiarmid，却不能把配对当独立？

评分模型**预先固定**；m 只猫、r 只狗**相互独立**地抽取。经验 AUC 是这 **m + r 个独立输入** 的函数。

**6 个格子不独立**

（表：猫 1 行的 $h_{11}$、$h_{12}$ 用橙色框出）$h_{11}$、$h_{12}$ 都用到了**猫 1** 的评分。不能把 $mr$ 当作 Hoeffding 的独立样本量。

**把 $c_i$ 平方后相加**

$$
\sum_{k=1}^{m+r} c_k^2 = m\Big(\frac{1}{m}\Big)^2 + r\Big(\frac{1}{r}\Big)^2 = \frac{1}{m} + \frac{1}{r}
$$

**代入 McDiarmid**

$$
\mathbb{P}\big(\big|\widehat{\mathrm{AUC}} - \mathbb{E}\widehat{\mathrm{AUC}}\big|\ge t\big)\le 2\exp\bigg(-\frac{2t^2}{1/m + 1/r}\bigg)
$$

**大样本例子：m = 1000，r = 2000，δ = 0.05**

$$
t = \sqrt{\frac{(1/m + 1/r)\log(2/\delta)}{2}}\approx 0.0526
\qquad
\mathbb{P}\big(\big|\widehat{\mathrm{AUC}} - \mathrm{AUC}_{\mathrm{pop}}\big|\le 0.0526\big)\ge 0.95
$$

$\mathbb{E}[\text{经验 AUC}]$ 等于 **固定模型的总体 AUC（AUC_pop）**。

## 只换一张训练图片，模型会变多少？

刚才模型固定、只换验证图片；现在换的是**训练**图片：两份训练集各 1000 张，**999 张相同**，只替换第 100 张，分别重新训练。

```
训练集 S（1000 张） —训练→ 模型 A(S) —同一张测试图→ 猫的概率 0.80
        ↓ 只替换 1 张
训练集 S′（999 张相同）—训练→ 模型 A(S) —同一张测试图→ 猫的概率 ？
```

- **算法甲（示意）：0.80 → 0.79**　输出几乎不变
- **算法乙（示意）：0.80 → 0.20**　输出变化很大

> **训练样本只动一点，模型的表现会不会大变？—— 这就是算法稳定性的直觉**

## 算法稳定性：把「变化小」写成数学条件

**比较三样东西**

1. 原训练集 S；只替换第 $i$ 条：$S^{(i)}$
2. 用**同一条**新样本 $z$ 分别测试 $A(S)$ 与 $A(S^{(i)})$
3. 比较两次的**损失 $\ell$**，不比较参数，也不只看一张图的概率

**定义：替换样本型 uniform stability**

$$
\big|\ell(A(S), z) - \ell(A(S^{(i)}), z)\big| \le \beta_n
$$

对**所有**只差一个样本的 $S$、$S^{(i)}$，以及**所有**测试样本 $z$ 都成立；损失取值在 $[0,1]$。

$\beta_n$ 越小，算法受单条训练样本影响的**最坏情形**越小。

> **稳定 ≠ 准确**：$\beta_n$ 控制的是「受单条数据影响多大」，不是模型成绩本身。

## 训练得好，就一定预测得好吗？

模型在训练集上答得好，不代表遇到**新的同分布数据**仍然一样好。

**训练平均损失（做过的题）**

$$
R_S\big(A(S)\big) = \frac{1}{n}\sum_{j=1}^{n}\ \ell\big(A(S), Z_j\big)
$$

**真实平均损失（同类新题）**

$$
R\big(A(S)\big) = \mathbb{E}_{Z\sim P}\ \ell\big(A(S), Z\big)
$$

（$Z$ 是独立于训练集的新样本）

$$
G(S) = R\big(A(S)\big) - R_S\big(A(S)\big)
$$

训练集一变，模型可能变，**G(S) 也跟着变**；它是 S 的函数，G(S) 可正可负。

## 稳定性怎样变成有界差分？

条件：$0\le\ell\le 1$；算法满足替换稳定性 $\beta_n$；$S$ 与 $S^{(i)}$ 只有第 $i$ 项不同。

**① 真实平均损失**

$$
\Big|R\big(A(S)\big) - R\big(A(S^{(i)})\big)\Big| \le \beta_n
\qquad \text{每个新样本 } z \text{ 至多变 } \beta_n\text{，取期望也如此}
$$

**② 训练平均损失**

$$
\Big|R_S\big(A(S)\big) - R_{S^{(i)}}\big(A(S^{(i)})\big)\Big|
\le \frac{n-1}{n}\beta_n + \frac{1}{n} \le \beta_n + \frac{1}{n}
$$

（图示：灰 $n-1$ 项：各至多变 $\beta_n$；橙 1 项（被替换）：至多变 1。）

**③ 两项相减**

$$
\big|G(S) - G(S^{(i)})\big| \le 2\beta_n + \frac{1}{n}
\qquad \textbf{这就是 McDiarmid 需要的 } \mathbf{c_i}
$$

注意：**不是** $c_i = \beta_n$——泛化间隙同时包含真实损失和训练损失两部分。

## 为什么还需要控制平均泛化误差？

**单次训练**：训练集 $S = (Z_1,\cdots,Z_n)\sim P^n$ 随机抽取，算法 $A$ 用 $S$ 训练模型，这一次的泛化间隙为

$$
G(S) = R\big(A(S)\big) - R_S\big(A(S)\big)
$$

**反复抽取训练集、每次重新训练、再取平均**：对所有可能抽到的 $S$ 求平均，得到期望泛化间隙（平均泛化误差）：

$$
\mathbb{E}_S\,G(S) = \mathbb{E}_S\big[R\big(A(S)\big) - R_S\big(A(S)\big)\big]
$$

于是对任意 $t>0$，McDiarmid 给出：

$$
\mathbb{P}\big(\big|G(S) - \mathbb{E}_S\,G(S)\big|\ge t\big) \le 2\exp\bigg(-\frac{2t^2}{n(2\beta_n + 1/n)^2}\bigg)
$$

这保证 $G(S)$ **集中在它自己的期望附近**，并不单独保证 $\mathbb{E}_S G(S)$ 很小。

（图示：波动小，但中心离 0 较远；波动小，中心也接近 0。概念示意，非实验数据；$0\le\ell\le 1\ \Rightarrow\ G(S)\in[-1,1]$。）

$$
|G(S)| \le |G(S) - \mathbb{E}_S\,G(S)| + |\mathbb{E}_S\,G(S)|
\qquad \textbf{波动小 + 期望接近 0，才能得到泛化间隙接近 0。}
$$

## 期望泛化间隙怎样改写？

**设定**：$Z_1,\cdots,Z_n$ 独立同分布 $\sim P$，$S = (Z_1,\cdots,Z_n)$；再取与 $S$ 独立的复制样本 $Z_i'\sim P$。

**构造替换**：把第 $i$ 个样本换成独立复制样本

$$
S^{(i)} = (Z_1,\cdots,Z_{i-1},\,Z_i',\,Z_{i+1},\cdots,Z_n)
$$

（图示：S 行第 $i$ 位为 $z$，$S^{(i)}$ 行第 $i$ 位为 $z'$。）

**期望改写**

$$
\mathbb{E}_S\,R\big(A(S)\big) = \mathbb{E}_{S,Z_i'}\ \ell\big(A(S), Z_i'\big)
\qquad \text{真实风险：} Z_i' \text{ 与 } S \text{ 独立，对 } Z_i' \text{ 取期望就得到 } R(A(S))。
$$

$$
\mathbb{E}_{S,Z_i'}\ \ell\big(A(S^{(i)}), Z_i\big) = \mathbb{E}_S\ \ell\big(A(S), Z_i\big)
\qquad \text{训练损失的第 } i \text{ 项：右边是它的期望；等号来自下方的同分布关系。}
$$

**两式代入 G(S) 的定义**

$$
\mathbb{E}_S\,G(S) = \frac{1}{n}\sum_{i=1}^{n}\ \mathbb{E}_{S,Z_i'}\Big[\ell\big(A(S), Z_i'\big) - \ell\big(A(S^{(i)}), Z_i\big)\Big]
$$

$$
\big(S^{(i)}, Z_i\big)\ \overset{d}{=}\ \big(S, Z_i\big)
\qquad \textbf{为什么第二项能替换？}
$$

$S^{(i)}$ 中的 $Z_i'$ 恰是第 $i$ 个训练样本，其余坐标仍独立同分布 $\sim P$，故 $(S^{(i)}, Z_i)$ 与 $(S, Z_i)$ 同分布。注意：这里的 $Z_i$ 在训练集之内；只有 $(S, Z_i)$ 中的 $Z_i'$ 才独立于训练集。

## 为什么稳定性控制期望泛化间隙？

**回顾** uniform replacement stability：对任意只差一个训练样本的 $S$、$S^{(i)}$，以及任意测试样本 $z$：

$$
\big|\ell(A(S), z) - \ell(A(S^{(i)}), z)\big| \le \beta_n
$$

特别地，取测试点 $z = Z_i'$：

$$
\big|\ell(A(S), Z_i') - \ell(A(S^{(i)}), Z_i')\big| \le \beta_n
$$

$$
\big|\mathbb{E}_S\,G(S)\big|
= \bigg|\frac{1}{n}\sum_{i=1}^{n}\ \mathbb{E}_{S,Z_i'}\Big[\ell\big(A(S), Z_i'\big) - \ell\big(A(S^{(i)}), Z_i'\big)\Big]\bigg|
$$

$$
\le \frac{1}{n}\sum_{i=1}^{n}\ \mathbb{E}_{S,Z_i'}\ \Big|\ell\big(A(S), Z_i'\big) - \ell\big(A(S^{(i)}), Z_i'\big)\Big|
$$

$$
\le \frac{1}{n}\sum_{i=1}^{n}\beta_n = \beta_n
$$

$$
\boxed{\ \big|\mathbb{E}_S\,G(S)\big| \le \beta_n\ }
\qquad \textbf{只要满足 iid 抽样和 uniform replacement stability，期望泛化间隙自动受控。}
$$

## McDiarmid 给出怎样的泛化保证？

每次替换一个训练样本，G(S) 最多变化 $c_i = 2\beta_n + 1/n$（共 $n$ 个输入），代入 McDiarmid：

$$
\mathbb{P}\big(\big|G(S) - \mathbb{E}_S\,G(S)\big|\ge t\big)\le 2\exp\bigg(-\frac{2t^2}{n(2\beta_n + 1/n)^2}\bigg)
$$

$$
\Big\downarrow\qquad
t = (2\beta_n + 1/n)\sqrt{\frac{n}{2}\log\frac{2}{\delta}} = (2n\beta_n + 1)\sqrt{\frac{\log(2/\delta)}{2n}}
$$

（右注：令右侧 $=\delta$，解出 $t$；再用前两页已证的 $|\mathbb{E}_S G(S)|\le\beta_n$ 与三角不等式，得到下式：）

$$
\mathbb{P}\Bigg(\big|R\big(A(S)\big) - R_S\big(A(S)\big)\big| \le \beta_n + (2n\beta_n + 1)\sqrt{\frac{\log(2/\delta)}{2n}}\Bigg) \ge 1-\delta
$$

当 $\beta_n$ 足够小（例如 $\beta_n = O(1/n)$），训练损失与真实平均损失之差，获得**随 $n$ 增大而收紧**的高概率上界。概率针对的是随机抽到的训练集 $S$。

## 训练数据越多，保证会更好吗？

假设某确定性算法满足 $\beta_n = 1/n$，损失在 $[0,1]$，要求失败概率 $\delta = 0.05$。

$$
|G(S)| \le \frac{1}{n} + 3\sqrt{\frac{\log 40}{2n}}
\qquad (\text{至少 95\% 的概率})
$$

| | |
|---|---|
| n = 1000 | $\|G\| \le 0.1298$ |
| n = 10000 | $\|G\| \le 0.0408$ |

**样本量增加 10 倍，界明显收紧**（约按 $1/\sqrt{n}$）。

它是**上界**，不是实际误差；也不意味着模型一定准确。

## 从 McDiarmid 到 SGD

> **最难的往往不是代入 McDiarmid，而是证明训练算法足够稳定**

**Stability and Generalization（JMLR）**：算法具有 uniform stability 时，借助集中不等式得到泛化保证；其中**直接使用 McDiarmid** 得到高概率界。

**Train Faster, Generalize Better: Stability of SGD（ICML）**：分析 SGD 迭代，证明适当条件下的**期望型**稳定性，进而得到**期望**泛化保证。

**训练数据变化 → 损失变化受控 → 泛化有保证**

## 课后习题

**题目**：固定一个已训练好的大模型。从同一个题目分布中相互独立地随机抽取 $n = 1000$ 道题，每题答对记 $X_i = 1$，答错记 0。样本准确率：

$$
\hat{p} = \frac{1}{n}\sum_{i=1}^{n}X_i
$$

观测：**850 道答对**，$\hat{p}_{\mathrm{obs}} = 0.85$。真实准确率 $p = \mathbb{E}\hat{p}$，即从题目分布随机抽一题时答对的概率。

约定：模型、生成与判分规则固定，各 $X_i$ 独立同分布。

**三问**

1. 只替换其中一道题，$\hat{p}$ 最多改变多少？
2. 用 McDiarmid 求 $t$，使 $\mathbb{P}(|\hat{p} - p|\ge t)\le 0.05$。

**可用知识：McDiarmid 不等式**

$Z_1,\cdots,Z_n$ 相互独立；只替换第 $i$ 个输入时，函数 $f$ 至多变化 $c_i$，则：

$$
\mathbb{P}\big(|f - \mathbb{E}f|\ge t\big)\le 2\exp\bigg(-\frac{2t^2}{\sum_{i=1}^{n}c_i^2}\bigg)
$$

**提示**

- 取 $f = \hat{p}$，先求 $c_i$。
- 令右侧 $= 0.05$，解出 $t$。

### 解析 ①②：有界差分与误差上界

**① 有界差分：只替换一道题**

其余 999 道题不变，且 $X_i, X_{i'}\in\{0,1\}$，所以：

$$
|\hat{p} - \hat{p}'| = \frac{|X_i - X_{i'}|}{n} \le \frac{1}{n}
$$

$$
\boxed{c_i = \frac{1}{1000}},\qquad
\boxed{\sum_{i=1}^{n}c_i^2 = n\Big(\frac{1}{n}\Big)^2 = \frac{1}{1000}}
$$

**② 代入 McDiarmid，令上界等于 0.05**

各题同分布，所以 $\mathbb{E}\hat{p} = p$；代入 $\sum c_i^2 = 1/1000$：

$$
\mathbb{P}\big(|\hat{p} - p|\ge t\big)\le 2\exp\bigg(-\frac{2t^2}{1/1000}\bigg) = 2e^{-2000t^2}
$$

$$
2e^{-2000t^2} = 0.05
\ \Longleftrightarrow\
t = \sqrt{\frac{\ln 40}{2000}}\approx \boxed{0.04295}
$$

## 课堂练习

**题目**：模型 A 与模型 B 先固定；在 $n$ 条相互独立的验证样本上，同时记录两个模型是否出错。对第 $i$ 条样本定义

$$
D_i = \mathbf{1}\{\text{B 出错}\} - \mathbf{1}\{\text{A 出错}\}\in[-1, 1]
$$

不同 $i$ 之间相互独立；假设总体平均差 $\varDelta = \mathbb{E}D_i = 0.10$。事件 $\bar{D}_n\le 0$ 表示这批数据未显示 A 的错误率更低。

**两问**

1. 针对 $\mathbb{P}(\bar{D}_n\le 0)$，核对单侧 Hoeffding 的独立性、区间宽度与事件方向。
2. 求 $n = 1000$ 时 $\mathbb{P}(\bar{D}_n\le 0)$ 的上界，以及使上界至多 0.05 的**充分样本量**。

**可用知识：单侧 Hoeffding（样本均值，下尾）**

$D_1,\cdots,D_n$ 相互独立，$D_i\in[a,b]$；对任意 $\varepsilon>0$：

$$
\mathbb{P}\big(\bar{D}_n - \mathbb{E}\bar{D}_n\le -\varepsilon\big)\le\exp\bigg(-\frac{2n\varepsilon^2}{(b-a)^2}\bigg)
$$

- 上尾（事件取 $\ge\varepsilon$）的界形式相同；双侧再乘 2。
- 分母是区间宽度的平方 $(b-a)^2$。

### 练习解析 ①

**① 条件核对**

- **独立**：不同样本上的成对结果相互独立；同一样本内 A、B 的错误可以相关
- **范围**：$D_i\in[-1,1]$，区间宽度为 2
- **方向**：下尾单侧，不乘 2

**单侧 Hoeffding（下尾）**

$$
\mathbb{P}\big(\bar{D}_n\le 0\big) = \mathbb{P}\big(\bar{D}_n - \varDelta\le -0.10\big)
\le \exp\bigg(-\frac{2n(0.10)^2}{(1 - (-1))^2}\bigg) = e^{-0.005n}
$$

$$
n = 1000:\qquad \mathbb{P}\big(\bar{D}_{1000}\le 0\big)\le e^{-5}\approx 0.00674
$$

### 练习解析 ②

**② 令上界不超过 0.05**

$$
e^{-0.005n}\le 0.05\ \Longrightarrow\ n\ge\frac{\log 20}{0.005}\approx 599.15
$$

故取 $n = 600$ 为**充分**样本量（一定够用，但未必是最小的）。

---

# 3.6 本讲小结

## 方法选择：先判断要什么样的结论

**对每个有限 n 严格成立的上界**

- 需要「保证」：例如样本量的充分条件、失败概率不超过 $\delta$。
- **工具**：Markov、Chebyshev、Mills、Hoeffding、Bernstein、Chernoff、McDiarmid…（下一页按条件选择）。
- **代价**：常常偏保守。

**大样本下的渐近近似**

- **CLT**：i.i.d.，$0<\sigma^2<\infty$；

$$
\mathbb{P}\big(\bar{X}_n\le x\big)\approx\Phi\big(\sqrt{n}(x-\mu)/\sigma\big)
$$

- **Delta 方法**：前提 $\sqrt{n}(T_n - \theta)\xrightarrow{d}N(0, \sigma^2)$，且 $g$ 在 $\theta$ 处可微、$g'(\theta)\ne 0$；则渐近方差为 $g'(\theta)^2\sigma^2$。
- 给出的是**近似值，不是上界**。样本均值的正态近似误差可用 Berry–Esseen 衡量；一般 Delta 统计量还需额外论证。

## 不等式简单总结

| 已知条件 | 工具 | 标准形式 |
|---|---|---|
| 只知非负与均值 | **Markov** | $\mathbb{P}(Y\ge t)\le\mathbb{E}Y/t$ |
| 知道方差 | **Chebyshev** | $\mathbb{P}(\lvert X-\mu\rvert\ge t)\le\sigma^2/t^2$ |
| 变量本身 $Z\sim N(0,1)$ | **Mills** | $\mathbb{P}(\lvert Z\rvert\ge t)\le 2\varphi(t)/t$ |
| 独立，$a_i\le X_i\le b_i$ | **Hoeffding** | $\mathbb{P}(S_n - \mathbb{E}S_n\ge t)\le\exp\{-2t^2/\sum_i(b_i-a_i)^2\}$ |
| 独立，$\lvert X_i - \mathbb{E}X_i\rvert\le M$，方差和 $\nu$ | **Bernstein** | $\mathbb{P}(S_n - \mathbb{E}S_n\ge t)\le\exp\{-t^2/[2(\nu + Mt/3)]\}$ |
| 独立 Bernoulli 计数，$\mu = \mathbb{E}S$ | **Chernoff** | $\mathbb{P}(S\ge (1+\delta)\mu)\le\big[e^{\delta}/(1+\delta)^{1+\delta}\big]^{\mu}$ |
| 独立，有界差分 $c_i$ | **McDiarmid** | $\mathbb{P}(\lvert f - \mathbb{E}f\rvert\ge t)\le 2\exp\big(-2t^2/\sum_i c_i^2\big)$ |
