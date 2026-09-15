# LECTURE 12：独立随机变量之和；协方差与相关系数

（本译稿为 MIT 6.041SC Lecture 12 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 12：独立随机变量之和；**
**协方差与相关系数**

- $X + Y$ 的 PMF/PDF（$X$ 与 $Y$ 独立）
  - 离散情形
  - 连续情形
  - 计算方法
  - 独立正态变量之和
- 协方差与相关系数
  - 定义
  - 数学性质
  - 解读

---

## 第 2 页

**$X+Y$ 的分布：离散情形**

- $Z = X + Y$；$X, Y$ 独立，离散
  - 已知 PMF
- $p_Z(3) = $（讲义留白）

（图示：$x$–$y$ 坐标系，直线 $x + y = 3$ 上的点 $(0,3)$、$(1,2)$、$(2,1)$、$(3,0)$）

- $p_Z(z) = \sum_x p_X(x) p_Y(z - x)$

---

## 第 3 页

**离散卷积的计算方法**

（图示：左侧四幅图——$p_X$（取值 1、4，概率 1/3、2/3）；$p_Y$（取值 −1、1、2，概率 2/6、1/6、3/6）；$Y$ 的 PMF 水平翻转（取值 −2、−1、1，概率 3/6、1/6、2/6）；翻转后右移 3 个单位（取值 1、2、4，概率 3/6、1/6、2/6））

- $p_Z(z) = \sum_x p_X(x) p_Y(z - x)$
- 求 $p_Z(3)$：
  - 将 $Y$ 的 PMF 水平翻转
  - 把它放在 $X$ 的 PMF 下方
  - 将翻转后的 PMF 右移 3
  - 交叉相乘并相加
  - 对其他 $z$ 值重复

---

## 第 4 页

**$X+Y$ 的分布：连续情形**

- $Z = X + Y$；$X, Y$ 独立，连续
  - 已知 PDF
- 以 $X = x$ 为条件：（讲义留白）

（图示：$x$–$y$ 坐标系，直线 $x + y = 3$ 上的点 $(0,3)$、$(1,2)$、$(2,1)$、$(3,0)$）

- $Z$ 与 $X$ 的联合 PDF：（讲义留白）
- 从联合到边缘：$f_Z(z) = \int_{-\infty}^{\infty} f_{X,Z}(x,z) \, dx$
- 与离散情形相同的计算方法（翻转、平移等）
- $p_Z(z) = \sum_x p_X(x) p_Y(z - x)$
- $f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z - x) \, dx$

---

## 第 5 页

**独立正态随机变量之和**

- $X \sim N(\mu_x, \sigma_x^2)$，$Y \sim N(\mu_y, \sigma_y^2)$，独立
  - $Z = X + Y$
- $f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z - x) \, dx$
- $f_X(x) = \dfrac{1}{\sqrt{2\pi}\sigma_x} e^{-(x-\mu_x)^2/2\sigma_x^2}$
- $f_Y(y) = \dfrac{1}{\sqrt{2\pi}\sigma_y} e^{-(y-\mu_y)^2/2\sigma_y^2}$
- $f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z - x) \, dx$
- $= \int_{-\infty}^{\infty} \dfrac{1}{\sqrt{2\pi}\sigma_x}\exp\left\{-\dfrac{(x-\mu_x)^2}{2\sigma_x^2}\right\}\dfrac{1}{\sqrt{2\pi}\sigma_y}\exp\left\{-\dfrac{(z-x-\mu_y)^2}{2\sigma_y^2}\right\} dx$
- （代数运算）
- $= \dfrac{1}{\sqrt{2\pi(\sigma_x^2+\sigma_y^2)}}\exp\left\{-\dfrac{(z-\mu_x-\mu_y)^2}{2(\sigma_x^2+\sigma_y^2)}\right\}$
- 有限个独立正态变量之和是正态的

---

## 第 6 页

**协方差**

- 零均值、离散的 $X$ 和 $Y$
  - 若独立：$E[XY] = $（讲义留白）

（图示：左侧为 $E[XY]$ 示意散点图与四点坐标示意图 $(0,1)$、$(-1,0)$、$(1,0)$、$(0,-1)$）

- 一般情形的定义：
  - $\text{cov}(X,Y) = E[(X - E[X]) \cdot (Y - E[Y])]$
- 独立 $\Rightarrow$ $\text{cov}(X,Y) = 0$
  - （逆命题不成立）

---

## 第 7 页

**协方差性质**

- $\text{cov}(X,X) = $（讲义留白）
- $\text{cov}(aX + b, Y) = $（讲义留白）
- $\text{cov}(X, Y + Z) = $（讲义留白）
- $\text{cov}(X,Y) = E[(X - E[X]) \cdot (Y - E[Y])]$
- $\text{cov}(X,Y) = E[XY] - E[X]E[Y]$

---

## 第 8 页

**随机变量之和的方差**

- $\text{var}(X_1 + X_2) = $（讲义留白）

---

## 第 9 页

**随机变量之和的方差**

- $\text{var}(X_1 + X_2) = \text{var}(X_1) + \text{var}(X_2) + 2\text{cov}(X_1,X_2)$
- $\text{var}(X_1 + \dots + X_n) = $（讲义留白）
- $\text{var}(X_1 + \dots + X_n) = \sum_{i=1}^{n} \text{var}(X_i) + \sum_{\{(i,j): i \neq j\}} \text{cov}(X_i,X_j)$

---

## 第 10 页

**相关系数**

- 协方差的无量纲版本：
  - $-1 \le \rho \le 1$
- $\rho(X,Y) = E\left[\dfrac{X - E[X]}{\sigma_X} \cdot \dfrac{Y - E[Y]}{\sigma_Y}\right] = \dfrac{\text{cov}(X,Y)}{\sigma_X\sigma_Y}$
- 衡量 $X$ 与 $Y$ 之间"关联"程度的度量
- 独立 $\Rightarrow$ $\rho = 0$，"不相关"
  - （逆命题不成立）
- $\rho(X,X) = $（讲义留白）
- $|\rho| = 1 \Leftrightarrow (X - E[X]) = c(Y - E[Y])$（线性相关）
- $\text{cov}(aX + b, Y) = a \cdot \text{cov}(X,Y) \Rightarrow \rho(aX + b, Y) = $（讲义留白）

---

## 第 11 页

**相关系数关键性质的证明**

- $\rho(X,Y) = E\left[\left(\frac{X - E[X]}{\sigma_X}\right) \cdot \left(\frac{Y - E[Y]}{\sigma_Y}\right)\right]$
- $-1 \le \rho \le 1$
- 为简化起见，假设零均值、单位方差，于是 $\rho(X,Y) = E[XY]$
- $E[(X - \rho Y)^2] = $（讲义留白）
- 若 $|\rho| = 1$，则（讲义留白）

---

## 第 12 页

**解读相关系数**

- $\rho(X,Y) = \text{cov}(X,Y)/\sigma_X\sigma_Y$
- 关联并不意味着因果或影响
  - $X$：数学能力
  - $Y$：音乐能力
- 相关性往往反映潜在的、共同的、隐藏的因素
  - 假设 $Z, V, W$ 独立
  - $X = Z + V$
  - $Y = Z + W$
  - 为简化起见，假设 $Z, V, W$ 零均值、单位方差
  - （讲义留白）

---

## 第 13 页

**相关性很重要……**

- 一家房地产投资公司在 10 个州各投资 1000 万美元。
- 在每个州 $i$，其投资回报是随机变量 $X_i$，
  - 均值 1，标准差 1.3（单位：百万）。
- $\mathrm{var}(X_1 + \dots + X_{10}) = \sum_{i=1}^{10} \mathrm{var}(X_i) + \sum_{\{(i,j): i \neq j\}} \mathrm{cov}(X_i,X_j)$
- 若 $X_i$ 不相关，则：
  - $\mathrm{var}(X_1 + \dots + X_{10}) = $（讲义留白）
  - $\sigma(X_1 + \dots + X_{10}) = $（讲义留白）
- 若对 $i \neq j$，$\rho(X_i,X_j) = 0.9$：
  - $\sigma(X_1 + \dots + X_{10}) = $（讲义留白）

---

## 第 14 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
