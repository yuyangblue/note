# LECTURE 10：在随机变量上的条件作用；独立性；贝叶斯法则

（本译稿为 MIT 6.041SC Lecture 10 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 10：在随机变量上的条件作用；独立性；贝叶斯法则**

- 在 $Y$ 上对 $X$ 取条件
  - 全概率定理
  - 全期望定理
- 独立性
  - 独立正态变量
- 一个综合性示例
- 贝叶斯法则的四种变体

---

## 第 2 页

**给定另一个随机变量的条件 PDF**

- $p_{X \mid Y}(x \mid y) = \mathrm{P}(X = x \mid Y = y) = \dfrac{p_{X,Y}(x,y)}{p_Y(y)}$，若 $p_Y(y) > 0$
- 定义：$f_{X \mid Y}(x \mid y) = \dfrac{f_{X,Y}(x,y)}{f_Y(y)}$，若 $f_Y(y) > 0$
- $\mathrm{P}(x \le X \le x+\delta \mid A) \approx f_{X \mid A}(x) \cdot \delta$，其中 $\mathrm{P}(A) > 0$
- $\mathrm{P}(x \le X \le x+\delta \mid y \le Y \le y+\epsilon)$（讲义留白）
- 定义：$\mathrm{P}(X \in A \mid Y = y) = \int_A f_{X \mid Y}(x \mid y) \, dx$

（右侧符号速查框：$p_{X,Y}(x,y)$、$f_{X,Y}(x,y)$、$p_{X \mid A}(x)$、$f_{X \mid A}(x)$、$p_{X \mid Y}(x \mid y)$、$f_{X \mid Y}(x \mid y)$）

---

## 第 3 页

**关于条件 PDF 的评论**

- $f_{X \mid Y}(x \mid y) = \dfrac{f_{X,Y}(x,y)}{f_Y(y)}$
  - $f_{X \mid Y}(x \mid y) \ge 0$
- 把 $Y$ 的值视为固定在某个 $y$ 处
  - $f_{X \mid Y}(\cdot \mid y)$ 的形状：联合密度的切片
- $\int_{-\infty}^{\infty} f_{X \mid Y}(x \mid y) \, dx = \dfrac{\int_{-\infty}^{\infty} f_{X,Y}(x,y) \, dx}{f_Y(y)} = 1$
- 乘法法则：
  - $f_{X,Y}(x,y) = f_Y(y) \cdot f_{X \mid Y}(x \mid y)$
  - $= f_X(x) \cdot f_{Y \mid X}(y \mid x)$

（图示：右侧三维联合概率密度曲面图，钟形高斯曲面，坐标轴标注 0、±2、2、4 等刻度）

---

## 第 4 页

**全概率与全期望定理**

- $p_X(x) = \sum_y p_Y(y) p_{X \mid Y}(x \mid y)$
- $\mathbf{E}[X \mid Y = y] = \sum_x x p_{X \mid Y}(x \mid y)$
- $\mathbf{E}[X] = \sum_y p_Y(y) \mathbf{E}[X \mid Y = y]$
- $f_X(x) = \int_{-\infty}^{\infty} f_Y(y) f_{X \mid Y}(x \mid y) \, dy$
- $\mathbf{E}[X \mid Y = y] = \int_{-\infty}^{\infty} x f_{X \mid Y}(x \mid y) \, dx$
- $\mathbf{E}[X] = \int_{-\infty}^{\infty} f_Y(y) \mathbf{E}[X \mid Y = y] \, dy$
- 期望值法则……（讲义留白）

---

## 第 5 页

**独立性**

- $p_{X,Y}(x,y) = p_X(x) p_Y(y)$，对所有 $x, y$
- $f_{X,Y}(x,y) = f_X(x) f_Y(y)$，对所有 $x$ 和 $y$
- $f_{X,Y}(x,y) = f_{X \mid Y}(x \mid y) f_Y(y)$
- 等价于：$f_{X \mid Y}(x \mid y) = f_X(x)$，对所有满足 $f_Y(y) > 0$ 的 $y$ 及所有 $x$
- 若 $X, Y$ 独立：
  - $E[XY] = E[X]E[Y]$
  - $\text{var}(X + Y) = \text{var}(X) + \text{var}(Y)$
  - $g(X)$ 与 $h(Y)$ 也独立：$E[g(X)h(Y)] = E[g(X)] \cdot E[h(Y)]$

---

## 第 6 页

**断棒示例**

- 将长度为 $\ell$ 的木棒折断两次
  - 第一次在 $X$ 处折断：在 $[0, \ell]$ 上均匀
  - 第二次在 $Y$ 处折断：在 $[0, X]$ 上均匀
- $f_{X,Y}(x,y) = f_X(x) f_{Y \mid X}(y \mid x) = $（讲义留白）

（图示：左下为联合分布定义域三角形 $0 \le y \le x \le \ell$；右上为 $f_X(x)$ 图（$[0,\ell]$ 上为常数）；右下为 $f_{Y \mid X}(y \mid x)$ 图（$[0,x]$ 上为常数））

---

## 第 7 页

**断棒示例**

- $f_{X,Y}(x,y) = \dfrac{1}{\ell x}$，$0 \le y \le x \le \ell$
- $f_Y(y) = $（讲义留白）
- $\mathrm{E}[Y] = $（讲义留白）
- 用全期望定理：（讲义留白）

（图示：右侧 $x$–$y$ 坐标系，阴影三角形区域满足 $0 \le y \le x \le \ell$）

---

## 第 8 页

**独立标准正态变量**

- $f_{X,Y}(x,y) = f_X(x) f_Y(y)$
- $= \dfrac{1}{\sqrt{2\pi}}\exp\left\{-\dfrac{x^2}{2}\right\} \cdot \dfrac{1}{\sqrt{2\pi}}\exp\left\{-\dfrac{y^2}{2}\right\}$
- $\mu_X = \mu_Y = 0$；$\sigma_X^2 = \sigma_Y^2 = 1$

（图示：右侧三维联合概率密度曲面图，钟形曲面，纵轴 Probability Density，刻度 0、0.05、0.1、0.15、0.2，坐标轴 $x$、$y$ 刻度 −4 至 4）

---

## 第 9 页

**独立正态变量**

- $f_{X,Y}(x,y) = f_X(x) f_Y(y)$
- $= \dfrac{1}{2\pi\sigma_x\sigma_y}\exp\left\{-\dfrac{(x-\mu_x)^2}{2\sigma_x^2} - \dfrac{(y-\mu_y)^2}{2\sigma_y^2}\right\}$
- $\mu_x = \mu_y = 0$；$\sigma_x^2 = 1$，$\sigma_y^2 = 4$

（图示：左侧为等高线图，标注中心点 $(\mu_x, \mu_y)$、$\sigma_y$、$\sigma_x$、坐标轴 $y$、$x$；右侧为三维联合概率密度曲面图，纵轴 Probability Density，刻度 0、0.02、0.04、0.06、0.08、0.1，坐标轴刻度 −5 至 5）

---

## 第 10 页

**贝叶斯法则——一个带变奏的主题**

- 推断

（图示：$X$ 指向 $Y$ 的箭头示意，$X$ 为未观测值 $x$、先验 $p_X(\cdot)$，$Y$ 为观测值 $y$、模型 $p_{Y \mid X}(\cdot \mid \cdot)$，推断得到 $p_{X \mid Y}(\cdot \mid y)$）

- $p_{X,Y}(x,y) = p_X(x) p_{Y \mid X}(y \mid x)$
  - $= p_Y(y) p_{X \mid Y}(x \mid y)$
- $f_{X,Y}(x,y) = f_X(x) f_{Y \mid X}(y \mid x)$
  - $= f_Y(y) f_{X \mid Y}(x \mid y)$
- $p_{X \mid Y}(x \mid y) = \dfrac{p_X(x) p_{Y \mid X}(y \mid x)}{p_Y(y)}$
- $f_{X \mid Y}(x \mid y) = \dfrac{f_X(x) f_{Y \mid X}(y \mid x)}{f_Y(y)}$
- $p_Y(y) = \sum_{x'} p_X(x') p_{Y \mid X}(y \mid x')$
- $f_Y(y) = \int f_X(x') f_{Y \mid X}(y \mid x') \, dx'$

---

## 第 11 页

**贝叶斯法则——一个离散与一个连续随机变量**

- $K$：离散
- $Y$：连续
- $p_{K \mid Y}(k \mid y) = \dfrac{p_K(k) f_{Y \mid K}(y \mid k)}{f_Y(y)}$
- $f_{Y \mid K}(y \mid k) = \dfrac{f_Y(y) p_{K \mid Y}(k \mid y)}{p_K(k)}$
- $f_Y(y) = \sum_{k'} p_K(k') f_{Y \mid K}(y \mid k')$
- $p_K(k) = \int f_Y(y') p_{K \mid Y}(k \mid y') \, dy'$

---

## 第 12 页

**贝叶斯法则——离散未知量，连续测量值**

- 未知量 $K$：等可能地为 −1 或 +1
- 测量值 $Y$：$Y = K + W$；$W \sim N(0,1)$
- 已知 $Y = y$ 时 $K = 1$ 的概率？
- $p_K(k) = $（讲义留白）
- $f_{Y \mid K}(y \mid k) = $（讲义留白）
- $f_Y(y) = $（讲义留白）
- $p_{K \mid Y}(1 \mid y) = $（讲义留白）
- $p_{K \mid Y}(k \mid y) = \dfrac{p_K(k) f_{Y \mid K}(y \mid k)}{f_Y(y)}$
- $f_Y(y) = \sum_{k'} p_K(k') f_{Y \mid K}(y \mid k')$

---

## 第 13 页

**贝叶斯法则——连续未知量，离散测量值**

- 测量值 $K$：参数为 $Y$ 的伯努利分布
- 未知量 $Y$：在 $[0,1]$ 上均匀
- 已知 $K = 1$ 时 $Y$ 的分布？
- $f_{Y \mid K}(y \mid k) = \dfrac{f_Y(y) p_{K \mid Y}(k \mid y)}{p_K(k)}$
- $p_K(k) = \int f_Y(y') p_{K \mid Y}(k \mid y') \, dy'$
- $f_Y(y) = $（讲义留白）
- $p_{K \mid Y}(1 \mid y) = $（讲义留白）
- $p_K(1) = $（讲义留白）
- $f_{Y \mid K}(y \mid 1) = $（讲义留白）

---

## 第 14 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
