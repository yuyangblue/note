# LECTURE 17：线性最小均方（LLMS）估计

（本译稿为 MIT 6.041SC Lecture 17 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 17：线性最小均方（LLMS）估计**

- 条件期望 $E[\Theta \mid X]$ 可能难以计算/实现
- 限制估计器为 $\hat{\Theta} = aX + b$
  - 最小化均方误差
- 简单解
- 数学性质
- 示例

---

## 第 2 页

**LLMS 表述**

（图示：左侧为 $x$–$\theta$ 坐标系，含斜向平行四边形区域、红色直线与蓝色折线，坐标轴刻度 x：3, 5, 9, 11；θ：4, 10）

- 未知 $\Theta$；观测 $X$
- 最小化 $E[(\hat{\Theta} - \Theta)^2]$
- 估计器 $\hat{\Theta} = g(X) \to \hat{\Theta}_{LMS} = E[\Theta \mid X]$
- 考虑形式为 $\hat{\Theta} = aX + b$ 的 $\Theta$ 的估计器
- 对 $a$、$b$ 最小化 $E[(\Theta - aX - b)^2]$
- 若 $E[\Theta \mid X]$ 关于 $X$ 线性，则 $\hat{\Theta}_{LMS} = \hat{\Theta}_{LLMS}$

---

## 第 3 页

**LLMS 问题的解**

- 对 $a$、$b$ 最小化 $\mathbb{E}\left[(\Theta - aX - b)^2\right]$，关于 $a$、$b$
  - 假设 $a$ 已经找到：
- $\widehat{\Theta}_L = \mathbb{E}[\Theta] + \dfrac{\text{Cov}(\Theta, X)}{\text{var}(X)}(X - \mathbb{E}[X]) = \mathbb{E}[\Theta] + \rho\dfrac{\sigma_\Theta}{\sigma_X}(X - \mathbb{E}[X])$

---

## 第 4 页

**关于解与误差方差的备注**

- $\widehat{\Theta}_L = \mathbb{E}[\Theta] + \dfrac{\text{Cov}(\Theta,X)}{\text{var}(X)}(X - \mathbb{E}[X]) = \mathbb{E}[\Theta] + \rho\dfrac{\sigma_\Theta}{\sigma_X}(X - \mathbb{E}[X])$
- 只有均值、方差、协方差起作用
- $\rho > 0$：（讲义留白）
- $\rho = 0$：（讲义留白）
- $\mathbb{E}\left[(\widehat{\Theta}_L - \Theta)^2\right] = (1 - \rho^2)\text{var}(\Theta)$
- $|\rho| = 1$：（讲义留白）

---

## 第 5 页

**示例**

（图示：左侧为 $x$–$\theta$ 坐标系，含黑色矩形轮廓、红色直线与蓝色折线，坐标轴刻度 x：3, 5, 9, 11；θ：4, 10）

- $\widehat{\Theta}_L = E[\Theta] + \dfrac{Cov(\Theta,X)}{var(X)}(X - E[X]) = E[\Theta] + \rho\dfrac{\sigma_\Theta}{\sigma_X}(X - E[X])$（讲义留白）

---

## 第 6 页

**用于推断硬币参数的 LLMS**

- 标准示例：
  - 具有偏置 $\Theta$ 的硬币；先验 $f_\Theta(\cdot)$
  - 固定 $n$；$X$ = 正面朝上的次数
- 假设 $f_\Theta(\cdot)$ 在 $[0,1]$ 上均匀
- $\hat{\Theta}_{LMS} = \dfrac{X + 1}{n + 2} = \hat{\Theta}_{LLMS}$
- $\hat{\Theta}_{LLMS} = \mathbb{E}[\Theta] + \dfrac{\text{Cov}(\Theta,X)}{\text{var}(X)}(X - \mathbb{E}[X])$

---

## 第 7 页

**用于推断硬币参数的 LLMS**

- $\Theta$：$[0,1]$ 上均匀
  - $E[\Theta] = 1/2$
  - $\text{var}(\Theta) = 1/12$
  - $E[\Theta^2] = $（讲义留白）
- $p_{X \mid \Theta}$：Bin($n, \Theta$)
  - $E[X \mid \Theta] = n\Theta$
  - $\text{var}(X \mid \Theta) = n\Theta(1 - \Theta)$
- $E[X] = $（讲义留白）
- $E[X^2 \mid \Theta] = $（讲义留白）
- $E[X^2] = $（讲义留白）
- $\text{var}(X) = $（讲义留白）
- $E[\Theta X \mid \Theta] = $（讲义留白）
- $E[\Theta X] = $（讲义留白）
- $\text{cov}(\Theta, X) = $（讲义留白）

---

## 第 8 页

**用于推断硬币参数的 LLMS**

- $\widehat{\Theta}_{LLMS} = \mathbb{E}[\Theta] + \dfrac{Cov(\Theta,X)}{var(X)}(X - \mathbb{E}[X])$
- $\text{cov}(\Theta,X) = \dfrac{n}{12}$
- $\text{var}(X) = \dfrac{n(n + 2)}{12}$
- $\mathbb{E}[X] = \dfrac{n}{2}$
- $\widehat{\Theta}_{LLMS} = \dfrac{X + 1}{n + 2}$

---

## 第 9 页

**多观测下的 LLMS**

- 未知 $\Theta$；观测 $X = (X_1, \dots, X_n)$
- 考虑形式为 $\hat{\Theta} = a_1X_1 + \dots + a_nX_n + b$ 的估计器
  - 求 $a_1, \dots, a_n, b$ 的最佳选择
  - 最小化：$E[(a_1X_1 + \dots + a_nX_n + b - \Theta)^2]$
- 若 $E[\Theta \mid X]$ 关于 $X$ 线性，则 $\hat{\Theta}_{LMS} = \hat{\Theta}_{LLMS}$
- 求解关于 $b$ 和 $a_i$ 的线性方程组
- 只有均值、方差、协方差起作用
- 若有多个未知 $\Theta_j$，对每个单独应用

---

## 第 10 页

**多观测下最简单的 LLMS 示例**

- $X_1 = \Theta + W_1$
  - $\Theta \sim x_0, \sigma_0^2$
  - $W_i \sim 0, \sigma_i^2$
  - $\vdots$
- $X_n = \Theta + W_n$
  - $\Theta, W_1, \dots, W_n$ 不相关
- 假设 $\Theta, W_1, \dots, W_n$ 独立正态
  - $\hat{\theta}_{LMS} = \mathbb{E}[\Theta \mid X = x] = \dfrac{\sum_{i=0}^{n} \frac{x_i}{\sigma_i^2}}{\sum_{i=0}^{n} \frac{1}{\sigma_i^2}}$
  - $\widehat{\Theta}_{LMS} = \mathbb{E}[\Theta \mid X] = \dfrac{\frac{x_0}{\sigma_0^2} + \sum_{i=1}^{n} \frac{X_i}{\sigma_i^2}}{\sum_{i=0}^{n} \frac{1}{\sigma_i^2}} = \widehat{\Theta}_{LLMS}$
- 假设一般（非正态）分布，
  - 但与正态示例中均值、方差相同
  - 所有协方差也相同
  - 解必然相同

---

## 第 11 页

**数据表示在 LLMS 中很重要**

- 基于 $X$ 与 $X^3$ 的估计
  - LMS：$E[\Theta \mid X]$ 与 $E[\Theta \mid X^3]$ 相同
  - LLMS 不同：估计器 $\hat{\Theta} = aX + b$ 对比 $\hat{\Theta} = aX^3 + b$
- 也可以考虑 $\hat{\Theta} = a_1X + a_2X^2 + a_3X^3 + b$
- 也可以考虑 $\hat{\Theta} = a_1X + a_2e^x + a_3\log X + b$

---

## 第 12 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
