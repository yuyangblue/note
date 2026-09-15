# LECTURE 8：连续随机变量与概率密度函数

（本译稿为 MIT 6.041SC Lecture 8 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 8：连续随机变量与概率密度函数**

- 概率密度函数
  - 性质
  - 示例
- 期望及其性质
  - 期望值法则
  - 线性性
- 方差及其性质
- 均匀与指数随机变量
- 累积分布函数
- 正态随机变量
  - 期望与方差
  - 线性性质
  - 用表计算概率

---

## 第 2 页

**概率密度函数（PDF）**

- 离散情形：$p_X(x)$
- 连续情形：PDF $f_X(x)$
- $\mathrm{P}(a \le X \le b) = \sum_{x: a \le x \le b} p_X(x)$
- $\mathrm{P}(a \le X \le b) = \int_a^b f_X(x) \, dx$
- $p_X(x) \ge 0$
- $f_X(x) \ge 0$
- $\sum_x p_X(x) = 1$
- $\int_{-\infty}^{\infty} f_X(x) \, dx = 1$
- 定义：如果一个随机变量可以用一个 PDF 描述，则它是连续的

（图示：左侧为 $p_X(x)$ 柱状图，右侧为 $f_X(x)$ 曲线图，灰色区域标注 $\mathrm{P}(a \le X \le b)$）

---

## 第 3 页

**概率密度函数（PDF）**

- PDF $f_X(x)$
- $\mathrm{P}(a \le X \le b)$
- $\mathrm{P}(a \le X \le a + \delta) \approx f_X(a) \cdot \delta$
- $\mathrm{P}(X = a) = 0$
- $\mathrm{P}(a \le X \le b) = \int_a^b f_X(x) \, dx$
- $f_X(x) \ge 0$
- $\int_{-\infty}^{\infty} f_X(x) \, dx = 1$

（图示：右侧 $f_X(x)$ 曲线下 $a$ 到 $b$ 的灰色阴影区域标注 $\mathrm{P}(a \le X \le b)$）

---

## 第 4 页

**示例：连续均匀 PDF**

- 离散均匀：$p_X(x) = \dfrac{1}{b-a+1}$（取值 $a, a+1, \dots, b$）
- 连续均匀：$f_X(x) = \dfrac{1}{b-a}$（区间 $[a,b]$）
- 推广：分段常数 PDF

（图示：左侧为离散均匀 PMF 柱状图（横轴 $a$、$a+1$、$b$）；右上为连续均匀 PDF 矩形图（横轴 $a$、$b$）；右下为分段常数 PDF 阶梯图（横轴 $a$、$b$、$c$、$d$））

---

## 第 5 页

**连续随机变量的期望/均值**

- $E[X] = \sum_x x p_X(x)$
- $E[X] = \int_{-\infty}^{\infty} x f_X(x) \, dx$
- 解释：大量独立重复实验中取平均
- 小字说明：假设 $\int_{-\infty}^{\infty} |x| f_X(x) \, dx < \infty$

（图示：左侧为 $p_X(x)$ 柱状图；右侧为 PDF $f_X(x)$ 曲线图，标注 $P(a \le X \le b)$ 区域）

---

## 第 6 页

**期望的性质**

- 若 $X \ge 0$，则 $E[X] \ge 0$
- 若 $a \le X \le b$，则 $a \le E[X] \le b$
- 期望值法则：
  - $E[g(X)] = \sum_x g(x) p_X(x)$
  - $E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) \, dx$
- 线性性
  - $E[aX + b] = aE[X] + b$

---

## 第 7 页

**方差及其性质**

- 方差的定义：$\text{var}(X) = E[(X - \mu)^2]$
- 用期望值法则计算：$E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) \, dx$
  - $\text{var}(X) = $（讲义留白）
- 标准差：$\sigma_X = \sqrt{\text{var}(X)}$
- $\text{var}(aX + b) = a^2 \text{var}(X)$
- 一个有用的公式：$\text{var}(X) = E[X^2] - (E[X])^2$

---

## 第 8 页

**连续均匀随机变量；参数 $a, b$**

- $f_X(x) = \dfrac{1}{b-a}$（区间 $[a,b]$）
- $\mathbb{E}[X] = \int_{-\infty}^{\infty} x f_X(x) \, dx$（讲义留白）
- $\mathbb{E}[X^2] = $（讲义留白）
- $\text{var}(X) = $（讲义留白）

（图示：左侧为连续均匀 PDF 矩形图；右侧为离散均匀 PMF 柱状图（取值 $a, a+1, \dots, b$））

- 离散均匀：$\mathbb{E}[X] = \dfrac{a+b}{2}$，$\text{var}(X) = \dfrac{1}{12}(b-a)(b-a+2)$

---

## 第 9 页

**指数随机变量；参数 $\lambda > 0$**

- $f_X(x) = \begin{cases} \lambda e^{-\lambda x}, & x \ge 0 \\ 0, & x < 0 \end{cases}$

（图示：左中为小 $\lambda$ 时 $f_X(x)$ 曲线图（纵轴 $\lambda$、横轴 $x$）；右中为大 $\lambda$ 时 $f_X(x)$ 曲线图；右侧为几何分布 $p_X(k) = (1-p)^{k-1}p$ 的柱状图（横轴 $k = 1, \dots, 9$））

- $E[X] = $（讲义留白）
- $E[X^2] = $（讲义留白）
- $\text{var}(X) = $（讲义留白）

---

## 第 10 页

**累积分布函数（CDF）**

- CDF 定义：$F_X(x) = \text{P}(X \le x)$
- 连续随机变量：
  - $F_X(x) = \text{P}(X \le x) = \int_{-\infty}^x f_X(t) \, dt$

（图示：右上为均匀分布 $f_X(x)$ 矩形图（横轴 $a$、$b$）；右下为待绘 $F_X(x)$ 坐标轴（横轴 $a$、$b$））

---

## 第 11 页

**累积分布函数（CDF）**

- CDF 定义：$F_X(x) = P(X \le x)$
- 离散随机变量：
  - $F_X(x) = P(X \le x) = \sum_{k \le x} p_X(k)$

（图示：右上为 $p_X(k)$ 柱状图（取值 1、3、4，概率 1/4、1/2、1/4；$k=2$ 处概率为 0）；右下为待绘 $F_X(x)$ 坐标轴（横轴 1、2、3、4））

---

## 第 12 页

**CDF 的通用性质**

- $F_X(x) = \text{P}(X \le x)$
- 非递减
- $F_X(x)$ 趋于 1，当 $x \to \infty$
- $F_X(x)$ 趋于 0，当 $x \to -\infty$

---

## 第 13 页

**正态（高斯）随机变量**

- 在概率论理论中很重要
  - 中心极限定理
- 在应用中很普遍
  - 便捷的分析性质
  - 由许多微小独立噪声项构成的噪声模型

---

## 第 14 页

**标准正态（高斯）随机变量**

- 标准正态 $N(0,1)$：$f_X(x) = \dfrac{1}{\sqrt{2\pi}} e^{-x^2/2}$
- $\mathbb{E}[X] = $（讲义留白）
- $\text{var}(X) = 1$

---

## 第 15 页

**一般正态（高斯）随机变量**

- 一般正态 $N(\mu, \sigma^2)$：
  - $f_X(x) = \dfrac{1}{\sigma\sqrt{2\pi}} e^{-(x-\mu)^2/(2\sigma^2)}$
- $E[X] = $（讲义留白）
- $\text{var}(X) = \sigma^2$

（图示：右侧钟形 PDF 曲线图，横轴标注 −1、0、1、2、3）

---

## 第 16 页

**正态随机变量的线性函数**

- 令 $Y = aX + b$，$X \sim N(\mu, \sigma^2)$
- $E[Y] = $（讲义留白）
- $\text{Var}(Y) = $（讲义留白）
- 事实（将在本课程后面证明）：
  - $Y \sim N(a\mu + b, a^2\sigma^2)$
- 特殊情况：$a = 0$？（讲义留白）

---

## 第 17 页

**标准正态表**

- CDF 没有闭合形式
- 但标准正态有表可查

（图示：右侧标准正态分布表，行头为 0.0 至 2.9，列头为 .00 至 .09，单元格为标准正态 CDF 值 Φ(z)，如 Φ(0.0)=.5000、Φ(1.0)=.8413、Φ(2.0)=.9772 等）

---

## 第 18 页

**标准化一个随机变量**

- 令 $X$ 有均值 $\mu$ 和方差 $\sigma^2 > 0$
- 令 $Y = (X - \mu)/\sigma$
- 若 $X$ 也是正态的，则：（讲义留白）

---

## 第 19 页

**计算正态概率**

- 把关注的事件
  - 用标准正态来表示

（图示：右侧标准正态分布表，行头 0.0 至 2.9，列头 .00 至 .09，单元格为标准正态 CDF 值）

---

## 第 20 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
