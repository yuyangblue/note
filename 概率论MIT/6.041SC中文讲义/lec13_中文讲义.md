# LECTURE 13：条件期望与条件方差再探；应用：随机个独立随机变量之和

（本译稿为 MIT 6.041SC Lecture 13 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 13：条件期望与条件方差再探；**
**应用：随机个独立随机变量之和**

- 条件期望的更抽象版本：$E[X \mid Y]$
  - 把它看作随机变量
  - 迭代期望律
- 条件方差的更抽象版本
  - 把它看作随机变量
  - 全方差律
- 随机个独立随机变量之和
  - 均值
  - 方差

---

## 第 2 页

**作为随机变量的条件期望**

- 函数 $h$
  - 例如，$h(x) = x^2$，对所有 $x$
- 随机变量 $X$；$h(X)$ 是什么？
  - $h(X)$ 是这样一个随机变量：若 $X$ 恰好取值 $x$，则它取值 $x^2$，
- $g(y) = E[X \mid Y = y] = \sum_x x \, p_{X \mid Y}(x \mid y)$
  - （连续情形下为积分）
- $g(Y)$：是这样一个随机变量：若 $Y$ 恰好取值 $y$，则它取值 $E[X \mid Y = y]$，
- 定义：$E[X \mid Y] = g(Y)$
- 备注：
  - 它是 $Y$ 的函数
  - 它是一个随机变量
  - 有分布、均值、方差等

---

## 第 3 页

**$E[X \mid Y]$ 的均值：迭代期望律**

- $g(y) = E[X \mid Y = y]$
- $E[E[X \mid Y]]$
- $E[E[X \mid Y]] = E[X]$

---

## 第 4 页

**断棒示例**

- 木棒示例：长度为 $\ell$ 的木棒
  - 在均匀选取的点 $Y$ 处折断
  - 在均匀选取的点 $X$ 处将剩余部分折断

（图示：右侧上方为 $f_Y(y)$ 的矩形密度图，横轴标注 $\ell$、$y$；下方为 $f_{X \mid Y}(x \mid y)$ 的矩形密度图，横轴标注 $y$、$x$）

- $E[X \mid Y = y] = $（讲义留白）
- $E[X \mid Y] = $（讲义留白）
- $E[X] = $（讲义留白）

---

## 第 5 页

**预测修正**

- 假设预测是通过计算期望值作出的，
  - 给定任何可获得的信息
- $X$：二月的销售额
- 年初的预测：（讲义留白）
- 一月底：将获得新信息，$Y$ 的值 $y$
  - 修正后的预测：（讲义留白）
- 迭代期望定律：（讲义留白）
- $E[E[X \mid Y]] = E[X]$

---

## 第 6 页

**作为随机变量的条件方差**

- $\text{var}(X) = E[(X - E[X])^2]$
- $\text{var}(X \mid Y = y) = E[(X - E[X \mid Y = y])^2 \mid Y = y]$
- $\text{var}(X \mid Y)$ 是这样一个随机变量：当 $Y = y$ 时，它取值 $\text{var}(X \mid Y = y)$，
- 示例：$X$ 在 $[0, Y]$ 上均匀
  - $\text{var}(X \mid Y = y) = $（讲义留白）
  - $\text{var}(X \mid Y) = $（讲义留白）
- 全方差律：$\text{var}(X) = E[\text{var}(X \mid Y)] + \text{var}(E[X \mid Y])$

---

## 第 7 页

**全方差律的推导**

- $\text{var}(X) = E[\text{var}(X \mid Y)] + \text{var}(E[X \mid Y])$
- $\text{var}(X) = E[X^2] - (E[X])^2$
- $\text{var}(X \mid Y = y) = $（讲义留白）
- $\text{var}(X \mid Y) = $（讲义留白）
- $E[\text{var}(X \mid Y)] = $（讲义留白）
- $\text{var}(E[X \mid Y]) = $（讲义留白）

---

## 第 8 页

**一个简单的示例**

- $\text{var}(X) = E[\text{var}(X \mid Y)] + \text{var}(E[X \mid Y])$

（图示：左侧为 $f_X(x)$ 分段阶梯图，$Y=1$ 对应区间 $[0,1]$（密度 $1/2$），$Y=2$ 对应区间 $[1,3]$（密度 $1/4$），横轴标注 1、3、$x$）

- $\text{var}(X \mid Y) = \begin{cases} \text{var}(X \mid Y = 1) = & \text{（讲义留白）} \\ \text{var}(X \mid Y = 2) = & \text{（讲义留白）} \end{cases}$
- $E[\text{var}(X \mid Y)] = $（讲义留白）
- $E[X \mid Y] = \begin{cases} E[X \mid Y = 1] = & \text{（讲义留白）} \\ E[X \mid Y = 2] = & \text{（讲义留白）} \end{cases}$
- $E[E[X \mid Y]] = $（讲义留白）
- $\text{var}(E[X \mid Y]) = $（讲义留白）

---

## 第 9 页

**分组均值与方差**

- 班级的两个分组：$y = 1$（10 名学生）；$y = 2$（20 名学生）
- $x_i$：学生 $i$ 的分数
- 实验：随机（均匀地）抽取一名学生
  - 随机变量：$X$ 和 $Y$
- 数据：
  - $y = 1$：$\dfrac{1}{10}\sum_{i=1}^{10} x_i = 90$
  - $y = 2$：$\dfrac{1}{20}\sum_{i=11}^{30} x_i = 60$
- $E[X] = $（讲义留白）
- $E[X \mid Y = 1] = $（讲义留白）
- $E[X \mid Y = 2] = $（讲义留白）
- $E[X \mid Y] = $（讲义留白）
- $E[E[X \mid Y]] = $（讲义留白）

---

## 第 10 页

**分组均值与方差（续）**

- $\mathbb{E}[X \mid Y] = \begin{cases} 90, & \text{w.p. } 1/3 \\ 60, & \text{w.p. } 2/3 \end{cases}$
- $\mathbb{E}[\mathbb{E}[X \mid Y]] = 70 = \mathbb{E}[X]$
- $\text{var}(\mathbb{E}[X \mid Y]) = $（讲义留白）
- 更多数据：
  - $\dfrac{1}{10}\sum_{i=1}^{10}(x_i - 90)^2 = 10$
  - $\dfrac{1}{20}\sum_{i=11}^{30}(x_i - 60)^2 = 20$
- $\text{var}(X \mid Y = 1) = $（讲义留白）
- $\text{var}(X \mid Y = 2) = $（讲义留白）
- $\text{var}(X \mid Y) = $（讲义留白）
- $\mathbb{E}[\text{var}(X \mid Y)] = $（讲义留白）
- $\text{var}(X) = \mathbb{E}[\text{var}(X \mid Y)] + \text{var}(\mathbb{E}[X \mid Y])$
- $\text{var}(X) = $（组内平均变异性）+（组间变异性）

---

## 第 11 页

**随机个独立随机变量之和**

- $N$：访问的商店数量
  - （$N$ 是非负整数随机变量）
- $X_i$：在第 $i$ 家商店花的钱
  - $X_i$ 独立、同分布
  - 与 $N$ 独立
- 令 $Y = X_1 + \dots + X_N$
- $E[Y \mid N = n] = $（讲义留白）
- 全期望定理：
  - $E[Y] = \sum_n p_N(n) E[Y \mid N = n]$
- 迭代期望律：
  - $E[Y] = E[E[Y \mid N]]$
- $E[Y] = E[N] \cdot E[X]$

---

## 第 12 页

**随机个独立随机变量之和的方差**

- $Y = X_1 + \dots + X_N$
- $\text{var}(Y) = \text{E}[\text{var}(Y \mid N)] + \text{var}(\text{E}[Y \mid N])$
- $\text{E}[Y \mid N] = N \text{E}[X]$
- $\text{var}(\text{E}[Y \mid N]) = $（讲义留白）
- $\text{var}(Y \mid N = n) = $（讲义留白）
- $\text{var}(Y \mid N) = $（讲义留白）
- $\text{E}[\text{var}(Y \mid N)] = $（讲义留白）
- $\text{var}(Y) = \text{E}[N] \text{var}(X) + (\text{E}[X])^2 \text{var}(N)$

---

## 第 13 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
