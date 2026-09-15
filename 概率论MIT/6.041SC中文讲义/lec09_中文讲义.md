# LECTURE 9：对事件取条件；多个连续随机变量

（本译稿为 MIT 6.041SC Lecture 9 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 9：对事件取条件；多个连续随机变量**

- 对一个事件取条件的随机变量
  - 条件 PDF
  - 条件期望与期望值法则
  - 指数 PDF：无记忆性
  - 全概率与全期望定理
  - 混合分布
- 联合连续随机变量与联合 PDF
  - 从联合到边缘
  - 均匀联合 PDF 示例
  - 期望值法则与期望的线性
  - 联合 CDF

---

## 第 2 页

**给定一个事件的条件 PDF**

- $p_X(x) = P(X = x)$ ｜ $f_X(x) \cdot \delta \approx P(x \le X \le x + \delta)$
- $p_{X|A}(x) = P(X = x \mid A)$ ｜ $f_{X|A}(x) \cdot \delta \approx P(x \le X \le x + \delta \mid A)$
- $P(X \in B) = \sum_{x \in B} p_X(x)$ ｜ $P(X \in B) = \int_B f_X(x) dx$
- $P(X \in B \mid A) = \sum_{x \in B} p_{X|A}(x)$ ｜ $P(X \in B \mid A) = \int_B f_{X|A}(x) dx$
- $\sum_x p_{X|A}(x) = 1$ ｜ $\int f_{X|A}(x) dx = 1$

---

## 第 3 页

**给定 $X \in A$ 时 $X$ 的条件 PDF**

- $P(x \le X \le x + \delta \mid X \in A) \approx f_{X|X \in A}(x) \cdot \delta$
- $f_{X|X \in A}(x) = \begin{cases} 0, & \text{若 } x \notin A \\ \dfrac{f_X(x)}{P(A)}, & \text{若 } x \in A \end{cases}$

---

## 第 4 页

**给定一个事件时 $X$ 的条件期望**

- $E[X] = \sum_x x p_X(x)$ ｜ $E[X] = \int x f_X(x) dx$
- $E[X \mid A] = \sum_x x p_{X|A}(x)$ ｜ $E[X \mid A] = \int x f_{X|A}(x) dx$
- 期望值法则：
  - $E[g(X)] = \sum_x g(x) p_X(x)$ ｜ $E[g(X)] = \int g(x) f_X(x) dx$
  - $E[g(X) \mid A] = \sum_x g(x) p_{X|A}(x)$ ｜ $E[g(X) \mid A] = \int g(x) f_{X|A}(x) dx$

---

## 第 5 页

**示例**

（图示：上为 $f_X(x)$ 的分段矩形密度图，横轴标注 $a, b, c, d, x$，区间 $[a,b]$ 与 $[c,d]$ 上密度较高、$[b,c]$ 上密度较低；下为空的 $f_{X|A}(x)$ 坐标系，横轴同样标注 $a, b, c, d, x$）

- $A$：$\dfrac{a+b}{2} \le X \le b$
- $E[X \mid A] = $（讲义留白）
- $E[X^2 \mid A] = $（讲义留白）

---

## 第 6 页

**指数 PDF 的无记忆性**

- 你更喜欢用过的还是全新的"指数型"灯泡？概率上完全相同！
- 灯泡寿命 $T$：指数分布 $(\lambda)$
  - $P(T > x) = e^{-\lambda x}$，对 $x \ge 0$
  - 已知 $T > t$
  - 随机变量 $X$：剩余寿命
  - $P(X > x \mid T > t) = e^{-\lambda x}$，对 $x \ge 0$

---

## 第 7 页

**指数 PDF 的无记忆性**

- $f_T(x) = \lambda e^{-\lambda x}$，对 $x \ge 0$
- $P(0 \le T \le \delta)$（讲义留白，与下式对照）
- $P(t \le T \le t + \delta \mid T > t)$（讲义留白，与上式相等）
- 类似于独立抛硬币：
  - 每个 $\delta$ 时间步长，
  - 成功概率 $\approx \lambda \delta$

---

## 第 8 页

**全概率与全期望定理**

（图示：左为两个分支图——上面一组从节点分出 $A_1, A_2, A_3$，各自延伸到 $A_1 \cap B, A_2 \cap B, A_3 \cap B$；下面一组从节点分出标有 $P(A_1), P(A_2), P(A_3)$ 的分支，各自延伸到 $E[X \mid A_1], E[X \mid A_2], E[X \mid A_3]$）

- $P(B) = P(A_1)P(B \mid A_1) + \dots + P(A_n)P(B \mid A_n)$
- $p_X(x) = P(A_1) p_{X|A_1}(x) + \dots + P(A_n) p_{X|A_n}(x)$
- $f_X(x) = P(A_1) f_{X|A_1}(x) + \dots + P(A_n) f_{X|A_n}(x)$
- $E[X] = P(A_1)E[X \mid A_1] + \dots + P(A_n)E[X \mid A_n]$

---

## 第 9 页

**示例**

- Bill 以概率 $1/3$ 在不久后去超市，
  - 时间在从现在起 0 到 2 小时之间均匀分布；
  - 或以概率 $2/3$ 在当天晚些时候，
  - 时间在从现在起 6 到 8 小时之间均匀分布

（图示：$f_X(x)$ 坐标系，横轴标注 $0, 1, 2, 6, 7, 8, x$）

- $f_X(x) = P(A_1) f_{X|A_1}(x) + \dots + P(A_n) f_{X|A_n}(x)$
- $E[X] = P(A_1)E[X \mid A_1] + \dots + P(A_n)E[X \mid A_n]$

---

## 第 10 页

**混合分布**

- $X = \begin{cases} [0,2] \text{ 上的均匀分布}, & \text{以概率 } 1/2 \\ 1, & \text{以概率 } 1/2 \end{cases}$
  - $X$ 是离散的吗？
  - $X$ 是连续的吗？
- $Y$ 离散；$Z$ 连续
- $X = \begin{cases} Y, & \text{以概率 } p \\ Z, & \text{以概率 } 1-p \end{cases}$ ｜ $X$ 是混合的
- $F_X(x) = $（讲义留白）
- $E[X] = $（讲义留白）

---

## 第 11 页

**混合分布**

- $X = \begin{cases} [0,2] \text{ 上的均匀分布}, & \text{以概率 } 1/2 \\ 1, & \text{以概率 } 1/2 \end{cases}$
- $F_X(x) = P(A_1) F_{X|A_1}(x) + P(A_2) F_{X|A_2}(x)$

（图示：三个 CDF 坐标系，横轴均标注 $0, 1, 2, x$——上为 $F_{X|A_1}(x)$，中为 $F_{X|A_2}(x)$，下为 $F_X(x)$）

---

## 第 12 页

**联合连续随机变量与联合 PDF**

- $p_X(x)$ ｜ $f_X(x)$
- $p_{X,Y}(x, y)$ ｜ $f_{X,Y}(x, y)$
- $p_{X,Y}(x, y) = P(X = x \text{ 且 } Y = y) \ge 0$ ｜ $f_{X,Y}(x, y) \ge 0$
- $P((X, Y) \in B) = \sum\sum_{(x,y) \in B} p_{X,Y}(x, y)$ ｜ $P((X, Y) \in B) = \iint_{(x,y) \in B} f_{X,Y}(x, y) dx dy$
- $\sum_x \sum_y p_{X,Y}(x, y) = 1$ ｜ $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x, y) dx dy = 1$
- 定义：若两个随机变量可以由一个联合 PDF 描述，则称它们是联合连续的

---

## 第 13 页

**可视化一个联合 PDF**

（图示：三维网格上的钟形曲面，即联合 PDF 的图像）

- $P((X, Y) \in B) = \iint_{(x,y) \in B} f_{X,Y}(x, y) dx dy$

---

## 第 14 页

**关于联合 PDF**

- $P((X, Y) \in B) = \iint_{(x,y) \in B} f_{X,Y}(x, y) dx dy$
- $P(a \le X \le b, c \le Y \le d) = \int_c^d \int_a^b f_{X,Y}(x, y) dx dy$
- $P(a \le X \le a + \delta, c \le Y \le c + \delta) \approx f_{X,Y}(a, c) \cdot \delta^2$
- $f_{X,Y}(x, y)$：单位面积上的概率
- $\text{area}(B) = 0 \Rightarrow P((X, Y) \in B) = 0$

---

## 第 15 页

**从联合到边缘**

- $p_X(x) = \sum_y p_{X,Y}(x, y)$ ｜ $f_X(x) = \int f_{X,Y}(x, y) dy$
- $p_Y(y) = \sum_x p_{X,Y}(x, y)$ ｜ $f_Y(y) = \int f_{X,Y}(x, y) dx$

---

## 第 16 页

**集合 $S$ 上的均匀联合 PDF**

- $f_{X,Y}(x, y) = \begin{cases} \dfrac{1}{S \text{ 的面积}}, & \text{若 } (x, y) \in S, \\ 0, & \text{否则}. \end{cases}$

（图示：右为平面上的十字形区域 $S$（横轴 $1, 2, 3, x$，纵轴 $1, 2, 3, 4, y$）；左下为边缘密度 $f_Y(y)$ 的阶梯状图（标注 $1/4, 1/2$）；右下为边缘密度 $f_X(x)$ 的阶梯状图（标注 $3/4, 1/4$））

- $f_X(x) = \int f_{X,Y}(x, y) dy$
- $f_Y(y) = \int f_{X,Y}(x, y) dx$

---

## 第 17 页

**多于两个随机变量**

- $p_{X,Y,Z}(x, y, z)$ ｜ $f_{X,Y,Z}(x, y, z)$
- $\sum_x \sum_y \sum_z p_{X,Y,Z}(x, y, z) = 1$
- $p_X(x) = \sum_y \sum_z p_{X,Y,Z}(x, y, z)$
- $p_{X,Y}(x, y) = \sum_z p_{X,Y,Z}(x, y, z)$

---

## 第 18 页

**多个随机变量的函数**

- $Z = g(X, Y)$
- 期望值法则：$E[g(X, Y)] = \sum_x \sum_y g(x, y) p_{X,Y}(x, y)$ ｜ $E[g(X, Y)] = \int\int g(x, y) f_{X,Y}(x, y) dx dy$
- 期望的线性
  - $E[aX + b] = aE[X] + b$
  - $E[X + Y] = E[X] + E[Y]$
  - $E[X_1 + \dots + X_n] = E[X_1] + \dots + E[X_n]$

---

## 第 19 页

**联合 CDF**

- $F_X(x) = P(X \le x) = \int_{-\infty}^x f_X(t) dt$ ｜ $f_X(x) = \dfrac{dF_X}{dx}(x)$
- $F_{X,Y}(x, y) = P(X \le x, Y \le y)$
- $f_{X,Y}(x, y) = \dfrac{\partial^2 F_{X,Y}}{\partial x \partial y}(x, y)$

---

## 第 20 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
