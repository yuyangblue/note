# LECTURE 15：带正态噪声的线性模型

（本译稿为 MIT 6.041SC Lecture 15 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 15：带正态噪声的线性模型**

- $X_i = \sum_{j=1}^{m} a_{ij}\Theta_j + W_i$
  - $W_i, \Theta_j$：独立，正态
- 非常常见且方便的模型
- 贝叶斯法则：正态后验
- MAP 与 LMS 估计一致
  - 简单公式
  - （关于观测线性）
- 许多优良性质
- 轨迹估计示例

---

## 第 2 页

**识别正态 PDF**

- $X \sim N(\mu, \sigma^2)$
- $f_X(x) = \dfrac{1}{\sigma\sqrt{2\pi}} e^{-(x-\mu)^2/(2\sigma^2)}$
- $c \cdot e^{-8(x-3)^2}$
- $f_X(x) = c \cdot e^{-(\alpha x^2 + \beta x + \gamma)}$，$\alpha > 0$：正态，均值 $-\beta/(2\alpha)$，方差 $1/(2\alpha)$

---

## 第 3 页

**在加性正态噪声存在时估计正态随机变量**

- $X = \Theta + W$
  - $\Theta, W$：$N(0,1)$，独立
- $f_{X \mid \Theta}(x \mid \theta):$（讲义留白）
- $f_{\Theta \mid X}(\theta \mid x) = $（讲义留白）
- $\hat{\theta}_{MAP} = \hat{\theta}_{LMS} = \mathbb{E}[\Theta \mid X = x] = $（讲义留白）
- $\widehat{\Theta}_{MAP} = \mathbb{E}[\Theta \mid X] = $（讲义留白）
- $f_{\Theta \mid X}(\theta \mid x) = \dfrac{f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta)}{f_X(x)}$
- $f_X(x) = \int f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta) \, d\theta$

---

## 第 4 页

**在加性正态噪声存在时估计正态随机变量**

- $X = \Theta + W$
  - $\Theta, W$：$N(0,1)$，独立
- $\widehat{\Theta}_{MAP} = \widehat{\Theta}_{LMS} = \mathbb{E}[\Theta \mid X] = \dfrac{X}{2}$
- 即使对一般的均值与方差：
  - 后验是正态的
  - LMS 与 MAP 估计器一致
  - 这些估计器是"线性"的，形式为 $\widehat{\Theta} = aX + b$
- $f_{\Theta \mid X}(\theta \mid x) = \dfrac{f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta)}{f_X(x)}$
- $f_X(x) = \int f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta) \, d\theta$

---

## 第 5 页

**多观测的情形**

- $X_1 = \Theta + W_1$
  - $\Theta \sim N(x_0, \sigma_0^2)$
  - $W_i \sim N(0, \sigma_i^2)$
  - $\vdots$
- $X_n = \Theta + W_n$
  - $\Theta, W_1, \dots, W_n$ 独立
- $f_{X_i \mid \Theta}(x_i \mid \theta) = $（讲义留白）
- $f_{X \mid \Theta}(x \mid \theta) = $（讲义留白）
- $f_{\Theta \mid X}(\theta \mid x) = $（讲义留白）
- $f_{\Theta \mid X}(\theta \mid x) = \dfrac{f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta)}{f_X(x)}$
- $f_X(x) = \int f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta) \, d\theta$

---

## 第 6 页

**多观测的情形**

- $f_{\Theta \mid X}(\theta \mid x) = c \cdot \exp\{-\text{quad}(\theta)\}$
- $\text{quad}(\theta) = \dfrac{(\theta - x_0)^2}{2\sigma_0^2} + \dfrac{(\theta - x_1)^2}{2\sigma_1^2} + \dots + \dfrac{(\theta - x_n)^2}{2\sigma_n^2}$
- $\hat{\theta}_{MAP} = \hat{\theta}_{LMS} = E[\Theta \mid X = x] = \dfrac{\sum_{i=0}^{n} x_i/\sigma_i^2}{\sum_{i=0}^{n} 1/\sigma_i^2}$

---

## 第 7 页

**多观测的情形**

- 关键结论：
  - 后验是正态的
  - LMS 与 MAP 估计一致
  - 这些估计是"线性"的，形式为 $\hat{\theta} = a_0 + a_1x_1 + \dots + a_nx_n$
- 解读：
  - 估计 $\hat{\theta}$：$x_0$（先验均值）与 $x_i$（观测）的加权平均
  - 权重由方差决定
- $\hat{\theta}_{MAP} = \hat{\theta}_{LMS} = E[\Theta \mid X = x] = \dfrac{\sum_{i=0}^{n} x_i/\sigma_i^2}{\sum_{i=0}^{n} 1/\sigma_i^2}$

---

## 第 8 页

**均方误差**

- $f_{\Theta \mid X}(\theta \mid x) = c \cdot \exp\{-\text{quad}(\theta)\}$
- $\text{quad}(\theta) = \dfrac{(\theta - x_0)^2}{2\sigma_0^2} + \dfrac{(\theta - x_1)^2}{2\sigma_1^2} + \dots + \dfrac{(\theta - x_n)^2}{2\sigma_n^2}$
- 性能度量：
  - $\mathbb{E}[(\Theta - \widehat{\Theta})^2 \mid X = x] = \mathbb{E}[(\Theta - \hat{\theta})^2 \mid X = x] = \text{var}(\Theta \mid X = x) = 1\Big/\sum_{i=0}^{n} \dfrac{1}{\sigma_i^2}$
  - $\mathbb{E}[(\Theta - \widehat{\Theta})^2] = $（讲义留白）
- $\hat{\theta} = \dfrac{\sum_{i=0}^{n} \frac{x_i}{\sigma_i^2}}{\sum_{i=0}^{n} \frac{1}{\sigma_i^2}}$
- $f_X(x) = c \cdot e^{-(\alpha x^2 + \beta x + \gamma)}$，$\alpha > 0$：正态，均值 $-\beta/2\alpha$，方差 $1/2\alpha$

---

## 第 9 页

**均方误差**

- $\mathrm{E}[(\Theta - \widehat{\Theta})^2 \mid X = x] = \mathrm{E}[(\Theta - \widehat{\Theta})^2] = 1\Big/\sum_{i=0}^{n} \frac{1}{\sigma_i^2}$
- 示例：$\sigma_0^2 = \sigma_1^2 = \dots = \sigma_n^2 = \sigma^2$
  - 条件均方误差对所有 $x$ 相同
- 示例：$X = \Theta + W$，$\Theta \sim N(0,1)$，$W \sim N(0,1)$
  - $\Theta, W$ 独立
  - $\widehat{\Theta} = X/2$
  - $\mathrm{E}[(\Theta - \widehat{\Theta})^2 \mid X = x] = $（讲义留白）
- $\widehat{\theta} = \dfrac{\sum_{i=0}^{n} \frac{x_i}{\sigma_i^2}}{\sum_{i=0}^{n} \frac{1}{\sigma_i^2}}$

---

## 第 10 页

**多参数的情形：轨迹估计**

（图示：左侧为 $t$–$y$ 坐标系中的二次曲线，纵轴刻度 100–400，横轴 t 刻度 0–10）

- $x(t) = \theta_0 + \theta_1t + \theta_2t^2$
- 随机变量 $\Theta_0, \Theta_1, \Theta_2$
  - 独立；先验 $f_{\Theta_j}$
- 时刻 $t_1, \dots, t_n$ 处的测量
  - $X_i = \Theta_0 + \Theta_1t_i + \Theta_2t_i^2 + W_i$
  - 噪声模型：$f_{W_i}$
  - $W_i$ 独立；且与 $\Theta_j$ 独立

---

## 第 11 页

**带正态性假设的模型**

- $X_i = \Theta_0 + \Theta_1t_i + \Theta_2t_i^2 + W_i$，$i = 1, \dots, n$
- 假设 $\Theta_j \sim N(0, \sigma_j^2)$，$W_i \sim N(0, \sigma^2)$；独立
- 给定 $\Theta = \theta = (\theta_0, \theta_1, \theta_2)$，$X_i$ 为：
  - $f_{X_i \mid \Theta}(x_i \mid \theta) = c \cdot \exp\left\{-(x_i - \theta_0 - \theta_1t_i - \theta_2t_i^2)^2/2\sigma^2\right\}$
- 后验：$f_{\Theta \mid X}(\theta \mid x) = $（讲义留白）
  - $c(x)\exp\left\{-\frac{1}{2}\left(\frac{\theta_0^2}{\sigma_0^2} + \frac{\theta_1^2}{\sigma_1^2} + \frac{\theta_2^2}{\sigma_2^2}\right) - \frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i - \theta_0 - \theta_1t_i - \theta_2t_i^2)^2\right\}$
- $f_{\Theta \mid X}(\theta \mid x) = \dfrac{f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta)}{f_X(x)}$
- $f_X(x) = \int f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta) \, d\theta$

---

## 第 12 页

**带正态性假设的模型**

- $f_{\Theta \mid X}(\theta \mid x) = c(x)\exp\left\{-\frac{1}{2}\left(\frac{\theta_0^2}{\sigma_0^2} + \frac{\theta_1^2}{\sigma_1^2} + \frac{\theta_2^2}{\sigma_2^2}\right) - \frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i - \theta_0 - \theta_1t_i - \theta_2t_i^2)^2\right\}$
- MAP 估计：对 $(\theta_0, \theta_1, \theta_2)$ 最大化；
  - （最小化二次函数）

---

## 第 13 页

**线性正态模型**

- $\Theta_j$ 与 $X_i$ 是独立正态随机变量的线性函数
- $f_{\Theta \mid X}(\theta \mid x) = c(x)\exp\left\{-\text{quadratic}(\theta_1, \dots, \theta_m)\right\}$
- MAP 估计：对 $(\theta_1, \dots, \theta_m)$ 最大化；
  - （最小化二次函数）
- $\widehat{\Theta}_{MAP,j}$：$X = (X_1, \dots, X_n)$ 的线性函数
- 事实：
  - $\widehat{\Theta}_{MAP,j} = \mathbb{E}[\Theta_j \mid X]$
  - $\Theta_j$ 的边缘后验 PDF：$f_{\Theta_j \mid X}(\theta_j \mid x)$，是正态的
  - 基于联合后验 PDF 的 MAP 估计：与基于边缘后验 PDF 的 MAP 估计相同
  - $\mathbb{E}\left[(\widehat{\Theta}_{i,MAP} - \Theta_i)^2 \mid X = x\right]$：对所有 $x$ 相同

---

## 第 14 页

**一个示例**

- 估计自由落体物体的轨迹
- $\Theta_0 \sim N(200, 50^2)$，$\Theta_1 \sim N(50, 50^2)$，$\Theta_2 = -9.81$，$W_i \sim N(0, 50^2)$

（图示：左侧为 $t$–$X(t)$ 坐标系，蓝色为理论轨迹曲线，红色星号为观测样本点，纵轴 300 至 -400，横轴 t 0–10）

- $X(t) = \Theta_0 + \Theta_1t + \Theta_2t^2$
- $X_i = \Theta_0 + \Theta_1t_i + \Theta_2t_i^2 + W_i$
- 最小化
  - $\dfrac{1}{2}\left(\dfrac{\theta_0^2}{\sigma_0^2} + \dfrac{\theta_1^2}{\sigma_1^2} + \dfrac{\theta_2^2}{\sigma_2^2}\right)$
  - $+ \dfrac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i - \theta_0 - \theta_1t_i - \theta_2t_i^2)^2$，关于 $\theta_0, \theta_1, \theta_2$

---

## 第 15 页

**一个示例**

- 估计自由落体物体的轨迹
- $\Theta_0 \sim N(200, 50^2)$，$\Theta_1 \sim N(50, 50^2)$，$\Theta_2 = -9.81$，$W_i \sim N(0, 50^2)$

（图示：左侧为 $t$–$X(t)$ 坐标系，蓝色抛物线、红色观测散点，纵轴 300 至 -400，横轴 t 0–10）

- $X(t) = \Theta_0 + \Theta_1t + \Theta_2t^2$
- $X_i = \Theta_0 + \Theta_1t_i + \Theta_2t_i^2 + W_i$
- 最小化，关于 $\theta_0, \theta_1$：
  - $\dfrac{(\theta_0 - 200)^2 + (\theta_1 - 50)^2}{}$
  - $+ \sum_{i=1}^{n}(x_i - \theta_0 - \theta_1t_i + 9.81t_i^2)^2$

---

## 第 16 页

**一个示例**

- 估计自由落体物体的轨迹
- $\Theta_0 \sim N(200, 50^2)$，$\Theta_1 \sim N(50, 50^2)$，$\Theta_2 = -9.81$，$W_i \sim N(0, 50^2)$

（图示：左侧为 $t$–$X(t)$ 坐标系，红色数据点、红色曲线与蓝色曲线，纵轴 300 至 -500，横轴 t 0–10）

- $X_i = \Theta_0 + \Theta_1t_i + \Theta_2t_i^2 + W_i$
- 最小化，关于 $\theta_0, \theta_1$：
  - $(\theta_0 - 200)^2 + (\theta_1 - 50)^2$
  - $+ \sum_{i=1}^{n}(x_i - \theta_0 - \theta_1t_i + 9.81t_i^2)^2$

---

## 第 17 页

**一个示例**

- 估计自由落体物体的轨迹
- $\Theta_0 \sim N(200, 50^2)$，$\Theta_1 \sim N(50, 50^2)$，$\Theta_2 = -9.81$，$W_i \sim N(0, 50^2)$

（图示：左侧为 $t$–$X(t)$ 坐标系，蓝色抛物线、红色星号观测点，纵轴 400 至 -300，横轴 t 0–10）

- $X_i = \Theta_0 + \Theta_1t_i + \Theta_2t_i^2 + W_i$
- 最小化，关于 $\theta_0, \theta_1$：
  - $(\theta_0 - 200)^2 + (\theta_1 - 50)^2$
  - $+ \sum_{i=1}^{n}(x_i - \theta_0 - \theta_1t_i + 9.81t_i^2)^2$

---

## 第 18 页

**一个示例**

- 估计自由落体物体的轨迹
- $\Theta_0 \sim N(200, 50^2)$，$\Theta_1 \sim N(50, 50^2)$，$\Theta_2 = -9.81$，$W_i \sim N(0, 50^2)$

（图示：左侧为 $t$–$X(t)$ 坐标系，红色与蓝色两条抛物曲线、红色星型数据点，纵轴 400 至 -300，横轴 t 0–10）

- $X_i = \Theta_0 + \Theta_1t_i + \Theta_2t_i^2 + W_i$
- 最小化，关于 $\theta_0, \theta_1$：
  - $(\theta_0 - 200)^2 + (\theta_1 - 50)^2$
  - $+ \sum_{i=1}^{n}(x_i - \theta_0 - \theta_1t_i + 9.81t_i^2)^2$

---

## 第 19 页

**一个示例**

- 估计自由落体物体的轨迹
- $\Theta_0 \sim N(200, 50^2)$，$\Theta_1 \sim N(50, 50^2)$，$\Theta_2 = -9.81$，$W_i \sim N(0, 50^2)$

（图示：左侧为 $t$–$X(t)$ 坐标系，蓝色真实轨迹、红色基于 MAP 的估计轨迹、红色星号采样点、灰色 95% 置信区间，纵轴 400 至 -300，横轴 t 0–10；图下方列出：True $\theta_0 = 236.2702$，MAP $\hat{\theta}_0 = 256.0561$，Error std($\tilde{\theta}_0$) = 21.1193；True $\theta_1 = 46.8473$，MAP $\hat{\theta}_1 = 48.282$，Error std($\tilde{\theta}_1$) = 3.2538；图例：真实轨迹、采样点、基于 MAP 的估计轨迹、95% 置信区间）

- $X_i = \Theta_0 + \Theta_1t_i + \Theta_2t_i^2 + W_i$
- 最小化，关于 $\theta_0, \theta_1$：
  - $(\theta_0 - 200)^2 + (\theta_1 - 50)^2$
  - $+ \sum_{i=1}^{n}(x_i - \theta_0 - \theta_1t_i + 9.81t_i^2)^2$

---

## 第 20 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
