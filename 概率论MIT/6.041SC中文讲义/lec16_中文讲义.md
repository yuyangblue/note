# LECTURE 16：最小均方（LMS）估计

（本译稿为 MIT 6.041SC Lecture 16 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 16：最小均方（LMS）估计**

- 最小化（条件）均方误差 $E[(\Theta - \hat{\theta})^2 \mid X = x]$
  - 解：$\hat{\theta} = E[\Theta \mid X = x]$
  - 通用的估计方法
- 数学性质
- 示例

---

## 第 2 页

**没有观测时的 LMS 估计**

- 未知 $\Theta$；先验 $p_\Theta(\theta)$
  - 关注点估计 $\hat{\theta}$
  - 没有可用的观测
- MAP 准则：
- （条件）期望：
- 准则：均方误差（MSE）：$E\left[(\Theta - \hat{\theta})^2\right]$
  - 最小化均方误差

（图示：先验 $f_\Theta(\theta)$ 图，$[4, 10]$ 上均匀，密度值 $1/6$）

---

## 第 3 页

**没有观测时的 LMS 估计**

- 最小均方表述：
  - 最小化均方误差（MSE）$E[(\Theta - \hat{\theta})^2]$：$\hat{\theta} = E[\Theta]$
- 最优均方误差：$E[(\Theta - E[\Theta])^2] = \text{var}(\Theta)$

---

## 第 4 页

**基于 $X$ 的 $\Theta$ 的 LMS 估计**

- 未知 $\Theta$；先验 $p_\Theta(\theta)$
  - 关注点估计 $\hat{\theta}$
- 观测 $X$；模型 $p_{X \mid \Theta}(x \mid \theta)$
  - 观测到 $X = x$
- 最小化均方误差（MSE），$E[(\Theta - \hat{\theta})^2]$：$\hat{\theta} = E[\Theta]$
- 最小化条件均方误差，$E[(\Theta - \hat{\theta})^2 \mid X = x]$：$\hat{\theta} = E[\Theta \mid X = x]$
- LMS 估计值：$\hat{\theta} = E[\Theta \mid X = x]$
  - 估计子：$\hat{\Theta} = E[\Theta \mid X]$

---

## 第 5 页

**基于 $X$ 的 $\Theta$ 的 LMS 估计**

- $E[\Theta]$ 最小化 $E[(\Theta - \hat{\theta})^2]$
- $E[\Theta \mid X = x]$ 最小化 $E[(\Theta - \hat{\theta})^2 \mid X = x]$
- $\hat{\Theta}_{LMS} = E[\Theta \mid X]$ 在所有形如 $\hat{\Theta} = g(X)$ 的估计子中最小化 $E[(\Theta - g(X))^2]$

---

## 第 6 页

**LMS 性能评估**

- LMS 估计值：$\hat{\theta} = E[\Theta \mid X = x]$
  - 估计子：$\hat{\Theta} = E[\Theta \mid X]$
- 一旦我们有了测量值后的期望性能：
  - MSE $= E[(\Theta - E[\Theta \mid X = x])^2 \mid X = x] = \text{var}(\Theta \mid X = x)$
- 该设计的期望性能：
  - MSE $= E[(\Theta - E[\Theta \mid X])^2] = E[\text{var}(\Theta \mid X)]$

---

## 第 7 页

**基于 $X$ 的 $\Theta$ 的 LMS 估计**

- LMS 与估计相关（而非假设检验）
- 若后验是单峰且关于均值对称，则与 MAP 相同
  - 例：后验为正态时（"线性—正态"模型的情形）

---

## 第 8 页

**示例**

（图示：上左为 $f_\Theta(\theta)$ 图，$[4, 10]$ 上均匀，密度 $1/6$；下左为 $f_{X \mid \Theta}(x \mid \theta)$ 图，$[\theta-1, \theta+1]$ 上均匀，密度 $1/2$；右为 $x$–$\theta$ 平面上的平行四边形联合取值区域，$x$ 轴刻度 $3, 5, 9, 11$，$\theta$ 轴刻度 $4, 10$）

---

## 第 9 页

**条件均方误差**

（图示：上左为 $f_\Theta(\theta)$ 图，$[4, 10]$ 上均匀，密度 $1/6$；中左为 $f_{X \mid \Theta}(x \mid \theta)$ 图，$[\theta-1, \theta+1]$ 上均匀，密度 $1/2$；右上为 $x$–$\theta$ 平面上的平行四边形区域（斜向矩形，内部有蓝色线条，两端红色标记）；右下为 $\text{Var}(\Theta \mid X = x)$ 随 $x$ 变化的图，$x$ 轴刻度 $3, 5, 9, 11$）

- $E[(\Theta - E[\Theta \mid X = x])^2 \mid X = x]$
  - 与 $\text{Var}(\Theta \mid X = x)$ 相同：即 $\Theta$ 的条件分布的方差

---

## 第 10 页

**多个观测或未知量的 LMS 估计**

- 未知 $\Theta$；先验 $p_\Theta(\theta)$
  - 关注点估计 $\hat{\theta}$
- 观测 $X = (X_1, X_2, \dots, X_n)$；模型 $p_{X \mid \Theta}(x \mid \theta)$
  - 观测到 $X = x$
  - 新的宇宙：以 $X = x$ 为条件
- LMS 估计值：$E[\Theta \mid X_1 = x_1, \dots, X_n = x_n]$
- 若 $\Theta$ 是向量，则对每个分量分别应用

---

## 第 11 页

**LMS 估计中的一些挑战**

- $f_{\Theta \mid X}(\theta \mid x) = \dfrac{f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta)}{f_X(x)}$
- $f_X(x) = \int f_\Theta(\theta') f_{X \mid \Theta}(x \mid \theta') d\theta'$
- 完整正确的模型 $f_{X \mid \Theta}(x \mid \theta)$ 可能不可用
- 可能难以计算/实现/分析

---

## 第 12 页

**LMS 估计中估计误差的性质**

- 估计子：$\hat{\Theta} = E[\Theta \mid X]$ ｜ 误差：$\tilde{\Theta} = \hat{\Theta} - \Theta$
- $E[\tilde{\Theta} \mid X = x] = 0$
- $\text{cov}(\tilde{\Theta}, \hat{\Theta}) = 0$
- $\text{var}(\Theta) = \text{var}(\hat{\Theta}) + \text{var}(\tilde{\Theta})$

---

## 第 13 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
