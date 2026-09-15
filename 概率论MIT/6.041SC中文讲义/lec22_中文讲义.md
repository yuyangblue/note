# LECTURE 22：泊松过程

（本译稿为 MIT 6.041SC Lecture 22 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 22：泊松过程**

- 泊松过程的定义
  - 应用
- 到达次数的分布
- 第 $k$ 次到达的时间
- 无记忆性
- 到达间隔时间的分布

---

## 第 2 页

**泊松过程的定义**

（图示：左侧为泊松过程时间轴示意；右侧为伯努利过程时间轴示意）

- 泊松：
  - 不相交时间区间内的到达数是独立的
  - $P(k,\tau)$ = 时长 $\tau$ 的区间内到达 $k$ 次的概率
  - 小区间概率：
    - 对很小的 $\delta$：
    - $P(k,\delta) \approx \begin{cases} 1-\lambda\delta & k=0 \\ \lambda\delta & k=1 \\ 0 & k>1 \end{cases}$
    - $P(k,\delta) = \begin{cases} 1-\lambda\delta+O(\delta^2) & k=0 \\ \lambda\delta+O(\delta^2) & k=1 \\ 0+O(\delta^2) & k>1 \end{cases}$
  - $\lambda$："到达率"
- 伯努利：
  - 独立性
  - 时间齐性：每个时隙 $p$ 恒定

---

## 第 3 页

**泊松过程的应用**

（图示：时间轴示意，轴上若干叉号代表事件发生点）

- 普鲁士军队中马蹄踢伤致死事件（1898）
- 粒子发射与放射性衰变
- 弱光源的光子到达
- 金融市场冲击
- 电话呼叫、服务请求的到达等

（图示：右侧为西梅翁·德尼·泊松（Siméon Denis Poisson, 1781–1840）肖像，公共领域图片，来源：维基百科）

---

## 第 4 页

**到达次数的泊松 PMF**

（图示：时间轴 0 到 $\tau$）

- $N_\tau$：$[0,\tau]$ 内的到达数 ｜ $P(k,\tau) = P(N_\tau = k)$
- $n = \tau/\delta$ 个长度为 $\delta$ 的区间/时隙
- $P(\text{某个时隙包含两次或更多到达})$（讲义留白）
- $N_\tau \approx$ 二项 ｜ $p = \lambda\delta + O(\delta^2)$ ｜ $np = $（讲义留白）
- 伯努利：$p_S(k) = \dfrac{n!}{(n-k)!k!} \cdot p^k(1-p)^{n-k}$，$k = 0, \dots, n$
  - $\lambda = np \quad n \to \infty \quad p \to 0$
  - 对固定 $k = 0, 1, \dots,$
  - $p_S(k) \to \dfrac{\lambda^k}{k!}e^{-\lambda}$，
- $P(k,\tau) = \dfrac{(\lambda\tau)^k e^{-\lambda\tau}}{k!}, \quad k = 0, 1, \dots$

---

## 第 5 页

**到达次数的均值与方差**

- $P(k,\tau) = P(N_\tau = k) = \dfrac{(\lambda\tau)^k e^{-\lambda\tau}}{k!}, \quad k = 0, 1, \dots$
- $E[N_\tau] = \sum_{k=0}^{\infty} k \cdot \dfrac{(\lambda\tau)^k e^{-\lambda\tau}}{k!} = \dots$（讲义留白）
- $N_\tau \approx$ Binomial($n, p$)
  - $n = \tau/\delta$，$p = \lambda\delta + O(\delta^2)$
- $E[N_\tau] = \lambda\tau$
- $\text{var}(N_\tau) = \lambda\tau$

---

## 第 6 页

**示例**

- 你按泊松过程收到邮件，
  - 速率为 $\lambda = 5$ 封/小时。
- 一天内收到邮件的均值与方差 = （讲义留白）
- 下一小时收到一封新邮件的概率 $P(\text{下一小时收到一封新邮件})$ = （讲义留白）
- 接下来三小时中每小时恰好收到两封邮件的概率 = （讲义留白）
- $P(k,\tau) = \dfrac{(\lambda\tau)^k e^{-\lambda\tau}}{k!}, \quad k = 0, 1, \dots$ ｜ $E[N_\tau] = \lambda\tau$ ｜ $\text{var}(N_\tau) = \lambda\tau$

---

## 第 7 页

**直到首次到达的时间 $T_1$**

- $P(k,\tau) = \dfrac{(\lambda\tau)^k e^{-\lambda\tau}}{k!}, \quad k = 0, 1, \dots$
- 求 CDF：$P(T_1 \le t) = $（讲义留白）
- $f_{T_1}(t) = \lambda e^{-\lambda t}, \quad \text{对 } t \ge 0$
- Exponential($\lambda$)
- 无记忆性：以 $T_1 > t$ 为条件，
  - $T_1 - t$ 的 PDF 仍是指数分布

---

## 第 8 页

**第 $k$ 次到达的时间 $Y_k$**

- $P(k,\tau) = \dfrac{(\lambda\tau)^k e^{-\lambda\tau}}{k!}, \quad k = 0, 1, \dots$
- 可以先求 CDF 再推导其 PDF
- 更直观的论证：
  - $f_{Y_k}(y)\delta \approx P(y \le Y_k \le y + \delta) = $（讲义留白）
- 爱尔朗分布：$f_{Y_k}(y) = \dfrac{\lambda^k y^{k-1} e^{-\lambda y}}{(k-1)!}, \quad y \ge 0$

（图示：右侧为 $f_{Y_k}(y)$ 曲线示意，$k = 1, 2, 3$ 三条曲线）

---

## 第 9 页

**无记忆性与全新开始性质**

- 与伯努利过程的性质类似
  - 鉴于两个过程之间的联系，这是合理的
  - 使用直观推理
  - 可以严格证明

---

## 第 10 页

**无记忆性与全新开始性质**

（图示：两条时间轴示意）

- 若我们在时刻 $t$ 开始观测，
  - 我们看到泊松过程，且与时刻 $t$ 之前的历史独立
  - 到下次到达的时间：（讲义留白）
- 若我们在时刻 $T_1$ 开始观测，
  - 我们看到泊松过程，且与时刻 $T_1$ 之前的历史独立
  - 因此：第一次与第二次到达之间的时间，$T_2 = Y_2 - Y_1$：（讲义留白）
  - 类似地，对所有 $T_k = Y_k - Y_{k-1}$，$k \ge 2$
- $Y_k = T_1 + \dots + T_k$ 是独立指数变量之和
  - $E[Y_k] = k/\lambda$
  - $\text{var}(Y_k) = k/\lambda^2$
- 一个等价定义
- 一种模拟方法

---

## 第 11 页

**伯努利/泊松关系**

（图示：时间轴，0 到 $\tau$）

- $n = \tau/\delta$ ｜ $p = \lambda\delta$ ｜ $np = \lambda\tau$

|  | POISSON（泊松） | BERNOULLI（伯努利） |
|---|---|---|
| 到达时间 | 连续 | 离散 |
| 到达率 | $\lambda$/单位时间 | $p$/每次试验 |
| 到达次数的 PMF | 泊松 | 二项 |
| 到达间隔时间分布 | 指数 | 几何 |
| 到第 $k$ 次到达的时间 | 爱尔朗 | 帕斯卡 |

---

## 第 12 页

**示例：泊松钓鱼**

- 鱼按泊松过程被捕获，$\lambda = 0.6$/小时
  - 钓两小时；
  - 若至少钓到一条鱼，停止
  - 否则继续直到钓到第一条鱼

（图示：两条时间轴，上轴在时刻 2 前有若干叉号（钓到鱼），下轴在时刻 2 后有一个叉号（未钓到，继续钓））

- $P(\text{钓鱼超过两小时}) = $（讲义留白）
- $P(\text{钓鱼超过两小时且不到五小时}) = $（讲义留白）
- $P(k,\tau) = \dfrac{(\lambda\tau)^k e^{-\lambda\tau}}{k!}$ ｜ $E[N_\tau] = \lambda\tau$ ｜ $f_{Y_k}(y) = \dfrac{\lambda^k y^{k-1} e^{-\lambda y}}{(k-1)!}$

---

## 第 13 页

**示例：泊松钓鱼**

- 鱼按泊松过程被捕获，$\lambda = 0.6$/小时
  - 钓两小时；
  - 若至少钓到一条鱼，停止
  - 否则继续直到钓到第一条鱼

（图示：两条时间轴示意）

- $P(\text{至少钓到两条鱼}) = $（讲义留白）
- $E[\text{未来钓鱼时间} \mid \text{已钓三小时}] = $（讲义留白）
- $P(k,\tau) = \dfrac{(\lambda\tau)^k e^{-\lambda\tau}}{k!}$ ｜ $E[N_\tau] = \lambda\tau$ ｜ $f_{Y_k}(y) = \dfrac{\lambda^k y^{k-1} e^{-\lambda y}}{(k-1)!}$

---

## 第 14 页

**示例：泊松钓鱼**

- 鱼按泊松过程被捕获，$\lambda = 0.6$/小时
  - 钓两小时；
  - 若至少钓到一条鱼，停止
  - 否则继续直到钓到第一条鱼

（图示：两条时间轴，上轴在时刻 2 前有三个叉号（钓到鱼停止），下轴在时刻 2 后有一个叉号（未钓到继续））

- $E[\text{总钓鱼时间}] = $（讲义留白）
- $E[\text{鱼的数量}] = $（讲义留白）
- $P(k,\tau) = \dfrac{(\lambda\tau)^k e^{-\lambda\tau}}{k!}$ ｜ $E[N_\tau] = \lambda\tau$ ｜ $f_{Y_k}(y) = \dfrac{\lambda^k y^{k-1} e^{-\lambda y}}{(k-1)!}$

---

## 第 15 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
