# LECTURE 20：经典统计学导论

（本译稿为 MIT 6.041SC Lecture 20 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 20：经典统计学导论**

- 未知常数 $\theta$（不是随机变量）
- 若 $\theta = E[X]$：用样本均值 $(X_1 + \dots + X_n)/n$ 估计
  - 术语与性质
- 置信区间（CI）
  - 用 CLT 构造的置信区间
  - 方差未知时的置信区间
- 样本均值的其他用途
- 最大似然估计

---

## 第 2 页

**经典统计学**

- 用贝叶斯法则推断：
  - 未知 $\Theta$ 与观测 $X$ 都是随机变量
  - 求 $p_{\Theta \mid X}$
- 经典统计学：未知常数 $\theta$

（图示：流程图，$\theta$ → $p_X(x; \theta)$ → $X$ → 估计器（Estimator）→ $\hat{\Theta}$）

- 也适用于向量 $X$ 与 $\theta$：$p_{X_1,\dots,X_n}(x_1,\dots,x_n;\theta_1,\dots,\theta_m)$
- $p_X(x;\theta)$ 不是条件概率；$\theta$ 不是随机的
- 数学上：多个模型，$\theta$ 的每个可能取值对应一个模型

---

## 第 3 页

**经典统计学中的问题类型**

- 经典统计学：未知常数 $\theta$

（图示：流程图，$\theta$ → $p_X(x;\theta)$ → $X$ → 估计器（Estimator）→ $\hat{\Theta}$）

- 假设检验：$H_0: \theta = 1/2$ 对 $H_1: \theta = 3/4$
- 复合假设：$H_0: \theta = 1/2$ 对 $H_1: \theta \ne 1/2$
- 估计：设计估计子 $\hat{\Theta}$，使"估计误差 $\hat{\Theta} - \theta$ 保持很小"

---

## 第 4 页

**估计均值**

- $X_1, \dots, X_n$：独立同分布，均值 $\theta$，方差 $\sigma^2$
- $\hat{\Theta}_n =$ 样本均值 $= M_n = \dfrac{X_1 + \dots + X_n}{n}$
  - $\hat{\Theta}_n$：估计子（一个随机变量）
- 性质与术语：
  - $E[\hat{\Theta}_n] = \theta$（无偏）
  - WLLN：$\hat{\Theta}_n \to \theta$（一致性）
  - 均方误差（MSE）：$E[(\hat{\Theta}_n - \theta)^2]$

---

## 第 5 页

**关于估计子的均方误差**

- 对任意估计子，利用 $E[Z^2] = \text{var}(Z) + (E[Z])^2$：
  - $E[(\hat{\Theta} - \theta)^2] = \text{var}(\hat{\Theta} - \theta) + (E[\hat{\Theta} - \theta])^2 = \text{var}(\hat{\Theta}) + (\text{bias})^2$
- $\sqrt{\text{var}(\hat{\Theta})}$ 称为标准误差

---

## 第 6 页

**置信区间（CI）**

- 估计子的值 $\hat{\Theta}$ 可能信息量不够
- $1 - \alpha$ 置信区间是一个区间 $[\hat{\Theta}^-, \hat{\Theta}^+]$，满足 $P(\hat{\Theta}^- \le \theta \le \hat{\Theta}^+) \ge 1 - \alpha$，对所有 $\theta$ 成立
  - 通常 $\alpha = 0.05$，或 $0.025$，或 $0.01$
  - 解释很微妙

---

## 第 7 页

**估计均值的置信区间**

- $\hat{\Theta}_n =$ 样本均值 $= M_n = \dfrac{X_1 + \dots + X_n}{n}$
- 正态表：$\Phi(1.96) = 0.975 = 1 - 0.025$
- $P\left(\dfrac{|\hat{\Theta}_n - \theta|}{\sigma/\sqrt{n}} \le 1.96\right) \approx 0.95$（CLT）
- $P\left(\hat{\Theta}_n - \dfrac{1.96\sigma}{\sqrt{n}} \le \theta \le \hat{\Theta}_n + \dfrac{1.96\sigma}{\sqrt{n}}\right) \approx 0.95$

---

## 第 8 页

**$\sigma$ 未知时均值的置信区间**

- $\hat{\Theta}_n =$ 样本均值 $= M_n = \dfrac{X_1 + \dots + X_n}{n}$
- $P\left(\hat{\Theta}_n - \dfrac{1.96\sigma}{\sqrt{n}} \le \theta \le \hat{\Theta}_n + \dfrac{1.96\sigma}{\sqrt{n}}\right) \approx 0.95$
- 方案 1：使用 $\sigma$ 的上界
  - 若 $X_i$ 是 Bernoulli：$\sigma \le 1/2$
- 方案 2：使用 $\sigma$ 的特设估计
  - 若 $X_i$ 是 Bernoulli：$\hat{\sigma} = \sqrt{\hat{\Theta}_n(1 - \hat{\Theta}_n)}$

---

## 第 9 页

**$\sigma$ 未知时均值的置信区间**

- $P\left(\hat{\Theta}_n - \dfrac{1.96\sigma}{\sqrt{n}} \le \theta \le \hat{\Theta}_n + \dfrac{1.96\sigma}{\sqrt{n}}\right) \approx 0.95$
- 方案 3：使用方差的样本均值估计
  - 这里涉及两个近似：
    - CLT：近似正态
    - 使用 $\sigma$ 的估计值
  - 对第二个近似的修正（t 分布表）
    - 当 $n$ 较小时使用
- 从 $\sigma^2 = E[(X_i - \theta)^2]$ 开始
  - $\dfrac{1}{n}\sum_{i=1}^{n} (X_i - \theta)^2 \to \sigma^2$
  - （但不知道 $\theta$）
  - $\dfrac{1}{n}\sum_{i=1}^{n} (X_i - \hat{\Theta}_n)^2 \to \sigma^2$

---

## 第 10 页

**其他自然估计子**

- $\theta_X = E[X]$ ｜ $\hat{\Theta}_X = \dfrac{1}{n}\sum_{i=1}^{n} X_i$
- $\theta = E[g(X)]$ ｜ $\hat{\Theta} = \dfrac{1}{n}\sum_{i=1}^{n} g(X_i)$
- $v_X = \text{var}(X) = E[(X - \theta_X)^2]$ ｜ $\hat{v}_X = \dfrac{1}{n}\sum_{i=1}^{n} (X_i - \hat{\Theta}_X)^2$
- $\text{cov}(X,Y) = E[(X - \theta_X)(Y - \theta_Y)]$ ｜ $\widehat{\text{cov}}(X,Y) = \dfrac{1}{n}\sum_{i=1}^{n} (X_i - \hat{\Theta}_X)(Y_i - \hat{\Theta}_Y)$
- $\rho = \dfrac{\text{cov}(X,Y)}{\sqrt{v_x} \cdot \sqrt{v_Y}}$ ｜ $\hat{\rho} = \dfrac{\widehat{\text{cov}}(X,Y)}{\sqrt{\hat{v}_x} \cdot \sqrt{\hat{v}_Y}}$
- 后续步骤：求 $\hat{\Theta}$ 的分布、MSE、置信区间……

---

## 第 11 页

**最大似然（ML）估计**

- $\theta = E[g(X)]$ ｜ $\hat{\Theta} = \dfrac{1}{n}\sum_{i=1}^{n} g(X_i)$
- 选取使"数据最可能"的 $\theta$
  - $\hat{\theta}_{ML} = \arg\max_{\theta} p_X(x;\theta)$
  - 也适用于 $x$、$\theta$ 是向量或 $x$ 连续的情形
- 与贝叶斯后验比较：
  - $p_{\Theta \mid X}(\theta \mid x) = \dfrac{p_{X \mid \Theta}(x \mid \theta)p_\Theta(\theta)}{p_X(x)}$
  - 解释非常不同

---

## 第 12 页

**关于 ML 的评论**

- 最大化 $p_X(x;\theta)$
- 最大化通常用数值方法完成
- 若有 $n$ 个来自模型 $p_X(x;\theta)$ 的独立同分布数据，则在温和假设下：
  - 一致：$\hat{\Theta}_n \to \theta$
  - 渐近正态：$\dfrac{\hat{\Theta}_n - \theta}{\sigma(\hat{\Theta}_n)} \to N(0,1)$（CDF 收敛）
  - 计算 $\hat{\sigma} \approx \sigma(\hat{\Theta}_n)$ 的解析与模拟方法
  - 因此置信区间 $P\left(\hat{\Theta}_n - 1.96\hat{\sigma} \le \theta \le \hat{\Theta}_n + 1.96\hat{\sigma}\right) \approx 0.95$
  - 渐近"有效"（"最优"）

---

## 第 13 页

**ML 估计示例：二项分布的参数**

- $K$：二项分布，参数 $n$（已知）与 $\theta$（未知）
- $p_K(k;\theta) = \binom{n}{k}\theta^k(1-\theta)^{n-k}$
- $\hat{\theta}_{ML} = \dfrac{k}{n}$ ｜ $\hat{\Theta}_{ML} = \dfrac{K}{n}$
- 与 $\theta$ 上均匀先验的 MAP 估计子相同

---

## 第 14 页

**ML 估计示例——正态的均值与方差**

- $X_1, \dots, X_n$：独立同分布，$N(\mu, v)$
- $f_X(x;\mu,v) = \prod_{i=1}^{n} \dfrac{1}{\sqrt{2\pi v}}\exp\left\{-\dfrac{(x_i-\mu)^2}{2v}\right\}$
- 最小化 $\dfrac{n}{2}\log v + \sum_{i=1}^{n} \dfrac{(x_i-\mu)^2}{2v}$
  - 关于 $\mu$ 最小化：$\hat{\mu} = \dfrac{x_1 + \dots + x_n}{n}$
  - 关于 $v$ 最小化：$\hat{v} = \dfrac{1}{n}\sum_{i=1}^{n} (x_i - \hat{\mu})^2$

---

## 第 15 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
