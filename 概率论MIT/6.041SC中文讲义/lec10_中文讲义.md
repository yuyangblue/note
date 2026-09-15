# LECTURE 10：对随机变量取条件；独立性；贝叶斯法则

（本译稿为 MIT 6.041SC Lecture 10 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 10：对随机变量取条件；独立性；贝叶斯法则**

- 对 $Y$ 取条件的 $X$
  - 全概率定理
  - 全期望定理
- 独立性
  - 独立正态
- 一个综合示例
- 贝叶斯法则的四种变体

---

## 第 2 页

**给定另一个随机变量的条件 PDF**

- $p_{X|Y}(x \mid y) = P(X = x \mid Y = y) = \dfrac{p_{X,Y}(x, y)}{p_Y(y)}$，若 $p_Y(y) > 0$
- $p_{X,Y}(x, y)$ ｜ $f_{X,Y}(x, y)$
- $p_{X|A}(x)$ ｜ $f_{X|A}(x)$
- $p_{X|Y}(x \mid y)$ ｜ $f_{X|Y}(x \mid y)$
- 定义：$f_{X|Y}(x \mid y) = \dfrac{f_{X,Y}(x, y)}{f_Y(y)}$，若 $f_Y(y) > 0$
- $P(x \le X \le x + \delta \mid A) \approx f_{X|A}(x) \cdot \delta$，其中 $P(A) > 0$
- $P(x \le X \le x + \delta \mid y \le Y \le y + \epsilon)$（讲义留白，与上式对照）
- 定义：$P(X \in A \mid Y = y) = \int_A f_{X|Y}(x \mid y) dx$

---

## 第 3 页

**关于条件 PDF 的评论**

- $f_{X|Y}(x \mid y) = \dfrac{f_{X,Y}(x, y)}{f_Y(y)}$ ｜ $f_{X|Y}(x \mid y) \ge 0$
- 把 $Y$ 的值看作固定在某个 $y$
  - $f_{X|Y}(\cdot \mid y)$ 的形状：联合分布的切片
- $\int_{-\infty}^{\infty} f_{X|Y}(x \mid y) dx = \dfrac{\int_{-\infty}^{\infty} f_{X,Y}(x, y) dx}{f_Y(y)} = 1$
- 乘法法则：
  - $f_{X,Y}(x, y) = f_Y(y) \cdot f_{X|Y}(x \mid y)$
  - $= f_X(x) \cdot f_{Y|X}(y \mid x)$

（图示：三维钟形曲面，即联合 PDF 的图像，坐标轴标注 $-2, 0, 2, 4$）

---

## 第 4 页

**全概率与全期望定理**

- $p_X(x) = \sum_y p_Y(y) p_{X|Y}(x \mid y)$ ｜ $f_X(x) = \int_{-\infty}^{\infty} f_Y(y) f_{X|Y}(x \mid y) dy$
- $E[X \mid Y = y] = \sum_x x p_{X|Y}(x \mid y)$ ｜ $E[X \mid Y = y] = \int_{-\infty}^{\infty} x f_{X|Y}(x \mid y) dx$
- $E[X] = \sum_y p_Y(y) E[X \mid Y = y]$ ｜ $E[X] = \int_{-\infty}^{\infty} f_Y(y) E[X \mid Y = y] dy$
- 期望值法则……（讲义留白）

---

## 第 5 页

**独立性**

- $p_{X,Y}(x, y) = p_X(x) p_Y(y)$，对所有 $x, y$
- $f_{X,Y}(x, y) = f_X(x) f_Y(y)$，对所有 $x$ 和 $y$
- $f_{X,Y}(x, y) = f_{X|Y}(x \mid y) f_Y(y)$
  - 等价于：$f_{X|Y}(x \mid y) = f_X(x)$，对所有满足 $f_Y(y) > 0$ 的 $y$ 和所有 $x$
- 若 $X, Y$ 独立：
  - $E[XY] = E[X]E[Y]$
  - $\text{var}(X + Y) = \text{var}(X) + \text{var}(Y)$
- $g(X)$ 和 $h(Y)$ 也独立：
  - $E[g(X)h(Y)] = E[g(X)] \cdot E[h(Y)]$

---

## 第 6 页

**断棒示例**

- 把一根长度为 $\ell$ 的棍子折断两次
  - 第一次折断点 $X$：在 $[0, \ell]$ 上均匀
  - 第二次折断点 $Y$：在 $[0, X]$ 上均匀
- $f_{X,Y}(x, y) = f_X(x) f_{Y|X}(y \mid x) = $（讲义留白）

（图示：左为定义域坐标系，横轴、纵轴均为 $0$ 到 $\ell$，灰色三角形区域即 $X, Y$ 的取值定义域；右上为 $f_X(x)$ 图，在 $[0, \ell]$ 上为水平直线；右下为 $f_{Y|X}(y \mid x)$ 图，在 $[0, x]$ 上为水平直线）

---

## 第 7 页

**断棒示例**

- $f_{X,Y}(x, y) = \dfrac{1}{\ell x}$，$0 \le y \le x \le \ell$

（图示：平面坐标系，横轴、纵轴均为 $\ell$，直角三角形灰色阴影区域即定义域 $0 \le y \le x \le \ell$）

- $f_Y(y) = $（讲义留白）
- $E[Y] = $（讲义留白）
- 用全期望定理：

---

## 第 8 页

**独立标准正态**

- $f_{X,Y}(x, y) = f_X(x) f_Y(y) = \dfrac{1}{\sqrt{2\pi}} \exp\left\{-\dfrac{x^2}{2}\right\} \cdot \dfrac{1}{\sqrt{2\pi}} \exp\left\{-\dfrac{y^2}{2}\right\}$
- $\mu_X = \mu_Y = 0$；$\sigma_X^2 = \sigma_Y^2 = 1$

（图示：三维钟形曲面，纵轴为概率密度（0–0.2），横轴为 $x, y$（$-4$ 到 $4$），中心高、四周低）

---

## 第 9 页

**独立正态**

- $f_{X,Y}(x, y) = f_X(x) f_Y(y)$
  - $= \dfrac{1}{2\pi\sigma_x\sigma_y} \exp\left\{-\dfrac{(x-\mu_x)^2}{2\sigma_x^2} - \dfrac{(y-\mu_y)^2}{2\sigma_y^2}\right\}$

（图示：左为二维平面上的等高线椭圆，中心 $(\mu_x, \mu_y)$，长短半轴对应 $\sigma_y$ 与 $\sigma_x$；右为三维钟形曲面，$\mu_X = \mu_Y = 0$，$\sigma_X^2 = 1$，$\sigma_Y^2 = 4$，纵轴为概率密度（0–0.1），横轴为 $x, y$（$-5$ 到 $5$））

---

## 第 10 页

**贝叶斯法则——一个有变奏的主题**

（图示：推断方向示意图——未观测值 $x$、先验 $p_X(\cdot)$ 从 $X$ 指向 $Y$ 的观测值 $y$、模型 $p_{Y|X}(\cdot \mid \cdot)$，再经推断得到后验 $p_{X|Y}(\cdot \mid y)$）

- 离散情形：
  - $p_{X,Y}(x, y) = p_X(x) p_{Y|X}(y \mid x) = p_Y(y) p_{X|Y}(x \mid y)$
  - $p_{X|Y}(x \mid y) = \dfrac{p_X(x) p_{Y|X}(y \mid x)}{p_Y(y)}$
  - $p_Y(y) = \sum_{x'} p_X(x') p_{Y|X}(y \mid x')$
- 连续情形：
  - $f_{X,Y}(x, y) = f_X(x) f_{Y|X}(y \mid x) = f_Y(y) f_{X|Y}(x \mid y)$
  - $f_{X|Y}(x \mid y) = \dfrac{f_X(x) f_{Y|X}(y \mid x)}{f_Y(y)}$
  - $f_Y(y) = \int f_X(x') f_{Y|X}(y \mid x') dx'$

---

## 第 11 页

**贝叶斯法则——一个离散与一个连续随机变量**

- $K$：离散 ｜ $Y$：连续
- $p_{K|Y}(k \mid y) = \dfrac{p_K(k) f_{Y|K}(y \mid k)}{f_Y(y)}$ ｜ $f_{Y|K}(y \mid k) = \dfrac{f_Y(y) p_{K|Y}(k \mid y)}{p_K(k)}$
- $f_Y(y) = \sum_{k'} p_K(k') f_{Y|K}(y \mid k')$ ｜ $p_K(k) = \int f_Y(y') p_{K|Y}(k \mid y') dy'$

---

## 第 12 页

**贝叶斯法则——离散未知量、连续测量**

- 未知量 $K$：等可能地取 $-1$ 或 $+1$
- 测量 $Y$：$Y = K + W$；$W \sim N(0, 1)$
- 已知 $Y = y$ 时，$K = 1$ 的概率？
- $p_K(k) = $（讲义留白）
- $f_{Y|K}(y \mid k) = $（讲义留白）
- $f_Y(y) = $（讲义留白）
- $p_{K|Y}(1 \mid y) = $（讲义留白）
- $p_{K|Y}(k \mid y) = \dfrac{p_K(k) f_{Y|K}(y \mid k)}{f_Y(y)}$
- $f_Y(y) = \sum_{k'} p_K(k') f_{Y|K}(y \mid k')$

---

## 第 13 页

**贝叶斯法则——连续未知量、离散测量**

- 测量 $K$：参数为 $Y$ 的伯努利分布
- 未知量 $Y$：$[0, 1]$ 上的均匀分布
- 已知 $K = 1$ 时 $Y$ 的分布？
- $f_Y(y) = $（讲义留白）
- $p_{K|Y}(1 \mid y) = $（讲义留白）
- $p_K(1) = $（讲义留白）
- $f_{Y|K}(y \mid 1) = $（讲义留白）
- $f_{Y|K}(y \mid k) = \dfrac{f_Y(y) p_{K|Y}(k \mid y)}{p_K(k)}$
- $p_K(k) = \int f_Y(y') p_{K|Y}(k \mid y') dy'$

---

## 第 14 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
