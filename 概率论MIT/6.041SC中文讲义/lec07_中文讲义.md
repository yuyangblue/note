# LECTURE 7：在随机变量上的条件作用；随机变量的独立性

（本译稿为 MIT 6.041SC Lecture 7 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 7：在随机变量上的条件作用；随机变量的独立性**

- 条件 PMF
- 条件期望
- 全期望定理
- 随机变量的独立性
  - 期望性质
  - 方差性质
- 二项分布的方差
- 帽子问题：均值与方差

---

## 第 2 页

**条件 PMF**

- $p_{X \mid A}(x \mid A) = \mathbf{P}(X = x \mid A)$
- $p_{X \mid Y}(x \mid y) = \mathbf{P}(X = x \mid Y = y)$
- $p_{X \mid Y}(x \mid y) = \dfrac{p_{X,Y}(x,y)}{p_Y(y)}$
  - 对满足 $p_Y(y) > 0$ 的 $y$ 定义
  - $\sum_x p_{X \mid Y}(x \mid y) = 1$

（图示：左下为联合 PMF 表格 $p_{X,Y}(x,y)$，行 $y = 1,2,3,4$，列 $x = 1,2,3,4$，单元格为 1/20、2/20、4/20、3/20 等分数值）

- $p_{X,Y}(x,y) = p_Y(y) p_{X \mid Y}(x \mid y)$
- $p_{X,Y}(x,y) = p_X(x) p_{Y \mid X}(y \mid x)$

---

## 第 3 页

**涉及多于两个随机变量的条件 PMF**

- 自解释的符号
  - $p_{X \mid Y,Z}(x \mid y, z)$
  - $p_{X,Y \mid Z}(x, y \mid z)$
- 乘法法则
  - $\mathbf{P}(A \cap B \cap C) = \mathbf{P}(A)\mathbf{P}(B \mid A)\mathbf{P}(C \mid A \cap B)$
  - $p_{X,Y,Z}(x,y,z) = p_X(x) p_{Y \mid X}(y \mid x) p_{Z \mid X,Y}(z \mid x,y)$

---

## 第 4 页

**条件期望**

- $E[X] = \sum_x x p_X(x)$
- $E[X \mid A] = \sum_x x p_{X \mid A}(x)$
- $E[X \mid Y = y] = \sum_x x p_{X \mid Y}(x \mid y)$
- 期望值法则
  - $E[g(X)] = \sum_x g(x) p_X(x)$
  - $E[g(X) \mid A] = \sum_x g(x) p_{X \mid A}(x)$
  - $E[g(X) \mid Y = y] = \sum_x g(x) p_{X \mid Y}(x \mid y)$

---

## 第 5 页

**全概率与全期望定理**

- $A_1, \dots, A_n$：$\Omega$ 的一个划分
- $p_X(x) = P(A_1) p_{X \mid A_1}(x) + \dots + P(A_n) p_{X \mid A_n}(x)$
- $p_X(x) = \sum_y p_Y(y) p_{X \mid Y}(x \mid y)$
- $E[X] = P(A_1) E[X \mid A_1] + \dots + P(A_n) E[X \mid A_n]$
- $E[X] = \sum_y p_Y(y) E[X \mid Y = y]$
- 小字说明：
  - 当 $Y$ 是在无限集上取值的离散随机变量时同样成立，
  - 只要 $E[|X|] < \infty$

---

## 第 6 页

**独立性**

- 两个事件的独立：
  - $P(A \cap B) = P(A) \cdot P(B)$
  - $P(A \mid B) = P(A)$
- 随机变量与事件的独立：
  - $P(X = x \text{ 且 } A) = P(X = x) \cdot P(A)$，对所有 $x$
- 两个随机变量的独立：
  - $P(X = x \text{ 且 } Y = y) = P(X = x) \cdot P(Y = y)$，对所有 $x, y$
  - $p_{X,Y}(x,y) = p_X(x) p_Y(y)$，对所有 $x, y$
- 若 $p_{X,Y,Z}(x,y,z) = p_X(x) p_Y(y) p_Z(z)$ 对所有 $x,y,z$ 成立，则 $X, Y, Z$ 独立

---

## 第 7 页

**示例：独立性与条件独立性**

（图示：左侧联合 PMF 表格，行 $y = 1,2,3,4$，列 $x = 1,2,3,4$，单元格为 1/20、2/20、4/20、3/20 等分数值，部分单元格为空）

- 独立吗？（讲义留白）
- 如果我们以 $X \le 2$ 且 $Y \ge 3$ 为条件呢？（讲义留白）

---

## 第 8 页

**独立性与期望**

- 一般而言：$E[g(X,Y)] \neq g(E[X], E[Y])$
- 例外：$E[aX + b] = aE[X] + b$
  - $E[X + Y + Z] = E[X] + E[Y] + E[Z]$
- 若 $X, Y$ 独立：
  - $E[XY] = E[X]E[Y]$
- $g(X)$ 与 $h(Y)$ 也独立：
  - $E[g(X)h(Y)] = E[g(X)] \cdot E[h(Y)]$

---

## 第 9 页

**独立性与方差**

- 恒成立：$\text{var}(aX) = a^2\text{var}(X)$，$\text{var}(X+a) = \text{var}(X)$
- 一般而言：$\text{var}(X+Y) \neq \text{var}(X) + \text{var}(Y)$
- 若 $X, Y$ 独立：$\text{var}(X+Y) = \text{var}(X) + \text{var}(Y)$
- 示例：
  - 若 $X = Y$：$\text{var}(X+Y) = $（讲义留白）
  - 若 $X = -Y$：$\text{var}(X+Y) = $（讲义留白）
  - 若 $X, Y$ 独立：$\text{var}(X-3Y) = $（讲义留白）

---

## 第 10 页

**二项分布的方差**

- $X$：参数为 $n, p$ 的二项分布
  - $n$ 次独立试验中的成功次数
- $X_i = 1$，若第 $i$ 次试验成功；
  - $X_i = 0$，否则（指示变量）
- $X = X_1 + \dots + X_n$

---

## 第 11 页

**帽子问题**

- $n$ 个人把帽子扔进盒子，然后随机各取一顶
  - 所有排列等可能
  - 等价于一次一顶地抽取
- $X$：拿到自己帽子的人数
  - 求 $E[X]$
- $X_i = \begin{cases} 1, & \text{若 } i \text{ 拿到自己的帽子} \\ 0, & \text{否则}. \end{cases}$
- $X = X_1 + X_2 + \dots + X_n$
- $E[X_i] = $（讲义留白）

---

## 第 12 页

**帽子问题中的方差**

- $X$：拿到自己帽子的人数
  - 求 $\text{var}(X)$
- $X_i = \begin{cases} 1, & \text{若 } i \text{ 拿到自己的帽子} \\ 0, & \text{否则}. \end{cases}$
- $X = X_1 + X_2 + \dots + X_n$
- $\text{var}(X) = E[X^2] - (E[X])^2$
- $X^2 = \sum_i X_i^2 + \sum_{i,j: i \neq j} X_i X_j$
- $E[X_i^2] = $（讲义留白）
- 对 $i \neq j$：$E[X_i X_j] = $（讲义留白）
- $E[X^2] = $（讲义留白）

---

## 第 13 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
