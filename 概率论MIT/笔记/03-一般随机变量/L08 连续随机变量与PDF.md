# L08 连续随机变量与概率密度函数 - 笔记

> **参考来源**
> - 本章归属：教材第 3 章 General Random Variables（原索引误标为"第 2 章 2.4–2.6"，实际为连续随机变量内容）
> - 视频：B站 6.041SC 上集 BV1JZhFzYEXH，**p80–p88**（L08.1 课程概览 ~ L08.9 正态概率计算）
> - 讲义：Lecture 8（L08.pdf，20 页；含答案版 L08AS.pdf）
> - 教材：《Introduction to Probability》第 2 版 第 3 章 3.1 连续随机变量与 PDF（p150）、3.2 CDF（p158）、3.3 正态随机变量（p163）

## 目录
- [[#1. 核心概念]]
- [[#2. 公式与定义]]
- [[#3. 关键性质]]
- [[#4. 例题]]
- [[#5. 本节重点]]

---

## 1. 核心概念

> **贯穿全课的翻译规则（p81 / lec08）**：从离散到连续，"求和换成积分，PMF 换成 PDF"（sums → integrals，mass functions → density functions）。几乎每条离散公式都可以做这个替换得到连续版本。计算上要多做微积分，但概念是同一批。

### 1.1 PDF：连续世界的"概率律"
对连续随机变量，单点概率恒为 0（对一个点积分 = 0），改用**概率密度函数**描述：
$$P(a \le X \le b) = \int_a^b f_X(x)\, dx$$
- $f_X(x) \ge 0$（否则算出负概率），$\int_{-\infty}^{\infty} f_X(x)\, dx = 1$（整条实轴上必出现）；
- **密度不是概率（p81）**：把 1 单位概率"涂抹"在实轴上，$f$ 描述的是"涂得多厚"。$f_X(x) \cdot \delta \approx P(x \le X \le x+\delta)$——对充分小的 $\delta$，密度近似常数，区间概率 = 底 × 高。
- 单位：概率/单位长度。因此 $f_X(x)$ **可以大于 1**（甚至可以在某点 blow up），只要曲线下总面积 = 1。
- 一般集合："nice"集合（若干区间的并）上的概率 = 在该集合上积分 $f$；能算区间概率，其它都能算。

#### 推导：PDF 定义与概率公理的一致性
教材（3.1 节）把连续随机变量定义为：存在非负函数 $f_X$，使得对实轴上任意"好"集合 $B$ 都有

$$P(X\in B)=\int_B f_X(x)\,dx.$$

这个定义不是凭空给的，而是直接对接第 1 章的三条概率公理：

1. **非负性公理**要求 $P(X\in B)\ge 0$ 对一切 $B$ 成立。取 $B$ 为单点邻域 $[x,x+\delta]$，积分 $\int_x^{x+\delta}f_X(t)\,dt\approx f_X(x)\delta\ge 0$；令 $\delta\to 0$ 即得 $f_X(x)\ge 0$。
2. **归一性公理 $P(\Omega)=1$** 对应 $B=\mathbb{R}$（$X$ 必取某个实值）：

$$\int_{-\infty}^{\infty} f_X(x)\,dx = P(X\in\mathbb{R}) = P(\Omega) = 1.$$

这就是 PDF 归一化条件的来历——它不是额外假设，而是 $P(\Omega)=1$ 在连续模型下的翻译。
3. **可列可加性公理**对应积分的可加性：不交区间上积分相加 = 并集上积分。

#### 推导：区间概率 $P(a\le X\le b)=\int_a^b f$ 的论证
把区间 $[a,b]$ 切成 $n$ 等份，每段长 $\Delta x=(b-a)/n$，分点 $x_i=a+i\Delta x$。当 $n$ 很大时，$f_X$ 在每小段 $[x_i,x_{i+1}]$ 上近似常数 $f_X(x_i)$，于是

$$P(x_i\le X\le x_{i+1})\approx f_X(x_i)\,\Delta x.$$

由可列可加性，$[a,b]$ 的概率是各小段概率之和：

$$P(a\le X\le b)=\sum_{i=0}^{n-1}P(x_i\le X\le x_{i+1})\approx \sum_{i=0}^{n-1}f_X(x_i)\Delta x.$$

右端正是定积分的黎曼和，令 $n\to\infty$ 取极限即得 $\int_a^b f_X(x)\,dx$。几何上这就是 PDF 曲线下 $[a,b]$ 之间的面积。

**端点为何可忽略**：对连续型，单点概率 $P(X=a)=\int_a^a f=0$，因此

$$P(a\le X\le b)=P(a<X<b)=P(a<X\le b)=P(a\le X<b),$$

写区间时含不含端点都一样（离散型则不同）。

### 1.2 期望与方差（连续版）
$$E[X] = \int_{-\infty}^{\infty} x f_X(x)\, dx, \qquad E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x)\, dx$$
- **重心解释（p83）**：$E[X]$ 是 PDF 曲线下那片"物体"的重心（新生物理直觉）。对称性 ⇒ 均值在中点。
- 重复实验取平均，长期平均就是期望（频率解释仍成立；严格化是后面的极限定理）。
- 期望值法则：算 $E[g(X)]$ 不必先求 $g(X)$ 的 PDF，直接用原 PDF 代入 $g(x)$ 积分。
- 方差同定义：$\text{var}(X) = E[X^2]-(E[X])^2$，公式从离散平移过来。

### 1.3 CDF：统一离散与连续
$$F_X(x) = P(X \le x)$$
- 连续时 $F_X(x) = \int_{-\infty}^x f_X(t)\,dt$；离散时 $F_X(x) = \sum_{k \le x} p_X(k)$。
- **反过来**：$f_X(x) = F_X'(x)$（在 CDF 可导处；在折点/跳跃点导数不存在，密度取值任意，因为单点值不影响任何积分）。
- **形状（p86）**：
  - 连续：CDF 从 0 连续单调爬到 1，无跳跃；
  - 离散：CDF 是阶梯函数，每处跳跃高度 = 该点的 PMF 质量；
  - 跳跃点取值用 $\le$（包含该点质量），即 CDF 右连续。
- 意义：不用把离散/连续各证一遍，CDF 一套记号通吃。

#### 推导：CDF 四条基本性质
由定义 $F_X(x)=P(X\le x)$ 直接推出（教材 3.2 节）：

1. **单调不减**：若 $x\le y$，则事件 $\{X\le x\}\subseteq\{X\le y\}$。由概率单调性，$F_X(x)=P(X\le x)\le P(X\le y)=F_X(y)$。
2. **两端极限**：
   - $x\to-\infty$ 时，事件 $\{X\le x\}$ 趋于空集（$X$ 不可能比 $-\infty$ 还小），故 $F_X(x)\to 0$；
   - $x\to+\infty$ 时，$\{X\le x\}$ 趋于必然事件 $\Omega$，故 $F_X(x)\to P(\Omega)=1$。
3. **右连续**：$F_X(x^+)=F_X(x)$。原因是定义用的是 $\le$：$x$ 从右侧逼近 $x_0$ 时，$\{X\le x\}$ 始终把质量点 $X=x_0$ 包含在内；而左极限 $F_X(x_0^-)=P(X<x_0)$ 不含该点。若 $x_0$ 是离散质量点，跳跃高度 $F_X(x_0)-F_X(x_0^-)=P(X=x_0)=p_X(x_0)$。
4. **连续型时 CDF 连续**：$F_X(x)=\int_{-\infty}^x f_X(t)\,dt$ 是变上限积分，只要 $f_X$ 可积就连续；离散型则是阶梯函数。

#### 推导：$F_X'(x)=f_X(x)$ 与区间概率的 CDF 表达
对连续型，$F_X(x)=\int_{-\infty}^x f_X(t)\,dt$。由微积分基本定理，在 $f_X$ 的连续点 $x$ 处：

$$F_X'(x)=\frac{d}{dx}\int_{-\infty}^x f_X(t)\,dt=f_X(x).$$

反过来，任给 $a<b$，把事件 $\{X\le b\}$ 拆成不交并 $\{X\le a\}\cup\{a<X\le b\}$，由可加性：

$$P(X\le b)=P(X\le a)+P(a<X\le b),$$

移项得

$$P(a<X\le b)=F_X(b)-F_X(a).$$

这是 CDF 最常用的运算：**任意区间概率 = CDF 右端点减左端点**。对连续型，端点开闭不影响结果，$P(a<X\le b)$ 与 $P(a\le X\le b)$ 数值相同；对离散型，必须用 $\le$ 口径（右连续）才能把质量点算对。

---

## 2. 公式与定义

### 2.1 三种核心连续分布

| 分布 | 参数 | PDF | 均值 | 方差 |
|---|---|---|---|---|
| 连续均匀 | $a<b$ | $\frac{1}{b-a}$（$a\le x\le b$） | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ |
| 指数 | $\lambda>0$ | $\lambda e^{-\lambda x}$（$x\ge0$） | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |
| 正态 | $\mu,\sigma^2$ | $\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ |

- **均匀分布的真正含义（p82）**："每个 $x$ 概率都是 0"这句话没意义；均匀 = **等长区间等概率**——任意两个同样长度的小区间概率相等，表达"完全随机"。
- 高度 $1/(b-a)$ 是由总面积 = 1 逼出来的；考试时务必补一句"其余地方为 0"，否则扣分。
- 补充（$0,\dots,n$ 离散均匀的连续类比）：连续均匀 $[a,b]$ 方差 $\frac{(b-a)^2}{12}$；离散 $a,\dots,b$ 方差 $\frac{1}{12}(b-a)(b-a+2)$。
- 标准差 $\sigma \propto (b-a)$：与区间宽度成正比，单位与随机变量本身相同，直观反映"散开多宽"。

### 2.2 标准正态
$N(0,1)$：$f_X(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$，$E[X]=0$（对称），$\text{var}(X)=1$（需要一次微积分算出）；CDF 无闭合形式，用表查 $\Phi(z)$。
- **系数 $1/\sqrt{2\pi}$ 的来历（p87）**：从 $e^{-x^2/2}$ 出发，为使积分 = 1 乘上归一化常数（用极坐标二重积分那个漂亮的微积分习题）。

**高斯积分推导（补全）**：$\int_{-\infty}^{\infty} e^{-x^2/2} dx = \sqrt{2\pi}$。直接求原函数做不到（$e^{-x^2/2}$ 无初等原函数），核心技巧：平方化二维 → 极坐标。

被积函数是偶函数，先算半轴积分：

$$I = \int_0^{\infty} e^{-x^2/2} dx$$

$$I^2 = \int_0^{\infty} e^{-x^2/2} dx \cdot \int_0^{\infty} e^{-y^2/2} dy = \int_0^{\infty}\int_0^{\infty} e^{-(x^2+y^2)/2}\, dx\, dy$$

极坐标 $x = r\cos\theta,\ y = r\sin\theta$（第一象限 $r \ge 0,\ 0 \le \theta \le \pi/2$），$dx\,dy = r\,dr\,d\theta$，$x^2+y^2 = r^2$：

$$I^2 = \int_0^{\pi/2}\int_0^{\infty} e^{-r^2/2}\, r\, dr\, d\theta$$

内层令 $u = r^2/2$（$du = r\,dr$），恰好凑微分：

$$\int_0^{\infty} r e^{-r^2/2} dr = \int_0^{\infty} e^{-u} du = 1$$

$$I^2 = \int_0^{\pi/2} 1\, d\theta = \frac{\pi}{2} \Rightarrow I = \sqrt{\frac{\pi}{2}}$$

$$\int_{-\infty}^{\infty} e^{-x^2/2} dx = 2I = 2\sqrt{\frac{\pi}{2}} = \sqrt{2\pi} \quad \blacksquare$$

**为什么能这么算**：平方把一维变二维，$e^{-(x^2+y^2)/2}$ 在极坐标下恰好是 $e^{-r^2/2}$，而 $r\,dr = d(r^2/2)$ 完美凑微分 → 化为简单指数积分。标准正态的常数 $1/\sqrt{2\pi}$ 就来自这里（保证 $\int f = 1$）。
- **形状来历**：先画抛物线 $x^2/2$，取负指数 ⇒ 中间高、两边快速衰减的钟形；$\sigma$ 控制抛物线宽窄（$\sigma$ 小 ⇒ 抛物线陡 ⇒ 密度衰减快、峰窄）；$\mu$ 控制中心位置。

### 2.3 正态的线性性
$X \sim N(\mu, \sigma^2)$，$Y = aX + b$ ⇒ $Y \sim N(a\mu + b, a^2\sigma^2)$。
- $E[Y]=a\mu+b$、$\text{var}(Y)=a^2\sigma^2$ 这两步对任何随机变量都成立；**真正用到"正态"的地方是结论"$Y$ 仍是正态"**。
- 直觉：钟形曲线缩放/平移后仍是钟形（只是位置和宽度变了）。

标准化：$Z = (X-\mu)/\sigma \sim N(0,1)$。
- z 分数 = "离均值几个标准差"，是考试成绩等场景的常用解释；也是查标准正态表的唯一入口。

#### 推导：$X=\mu+\sigma Z$ 的 PDF 与 $1/|\sigma|$ 因子
已知 $Z\sim N(0,1)$，$\phi(z)=\frac{1}{\sqrt{2\pi}}e^{-z^2/2}$。令 $X=\mu+\sigma Z$（$\sigma>0$），反解 $Z=(X-\mu)/\sigma$。

先用 CDF 法求 $F_X$：

$$F_X(x)=P(X\le x)=P(\mu+\sigma Z\le x)=P\!\left(Z\le\frac{x-\mu}{\sigma}\right)=\Phi\!\left(\frac{x-\mu}{\sigma}\right).$$

两边对 $x$ 求导（链式法则）：

$$f_X(x)=F_X'(x)=\phi\!\left(\frac{x-\mu}{\sigma}\right)\cdot\frac{d}{dx}\!\left(\frac{x-\mu}{\sigma}\right)=\phi\!\left(\frac{x-\mu}{\sigma}\right)\cdot\frac{1}{\sigma}.$$

代入 $\phi$：

$$f_X(x)=\frac{1}{\sqrt{2\pi}\,\sigma}\exp\!\left\{-\frac{1}{2}\!\left(\frac{x-\mu}{\sigma}\right)^2\right\}=\frac{1}{\sqrt{2\pi}\,\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}}.$$

**$1/\sigma$ 因子的来历**：变量替换 $x=\mu+\sigma z$ 中 $dx=\sigma\,dz$，反解 $dz=dx/\sigma$。密度变换公式 $f_X(x)=f_Z(z)\left|\frac{dz}{dx}\right|$ 给出因子 $|dz/dx|=1/\sigma$。几何上：把标准钟形横向拉伸 $\sigma$ 倍后，为保持总面积 = 1，高度必须被压扁 $1/\sigma$ 倍——这正是"方差变大则曲线变矮变宽"的数学原因。

验证归一性：$\int f_X(x)\,dx=\int\phi((x-\mu)/\sigma)\frac{dx}{\sigma}=\int\phi(z)\,dz=1$。

### 2.4 CDF 通用性质
非递减；$x\to\infty$ 时趋于 1；$x\to-\infty$ 时趋于 0；连续随机变量的 CDF 连续，离散的有跳跃。

---

## 3. 关键性质

- **方差性质**（连续版同样成立）：$\text{var}(aX+b) = a^2\text{var}(X)$，$\text{var}(X) = E[X^2]-(E[X])^2$；
- **正态为什么到处都是（p87 预告）**：若一个量是大量**独立微小随机贡献**之和，无论每个小量是什么分布，其和都近似正态（中心极限定理，L19）。伯努利之和（二项分布）在 $n$ 大时也长成钟形。这是正态"最著名分布"的根本原因。
- **混合随机变量（p85）**：并非所有变量非离散即连续。例：抛硬币，以 $1/2$ 概率直接拿到 1/2 元奖金，另以 $1/2$ 概率进暗室转轮盘得到 $U[0,1]$ 的奖金。这个变量在 $1/2$ 处有正概率（非连续），又能取连续区间内的值（非离散）——称为**混合变量**。其 CDF 既有连续爬升段又有高度 $1/2$ 的跳跃。

### 3.1 指数分布无记忆性（证明）
设 $T\sim\text{指数}(\lambda)$，则 $P(T>t)=e^{-\lambda t}$（由 $P(T\le t)=\int_0^t\lambda e^{-\lambda x}dx=1-e^{-\lambda t}$）。已知灯已用了 $t$ 小时仍亮着（事件 $\{T>t\}$），求剩余寿命 $X=T-t$ 仍大于 $s$ 的概率：

$$P(X>s\mid T>t)=P(T>t+s\mid T>t)=\frac{P(T>t+s,\ T>t)}{P(T>t)}=\frac{P(T>t+s)}{P(T>t)}.$$

事件 $\{T>t+s\}\subseteq\{T>t\}$，故交集就是 $\{T>t+s\}$。代入生存函数：

$$P(X>s\mid T>t)=\frac{e^{-\lambda(t+s)}}{e^{-\lambda t}}=e^{-\lambda s}=P(X>s).$$

$t$ 被约掉，剩余寿命分布与已用时间 $t$ 无关——这就是**无记忆性**："用过的指数灯泡和新灯泡概率上一样"。

**反过来，指数分布是唯一具有无记忆性的连续分布**（教材 3.2 节用 CDF 方程 $1-F(t+s)=(1-F(t))(1-F(s))$ 证明解只能是指数）。它是连续版的"无记忆伯努利过程"：每个小时间步 $\delta$ 内"坏掉"的概率近似 $\lambda\delta$，与之前已熬了多久无关。

---

## 4. 例题

### 例 1：均匀分布的均值方差
$X \sim U[a,b]$：
- $E[X] = \int_a^b x \cdot \frac{1}{b-a} dx = \frac{a+b}{2}$（对称性：重心即中点，不必硬算）；
- $E[X^2] = \int_a^b x^2 \frac{dx}{b-a} = \frac{a^2+ab+b^2}{3}$；
- $\text{var}(X) = \frac{a^2+ab+b^2}{3} - \frac{(a+b)^2}{4} = \frac{(b-a)^2}{12}$。

### 例 2：指数分布的均值
$f_X(x) = \lambda e^{-\lambda x}$（$x\ge0$）：
- $E[X] = \int_0^\infty x\lambda e^{-\lambda x}dx = \frac{1}{\lambda}$（分部积分）；
- $E[X^2] = \frac{2}{\lambda^2}$ ⇒ $\text{var}(X) = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}$。

### 例 3：正态概率计算（标准化查表，p88）
- 设 $X \sim N(2, 9)$（$\mu=2,\sigma=3$），求 $P(X \le 5)$；
- 标准化：$P\left(Z \le \frac{5-2}{3}\right) = \Phi(1) \approx 0.8413$；
- 再一例（讲例题）：$X \sim N(2,16)$（$\sigma=4$），求 $P(X \le 3)$：
  $$P(X\le 3) = P\!\left(Z \le \frac{3-2}{4}\right) = \Phi(0.25) \approx 0.5987$$
- 一般步骤：先把不等式两边同时减均值、除以 $\sigma$ 化成标准正态，再查 $\Phi$ 表。注意 $\Phi(0.25)\approx0.5987$（不是 0.987）。

---

## 5. 本节重点

> **本节重点**：
> - 翻译规则：离散→连续 = 求和换积分、PMF 换 PDF；PDF 是密度（概率/单位长度），可大于 1，单点概率为 0。
> - $\int f = 1$ 来自 $P(\Omega)=1$；区间概率 = PDF 下面积（黎曼和论证）；端点开闭对连续型无影响。
> - 期望/期望值法则换积分；期望 = PDF 的重心，对称性给中点。
> - 均匀/指数/正态三兄弟的 PDF、均值、方差要背熟；均匀 = 等长区间等概率。
> - CDF 统一离散与连续：$F_X$ 单调不减、右连续、$x\to-\infty$ 为 0、$x\to+\infty$ 为 1；$f=F'$（连续点）；区间概率 $P(a<X\le b)=F(b)-F(a)$。
> - 指数无记忆性：$P(T>t+s\mid T>t)=P(T>s)=e^{-\lambda s}$，剩余寿命与已用时间无关。
> - 正态线性性：$aX+b \sim N(a\mu+b, a^2\sigma^2)$；标准化 $Z=(X-\mu)/\sigma$ 后查表，变量替换引入 $1/\sigma$ 因子（拉伸 $\sigma$ 倍、压矮 $1/\sigma$ 倍）。
> - **常见坑**：① 把 $f_X(x)$ 当概率（可能大于 1）；② 指数分布只对 $x \ge 0$ 定义；③ 正态查表前忘记标准化（$\sigma$ 在分母）；④ 写均匀 PDF 漏了"其余为 0"；⑤ 混合变量当纯离散或纯连续处理；⑥ 用 CDF 算区间概率时左右端点代反。
