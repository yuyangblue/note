# LECTURE 15：带正态噪声的线性模型

（本译稿为 MIT 6.041SC Lecture 15 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 15：带正态噪声的线性模型**

- $X_i = \sum_{j=1}^{m} a_{ij}\Theta_j + W_i$，$W_i, \Theta_j$：独立、正态
- 非常常见且方便的模型
- 贝叶斯法则：正态后验
- MAP 与 LMS 估计一致
  - 简单公式（关于观测值线性）
- 许多优良性质
- 轨迹估计示例

---

## 第 2 页

**识别正态 PDF**

- $X \sim N(\mu, \sigma^2)$ ｜ $f_X(x) = \dfrac{1}{\sigma\sqrt{2\pi}} e^{-(x-\mu)^2/2\sigma^2}$
- 例：$c \cdot e^{-8(x-3)^2}$
- 一般形式：$f_X(x) = c \cdot e^{-(\alpha x^2 + \beta x + \gamma)}$，$\alpha > 0$
  - 正态分布，均值 $-\beta/2\alpha$，方差 $1/2\alpha$

---

## 第 3 页

**在加性正态噪声存在时估计一个正态随机变量**

- $X = \Theta + W$ ｜ $\Theta, W$：$N(0,1)$，独立
- $f_{X \mid \Theta}(x \mid \theta)$：（讲义留白）
- $f_{\Theta \mid X}(\theta \mid x) = $（讲义留白）
- $\hat{\theta}_{MAP} = \hat{\theta}_{LMS} = E[\Theta \mid X = x] = $（讲义留白）
- $\hat{\Theta}_{MAP} = E[\Theta \mid X] = $（讲义留白）
- $f_{\Theta \mid X}(\theta \mid x) = \dfrac{f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta)}{f_X(x)}$
- $f_X(x) = \int f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta) d\theta$

---

## 第 4 页

**在加性正态噪声存在时估计一个正态随机变量**

- $X = \Theta + W$ ｜ $\Theta, W$：$N(0,1)$，独立
- $\hat{\Theta}_{MAP} = \hat{\Theta}_{LMS} = E[\Theta \mid X] = X/2$
- 即使在一般的均值和方差下：
  - 后验是正态
  - LMS 与 MAP 估计一致
  - 这些估计子是"线性的"，形如 $\hat{\Theta} = aX + b$
- $f_{\Theta \mid X}(\theta \mid x) = \dfrac{f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta)}{f_X(x)}$；$f_X(x) = \int f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta) d\theta$

---

## 第 5 页

**多个观测的情形**

- $X_1 = \Theta + W_1$ ｜ $\Theta \sim N(x_0, \sigma_0^2)$ ｜ $W_i \sim N(0, \sigma_i^2)$
  - $\vdots$
- $X_n = \Theta + W_n$ ｜ $\Theta, W_1, \dots, W_n$ 独立
- $f_{X_i \mid \Theta}(x_i \mid \theta) = $（讲义留白）
- $f_{X \mid \Theta}(x \mid \theta) = $（讲义留白）
- $f_{\Theta \mid X}(\theta \mid x) = $（讲义留白）
- $f_{\Theta \mid X}(\theta \mid x) = \dfrac{f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta)}{f_X(x)}$
- $f_X(x) = \int f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta) d\theta$

---

## 第 6 页

**多个观测的情形**

- $f_{\Theta \mid X}(\theta \mid x) = c \cdot \exp\{-\text{quad}(\theta)\}$
- $\text{quad}(\theta) = \dfrac{(\theta - x_0)^2}{2\sigma_0^2} + \dfrac{(\theta - x_1)^2}{2\sigma_1^2} + \dots + \dfrac{(\theta - x_n)^2}{2\sigma_n^2}$
- $\hat{\theta}_{MAP} = \hat{\theta}_{LMS} = E[\Theta \mid X = x] = \dfrac{\sum_{i=0}^{n} \dfrac{x_i}{\sigma_i^2}}{\sum_{i=0}^{n} \dfrac{1}{\sigma_i^2}}$

---

## 第 7 页

**多个观测的情形**

- 关键结论：
  - 后验是正态
  - LMS 与 MAP 估计一致
  - 这些估计是"线性的"，形如 $\hat{\theta} = a_0 + a_1 x_1 + \dots + a_n x_n$
- 解读：
  - 估计 $\hat{\theta}$：$x_0$（先验均值）与 $x_i$（观测值）的加权平均
  - 权重由方差决定
- $\hat{\theta}_{MAP} = \hat{\theta}_{LMS} = E[\Theta \mid X = x] = \dfrac{\sum_{i=0}^{n} x_i/\sigma_i^2}{\sum_{i=0}^{n} 1/\sigma_i^2}$

---

## 第 8 页

**均方误差**

- $f_{\Theta \mid X}(\theta \mid x) = c \cdot \exp\{-\text{quad}(\theta)\}$
- $\text{quad}(\theta) = \dfrac{(\theta - x_0)^2}{2\sigma_0^2} + \dfrac{(\theta - x_1)^2}{2\sigma_1^2} + \dots + \dfrac{(\theta - x_n)^2}{2\sigma_n^2}$
- 性能指标：
  - $E[(\Theta - \hat{\Theta})^2 \mid X = x] = E[(\Theta - \hat{\theta})^2 \mid X = x] = \text{var}(\Theta \mid X = x) = \dfrac{1}{\sum_{i=0}^{n} (1/\sigma_i^2)}$
  - $E[(\Theta - \hat{\Theta})^2] = $（讲义留白）
- $\hat{\theta} = \dfrac{\sum_{i=0}^{n} (x_i/\sigma_i^2)}{\sum_{i=0}^{n} (1/\sigma_i^2)}$
- $f_X(x) = c \cdot e^{-(\alpha x^2 + \beta x + \gamma)}$，$\alpha > 0$：正态分布，均值 $-\beta/(2\alpha)$，方差 $1/(2\alpha)$

---

## 第 9 页

**均方误差**

- $E[(\Theta - \hat{\Theta})^2 \mid X = x] = E[(\Theta - \hat{\Theta})^2] = 1/\sum_{i=0}^{n} \dfrac{1}{\sigma_i^2}$
- 示例：$\sigma_0^2 = \sigma_1^2 = \dots = \sigma_n^2 = \sigma^2$
  - 条件均方误差对所有 $x$ 相同
- 示例：$X = \Theta + W$，$\Theta \sim N(0,1)$，$W \sim N(0,1)$，$\Theta, W$ 独立
  - $\hat{\Theta} = X/2$
  - $E[(\Theta - \hat{\Theta})^2 \mid X = x] = $（讲义留白）
- $\hat{\theta} = \dfrac{\sum_{i=0}^{n} \dfrac{x_i}{\sigma_i^2}}{\sum_{i=0}^{n} \dfrac{1}{\sigma_i^2}}$

---

## 第 10 页

**多个参数的情形：轨迹估计**

（图示：坐标图，横轴 $t$（0–10），纵轴 $y$（100–400），曲线为 $x(t) = \theta_0 + \theta_1 t + \theta_2 t^2$）

- 随机变量 $\Theta_0, \Theta_1, \Theta_2$：独立；先验 $f_{\Theta_j}$
- 在时刻 $t_1, \dots, t_n$ 的测量值：
  - $X_i = \Theta_0 + \Theta_1 t_i + \Theta_2 t_i^2 + W_i$
  - 噪声模型：$f_{W_i}$
  - $W_i$ 相互独立；且与 $\Theta_j$ 独立

---

## 第 11 页

**一个带正态性假设的模型**

- $X_i = \Theta_0 + \Theta_1 t_i + \Theta_2 t_i^2 + W_i$，$i = 1, \dots, n$
- 假设 $\Theta_j \sim N(0, \sigma_j^2)$，$W_i \sim N(0, \sigma^2)$；独立
- 给定 $\Theta = \theta = (\theta_0, \theta_1, \theta_2)$，$X_i$ 是：
  - $f_{X_i \mid \Theta}(x_i \mid \theta) = c \cdot \exp\left\{-\dfrac{(x_i - \theta_0 - \theta_1 t_i - \theta_2 t_i^2)^2}{2\sigma^2}\right\}$
- 后验：$f_{\Theta \mid X}(\theta \mid x) = $（讲义留白）
  - $= c(x) \exp\left\{-\dfrac{1}{2}\left(\dfrac{\theta_0^2}{\sigma_0^2} + \dfrac{\theta_1^2}{\sigma_1^2} + \dfrac{\theta_2^2}{\sigma_2^2}\right) - \dfrac{1}{2\sigma^2}\sum_{i=1}^{n} (x_i - \theta_0 - \theta_1 t_i - \theta_2 t_i^2)^2\right\}$
- $f_{\Theta \mid X}(\theta \mid x) = \dfrac{f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta)}{f_X(x)}$
- $f_X(x) = \int f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta) d\theta$

---

## 第 12 页

**一个带正态性假设的模型**

- $f_{\Theta \mid X}(\theta \mid x) = c(x) \exp\left\{-\dfrac{1}{2}\left(\dfrac{\theta_0^2}{\sigma_0^2} + \dfrac{\theta_1^2}{\sigma_1^2} + \dfrac{\theta_2^2}{\sigma_2^2}\right) - \dfrac{1}{2\sigma^2}\sum_{i=1}^{n} (x_i - \theta_0 - \theta_1 t_i - \theta_2 t_i^2)^2\right\}$
- MAP 估计：对 $(\theta_0, \theta_1, \theta_2)$ 最大化；（最小化一个二次函数）

---

## 第 13 页

**线性正态模型**

- $\Theta_j$ 和 $X_i$ 都是独立正态随机变量的线性函数
- $f_{\Theta \mid X}(\theta \mid x) = c(x) \exp\{-\text{quadratic}(\theta_1, \dots, \theta_m)\}$
- MAP 估计：对 $(\theta_1, \dots, \theta_m)$ 最大化；（最小化一个二次函数）
- $\hat{\Theta}_{MAP,j}$：$X = (X_1, \dots, X_n)$ 的线性函数
- 事实：
  - $\hat{\Theta}_{MAP,j} = E[\Theta_j \mid X]$
  - $\Theta_j$ 的边缘后验 PDF $f_{\Theta_j \mid X}(\theta_j \mid x)$ 是正态
  - 基于联合后验 PDF 的 MAP 估计：与基于边缘后验 PDF 的 MAP 估计相同
  - $E[(\hat{\Theta}_{i,MAP} - \Theta_i)^2 \mid X = x]$：对所有 $x$ 相同

---

## 第 14 页

**一个图示：估计自由落体物体的轨迹**

- $\Theta_0 \sim N(200, 50^2)$，$\Theta_1 \sim N(50, 50^2)$，$\Theta_2 = -9.81$，$W_i \sim N(0, 50^2)$

（图示：坐标图，横轴 $t$（0–10），纵轴 $-400$ 到 $300$；蓝色曲线为 $X(t) = \Theta_0 + \Theta_1 t + \Theta_2 t^2$，橙色散点为观测数据）

- $X_i = \Theta_0 + \Theta_1 t_i + \Theta_2 t_i^2 + W_i$
- 对 $\theta_0, \theta_1, \theta_2$ 最小化：
  - $\dfrac{1}{2}\left(\dfrac{\theta_0^2}{\sigma_0^2} + \dfrac{\theta_1^2}{\sigma_1^2} + \dfrac{\theta_2^2}{\sigma_2^2}\right) + \dfrac{1}{2\sigma^2}\sum_{i=1}^{n} (x_i - \theta_0 - \theta_1 t_i - \theta_2 t_i^2)^2$

---

## 第 15 页

**一个图示：估计自由落体物体的轨迹**

- $\Theta_0 \sim N(200, 50^2)$，$\Theta_1 \sim N(50, 50^2)$，$\Theta_2 = -9.81$，$W_i \sim N(0, 50^2)$

（图示：坐标图，横轴 $t$（0–10），纵轴 $-400$ 到 $300$；蓝色曲线为轨迹 $X(t) = \Theta_0 + \Theta_1 t + \Theta_2 t^2$，红色散点为观测样本）

- $X_i = \Theta_0 + \Theta_1 t_i + \Theta_2 t_i^2 + W_i$
- 对 $\theta_0, \theta_1$ 最小化：
  - $(\theta_0 - 200)^2 + (\theta_1 - 50)^2 + \sum_{i=1}^{n}(x_i - \theta_0 - \theta_1 t_i + 9.81 t_i^2)^2$

---

## 第 16 页

**一个图示：估计自由落体物体的轨迹**

- $\Theta_0 \sim N(200, 50^2)$，$\Theta_1 \sim N(50, 50^2)$，$\Theta_2 = -9.81$，$W_i \sim N(0, 50^2)$

（图示：坐标图，横轴 $t$（0–10），纵轴 $-500$ 到 $300$；红色散点与曲线、蓝色曲线，先上升后下降）

- $X_i = \Theta_0 + \Theta_1 t_i + \Theta_2 t_i^2 + W_i$
- 对 $\theta_0, \theta_1$ 最小化：
  - $(\theta_0 - 200)^2 + (\theta_1 - 50)^2 + \sum_{(i=1)}^{n} (x_i - \theta_0 - \theta_1 t_i + 9.81 t_i^2)^2$

---

## 第 17 页

**一个图示：估计自由落体物体的轨迹**

- $\Theta_0 \sim N(200, 50^2)$，$\Theta_1 \sim N(50, 50^2)$，$\Theta_2 = -9.81$，$W_i \sim N(0, 50^2)$

（图示：坐标图，横轴 $t$（0–10），纵轴 $-300$ 到 $400$；蓝色抛物线轨迹与红色星号观测点）

- $X_i = \Theta_0 + \Theta_1 t_i + \Theta_2 t_i^2 + W_i$
- 对 $\theta_0, \theta_1$ 最小化：
  - $(\theta_0 - 200)^2 + (\theta_1 - 50)^2 + \sum_{i=1}^{n} (x_i - \theta_0 - \theta_1 t_i + 9.81 t_i^2)^2$

---

## 第 18 页

**一个图示：估计自由落体物体的轨迹**

- $\Theta_0 \sim N(200, 50^2)$，$\Theta_1 \sim N(50, 50^2)$，$\Theta_2 = -9.81$，$W_i \sim N(0, 50^2)$

（图示：坐标图，横轴 $t$（0–10），纵轴 $-300$ 到 $400$；红、蓝两条抛物线轨迹曲线与红色星号数据点）

- $X_i = \Theta_0 + \Theta_1 t_i + \Theta_2 t_i^2 + W_i$
- 对 $\theta_0, \theta_1$ 最小化：
  - $(\theta_0 - 200)^2 + (\theta_1 - 50)^2 + \sum_{i=1}^{n} (x_i - \theta_0 - \theta_1 t_i + 9.81 t_i^2)^2$

---

## 第 19 页

**一个图示：估计自由落体物体的轨迹**

- $\Theta_0 \sim N(200, 50^2)$，$\Theta_1 \sim N(50, 50^2)$，$\Theta_2 = -9.81$，$W_i \sim N(0, 50^2)$

（图示：坐标图，横轴 $t$（0–10），纵轴 $-300$ 到 $400$；蓝色为真实轨迹，红色为基于 MAP 的估计轨迹，红色星号为采样点，另有 95% 置信区间线）

- 真实 $\theta_0 = 236.2702$ ｜ MAP $\hat{\theta}_0 = 256.0561$ ｜ 误差标准差 $(\hat{\theta}_0) = 21.1193$
- 真实 $\theta_1 = 46.8473$ ｜ MAP $\hat{\theta}_1 = 48.282$ ｜ 误差标准差 $(\hat{\theta}_1) = 3.2538$
- 图例：真实轨迹、采样点、基于 MAP 的估计轨迹、95% 置信区间
- $X_i = \Theta_0 + \Theta_1 t_i + \Theta_2 t_i^2 + W_i$
- 对 $\theta_0, \theta_1$ 最小化：
  - $(\theta_0 - 200)^2 + (\theta_1 - 50)^2 + \sum_{i=1}^{n} (x_i - \theta_0 - \theta_1 t_i + 9.81 t_i^2)^2$

---

## 第 20 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
