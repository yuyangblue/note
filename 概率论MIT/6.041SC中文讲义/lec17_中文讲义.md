# LECTURE 17：线性最小均方（LLMS）估计

（本译稿为 MIT 6.041SC Lecture 17 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 17：线性最小均方（LLMS）估计**

- 条件期望 $E[\Theta \mid X]$ 可能难以计算/实现
- 限定估计子为 $\hat{\Theta} = aX + b$
  - 最小化均方误差
- 简单解
- 数学性质
- 示例

---

## 第 2 页

**LLMS 表述**

- 未知 $\Theta$；观测 $X$

（图示：坐标图，横轴 $x$（刻度 3, 5, 9, 11），纵轴 $\theta$（刻度 4, 10）；倾斜四边形区域内绘有红色直线与蓝色折线）

- 最小化 $E[(\hat{\Theta} - \Theta)^2]$
- 估计子 $\hat{\Theta} = g(X)$ → $\hat{\Theta}_{LMS} = E[\Theta \mid X]$
- 考虑 $\Theta$ 的形如 $\hat{\Theta} = aX + b$ 的估计子
- 关于 $a, b$ 最小化 $E[(\Theta - aX - b)^2]$
- 若 $E[\Theta \mid X]$ 关于 $X$ 线性，则 $\hat{\Theta}_{LMS} = \hat{\Theta}_{LLMS}$

---

## 第 3 页

**LLMS 问题的解**

- 关于 $a, b$ 最小化 $E[(\Theta - aX - b)^2]$
  - 假设 $a$ 已经求出：
- $\hat{\Theta}_L = E[\Theta] + \dfrac{\text{Cov}(\Theta, X)}{\text{var}(X)}(X - E[X]) = E[\Theta] + \rho\dfrac{\sigma_\Theta}{\sigma_X}(X - E[X])$

---

## 第 4 页

**关于解与误差方差的备注**

- $\hat{\Theta}_L = E[\Theta] + \dfrac{\text{Cov}(\Theta, X)}{\text{var}(X)}(X - E[X]) = E[\Theta] + \rho\dfrac{\sigma_\Theta}{\sigma_X}(X - E[X])$
- 只有均值、方差、协方差起作用
- $\rho > 0$：（讲义留白）
- $\rho = 0$：（讲义留白）
- $E[(\hat{\Theta}_L - \Theta)^2] = (1 - \rho^2)\text{var}(\Theta)$
- $|\rho| = 1$：（讲义留白）

---

## 第 5 页

**示例**

（图示：坐标图，横轴 $x$（刻度 3, 5, 9, 11），纵轴 $\theta$（刻度 4, 10）；黑色斜向带状区域内，红色直线与蓝色折线，红色直线对应线性拟合关系）

- $\hat{\Theta}_L = E[\Theta] + \dfrac{\text{Cov}(\Theta, X)}{\text{var}(X)}(X - E[X]) = E[\Theta] + \rho\dfrac{\sigma_\Theta}{\sigma_X}(X - E[X])$

---

## 第 6 页

**LLMS 用于推断一枚硬币的参数**

- 标准示例：
  - 硬币偏置 $\Theta$；先验 $f_\Theta(\cdot)$
  - 固定 $n$；$X$ = 正面次数
- 假设 $f_\Theta(\cdot)$ 在 $[0,1]$ 上均匀
- $\hat{\Theta}_{LMS} = \dfrac{X + 1}{n + 2} = \hat{\Theta}_{LLMS}$
- $\hat{\Theta}_{LLMS} = E[\Theta] + \dfrac{\text{Cov}(\Theta, X)}{\text{var}(X)}(X - E[X])$

---

## 第 7 页

**LLMS 用于推断一枚硬币的参数**

- $\Theta$：$[0,1]$ 上均匀 ｜ $E[\Theta] = 1/2$ ｜ $\text{var}(\Theta) = 1/12$ ｜ $E[\Theta^2] = $（讲义留白）
- $p_{X \mid \Theta}$：$\text{Bin}(n, \Theta)$ ｜ $E[X \mid \Theta] = n\Theta$ ｜ $\text{var}(X \mid \Theta) = n\Theta(1 - \Theta)$
- $E[X] = $（讲义留白）
- $E[X^2 \mid \Theta] = $（讲义留白）
- $E[X^2] = $（讲义留白）
- $\text{var}(X) = $（讲义留白）
- $E[\Theta X \mid \Theta] = $（讲义留白）
- $E[\Theta X] = $（讲义留白）
- $\text{cov}(\Theta, X) = $（讲义留白）

---

## 第 8 页

**LLMS 用于推断一枚硬币的参数**

- $\hat{\Theta}_{LLMS} = E[\Theta] + \dfrac{\text{Cov}(\Theta, X)}{\text{var}(X)}(X - E[X])$
- $\text{cov}(\Theta, X) = \dfrac{n}{12}$
- $\text{var}(X) = \dfrac{n(n + 2)}{12}$
- $E[X] = \dfrac{n}{2}$
- $\hat{\Theta}_{LLMS} = \dfrac{X + 1}{n + 2}$

---

## 第 9 页

**多个观测的 LLMS**

- 未知 $\Theta$；观测 $X = (X_1, \dots, X_n)$
- 考虑形如 $\hat{\Theta} = a_1 X_1 + \dots + a_n X_n + b$ 的估计子
- 找 $a_1, \dots, a_n, b$ 的最佳选择
  - 最小化：$E[(a_1 X_1 + \dots + a_n X_n + b - \Theta)^2]$
- 若 $E[\Theta \mid X]$ 关于 $X$ 线性，则 $\hat{\Theta}_{LMS} = \hat{\Theta}_{LLMS}$
- 求解关于 $b$ 和 $a_i$ 的线性方程组
- 只有均值、方差、协方差起作用
- 若有多个未知量 $\Theta_j$，对每个分别应用

---

## 第 10 页

**多观测情形下最简单的 LLMS 示例**

- $X_1 = \Theta + W_1$ ｜ $\Theta \sim x_0, \sigma_0^2$ ｜ $W_i \sim 0, \sigma_i^2$
  - $\vdots$
- $X_n = \Theta + W_n$ ｜ $\Theta, W_1, \dots, W_n$ 不相关
- 假设 $\Theta, W_1, \dots, W_n$ 是独立正态
  - $\hat{\theta}_{LMS} = E[\Theta \mid X = x] = \dfrac{\sum_{(i=0)}^{n} x_i/\sigma_i^2}{\sum_{(i=0)}^{n} 1/\sigma_i^2}$
  - $\hat{\Theta}_{LMS} = E[\Theta \mid X] = \dfrac{x_0/\sigma_0^2 + \sum_{(i=1)}^{n} X_i/\sigma_i^2}{\sum_{(i=0)}^{n} 1/\sigma_i^2} = \hat{\Theta}_{LLMS}$
- 假设一般（非正态）分布，
  - 但与正态示例具有相同的均值、方差，
  - 所有协方差也相同
  - 解必定相同

---

## 第 11 页

**数据的表示在 LLMS 中很重要**

- 基于 $X$ 与基于 $X^3$ 的估计
  - LMS：$E[\Theta \mid X]$ 与 $E[\Theta \mid X^3]$ 相同
  - LLMS 不同：估计子 $\hat{\Theta} = aX + b$ 与 $\hat{\Theta} = aX^3 + b$ 不同
- 也可以考虑 $\hat{\Theta} = a_1 X + a_2 X^2 + a_3 X^3 + b$
- 也可以考虑 $\hat{\Theta} = a_1 X + a_2 e^x + a_3 \log X + b$

---

## 第 12 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
