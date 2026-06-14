---
AIGC:
    Label: "1"
    ContentProducer: 001191110102MACQD9K64018705
    ProduceID: 7625646103391912243-data_volume/files/所有对话/主对话/Lecture_Notes习题解答.md
    ReservedCode1: ""
    ContentPropagator: 001191110102MACQD9K64028705
    PropagateID: 1470511051441884#1781425430005
    ReservedCode2: ""
---
# Lecture Notes 习题解答

---

## 第1题

**题目：** 设 $x = \begin{pmatrix} 1 \\ -2 \\ 2 \end{pmatrix}$，计算 $\|x\|_1,\ \|x\|_2,\ \|x\|_\infty$，并验证 $\|x\|_\infty \leq \|x\|_2 \leq \|x\|_1$。

**解答：**

**1-范数：** 各元素绝对值之和
$$\|x\|_1 = |1| + |-2| + |2| = 1 + 2 + 2 = \boldsymbol{5}$$

**2-范数（欧氏范数）：** 各元素平方和开根号
$$\|x\|_2 = \sqrt{1^2 + (-2)^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = \boldsymbol{3}$$

**无穷范数：** 元素绝对值的最大值
$$\|x\|_\infty = \max\{|1|, |-2|, |2|\} = \boldsymbol{2}$$

**验证不等式：**
$$\|x\|_\infty = 2 \leq \|x\|_2 = 3 \leq \|x\|_1 = 5$$
不等式成立。✓

---

## 第2题

**题目：** 设 $A = \begin{pmatrix} -2 & 1 & 0 \\ 3 & -1 & -1 \\ 2 & 4 & 1 \end{pmatrix}$，计算 $\|A\|_1,\ \|A\|_\infty,\ \|A\|_F$。

**解答：**

**1-范数（列和范数）：** 各列元素绝对值之和的最大值
- 第1列：$|-2| + |3| + |2| = 2 + 3 + 2 = 7$
- 第2列：$|1| + |-1| + |4| = 1 + 1 + 4 = 6$
- 第3列：$|0| + |-1| + |1| = 0 + 1 + 1 = 2$

$$\|A\|_1 = \max\{7, 6, 2\} = \boldsymbol{7}$$

**无穷范数（行和范数）：** 各行元素绝对值之和的最大值
- 第1行：$|-2| + |1| + |0| = 2 + 1 + 0 = 3$
- 第2行：$|3| + |-1| + |-1| = 3 + 1 + 1 = 5$
- 第3行：$|2| + |4| + |1| = 2 + 4 + 1 = 7$

$$\|A\|_\infty = \max\{3, 5, 7\} = \boldsymbol{7}$$

**Frobenius范数：** 所有元素平方和开根号
$$\|A\|_F = \sqrt{(-2)^2 + 1^2 + 0^2 + 3^2 + (-1)^2 + (-1)^2 + 2^2 + 4^2 + 1^2}$$
$$= \sqrt{4 + 1 + 0 + 9 + 1 + 1 + 4 + 16 + 1} = \sqrt{37} \approx \boldsymbol{6.08}$$

---

## 第3题

**题目：** 设 $A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix}$，计算 $A^T A$，求 $A$ 的全部奇异值，并求 $\|A\|_2$。

**解答：**

**第一步：计算 $A^T A$**
$$A^T A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$

**第二步：求特征值**
特征方程：$|A^T A - \lambda I| = 0$
$$\begin{vmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{vmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda-1)(\lambda-3) = 0$$

特征值：$\lambda_1 = 1,\ \lambda_2 = 3$

**第三步：求奇异值**
奇异值是 $A^T A$ 特征值的平方根：
$$\sigma_1 = \sqrt{\lambda_1} = \sqrt{1} = 1, \quad \sigma_2 = \sqrt{\lambda_2} = \sqrt{3} \approx 1.732$$

**全部奇异值：** $\boldsymbol{1, \sqrt{3}}$

**第四步：求 2-范数**
矩阵的2-范数等于最大奇异值：
$$\|A\|_2 = \sigma_{\text{max}} = \boldsymbol{\sqrt{3} \approx 1.732}$$

---

## 第4题

**题目：** 对于矩阵 $A \in \mathbb{R}^{m \times n}$，证明 $\|A\|_2 \leq \sqrt{\|A\|_1 \|A\|_\infty}$。

**证明：**

矩阵的2-范数等于 $A^T A$ 的最大特征值的平方根，即：
$$\|A\|_2^2 = \lambda_{\text{max}}(A^T A)$$

根据谱半径不超过任何一种矩阵范数的性质：
$$\lambda_{\text{max}}(A^T A) \leq \|A^T A\|_1$$

而矩阵1-范数满足次乘性：
$$\|A^T A\|_1 \leq \|A^T\|_1 \|A\|_1$$

又因为 $\|A^T\|_1 = \|A\|_\infty$（转置后列和变行和），所以：
$$\|A^T A\|_1 \leq \|A\|_\infty \|A\|_1$$

综上：
$$\|A\|_2^2 \leq \|A\|_1 \|A\|_\infty$$

两边开平方得：
$$\|A\|_2 \leq \sqrt{\|A\|_1 \|A\|_\infty}$$

证毕。✓

---

## 第5题

**题目：** 设 $u = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix},\ v = \begin{pmatrix} 2 \\ -1 \end{pmatrix},\ A = uv^T$。计算矩阵 $A$，并求 $\operatorname{rank}(A),\ \|A\|_F,\ \|A\|_2$。最后验证 $\|uv^T\|_2 = \|u\|_2 \|v\|_2$。

**解答：**

**第一步：计算矩阵 A**
$$A = uv^T = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} \begin{pmatrix} 2 & -1 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ 4 & -2 \\ 4 & -2 \end{pmatrix}$$

**第二步：求秩**
秩1矩阵（所有行都成比例）：
$$\operatorname{rank}(A) = \boldsymbol{1}$$

**第三步：求 Frobenius 范数**
$$\|A\|_F = \sqrt{2^2 + (-1)^2 + 4^2 + (-2)^2 + 4^2 + (-2)^2} = \sqrt{4 + 1 + 16 + 4 + 16 + 4} = \sqrt{45} = \boldsymbol{3\sqrt{5} \approx 6.71}$$

**第四步：求 2-范数**
方法一：秩1矩阵的2-范数等于 $\|u\|_2 \|v\|_2$

$$\|u\|_2 = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{9} = 3$$
$$\|v\|_2 = \sqrt{2^2 + (-1)^2} = \sqrt{5}$$
$$\|A\|_2 = \|u\|_2 \|v\|_2 = 3\sqrt{5} \approx \boldsymbol{6.71}$$

方法二：验证
$$A^T A = vu^T uv^T = (u^T u) vv^T = \|u\|_2^2 vv^T = 9 \cdot \begin{pmatrix} 4 & -2 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} 36 & -18 \\ -18 & 9 \end{pmatrix}$$
其特征值为 45 和 0，最大奇异值为 $\sqrt{45} = 3\sqrt{5}$。✓

**验证：**
$$\|uv^T\|_2 = 3\sqrt{5} = \|u\|_2 \|v\|_2$$
等式成立。

---

## 第6题

**题目：** 证明 Frobenius 范数不是由欧氏向量范数诱导出的矩阵范数。

**证明：**

**反证法：** 假设 Frobenius 范数是由某种向量范数诱导的，即：
$$\|A\|_F = \max_{x \neq 0} \frac{\|Ax\|}{\|x\|}$$

对于诱导范数，单位矩阵的范数一定等于 1：
$$\|I\| = \max_{x \neq 0} \frac{\|Ix\|}{\|x\|} = \max_{x \neq 0} \frac{\|x\|}{\|x\|} = 1$$

但是 Frobenius 范数下，n 阶单位矩阵的范数为：
$$\|I\|_F = \sqrt{\sum_{i=1}^n \sum_{j=1}^n |\delta_{ij}|^2} = \sqrt{n}$$

当 $n > 1$ 时，$\|I\|_F = \sqrt{n} > 1$，这与诱导范数满足 $\|I\| = 1$ 矛盾。

因此，Frobenius 范数**不是**由向量范数诱导出的矩阵范数。

证毕。✓

---

## 第7题

**题目：** 设 $a = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix},\ b = \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix},\ L = \operatorname{span}\{a\}$。求 $b$ 在直线 $L$ 上的正交投影 $\operatorname{proj}_L(b)$。

**解答：**

向量 $b$ 在向量 $a$ 方向上的正交投影公式为：
$$\operatorname{proj}_L(b) = \frac{a^T b}{a^T a} \cdot a$$

计算内积：
$$a^T b = 1 \times 3 + 2 \times 1 + 2 \times 1 = 3 + 2 + 2 = 7$$
$$a^T a = 1^2 + 2^2 + 2^2 = 1 + 4 + 4 = 9$$

代入公式：
$$\operatorname{proj}_L(b) = \frac{7}{9} \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} = \boldsymbol{\begin{pmatrix} \dfrac{7}{9} \\ \dfrac{14}{9} \\ \dfrac{14}{9} \end{pmatrix} \approx \begin{pmatrix} 0.778 \\ 1.556 \\ 1.556 \end{pmatrix}}$$

---

## 第8题

**题目：** 设 $a = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$，定义 $P = \frac{aa^T}{a^T a}$。计算 $P$，并验证 $P^2 = P,\ P^T = P$。再对 $b = \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix}$ 计算 $Pb$，并与上一题的结果比较。

**解答：**

**第一步：计算 P**
$$aa^T = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} \begin{pmatrix} 1 & 2 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 2 \\ 2 & 4 & 4 \\ 2 & 4 & 4 \end{pmatrix}$$
$$a^T a = 9$$
$$P = \frac{aa^T}{a^T a} = \boldsymbol{\frac{1}{9} \begin{pmatrix} 1 & 2 & 2 \\ 2 & 4 & 4 \\ 2 & 4 & 4 \end{pmatrix}}$$

**第二步：验证 $P^T = P$**
$aa^T$ 是对称矩阵，除以标量 $a^T a$ 后仍是对称矩阵，故 $P^T = P$。✓

**第三步：验证 $P^2 = P$**
$$P^2 = \left(\frac{aa^T}{a^T a}\right)^2 = \frac{aa^T aa^T}{(a^T a)^2} = \frac{a(a^T a)a^T}{(a^T a)^2} = \frac{(a^T a) \cdot aa^T}{(a^T a)^2} = \frac{aa^T}{a^T a} = P$$
幂等性成立。✓

**第四步：计算 Pb**
$$Pb = \frac{1}{9} \begin{pmatrix} 1 & 2 & 2 \\ 2 & 4 & 4 \\ 2 & 4 & 4 \end{pmatrix} \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix} = \frac{1}{9} \begin{pmatrix} 3+2+2 \\ 6+4+4 \\ 6+4+4 \end{pmatrix} = \frac{1}{9} \begin{pmatrix} 7 \\ 14 \\ 14 \end{pmatrix} = \begin{pmatrix} \dfrac{7}{9} \\ \dfrac{14}{9} \\ \dfrac{14}{9} \end{pmatrix}$$

**比较：** 结果与第7题的正交投影完全一致。这说明 $P$ 就是到直线 $L = \operatorname{span}\{a\}$ 的正交投影矩阵。

---

## 第9题

**题目：** 设 $b = \begin{pmatrix} 2 \\ 1 \\ 2 \end{pmatrix},\ A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix}$，计算 $P = A(A^T A)^{-1} A^T$。$P$ 是否是投影算子？定义 $\hat{b} = Pb,\ r = b - \hat{b}$，证明 $A^T r = 0$。

**解答：**

**第一步：计算 $A^T A$ 及其逆**
$$A^T A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$
$$(A^T A)^{-1} = \frac{1}{2 \times 2 - 1 \times 1} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$$

**第二步：计算投影矩阵 P**
$$P = A(A^T A)^{-1} A^T$$
$$= \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix} \cdot \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$
$$= \frac{1}{3} \begin{pmatrix} 2 & -1 \\ 1 & 1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$
$$= \frac{1}{3} \begin{pmatrix} 2 & 1 & -1 \\ 1 & 2 & 1 \\ -1 & 1 & 2 \end{pmatrix}$$

$$P = \boldsymbol{\frac{1}{3} \begin{pmatrix} 2 & 1 & -1 \\ 1 & 2 & 1 \\ -1 & 1 & 2 \end{pmatrix}}$$

**第三步：P 是否是投影算子？**

验证对称性：
$$P^T = \left(\frac{1}{3} \begin{pmatrix} 2 & 1 & -1 \\ 1 & 2 & 1 \\ -1 & 1 & 2 \end{pmatrix}\right)^T = \frac{1}{3} \begin{pmatrix} 2 & 1 & -1 \\ 1 & 2 & 1 \\ -1 & 1 & 2 \end{pmatrix} = P$$
对称 ✓

验证幂等性：
$$P^2 = [A(A^TA)^{-1}A^T][A(A^TA)^{-1}A^T] = A(A^TA)^{-1}(A^TA)(A^TA)^{-1}A^T = A(A^TA)^{-1}A^T = P$$
幂等 ✓

**结论：P 是正交投影算子**（投影到 A 的列空间）。

**第四步：证明 $A^T r = 0$**
$$r = b - \hat{b} = b - Pb$$
$$A^T r = A^T(b - Pb) = A^T b - A^T P b$$
$$A^T P = A^T A(A^T A)^{-1} A^T = I \cdot A^T = A^T$$
因此：
$$A^T r = A^T b - A^T b = 0$$

证毕。✓

**数值验证：**
$$\hat{b} = Pb = \frac{1}{3} \begin{pmatrix} 2 & 1 & -1 \\ 1 & 2 & 1 \\ -1 & 1 & 2 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}$$
$$r = b - \hat{b} = \begin{pmatrix} 2 \\ 1 \\ 2 \end{pmatrix} - \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}$$
$$A^T r = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
验证成立。✓

---

## 第10题

**题目：** 设 $A = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}$，写出 $A$ 的一个奇异值分解 $A = U \Sigma V^T$，其中 $U$ 与 $V$ 均为正交矩阵。

**解答：**

**第一步：求 $A^T A$ 的特征值和特征向量**
$$A^T A = \begin{pmatrix} 3 & 2 \\ 2 & 3 \\ 2 & -2 \end{pmatrix} \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix} = \begin{pmatrix} 13 & 12 & 2 \\ 12 & 13 & -2 \\ 2 & -2 & 8 \end{pmatrix}$$

特征方程：
$$|A^T A - \lambda I| = 0$$
解得特征值：$\lambda_1 = 25,\ \lambda_2 = 9,\ \lambda_3 = 0$

对应的单位特征向量：
- $\lambda_1 = 25$: $v_1 = \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{pmatrix}$
- $\lambda_2 = 9$: $v_2 = \begin{pmatrix} 1/3 \\ -1/3 \\ 2/3 \end{pmatrix} \times \sqrt{2}$？等等，让我重新算

让我们用标准方法计算：
对于 $\lambda = 25$，$A^TA - 25I = \begin{pmatrix} -12 & 12 & 2 \\ 12 & -12 & -2 \\ 2 & -2 & -17 \end{pmatrix}$
特征向量: $\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$ 的方向，单位化得 $v_1 = \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{pmatrix}$

对于 $\lambda = 9$，$A^TA - 9I = \begin{pmatrix} 4 & 12 & 2 \\ 12 & 4 & -2 \\ 2 & -2 & -1 \end{pmatrix}$
从第3行: $2x - 2y - z = 0 \Rightarrow z = 2x - 2y$
从第1行: $4x + 12y + 2z = 0$，代入z: $4x + 12y + 4x - 4y = 8x + 8y = 0 \Rightarrow x = -y$
取 $x = 1, y = -1$, 则 $z = 2 - (-2) = 4$？不对，$z = 2(1) - 2(-1) = 4$
特征向量: $\begin{pmatrix} 1 \\ -1 \\ 4 \end{pmatrix}$？但平方和是 $1+1+16=18$，且需要验证。

实际上，更简单的方法：
注意到 $A = \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix}$，可以观察到：
- 列1 + 列2 = (5, 5)^T = 5(1, 1)^T
- 列1 - 列2 + 2列3 = ...

让我直接给出SVD结果：

奇异值：$\sigma_1 = 5,\ \sigma_2 = 3$

**左奇异向量（U的列）：**
$$u_1 = \frac{1}{\sigma_1} Av_1 = \frac{1}{5} \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix} \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{pmatrix} = \frac{1}{5} \begin{pmatrix} 5/\sqrt{2} \\ 5/\sqrt{2} \end{pmatrix} = \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{pmatrix}$$

$$u_2 = \frac{1}{\sigma_2} Av_2$$
取 $v_2 = \begin{pmatrix} 1/3 \\ -1/3 \\ 2/3 \end{pmatrix} \times \sqrt{2}$？不对。

**正确的SVD：**

通过计算，$A$ 的奇异值分解为：
$$U = \begin{pmatrix} 1/\sqrt{2} & 1/\sqrt{2} \\ 1/\sqrt{2} & -1/\sqrt{2} \end{pmatrix}, \quad \Sigma = \begin{pmatrix} 5 & 0 & 0 \\ 0 & 3 & 0 \end{pmatrix}$$
$$V^T = \begin{pmatrix} 1/\sqrt{2} & 1/\sqrt{2} & 0 \\ 1/(3\sqrt{2}) & -1/(3\sqrt{2}) & 4/(3\sqrt{2}) \end{pmatrix} \text{？不对}$$

**重新整理：**

实际上更简洁的答案：
- $v_1 = \frac{1}{\sqrt{2}}(1, 1, 0)^T$ 对应 $\sigma_1 = 5$
- $v_2 = \frac{1}{3\sqrt{2}}(1, -1, 4)^T$？不对。

让我验证一下：
如果 $v_1 = (1/\sqrt{2}, 1/\sqrt{2}, 0)^T$，则：
$Av_1 = (3/\sqrt{2} + 2/\sqrt{2}, 2/\sqrt{2} + 3/\sqrt{2})^T = (5/\sqrt{2}, 5/\sqrt{2})^T$
$\|Av_1\| = 5 = \sigma_1$ ✓

对于第二个奇异值 $\sigma_2 = 3$：
我们需要找与 $v_1$ 正交的单位向量 $v_2$，使得 $\|Av_2\| = 3$。

设 $v_2 = (a, b, c)^T$，满足 $a + b = 0$（与v1正交）且 $a^2 + b^2 + c^2 = 1$。
令 $a = t, b = -t$，则 $2t^2 + c^2 = 1$。

$Av_2 = (3t - 2t + 2c, 2t - 3t - 2c)^T = (t + 2c, -t - 2c)^T$
$\|Av_2\|^2 = (t+2c)^2 + (-t-2c)^2 = 2(t+2c)^2 = 9$

所以 $t + 2c = \pm 3/\sqrt{2}$

结合 $2t^2 + c^2 = 1$，设 $t = 3/\sqrt{2} - 2c$，代入：
$2(9/2 - 6c/\sqrt{2} + 4c^2) + c^2 = 1$
$9 - 6\sqrt{2}c + 8c^2 + c^2 = 1$
$9c^2 - 6\sqrt{2}c + 8 = 0$
判别式 $= 72 - 288 < 0$，无解。

说明 $\sigma_2 = 3$ 不对？让我重新计算 $A^TA$ 的特征值。

$A^TA = \begin{pmatrix} 13 & 12 & 2 \\ 12 & 13 & -2 \\ 2 & -2 & 8 \end{pmatrix}$

迹 = 13 + 13 + 8 = 34
行列式呢？或者直接计算特征多项式。

实际上，注意到这是一个对称矩阵，可以尝试找特征值：
- 观察行和：13+12+2 = 27，12+13+(-2) = 23，2+(-2)+8 = 8，不相等。

换一种方式：
可以验证 25 是特征值吗？
$A^TA - 25I = \begin{pmatrix} -12 & 12 & 2 \\ 12 & -12 & -2 \\ 2 & -2 & -17 \end{pmatrix}$
行1 = -行2，行3 = 行1的... 2/-12 = -1/6, -2/12 = -1/6, -17/2 ≠ -1/6
所以秩为2，25是特征值。

另一个特征值可以是多少呢？
迹 = 34，所以另外两个特征值之和 = 34 - 25 = 9。

试试 9：
$A^TA - 9I = \begin{pmatrix} 4 & 12 & 2 \\ 12 & 4 & -2 \\ 2 & -2 & -1 \end{pmatrix}$
行3 × 6 = (12, -12, -6) ≠ 行1或行2
行2 - 行1 = (8, -8, -4) = 4×(2, -2, -1) = 4×行3
所以秩也是2，9是特征值。

第三个特征值 = 34 - 25 - 9 = 0。✓

好的，那 $\sigma_1 = 5, \sigma_2 = 3$ 是对的。

对于 $\lambda = 9$：
$A^TA - 9I = \begin{pmatrix} 4 & 12 & 2 \\ 12 & 4 & -2 \\ 2 & -2 & -1 \end{pmatrix}$
从行3: $2x_1 - 2x_2 - x_3 = 0 \Rightarrow x_3 = 2x_1 - 2x_2$
从行1: $4x_1 + 12x_2 + 2x_3 = 0$，代入 $x_3$:
$4x_1 + 12x_2 + 4x_1 - 4x_2 = 8x_1 + 8x_2 = 0 \Rightarrow x_1 = -x_2$

令 $x_1 = 1$，则 $x_2 = -1$，$x_3 = 2(1) - 2(-1) = 4$
特征向量：$(1, -1, 4)^T$
单位化：$\|(1, -1, 4)\| = \sqrt{1 + 1 + 16} = \sqrt{18} = 3\sqrt{2}$
$$v_2 = \frac{1}{3\sqrt{2}} \begin{pmatrix} 1 \\ -1 \\ 4 \end{pmatrix}$$

验证：$v_1^T v_2 = \frac{1}{\sqrt{2}} \cdot \frac{1}{3\sqrt{2}} + \frac{1}{\sqrt{2}} \cdot \frac{-1}{3\sqrt{2}} + 0 \cdot \frac{4}{3\sqrt{2}} = \frac{1}{6} - \frac{1}{6} + 0 = 0$ ✓

$v_3$ 与 $v_1, v_2$ 都正交，可以取：
$v_3 = \frac{1}{3} \begin{pmatrix} 2 \\ -2 \\ -1 \end{pmatrix}$ （验证：与v1点积 = 2/3√2 - 2/3√2 = 0，与v2点积 = 2/9√2 + 2/9√2 - 4/9√2 = 0 ✓）

**左奇异向量：**
$$u_1 = \frac{1}{\sigma_1} Av_1 = \frac{1}{5} \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix} \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} = \frac{1}{5\sqrt{2}} \begin{pmatrix} 5 \\ 5 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

$$u_2 = \frac{1}{\sigma_2} Av_2 = \frac{1}{3} \begin{pmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{pmatrix} \frac{1}{3\sqrt{2}} \begin{pmatrix} 1 \\ -1 \\ 4 \end{pmatrix} = \frac{1}{9\sqrt{2}} \begin{pmatrix} 3 - 2 + 8 \\ 2 - 3 - 8 \end{pmatrix} = \frac{1}{9\sqrt{2}} \begin{pmatrix} 9 \\ -9 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix}$$

**最终的奇异值分解：**
$$A = U \Sigma V^T$$
其中：
$$U = \begin{pmatrix} \dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{2}} \\ \dfrac{1}{\sqrt{2}} & -\dfrac{1}{\sqrt{2}} \end{pmatrix}, \quad \Sigma = \begin{pmatrix} 5 & 0 & 0 \\ 0 & 3 & 0 \end{pmatrix}$$
$$V = \begin{pmatrix} \dfrac{1}{\sqrt{2}} & \dfrac{1}{3\sqrt{2}} & \dfrac{2}{3} \\ \dfrac{1}{\sqrt{2}} & -\dfrac{1}{3\sqrt{2}} & -\dfrac{2}{3} \\ 0 & \dfrac{4}{3\sqrt{2}} & -\dfrac{1}{3} \end{pmatrix}$$

验证：$U \Sigma V^T = A$ ✓

---


## 第11题

**题目：** 设矩阵 $A$ 的奇异值为 $5, 3, 0, 0$。回答下列问题：
- $\operatorname{rank}(A) = ?$
- $\|A\|_2 = ?$
- $\|A\|_F = ?$
- 如果 $A$ 是 $4 \times 4$ 方阵，判断 $A$ 是否可逆，并说明理由。

**解答：**

**(1) 秩**
矩阵的秩等于非零奇异值的个数：
$$\operatorname{rank}(A) = \boldsymbol{2}$$

**(2) 2-范数（谱范数）**
矩阵的2-范数等于最大奇异值：
$$\|A\|_2 = \sigma_{\text{max}} = \boldsymbol{5}$$

**(3) Frobenius 范数**
Frobenius范数等于所有奇异值的平方和开根号：
$$\|A\|_F = \sqrt{\sigma_1^2 + \sigma_2^2 + \sigma_3^2 + \sigma_4^2} = \sqrt{5^2 + 3^2 + 0 + 0} = \sqrt{25 + 9} = \sqrt{34} \approx \boldsymbol{5.83}$$

**(4) 可逆性判断**

$A$ **不可逆**。

理由：$4 \times 4$ 方阵可逆当且仅当其秩为 4（满秩）。但 $\operatorname{rank}(A) = 2 < 4$，故不可逆。也可以从行列式角度：行列式等于所有奇异值的乘积（考虑符号），这里有零奇异值，故 $\det(A) = 0$，不可逆。

---

## 第12题

**题目：** 设
$$A = U \begin{pmatrix} 4 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix} V^T,$$
其中 $U, V \in \mathbb{R}^{3 \times 3}$ 均为正交矩阵。计算 $\|A\|_2,\ \|A\|_F,\ \operatorname{rank}(A),\ \kappa_2(A)$。

**解答：**

奇异值为 $\sigma_1 = 4, \sigma_2 = 2, \sigma_3 = 1$。

**(1) 2-范数**
$$\|A\|_2 = \sigma_{\text{max}} = \boldsymbol{4}$$

**(2) Frobenius 范数**
$$\|A\|_F = \sqrt{\sigma_1^2 + \sigma_2^2 + \sigma_3^2} = \sqrt{16 + 4 + 1} = \sqrt{21} \approx \boldsymbol{4.58}$$

**(3) 秩**
$$\operatorname{rank}(A) = \boldsymbol{3}$$（所有奇异值都非零）

**(4) 2-条件数**
条件数等于最大奇异值与最小奇异值之比：
$$\kappa_2(A) = \frac{\sigma_{\text{max}}}{\sigma_{\text{min}}} = \frac{4}{1} = \boldsymbol{4}$$

---

## 第13题

**题目：** 设矩阵 $A$ 的奇异值分解可写成
$$A = 5u_1 v_1^T + 3u_2 v_2^T + u_3 v_3^T,$$
其中 $\{u_1, u_2, u_3\}$ 与 $\{v_1, v_2, v_3\}$ 分别是标准正交向量组。写出最佳秩一逼近 $A_1$ 与最佳秩二逼近 $A_2$，并计算 $\|A - A_1\|_2,\ \|A - A_2\|_2$。

**解答：**

根据 Eckart-Young 定理，矩阵的最佳秩 $k$ 逼近（在谱范数和 Frobenius 范数意义下）就是取其前 $k$ 个最大奇异值对应的外积之和。

**最佳秩一逼近：**
$$A_1 = \boldsymbol{5u_1 v_1^T}$$

**最佳秩二逼近：**
$$A_2 = \boldsymbol{5u_1 v_1^T + 3u_2 v_2^T}$$

**谱范数误差：**

$$A - A_1 = 3u_2 v_2^T + u_3 v_3^T$$
其奇异值为 $3, 1, 0$，因此：
$$\|A - A_1\|_2 = \sigma_{\text{max}}(A - A_1) = \boldsymbol{3}$$

$$A - A_2 = u_3 v_3^T$$
其奇异值为 $1, 0, 0$，因此：
$$\|A - A_2\|_2 = \boldsymbol{1}$$

**一般结论：** $\|A - A_k\|_2 = \sigma_{k+1}$

---

## 第14题

**题目：** 沿用上一题中的矩阵 $A$。计算 $\|A - A_1\|_F,\ \|A - A_2\|_F$。并说明为什么同一个低秩逼近在谱范数与 Frobenius 范数下的误差表达式不同。

**解答：**

**Frobenius 范数误差：**

$$\|A - A_1\|_F = \sqrt{\sigma_2^2 + \sigma_3^2} = \sqrt{3^2 + 1^2} = \sqrt{10} \approx \boldsymbol{3.16}$$

$$\|A - A_2\|_F = \sqrt{\sigma_3^2} = \boldsymbol{1}$$

**为什么误差表达式不同？**

谱范数和 Frobenius 范数是两种不同的矩阵范数，衡量的角度不同：

- **谱范数** $\|A\|_2 = \sigma_{\text{max}}$ 只关心**最大的奇异值**，反映矩阵作为线性算子的最大放大倍数。因此截断后的误差就是下一个奇异值 $\sigma_{k+1}$。

- **Frobenius 范数** $\|A\|_F = \sqrt{\sum \sigma_i^2}$ 是**所有奇异值的平方和开根号**，把每个奇异值的贡献都考虑进去了。因此截断后的误差是剩余所有奇异值的平方和开根号，即 $\sqrt{\sum_{i=k+1}^r \sigma_i^2}$。

简单说：谱范数只看"最大的那个误差"，Frobenius 范数看"所有误差的平方和"。

---

## 第15题

**题目：** 设
$$A = \sum_{i=1}^r \sigma_i u_i v_i^T, \quad \sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0,$$
其中 $\{u_i\}_{i=1}^r$ 与 $\{v_i\}_{i=1}^r$ 分别是标准正交向量组。令
$$A_k = \sum_{i=1}^k \sigma_i u_i v_i^T, \quad 1 \leq k < r.$$
证明 $\|A - A_k\|_2 = \sigma_{k+1}$。
进一步证明对任意满足 $\operatorname{rank}(B) \leq k$ 的矩阵 $B$，都有 $\|A - B\|_2 \geq \sigma_{k+1}$。
从而证明 $\min_{\operatorname{rank}(B) \leq k} \|A - B\|_2 = \sigma_{k+1}$。

**证明：**

**第一部分：证明 $\|A - A_k\|_2 = \sigma_{k+1}$**

$$A - A_k = \sum_{i=k+1}^r \sigma_i u_i v_i^T$$

这是 $A - A_k$ 的一个奇异值分解，其非零奇异值为 $\sigma_{k+1}, \sigma_{k+2}, \dots, \sigma_r$。

矩阵的2-范数等于最大奇异值，因此：
$$\|A - A_k\|_2 = \max_{k+1 \leq i \leq r} \sigma_i = \sigma_{k+1}$$

（因为奇异值按降序排列，所以 $\sigma_{k+1}$ 是最大的）

**第二部分：证明对任意秩不超过 $k$ 的矩阵 $B$，有 $\|A - B\|_2 \geq \sigma_{k+1}$**

设 $B$ 是任意满足 $\operatorname{rank}(B) \leq k$ 的 $m \times n$ 矩阵。

考虑 $A$ 的前 $k+1$ 个右奇异向量 $v_1, v_2, \dots, v_{k+1}$ 张成的子空间 $V_{k+1} = \operatorname{span}\{v_1, \dots, v_{k+1}\}$，其维数为 $k+1$。

另一方面，$\ker(B)$（$B$ 的零空间）的维数满足：
$$\dim \ker(B) = n - \operatorname{rank}(B) \geq n - k$$

根据维数公式：
$$\dim(V_{k+1} \cap \ker(B)) \geq \dim V_{k+1} + \dim \ker(B) - n \geq (k+1) + (n-k) - n = 1$$

因此存在非零向量 $x \in V_{k+1} \cap \ker(B)$，即 $Bx = 0$。

设 $x = \sum_{i=1}^{k+1} c_i v_i$，其中 $\sum c_i^2 = \|x\|^2 > 0$。

则：
$$(A - B)x = Ax - Bx = Ax = \sum_{i=1}^{k+1} c_i \sigma_i u_i$$

因此：
$$\|(A - B)x\|_2^2 = \sum_{i=1}^{k+1} c_i^2 \sigma_i^2 \geq \sigma_{k+1}^2 \sum_{i=1}^{k+1} c_i^2 = \sigma_{k+1}^2 \|x\|^2$$

即：
$$\frac{\|(A - B)x\|_2}{\|x\|_2} \geq \sigma_{k+1}$$

而矩阵2-范数是所有单位向量像的范数的上确界，因此：
$$\|A - B\|_2 = \max_{\|x\|=1} \|(A-B)x\| \geq \sigma_{k+1}$$

**第三部分：结论**

综合两部分：
- 存在秩 $k$ 矩阵 $A_k$ 使得 $\|A - A_k\|_2 = \sigma_{k+1}$
- 对任意秩不超过 $k$ 的矩阵 $B$，都有 $\|A - B\|_2 \geq \sigma_{k+1}$

因此：
$$\min_{\operatorname{rank}(B) \leq k} \|A - B\|_2 = \sigma_{k+1}$$

这就是著名的 **Eckart-Young 定理**。

证毕。✓

---

## 第16题

**题目：** 设 $A = U_r \Sigma_r V_r^T$ 是 $A$ 的紧奇异值分解，其中 $U_r \in \mathbb{R}^{m \times r},\ U_r^T U_r = I_r$。证明 $P_U = U_r U_r^T$ 满足 $P_U^2 = P_U,\ P_U^T = P_U$。并证明 $P_U$ 是到 $\operatorname{Col}(A)$ 上的正交投影矩阵。

**证明：**

**第一步：证明对称性 $P_U^T = P_U$**
$$P_U^T = (U_r U_r^T)^T = (U_r^T)^T U_r^T = U_r U_r^T = P_U$$
对称成立。✓

**第二步：证明幂等性 $P_U^2 = P_U$**
$$P_U^2 = (U_r U_r^T)(U_r U_r^T) = U_r (U_r^T U_r) U_r^T = U_r I_r U_r^T = U_r U_r^T = P_U$$
（利用了 $U_r^T U_r = I_r$）

幂等成立。✓

**第三步：证明 $P_U$ 是到 $\operatorname{Col}(A)$ 上的正交投影**

首先，$\operatorname{Col}(A) = \operatorname{Col}(U_r)$，因为：
- $A = U_r \Sigma_r V_r^T$，所以 $A$ 的列都是 $U_r$ 列的线性组合，即 $\operatorname{Col}(A) \subseteq \operatorname{Col}(U_r)$
- 又 $\Sigma_r$ 可逆（对角元都是正奇异值），$V_r^T$ 行满秩，故 $\operatorname{rank}(A) = r = \operatorname{rank}(U_r)$，因此 $\operatorname{Col}(A) = \operatorname{Col}(U_r)$

现在验证正交投影的性质：

1. **对任意 $x \in \operatorname{Col}(U_r)$，有 $P_U x = x$：**
   设 $x = U_r c$，则 $P_U x = U_r U_r^T U_r c = U_r I_r c = U_r c = x$ ✓

2. **对任意 $x \in \operatorname{Col}(U_r)^\perp$，有 $P_U x = 0$：**
   若 $x$ 与 $U_r$ 的所有列正交，则 $U_r^T x = 0$，故 $P_U x = U_r U_r^T x = 0$ ✓

3. **$P_U$ 对称且幂等**（已证）

因此，$P_U = U_r U_r^T$ 是到 $\operatorname{Col}(U_r) = \operatorname{Col}(A)$ 上的正交投影矩阵。

证毕。✓

---


## 第17题

**题目：** 设
$$u_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad u_2 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}, \quad U = \begin{pmatrix} 1/\sqrt{2} & 0 \\ 1/\sqrt{2} & 0 \\ 0 & 1 \end{pmatrix}.$$
计算 $P = UU^T$。再对 $b = \begin{pmatrix} 2 \\ 0 \\ 3 \end{pmatrix}$ 计算 $b$ 在 $\operatorname{span}\{u_1, u_2\}$ 上的正交投影 $Pb$，并计算投影残差 $r = b - Pb$。验证 $U^T r = 0$。

**解答：**

**第一步：计算 $P = UU^T$**

$$P = UU^T = \begin{pmatrix} 1/\sqrt{2} & 0 \\ 1/\sqrt{2} & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1/\sqrt{2} & 1/\sqrt{2} & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1/2 & 1/2 & 0 \\ 1/2 & 1/2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

$$P = \boldsymbol{\begin{pmatrix} 1/2 & 1/2 & 0 \\ 1/2 & 1/2 & 0 \\ 0 & 0 & 1 \end{pmatrix}}$$

**第二步：计算正交投影 $Pb$**

$$Pb = \begin{pmatrix} 1/2 & 1/2 & 0 \\ 1/2 & 1/2 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 2 \\ 0 \\ 3 \end{pmatrix} = \begin{pmatrix} 1 + 0 + 0 \\ 1 + 0 + 0 \\ 0 + 0 + 3 \end{pmatrix} = \boldsymbol{\begin{pmatrix} 1 \\ 1 \\ 3 \end{pmatrix}}$$

**第三步：计算残差 $r$**

$$r = b - Pb = \begin{pmatrix} 2 \\ 0 \\ 3 \end{pmatrix} - \begin{pmatrix} 1 \\ 1 \\ 3 \end{pmatrix} = \boldsymbol{\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}}$$

**第四步：验证 $U^T r = 0$**

$$U^T r = \begin{pmatrix} 1/\sqrt{2} & 1/\sqrt{2} & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1/\sqrt{2} - 1/\sqrt{2} + 0 \\ 0 + 0 + 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

验证成立。✓

---

## 第18题

**题目：** 设
$$A = \begin{pmatrix} 2 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}.$$
求 Moore–Penrose 伪逆 $A^\dagger$。然后计算 $AA^\dagger$, $A^\dagger A$。说明 $AA^\dagger$ 与 $A^\dagger A$ 分别是到哪些子空间上的正交投影。

**解答：**

**第一步：求伪逆 $A^\dagger$**

对于对角矩阵，伪逆就是对非零对角元取倒数，零保持不变，然后转置（如果不是方阵的话）。

$$A^\dagger = \begin{pmatrix} 1/2 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$$

验证四个Moore-Penrose条件：
1. $AA^\dagger A = A$ ✓
2. $A^\dagger A A^\dagger = A^\dagger$ ✓
3. $(AA^\dagger)^T = AA^\dagger$ ✓
4. $(A^\dagger A)^T = A^\dagger A$ ✓

**第二步：计算 $AA^\dagger$**

$$AA^\dagger = \begin{pmatrix} 2 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 1/2 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} = \boldsymbol{\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}}$$

这是到 $\operatorname{Col}(A)$（即 $\mathbb{R}^3$ 中的 $xy$ 平面）上的正交投影。

**第三步：计算 $A^\dagger A$**

$$A^\dagger A = \begin{pmatrix} 1/2 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix} = \boldsymbol{\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}} = I_2$$

这是到 $\operatorname{Row}(A) = \mathbb{R}^2$（整个定义域空间）上的正交投影（即恒等映射）。

**总结：**
- $AA^\dagger$ 是到 $A$ 的**列空间** $\operatorname{Col}(A)$ 上的正交投影
- $A^\dagger A$ 是到 $A$ 的**行空间** $\operatorname{Row}(A)$ 上的正交投影

---

## 第19题

**题目：** 设 $A, E \in \mathbb{R}^{m \times n}$，并且 $\sigma_{\text{max}}(A) = 10, \sigma_{\text{min}}(A) = 2, \|E\|_2 \leq 0.3$。利用奇异值扰动估计给出 $\sigma_{\text{max}}(A + E)$ 的上界，以及 $\sigma_{\text{min}}(A + E)$ 的下界。

**解答：**

**Weyl 奇异值扰动定理：** 对任意矩阵 $A, E \in \mathbb{R}^{m \times n}$，设它们的奇异值分别为 $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_p$ 和 $\tau_1 \geq \tau_2 \geq \cdots \geq \tau_p$，则对每个 $i$，有
$$|\sigma_i(A + E) - \sigma_i(A)| \leq \|E\|_2 = \tau_1$$

**最大奇异值的上界：**
$$\sigma_{\text{max}}(A + E) \leq \sigma_{\text{max}}(A) + \|E\|_2 \leq 10 + 0.3 = \boldsymbol{10.3}$$

**最小奇异值的下界：**
$$\sigma_{\text{min}}(A + E) \geq \sigma_{\text{min}}(A) - \|E\|_2 \geq 2 - 0.3 = \boldsymbol{1.7}$$

---

## 第20题

**题目：** 设
$$A = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}.$$
计算 $\|A^{-1}\|_2, \|A\|_2, \kappa_2(A)$。
再对
$$B = \begin{pmatrix} 100 & 0 \\ 0 & 1 \end{pmatrix}$$
计算 $\|B\|_2, \|B^{-1}\|_2, \kappa_2(B)$。
比较 $A$ 与 $B$ 的条件数，并说明哪一个线性系统更可能对扰动敏感。

**解答：**

**对于矩阵 A：**
- 奇异值：$3, 1$
- $\|A\|_2 = \sigma_{\text{max}}(A) = \boldsymbol{3}$
- $\|A^{-1}\|_2 = \frac{1}{\sigma_{\text{min}}(A)} = \boldsymbol{\frac{1}{3} \approx 0.333}$
- $\kappa_2(A) = \|A\|_2 \|A^{-1}\|_2 = \frac{\sigma_{\text{max}}}{\sigma_{\text{min}}} = \frac{3}{1} = \boldsymbol{3}$

**对于矩阵 B：**
- 奇异值：$100, 1$
- $\|B\|_2 = \sigma_{\text{max}}(B) = \boldsymbol{100}$
- $\|B^{-1}\|_2 = \frac{1}{\sigma_{\text{min}}(B)} = \boldsymbol{1}$
- $\kappa_2(B) = \frac{\sigma_{\text{max}}}{\sigma_{\text{min}}} = \frac{100}{1} = \boldsymbol{100}$

**比较：**
$\kappa_2(B) = 100 > \kappa_2(A) = 3$，**B 的条件数大得多**。

条件数越大，线性系统 $Bx = b$ 对扰动越敏感。因此，**以 B 为系数矩阵的线性系统更容易受到扰动的影响**，即右端项或系数矩阵的微小变化可能导致解的较大误差。

---

## 第21题

**题目：** 给定数据点 $(0, 1), (1, 2), (2, 2), (3, 4)$。用直线 $y = c_0 + c_1 t$ 进行最小二乘拟合。写出设计矩阵 $A$、未知向量 $c$ 和观测向量 $b$，使问题写成 $\min_{c \in \mathbb{R}^2} \|Ac - b\|_2$。然后写出正规方程 $A^T Ac = A^T b$，并求出 $c_0, c_1$ 以及拟合直线。

**解答：**

**第一步：建立最小二乘问题**

设计矩阵：
$$A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{pmatrix}$$
（第一列全为1，对应截距项；第二列为各点的t坐标）

未知向量：
$$c = \begin{pmatrix} c_0 \\ c_1 \end{pmatrix}$$

观测向量：
$$b = \begin{pmatrix} 1 \\ 2 \\ 2 \\ 4 \end{pmatrix}$$

最小二乘问题：
$$\min_{c \in \mathbb{R}^2} \|Ac - b\|_2$$

**第二步：写出正规方程**

计算 $A^T A$：
$$A^T A = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{pmatrix} = \begin{pmatrix} 4 & 6 \\ 6 & 14 \end{pmatrix}$$

计算 $A^T b$：
$$A^T b = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 2 \\ 4 \end{pmatrix} = \begin{pmatrix} 9 \\ 18 \end{pmatrix}$$

正规方程：
$$\begin{pmatrix} 4 & 6 \\ 6 & 14 \end{pmatrix} \begin{pmatrix} c_0 \\ c_1 \end{pmatrix} = \begin{pmatrix} 9 \\ 18 \end{pmatrix}$$

**第三步：求解正规方程**

$$(A^T A)^{-1} = \frac{1}{4 \times 14 - 6 \times 6} \begin{pmatrix} 14 & -6 \\ -6 & 4 \end{pmatrix} = \frac{1}{20} \begin{pmatrix} 14 & -6 \\ -6 & 4 \end{pmatrix} = \begin{pmatrix} 0.7 & -0.3 \\ -0.3 & 0.2 \end{pmatrix}$$

$$c = (A^T A)^{-1} A^T b = \frac{1}{20} \begin{pmatrix} 14 & -6 \\ -6 & 4 \end{pmatrix} \begin{pmatrix} 9 \\ 18 \end{pmatrix} = \frac{1}{20} \begin{pmatrix} 126 - 108 \\ -54 + 72 \end{pmatrix} = \frac{1}{20} \begin{pmatrix} 18 \\ 18 \end{pmatrix} = \begin{pmatrix} 0.9 \\ 0.9 \end{pmatrix}$$

因此：
- $c_0 = \boldsymbol{0.9}$
- $c_1 = \boldsymbol{0.9}$

**拟合直线：**
$$\boldsymbol{y = 0.9 + 0.9t}$$

---

## 第22题

**题目：** 给定数据点 $(-1, 2), (0, 1), (1, 2), (2, 5)$。用二次函数 $y = c_0 + c_1 t + c_2 t^2$ 进行最小二乘拟合。写出对应的矩阵最小二乘问题 $\min_{c \in \mathbb{R}^3} \|Ac - b\|_2$。然后计算 $A^T A$ 与 $A^T b$，并写出正规方程 $A^T Ac = A^T b$。本题不要求求出 $c$ 的显式数值。

**解答：**

**第一步：建立最小二乘问题**

设计矩阵（三列分别对应 $1, t, t^2$）：
$$A = \begin{pmatrix} 1 & -1 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & 4 \end{pmatrix}$$

未知向量：
$$c = \begin{pmatrix} c_0 \\ c_1 \\ c_2 \end{pmatrix}$$

观测向量：
$$b = \begin{pmatrix} 2 \\ 1 \\ 2 \\ 5 \end{pmatrix}$$

最小二乘问题：
$$\min_{c \in \mathbb{R}^3} \|Ac - b\|_2$$

**第二步：计算 $A^T A$**

$$A^T = \begin{pmatrix} 1 & 1 & 1 & 1 \\ -1 & 0 & 1 & 2 \\ 1 & 0 & 1 & 4 \end{pmatrix}$$

$$A^T A = \begin{pmatrix} 1 & 1 & 1 & 1 \\ -1 & 0 & 1 & 2 \\ 1 & 0 & 1 & 4 \end{pmatrix} \begin{pmatrix} 1 & -1 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & 4 \end{pmatrix} = \begin{pmatrix} 4 & 2 & 6 \\ 2 & 6 & 8 \\ 6 & 8 & 18 \end{pmatrix}$$

验证：
- (1,1): 1+1+1+1 = 4 ✓
- (1,2): -1+0+1+2 = 2 ✓
- (1,3): 1+0+1+4 = 6 ✓
- (2,2): 1+0+1+4 = 6 ✓
- (2,3): -1+0+1+8 = 8 ✓
- (3,3): 1+0+1+16 = 18 ✓

**第三步：计算 $A^T b$**

$$A^T b = \begin{pmatrix} 1 & 1 & 1 & 1 \\ -1 & 0 & 1 & 2 \\ 1 & 0 & 1 & 4 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \\ 2 \\ 5 \end{pmatrix} = \begin{pmatrix} 2 + 1 + 2 + 5 \\ -2 + 0 + 2 + 10 \\ 2 + 0 + 2 + 20 \end{pmatrix} = \begin{pmatrix} 10 \\ 10 \\ 24 \end{pmatrix}$$

**第四步：正规方程**

$$\begin{pmatrix} 4 & 2 & 6 \\ 2 & 6 & 8 \\ 6 & 8 & 18 \end{pmatrix} \begin{pmatrix} c_0 \\ c_1 \\ c_2 \end{pmatrix} = \begin{pmatrix} 10 \\ 10 \\ 24 \end{pmatrix}$$

---

## 第23题

**题目：** 设
$$A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix}, \quad b = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}.$$
求最小二乘解 $x^* = \arg\min_{x \in \mathbb{R}^2} \|Ax - b\|_2$。然后计算 $\hat{b} = Ax^*$, $r = b - \hat{b}$。最后验证 $A^T r = 0$。

**解答：**

**第一步：求解最小二乘问题**

最小二乘解满足正规方程 $A^T A x = A^T b$。

$$A^T A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$

$$A^T b = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$$

解正规方程：
$$\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$$

$$x = (A^T A)^{-1} A^T b = \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 3 \\ 4 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 6 - 4 \\ -3 + 8 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 2 \\ 5 \end{pmatrix}$$

$$x^* = \boldsymbol{\begin{pmatrix} 2/3 \\ 5/3 \end{pmatrix} \approx \begin{pmatrix} 0.667 \\ 1.667 \end{pmatrix}}$$

**第二步：计算 $\hat{b} = Ax^*$**

$$\hat{b} = Ax^* = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2/3 \\ 5/3 \end{pmatrix} = \begin{pmatrix} 2/3 \\ 7/3 \\ 5/3 \end{pmatrix} \approx \begin{pmatrix} 0.667 \\ 2.333 \\ 1.667 \end{pmatrix}$$

**第三步：计算残差 $r$**

$$r = b - \hat{b} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} - \begin{pmatrix} 2/3 \\ 7/3 \\ 5/3 \end{pmatrix} = \begin{pmatrix} 1/3 \\ -1/3 \\ 1/3 \end{pmatrix}$$

**第四步：验证 $A^T r = 0$

$$A^T r = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1/3 \\ -1/3 \\ 1/3 \end{pmatrix} = \begin{pmatrix} 1/3 - 1/3 + 0 \\ 0 - 1/3 + 1/3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

验证成立。✓

---

## 第24题

**题目：** 设 $A \in \mathbb{R}^{m \times n}$ 满列秩。定义 $P = A(A^T A)^{-1} A^T$。证明 $P^2 = P$，$P^T = P$。进一步证明对任意 $b \in \mathbb{R}^m$，向量 $Pb$ 属于 $\operatorname{Col}(A)$，且 $b - Pb \perp \operatorname{Col}(A)$。因此 $Pb$ 是 $b$ 在 $\operatorname{Col}(A)$ 上的正交投影。

**证明：**

**第一步：证明对称性 $P^T = P$

$$P^T = [A(A^T A)^{-1} A^T]^T = (A^T)^T [(A^T A)^{-1}]^T A^T = A [(A^T A)^T]^{-1} A^T$$

因为 $A^T A$ 是对称矩阵，即 $(A^T A)^T = A^T A$，因此：

$$P^T = A(A^T A)^{-1} A^T = P$$

对称性成立。✓

**第二步：证明幂等性 $P^2 = P$**

$$P^2 = [A(A^T A)^{-1} A^T] [A(A^T A)^{-1} A^T] = A(A^T A)^{-1} (A^T A) (A^T A)^{-1} A^T$$

中间的 $(A^T A)^{-1}$ 和 $A^T A$ 相乘为单位矩阵，因此：

$$P^2 = A(A^T A)^{-1} A^T = P$$

幂等性成立。✓

**第三步：证明 $Pb \in \operatorname{Col}(A)$

$$Pb = A(A^T A)^{-1} A^T b = A \cdot [(A^T A)^{-1} A^T b$$

这是 $A$ 乘以一个向量（即 $(A^T A)^{-1} A^T b$），因此 $Pb$ 是 $A$ 的列的线性组合，属于 $\operatorname{Col}(A)$。✓

**第四步：证明 $b - Pb \perp \operatorname{Col}(A)$**

要证明 $b - Pb$ 与 $\operatorname{Col}(A)$ 正交，只需证明它与 $A$ 的每一列正交，即 $A^T (b - Pb) = 0$。

计算：
$$A^T (b - Pb) = A^T b - A^T Pb = A^T b - A^T A(A^T A)^{-1} A^T b$$

$$= A^T b - I \cdot A^T b = A^T b - A^T b = 0$$

因此 $b - Pb$ 与 $A$ 的所有列正交，即 $b - Pb \perp \operatorname{Col}(A)$。✓

**结论：** $P$ 满足对称且幂等，且满足正交投影的性质，因此 $P$ 是到 $\operatorname{Col}(A)$ 上的正交投影矩阵。

证毕。✓

---

## 第25题

**题目：** 设
$$A = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \quad b = \begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}.$$
求 $x^* = \arg\min_x \|Ax - b\|_2$。然后计算 $\hat{b} = Ax^*$, $r = b - \hat{b}$, $\|r\|_2$。

**解答：**

这是一个用常数拟合三个点的问题（相当于用水平线 $y = x$ 拟合三个点）。

**第一步：求最小二乘解 $x^*$**

$$A^T A = \begin{pmatrix} 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = 3$$

$$A^T b = \begin{pmatrix} 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix} = 7$$

由正规方程 $A^T A x = A^T b$：
$$3x = 7 \Rightarrow x^* = \boldsymbol{\frac{7}{3} \approx 2.333}$$

（这也等于三个点的平均值，符合直觉：用常数拟合的最小二乘解就是数据的均值）

**第二步：计算 $\hat{b}$**

$$\hat{b} = Ax^* = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \cdot \frac{7}{3} = \begin{pmatrix} 7/3 \\ 7/3 \\ 7/3 \end{pmatrix} \approx \begin{pmatrix} 2.333 \\ 2.333 \\ 2.333 \end{pmatrix}$$

**第三步：计算残差 $r$**

$$r = b - \hat{b} = \begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix} - \begin{pmatrix} 7/3 \\ 7/3 \\ 7/3 \end{pmatrix} = \begin{pmatrix} -4/3 \\ -1/3 \\ 5/3 \end{pmatrix}$$

**第四步：计算残差的2-范数**

$$\|r\|_2 = \sqrt{(-4/3)^2 + (-1/3)^2 + (5/3)^2} = \sqrt{\frac{16 + 1 + 25}{9}} = \sqrt{\frac{42}{9}} = \frac{\sqrt{42}}{3} \approx \boldsymbol{2.16}$$

---


## 第26题

**题目：** 设
$$A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}, \quad b = \begin{pmatrix} 1 \\ 1 \end{pmatrix}.$$
求线性方程组 $Ax = b$ 的全部解。然后在所有解中求欧氏范数最小的解。要求使用公式 $x^* = A^T (AA^T)^{-1} b$ 进行验证，并说明 $x^* \in \operatorname{Row}(A)$。

**解答：**

**第一步：求全部解**

方程组：
$$\begin{cases} x_1 + x_2 = 1 \\ x_2 + x_3 = 1 \end{cases}$$

这是一个欠定方程组（2个方程，3个未知数），解空间是一个仿射子空间。

令 $x_3 = t$ 为自由变量，则：
$x_2 = 1 - t$
$x_1 = 1 - x_2 = 1 - (1 - t) = t$

全部解为：
$$x = \begin{pmatrix} t \\ 1 - t \\ t \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}, \quad t \in \mathbb{R}$$

**第二步：求欧氏范数最小的解**

$\|x\|^2 = t^2 + (1-t)^2 + t^2 = 3t^2 - 2t + 1$

求导并令导数为0：$6t - 2 = 0 \Rightarrow t = 1/3$

最小范数解：
$$x^* = \begin{pmatrix} 1/3 \\ 2/3 \\ 1/3 \end{pmatrix}$$

**第三步：用公式验证**

计算 $AA^T$：
$$AA^T = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$

$$(AA^T)^{-1} = \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$$

$$x^* = A^T (AA^T)^{-1} b = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix} \cdot \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

$$= \frac{1}{3} \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 1/3 \\ 2/3 \\ 1/3 \end{pmatrix}$$

与之前的结果一致。✓

**第四步：说明 $x^* \in \operatorname{Row}(A)$**

$A$ 的行空间由行向量 $[1,1,0]$ 和 $[0,1,1]$ 张成。

$x^* = (1/3, 2/3, 1/3)^T = \frac{1}{3}[1,1,0]^T + \frac{1}{3}[0,1,1]^T \cdot 1$？不对。

实际上：
$\frac{1}{3} [1, 1, 0]^T + \frac{1}{3} [0, 1, 1]^T = (1/3, 2/3, 1/3)^T = x^*$

因此 $x^*$ 是 $A$ 的两个行向量的线性组合，即 $x^* \in \operatorname{Row}(A)$。✓

**几何意义：** 欠定方程组的最小范数解是 $b$ 在 $A$ 的行空间中的原像，它与零空间正交。

---

## 第27题

**题目：** 设
$$A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix}, \quad b = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}.$$
已知 $A$ 的薄 QR 分解为 $A = QR$，其中
$$Q = \begin{pmatrix} 1/\sqrt{2} & -1/\sqrt{6} \\ 1/\sqrt{2} & \sqrt{2}/\sqrt{6} \\ 0 & 1/\sqrt{6} \cdot 2? \end{pmatrix} \text{ 等等，题目给出：}$$
$$Q = \begin{pmatrix} 1/\sqrt{2} & -1/\sqrt{6} \\ 1/\sqrt{2} & \sqrt{2}/6? \\ 0 & 1/\sqrt{6} \end{pmatrix}, \quad R = \begin{pmatrix} \sqrt{2} & 1/\sqrt{2} \\ 0 & \sqrt{6}/2 \end{pmatrix}$$

先验证 $Q^T Q = I_2$, $QR = A$。然后利用 $Rx = Q^T b$ 求最小二乘解 $x^*$。最后计算 $\hat{b} = Ax^*$, $r = b - \hat{b}$，并验证 $Q^T r = 0$。

**解答：**

（注：题目中Q的第二列表述略模糊，我们按标准Gram-Schmidt结果来计算）

**标准QR分解结果：**
对 $A = [a_1, a_2]$ 做Gram-Schmidt正交化：
- $a_1 = (1, 1, 0)^T, \|a_1\| = \sqrt{2}$，故 $q_1 = (1/\sqrt{2}, 1/\sqrt{2}, 0)^T$
- $a_2 - (q_1^T a_2)q_1 = (0, 1, 1)^T - \frac{1}{\sqrt{2}}(1/\sqrt{2}, 1/\sqrt{2}, 0)^T = (-1/2, 1/2, 1)^T$
- 其范数 $= \sqrt{1/4 + 1/4 + 1} = \sqrt{3/2} = \sqrt{6}/2$
- $q_2 = (-1/\sqrt{6}, 1/\sqrt{6}, 2/\sqrt{6})^T$

因此：
$$Q = \begin{pmatrix} 1/\sqrt{2} & -1/\sqrt{6} \\ 1/\sqrt{2} & 1/\sqrt{6} \\ 0 & 2/\sqrt{6} \end{pmatrix}, \quad R = \begin{pmatrix} \sqrt{2} & 1/\sqrt{2} \\ 0 & \sqrt{6}/2 \end{pmatrix}$$

**验证 $Q^T Q = I_2$：**
$$Q^T Q = \begin{pmatrix} 1/\sqrt{2} & 1/\sqrt{2} & 0 \\ -1/\sqrt{6} & 1/\sqrt{6} & 2/\sqrt{6} \end{pmatrix} \begin{pmatrix} 1/\sqrt{2} & -1/\sqrt{6} \\ 1/\sqrt{2} & 1/\sqrt{6} \\ 0 & 2/\sqrt{6} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$
✓

**验证 $QR = A$：**
$$QR = \begin{pmatrix} 1/\sqrt{2} & -1/\sqrt{6} \\ 1/\sqrt{2} & 1/\sqrt{6} \\ 0 & 2/\sqrt{6} \end{pmatrix} \begin{pmatrix} \sqrt{2} & 1/\sqrt{2} \\ 0 & \sqrt{6}/2 \end{pmatrix} = \begin{pmatrix} 1 & 1/2 - 1/2 \\ 1 & 1/2 + 1/2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix} = A$$
✓

**求最小二乘解 $x^*$：**
$$Q^T b = \begin{pmatrix} 1/\sqrt{2} & 1/\sqrt{2} & 0 \\ -1/\sqrt{6} & 1/\sqrt{6} & 2/\sqrt{6} \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} = \begin{pmatrix} 3/\sqrt{2} \\ (-1+2+4)/\sqrt{6} \end{pmatrix} = \begin{pmatrix} 3/\sqrt{2} \\ 5/\sqrt{6} \end{pmatrix}$$

解 $Rx = Q^T b$：
$$\begin{pmatrix} \sqrt{2} & 1/\sqrt{2} \\ 0 & \sqrt{6}/2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 3/\sqrt{2} \\ 5/\sqrt{6} \end{pmatrix}$$

回代求解：
- $x_2 = (5/\sqrt{6}) / (\sqrt{6}/2) = (5/\sqrt{6}) \times (2/\sqrt{6}) = 10/6 = 5/3$
- $\sqrt{2} x_1 + (1/\sqrt{2}) \times (5/3) = 3/\sqrt{2}$
- $\sqrt{2} x_1 = 3/\sqrt{2} - 5/(3\sqrt{2}) = (9 - 5)/(3\sqrt{2}) = 4/(3\sqrt{2})$
- $x_1 = 4/(3\sqrt{2} \cdot \sqrt{2}) = 4/(3 \times 2) = 2/3$

$$x^* = \begin{pmatrix} 2/3 \\ 5/3 \end{pmatrix}$$

与第23题结果一致。✓

**计算 $\hat{b}$ 和 $r$：**
$$\hat{b} = Ax^* = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2/3 \\ 5/3 \end{pmatrix} = \begin{pmatrix} 2/3 \\ 7/3 \\ 5/3 \end{pmatrix}$$

$$r = b - \hat{b} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} - \begin{pmatrix} 2/3 \\ 7/3 \\ 5/3 \end{pmatrix} = \begin{pmatrix} 1/3 \\ -1/3 \\ 1/3 \end{pmatrix}$$

**验证 $Q^T r = 0$：**
$$Q^T r = \begin{pmatrix} 1/\sqrt{2} & 1/\sqrt{2} & 0 \\ -1/\sqrt{6} & 1/\sqrt{6} & 2/\sqrt{6} \end{pmatrix} \begin{pmatrix} 1/3 \\ -1/3 \\ 1/3 \end{pmatrix} = \begin{pmatrix} 0 \\ (-1 - 1 + 2)/3\sqrt{6}? \end{pmatrix}$$

等一下，重新算：
第一分量：$\frac{1}{\sqrt{2}} \cdot \frac{1}{3} + \frac{1}{\sqrt{2}} \cdot \frac{-1}{3} + 0 \cdot \frac{1}{3} = 0$
第二分量：$\frac{-1}{\sqrt{6}} \cdot \frac{1}{3} + \frac{1}{\sqrt{6}} \cdot \frac{-1}{3} + \frac{2}{\sqrt{6}} \cdot \frac{1}{3} = \frac{-1 - 1 + 2}{3\sqrt{6}} = 0$

$$Q^T r = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
验证成立。✓

---

## 第28题

**题目：** 设
$$A_\varepsilon = \begin{pmatrix} 1 & 1 \\ 1 & 1+\varepsilon \\ 1 & 1-\varepsilon \end{pmatrix}, \quad 0 < \varepsilon \ll 1.$$
计算 $A_\varepsilon^T A_\varepsilon$。求 $A_\varepsilon^T A_\varepsilon$ 的两个特征值，并由此写出 $\kappa_2(A_\varepsilon)^2 = \kappa_2(A_\varepsilon^T A_\varepsilon)$。进一步说明当 $\varepsilon \to 0$ 时，为什么 $A_\varepsilon$ 的两列接近线性相关，以及为什么正规方程 $A_\varepsilon^T A_\varepsilon x = A_\varepsilon^T b$ 会加重病态性。QR 分解是否可以解决这一问题？

**解答：**

**第一步：计算 $A_\varepsilon^T A_\varepsilon$**

$$A_\varepsilon^T A_\varepsilon = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1+\varepsilon & 1-\varepsilon \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 1+\varepsilon \\ 1 & 1-\varepsilon \end{pmatrix}$$
$$= \begin{pmatrix} 3 & 1 + (1+\varepsilon) + (1-\varepsilon) \\ 1 + (1+\varepsilon) + (1-\varepsilon) & 1 + (1+\varepsilon)^2 + (1-\varepsilon)^2 \end{pmatrix}$$
$$= \begin{pmatrix} 3 & 3 \\ 3 & 1 + 1 + 2\varepsilon + \varepsilon^2 + 1 - 2\varepsilon + \varepsilon^2 \end{pmatrix} = \begin{pmatrix} 3 & 3 \\ 3 & 3 + 2\varepsilon^2 \end{pmatrix}$$

**第二步：求特征值**

特征方程：$\det(A^TA - \lambda I) = 0$
$$(3 - \lambda)(3 + 2\varepsilon^2 - \lambda) - 9 = 0$$
$$\lambda^2 - (6 + 2\varepsilon^2)\lambda + 9 + 6\varepsilon^2 - 9 = 0$$
$$\lambda^2 - (6 + 2\varepsilon^2)\lambda + 6\varepsilon^2 = 0$$

解得：
$$\lambda = \frac{(6 + 2\varepsilon^2) \pm \sqrt{(6 + 2\varepsilon^2)^2 - 24\varepsilon^2}}{2} = \frac{6 + 2\varepsilon^2 \pm \sqrt{36 + 24\varepsilon^2 + 4\varepsilon^4 - 24\varepsilon^2}}{2}$$
$$= \frac{6 + 2\varepsilon^2 \pm \sqrt{36 + 4\varepsilon^4}}{2} = \frac{6 + 2\varepsilon^2 \pm 2\sqrt{9 + \varepsilon^4}}{2} = 3 + \varepsilon^2 \pm \sqrt{9 + \varepsilon^4}$$

当 $\varepsilon \to 0$ 时：
- $\lambda_1 \approx 3 + \varepsilon^2 + 3 = 6 + \varepsilon^2$（大特征值）
- $\lambda_2 \approx 3 + \varepsilon^2 - 3 = \varepsilon^2$（小特征值）

**第三步：条件数**

$$\kappa_2(A_\varepsilon) = \sqrt{\frac{\lambda_{\text{max}}}{\lambda_{\text{min}}}} \approx \sqrt{\frac{6}{\varepsilon^2}} = \frac{\sqrt{6}}{\varepsilon}$$

$$\kappa_2(A_\varepsilon^T A_\varepsilon) = \frac{\lambda_{\text{max}}}{\lambda_{\text{min}}} \approx \frac{6}{\varepsilon^2} = \kappa_2(A_\varepsilon)^2$$

**第四步：讨论**

1. **两列接近线性相关：** 当 $\varepsilon \to 0$ 时，第二列 $(1, 1+\varepsilon, 1-\varepsilon)^T$ 趋近于第一列 $(1, 1, 1)^T$，两列几乎相同，因此接近线性相关，矩阵接近秩亏。

2. **正规方程加重病态性：** 正规方程是 $A^T A x = A^T b$，其条件数是原矩阵条件数的平方（$\kappa(A^TA) = \kappa(A)^2$）。当 $A$ 的条件数已经很大时，$A^TA$ 的条件数会变得更大，数值求解时会有更严重的舍入误差。

3. **QR分解能否解决？** QR分解在一定程度上可以改善数值稳定性。因为QR分解直接对 $A$ 操作，通过正交变换将 $A$ 化为上三角矩阵 $R$，然后解 $Rx = Q^Tb$。正交变换不改变2-范数，因此不会放大条件数。相比直接求解正规方程，QR分解的数值稳定性更好，特别是对于病态问题。

但是，如果 $A$ 本身就非常病态（接近秩亏），无论用什么方法，解的敏感性都是问题固有的。QR分解只是数值上更稳定，不会引入额外的病态性放大。

---

## 第29题

**题目：** 设 $A \in \mathbb{R}^{m \times n}$。证明由欧氏向量范数诱导出的矩阵范数满足 $\|A\|_2 = \max_{\|x\|_2 = 1} \|Ax\|_2$。并证明对任意 $x \in \mathbb{R}^n$，有 $\|Ax\|_2 \leq \|A\|_2 \|x\|_2$。

**证明：**

**第一部分：诱导范数的定义**

由向量范数诱导出的矩阵范数定义为：
$$\|A\| = \max_{x \neq 0} \frac{\|Ax\|}{\|x\|}$$

对于欧氏范数（2-范数），就是：
$$\|A\|_2 = \max_{x \neq 0} \frac{\|Ax\|_2}{\|x\|_2}$$

令 $y = x/\|x\|_2$，则 $\|y\|_2 = 1$，且：
$$\frac{\|Ax\|_2}{\|x\|_2} = \|A \cdot \frac{x}{\|x\|_2}\|_2 = \|Ay\|_2$$

因此：
$$\|A\|_2 = \max_{\|x\|_2 = 1} \|Ax\|_2$$

这就是谱范数的定义。✓

**第二部分：相容性不等式**

对任意 $x \in \mathbb{R}^n$：

- 若 $x = 0$，不等式显然成立（两边都是0）。
- 若 $x \neq 0$，由诱导范数的定义：
  $$\|A\|_2 = \max_{y \neq 0} \frac{\|Ay\|_2}{\|y\|_2} \geq \frac{\|Ax\|_2}{\|x\|_2}$$
  
  两边乘以 $\|x\|_2$（正数，不等号方向不变）：
  $$\|Ax\|_2 \leq \|A\|_2 \|x\|_2$$

证毕。✓

---

## 第30题

**题目：** 设 $A \in \mathbb{R}^{m \times n}$，$B \in \mathbb{R}^{n \times p}$。从诱导范数定义出发证明 $\|AB\|_2 \leq \|A\|_2 \|B\|_2$。

**证明：**

对任意非零向量 $x \in \mathbb{R}^p$，由向量范数的相容性（第29题结论）：
$$\|ABx\|_2 = \|A(Bx)\|_2 \leq \|A\|_2 \|Bx\|_2$$

对 $Bx$ 再次应用相容性：
$$\|Bx\|_2 \leq \|B\|_2 \|x\|_2$$

因此：
$$\|ABx\|_2 \leq \|A\|_2 \|B\|_2 \|x\|_2$$

两边除以 $\|x\|_2$（$x \neq 0$）：
$$\frac{\|ABx\|_2}{\|x\|_2} \leq \|A\|_2 \|B\|_2$$

上式对所有非零 $x$ 成立，因此对最大值也成立：
$$\|AB\|_2 = \max_{x \neq 0} \frac{\|ABx\|_2}{\|x\|_2} \leq \|A\|_2 \|B\|_2$$

证毕。✓

---

## 第31题

**题目：** 设 $A \in \mathbb{R}^{m \times n}$。证明 $\|A\|_F^2 = \operatorname{tr}(A^T A)$。进一步证明若 $A = U\Sigma V^T$ 是奇异值分解，则 $\|A\|_F^2 = \sum_i \sigma_i^2$。

**证明：**

**第一部分：$\|A\|_F^2 = \operatorname{tr}(A^T A)$**

设 $A = (a_{ij})_{m \times n}$，则 $A^T A$ 的第 $k$ 个对角元为：
$$(A^T A)_{kk} = \sum_{i=1}^m a_{ik}^2$$

因此迹为：
$$\operatorname{tr}(A^T A) = \sum_{k=1}^n (A^T A)_{kk} = \sum_{k=1}^n \sum_{i=1}^m a_{ik}^2 = \sum_{i=1}^m \sum_{k=1}^n a_{ik}^2 = \|A\|_F^2$$

✓

**第二部分：$\|A\|_F^2 = \sum_i \sigma_i^2$**

设 $A = U\Sigma V^T$ 是SVD，其中 $U \in \mathbb{R}^{m \times m}, V \in \mathbb{R}^{n \times n}$ 是正交矩阵，$\Sigma \in \mathbb{R}^{m \times n}$ 是对角矩阵，对角元为奇异值 $\sigma_1, \sigma_2, \dots, \sigma_p$（$p = \min(m,n)$）。

则：
$$A^T A = V \Sigma^T U^T U \Sigma V^T = V \Sigma^T \Sigma V^T$$

（利用了 $U^T U = I$）

注意到 $\Sigma^T \Sigma$ 是 $n \times n$ 对角矩阵，对角元为 $\sigma_1^2, \sigma_2^2, \dots, \sigma_p^2, 0, \dots, 0$。

由迹的相似不变性（$\operatorname{tr}(P^{-1}AP) = \operatorname{tr}(A)$）：
$$\operatorname{tr}(A^T A) = \operatorname{tr}(V \Sigma^T \Sigma V^T) = \operatorname{tr}(\Sigma^T \Sigma V^T V) = \operatorname{tr}(\Sigma^T \Sigma) = \sum_{i=1}^p \sigma_i^2$$

（这里用了 $\operatorname{tr}(AB) = \operatorname{tr}(BA)$）

结合第一部分的结论：
$$\|A\|_F^2 = \operatorname{tr}(A^T A) = \sum_{i=1}^p \sigma_i^2$$

证毕。✓

---

## 第32题

**题目：** 设 $Q \in \mathbb{R}^{m \times m}$ 与 $P \in \mathbb{R}^{n \times n}$ 均为正交矩阵。证明 $\|QAP\|_2 = \|A\|_2$, $\|QAP\|_F = \|A\|_F$。并说明这两个等式在奇异值分解中的作用。

**证明：**

**第一部分：2-范数的正交不变性**

$$\|QAP\|_2^2 = \lambda_{\text{max}}((QAP)^T (QAP)) = \lambda_{\text{max}}(P^T A^T Q^T Q A P)$$

因为 $Q$ 是正交矩阵，$Q^T Q = I_m$，所以：
$$= \lambda_{\text{max}}(P^T A^T A P)$$

相似矩阵有相同的特征值，因此：
$$\lambda_{\text{max}}(P^T A^T A P) = \lambda_{\text{max}}(A^T A) = \|A\|_2^2$$

两边开平方得：
$$\|QAP\|_2 = \|A\|_2$$

✓

**第二部分：Frobenius范数的正交不变性**

由第31题，$\|B\|_F^2 = \operatorname{tr}(B^T B)$，所以：
$$\|QAP\|_F^2 = \operatorname{tr}((QAP)^T QAP) = \operatorname{tr}(P^T A^T Q^T Q A P) = \operatorname{tr}(P^T A^T A P)$$

由迹的相似不变性：
$$\operatorname{tr}(P^T A^T A P) = \operatorname{tr}(A^T A P P^T) = \operatorname{tr}(A^T A) = \|A\|_F^2$$

（或者直接用迹的循环性质：$\operatorname{tr}(P^T A^T A P) = \operatorname{tr}(A^T A P P^T) = \operatorname{tr}(A^T A)$）

因此：
$$\|QAP\|_F = \|A\|_F$$

✓

**在SVD中的作用：**

奇异值分解 $A = U\Sigma V^T$ 将矩阵分解为正交矩阵乘以对角矩阵再乘以正交矩阵。由于2-范数和Frobenius范数在正交变换下保持不变，因此：
- $\|A\|_2 = \|U\Sigma V^T\|_2 = \|\Sigma\|_2 = \sigma_{\text{max}}$（最大奇异值）
- $\|A\|_F = \|U\Sigma V^T\|_F = \|\Sigma\|_F = \sqrt{\sum \sigma_i^2}$

这使得我们可以通过SVD简洁地表达矩阵的范数，也为低秩逼近提供了理论基础（Eckart-Young定理）。

---

## 第33题

**题目：** 设
$$W = \operatorname{span}\left\{ \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \right\} \subset \mathbb{R}^3.$$
对 $b = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$，求 $b$ 在 $W$ 上的正交投影。

**解答：**

**方法一：使用投影矩阵公式**

设 $A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix}$（以 $W$ 的基向量为列），则投影到 $W = \operatorname{Col}(A)$ 的正交投影矩阵为：
$$P = A(A^T A)^{-1} A^T$$

计算：
$$A^T A = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$

$$(A^T A)^{-1} = \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$$

$$P = A(A^T A)^{-1} A^T = \begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix} \cdot \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}$$
$$= \frac{1}{3} \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}$$
$$= \frac{1}{3} \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & -1 \\ 1 & -1 & 2 \end{pmatrix}$$

正交投影：
$$\hat{b} = Pb = \frac{1}{3} \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & -1 \\ 1 & -1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 2 + 2 + 3 \\ 1 + 4 - 3 \\ 1 - 2 + 6 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 7 \\ 2 \\ 5 \end{pmatrix} = \boldsymbol{\begin{pmatrix} 7/3 \\ 2/3 \\ 5/3 \end{pmatrix}}$$

**验证：** $b - \hat{b} = (1 - 7/3, 2 - 2/3, 3 - 5/3)^T = (-4/3, 4/3, 4/3)^T$，应与 $W$ 正交。
- 与 $(1,1,0)^T$ 的内积：$-4/3 + 4/3 + 0 = 0$ ✓
- 与 $(1,0,1)^T$ 的内积：$-4/3 + 0 + 4/3 = 0$ ✓

---

## 第34题

**题目：** 设 $A \in \mathbb{R}^{m \times n}$ 满列秩，且 $x^*$ 是 $\min_{x \in \mathbb{R}^n} \|Ax - b\|_2$ 的解。证明以下命题等价：
1. $x^*$ 是最小二乘解，
2. $A^T (Ax^* - b) = 0$，
3. $Ax^*$ 是 $b$ 在 $\operatorname{Col}(A)$ 上的正交投影。

**证明：**

我们证明 $(1) \Rightarrow (2) \Rightarrow (3) \Rightarrow (1)$。

**$(1) \Rightarrow (2)$：若 $x^*$ 是最小二乘解，则 $A^T(Ax^* - b) = 0$**

最小二乘解最小化 $f(x) = \|Ax - b\|_2^2 = (Ax - b)^T (Ax - b)$。

展开：
$$f(x) = x^T A^T A x - 2x^T A^T b + b^T b$$

对 $x$ 求导（梯度）：
$$\nabla f(x) = 2A^T A x - 2A^T b$$

极小值点满足梯度为零：
$$2A^T A x^* - 2A^T b = 0 \Rightarrow A^T A x^* = A^T b \Rightarrow A^T(Ax^* - b) = 0$$

这就是正规方程。✓

**$(2) \Rightarrow (3)$：若 $A^T(Ax^* - b) = 0$，则 $Ax^*$ 是 $b$ 在 $\operatorname{Col}(A)$ 上的正交投影**

条件 $A^T(Ax^* - b) = 0$ 意味着向量 $Ax^* - b$ 与 $A$ 的每一列都正交，即与 $\operatorname{Col}(A)$ 正交。

即：$b - Ax^* \perp \operatorname{Col}(A)$

而 $Ax^* \in \operatorname{Col}(A)$（显然，因为它是 $A$ 乘以向量 $x^*$）。

根据正交投影的定义：若 $\hat{b} \in W$ 且 $b - \hat{b} \perp W$，则 $\hat{b}$ 是 $b$ 在 $W$ 上的正交投影。

这里 $\hat{b} = Ax^* \in \operatorname{Col}(A)$ 且 $b - Ax^* \perp \operatorname{Col}(A)$，故 $Ax^*$ 是 $b$ 在 $\operatorname{Col}(A)$ 上的正交投影。✓

**$(3) \Rightarrow (1)$：若 $Ax^*$ 是正交投影，则 $x^*$ 是最小二乘解**

正交投影的性质：对任意 $y \in \operatorname{Col}(A)$，有
$$\|b - y\|_2 \geq \|b - Ax^*\|_2$$

即 $Ax^*$ 是 $\operatorname{Col}(A)$ 中距离 $b$ 最近的点。

而 $\operatorname{Col}(A) = \{Ax : x \in \mathbb{R}^n\}$，因此对任意 $x \in \mathbb{R}^n$，有
$$\|Ax - b\|_2 \geq \|Ax^* - b\|_2$$

这说明 $x^*$ 是最小二乘问题的解。✓

综上，三个命题等价。

证毕。✓

---

## 第35题

**题目：** 设
$$b = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}, \quad A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \\ 1 & 1 \end{pmatrix}.$$
讨论最小二乘问题 $\min_x \|Ax - b\|_2$。求所有最小二乘解，并在其中求欧氏范数最小的解。并说明为什么最小二乘解不唯一。

**解答：**

**第一步：分析问题**

矩阵 $A$ 的两列完全相同，都是 $(1,1,1)^T$，因此 $\operatorname{rank}(A) = 1$，列空间是直线 $\operatorname{span}\{(1,1,1)^T\}$。

$Ax = \begin{pmatrix} 1 & 1 \\ 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = (x_1 + x_2) \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$

因此 $Ax$ 总是沿着 $(1,1,1)^T$ 方向。

**第二步：求正交投影（唯一的）**

$b$ 在列空间上的正交投影是唯一的：
$$\hat{b} = \frac{b^T a}{a^T a} a = \frac{1 + 2 + 3}{1 + 1 + 1} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \frac{6}{3} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = 2 \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix}$$

**第三步：求所有最小二乘解**

最小二乘解满足 $Ax = \hat{b} = (2, 2, 2)^T$，即：
$$x_1 + x_2 = 2$$

所有解为：
$$x = \begin{pmatrix} t \\ 2 - t \end{pmatrix}, \quad t \in \mathbb{R}$$

**为什么解不唯一？**
因为 $A$ 不是列满秩的（$\operatorname{rank}(A) = 1 < 2$），零空间非平凡。$N(A) = \operatorname{span}\{(1, -1)^T\}$。如果 $x^*$ 是一个最小二乘解，那么 $x^* + z$（其中 $z \in N(A)$）也是最小二乘解，因为 $A(x^* + z) = Ax^* + Az = Ax^* + 0 = Ax^*$。

**第四步：求范数最小的解**

$\|x\|^2 = t^2 + (2-t)^2 = 2t^2 - 4t + 4$

求导：$4t - 4 = 0 \Rightarrow t = 1$

最小范数解：
$$x_{\text{min}} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

验证：$Ax_{\text{min}} = (2, 2, 2)^T = \hat{b}$ ✓

也可以用伪逆公式：$x^* = A^\dagger b$

$A$ 的SVD：秩1矩阵，最大奇异值 $\sigma_1 = \sqrt{6}$，对应左奇异向量 $(1,1,1)^T/\sqrt{3}$，右奇异向量 $(1,1)^T/\sqrt{2}$

$$A^\dagger = \frac{1}{6} \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}$$

$$x^* = A^\dagger b = \frac{1}{6} \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \frac{1}{6} \begin{pmatrix} 6 \\ 6 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

一致。✓

---

## 第36题

**题目：** 设
$$A = \begin{pmatrix} 1 & 0 \\ 0 & 2 \\ 0 & 0 \end{pmatrix}.$$
计算 $A^\dagger$，并验证 Moore–Penrose 条件中的两个等式：$AA^\dagger A = A$, $A^\dagger A A^\dagger = A^\dagger$。

**解答：**

对于对角矩阵，伪逆就是将非零对角元取倒数，零保持，然后转置。

$$A^\dagger = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1/2 & 0 \end{pmatrix}$$

**验证 $AA^\dagger A = A$：**

$$AA^\dagger = \begin{pmatrix} 1 & 0 \\ 0 & 2 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1/2 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

$$AA^\dagger A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 2 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 2 \\ 0 & 0 \end{pmatrix} = A$$
✓

**验证 $A^\dagger A A^\dagger = A^\dagger$：**

$$A^\dagger A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1/2 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 2 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2$$

$$A^\dagger A A^\dagger = I_2 \cdot A^\dagger = A^\dagger$$
✓

（另外两个条件：$(AA^\dagger)^T = AA^\dagger$ 和 $(A^\dagger A)^T = A^\dagger A$ 也显然成立，因为它们都是对称矩阵。）

---

## 第37题

**题目：** 设
$$A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}.$$
求 $A$ 的奇异值分解，由此计算 $A^\dagger$ 并验证 Moore–Penrose 条件中的两个等式：$AA^\dagger A = A$, $A^\dagger A A^\dagger = A^\dagger$。

**解答：**

**第一步：求奇异值分解**

$A$ 已经是对角矩阵，非零对角元为 2 和 1，因此奇异值为 $\sigma_1 = 2, \sigma_2 = 1$。

$A$ 的SVD可以写成：
$$A = U \Sigma V^T$$
其中：
- $U = I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$（2阶单位矩阵）
- $\Sigma = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$
- $V = I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$（3阶单位矩阵）

验证：$U\Sigma V^T = I_2 \cdot \Sigma \cdot I_3 = \Sigma = A$ ✓

**第二步：计算伪逆 $A^\dagger$**

由SVD求伪逆：$A^\dagger = V \Sigma^\dagger U^T$，其中 $\Sigma^\dagger$ 是 $\Sigma$ 的转置，非零奇异值取倒数。

$$\Sigma^\dagger = \begin{pmatrix} 1/2 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}$$

$$A^\dagger = V \Sigma^\dagger U^T = I_3 \cdot \begin{pmatrix} 1/2 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix} \cdot I_2 = \begin{pmatrix} 1/2 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}$$

**验证 $AA^\dagger A = A$：**

$$AA^\dagger = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 1/2 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2$$

$$AA^\dagger A = I_2 \cdot A = A$$
✓

**验证 $A^\dagger A A^\dagger = A^\dagger$：**

$$A^\dagger A = \begin{pmatrix} 1/2 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

$$A^\dagger A A^\dagger = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 1/2 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1/2 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix} = A^\dagger$$
✓

---

## 第38题

**题目：** 设
$$A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad E = \begin{pmatrix} 0 & 0 \\ 0 & \delta \end{pmatrix}, \quad \delta > 0.$$
分别求 $A$ 与 $A + E$ 的奇异值。说明一个很小的扰动可以如何改变矩阵的秩。讨论当 $\delta \to 0$ 时，矩阵 $A + E$ 的病态性如何变化。

**解答：**

**矩阵 $A$ 的奇异值：**

$A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ 是对角矩阵，奇异值就是对角元的绝对值：
$$\sigma_1(A) = 1, \quad \sigma_2(A) = 0$$

秩：$\operatorname{rank}(A) = 1$（只有1个非零奇异值）

**矩阵 $A + E$ 的奇异值：**

$$A + E = \begin{pmatrix} 1 & 0 \\ 0 & \delta \end{pmatrix}$$

同样是对角矩阵，奇异值为：
$$\sigma_1(A+E) = 1, \quad \sigma_2(A+E) = \delta$$

秩：$\operatorname{rank}(A+E) = 2$（两个非零奇异值）

**小扰动对秩的影响：**

尽管 $\delta$ 可以非常小（比如 $\delta = 10^{-10}$），但 $A + E$ 的秩是 2，而 $A$ 的秩是 1。一个任意小的扰动就可以改变矩阵的秩，这说明**秩是一个"不稳定"的数值量**——微小的扰动就可能导致秩的跳变。

这也是为什么在数值计算中，我们通常不说"矩阵的秩是多少"，而是说"数值秩"，即大于某个阈值（如机器精度的倍数）的奇异值的个数。

**病态性变化：**

当 $\delta \to 0$ 时，$A + E$ 的条件数为：
$$\kappa_2(A + E) = \frac{\sigma_{\text{max}}}{\sigma_{\text{min}}} = \frac{1}{\delta} \to +\infty$$

条件数趋向于无穷大，矩阵越来越病态。这意味着：
- 以 $A+E$ 为系数矩阵的线性系统对扰动非常敏感
- 最小二乘问题的解会高度敏感
- 数值求解会有很大的误差

**总结：** 当矩阵接近秩亏时（最小奇异值很小），条件数很大，问题病态。一个小的扰动可能使矩阵从秩亏变为满秩，但条件数极大，问题仍然病态。

---

## 第39题

**题目：** 设 $A \in \mathbb{R}^{m \times n}$，证明 $\|A\|_2 \leq \|A\|_F \leq \|A\|_*$。

（注：$\|A\|_*$ 是核范数（nuclear norm），等于所有奇异值之和，也叫迹范数）

**证明：**

设 $A$ 的奇异值为 $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_p \geq 0$，其中 $p = \min(m, n)$。

**第一部分：$\|A\|_2 \leq \|A\|_F$**

已知：
- $\|A\|_2 = \sigma_1$（最大奇异值）
- $\|A\|_F = \sqrt{\sigma_1^2 + \sigma_2^2 + \dots + \sigma_p^2}$

显然：
$$\sigma_1^2 \leq \sigma_1^2 + \sigma_2^2 + \dots + \sigma_p^2$$

两边开平方：
$$\sigma_1 \leq \sqrt{\sigma_1^2 + \sigma_2^2 + \dots + \sigma_p^2}$$

即：
$$\|A\|_2 \leq \|A\|_F$$

✓

**第二部分：$\|A\|_F \leq \|A\|_*$**

核范数（迹范数）定义为所有奇异值之和：
$$\|A\|_* = \sigma_1 + \sigma_2 + \dots + \sigma_p$$

我们需要证明：
$$\sqrt{\sum_{i=1}^p \sigma_i^2} \leq \sum_{i=1}^p \sigma_i$$

两边都是非负数，平方后等价于：
$$\sum_{i=1}^p \sigma_i^2 \leq \left(\sum_{i=1}^p \sigma_i\right)^2$$

展开右边：
$$\left(\sum_{i=1}^p \sigma_i\right)^2 = \sum_{i=1}^p \sigma_i^2 + 2 \sum_{1 \leq i < j \leq p} \sigma_i \sigma_j$$

由于奇异值非负，交叉项 $2\sum_{i < j} \sigma_i \sigma_j \geq 0$，因此：
$$\left(\sum_{i=1}^p \sigma_i\right)^2 \geq \sum_{i=1}^p \sigma_i^2$$

即：
$$\|A\|_* \geq \|A\|_F$$

✓

综上：
$$\|A\|_2 \leq \|A\|_F \leq \|A\|_*$$

证毕。✓

---

## 第40题

**题目：** 设
$$A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \\ 1 & 1 \end{pmatrix}.$$
求 $A$ 的最佳秩一逼近和最佳秩二逼近。分别计算在谱范数下的逼近误差和在Frobenius范数下的逼近误差。

**解答：**

**第一步：求奇异值分解**

$A$ 是秩1矩阵（所有行/列都成比例），我们来求它的奇异值。

$$A^T A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 3 & 3 \\ 3 & 3 \end{pmatrix}$$

特征值：$\det(A^TA - \lambda I) = (3-\lambda)^2 - 9 = \lambda^2 - 6\lambda = \lambda(\lambda - 6) = 0$
$\lambda_1 = 6, \lambda_2 = 0$

因此奇异值：$\sigma_1 = \sqrt{6}, \sigma_2 = 0$

对应的右奇异向量：
- 对 $\lambda_1 = 6$：$(A^TA - 6I)v = 0 \Rightarrow \begin{pmatrix} -3 & 3 \\ 3 & -3 \end{pmatrix} v = 0 \Rightarrow v_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$
- 对 $\lambda_2 = 0$：$v_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$

左奇异向量：
- $u_1 = \frac{1}{\sigma_1} Av_1 = \frac{1}{\sqrt{6}} \cdot \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{12}} \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix} = \frac{1}{\sqrt{3}} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$

**第二步：最佳秩一逼近**

由于 $A$ 本身就是秩1矩阵，最佳秩一逼近就是 $A$ 自己：
$$A_1 = \sigma_1 u_1 v_1^T = A$$

- 谱范数误差：$\|A - A_1\|_2 = \|0\|_2 = 0$
- Frobenius范数误差：$\|A - A_1\|_F = 0$

**第三步：最佳秩二逼近**

$A$ 本身是秩1的，秩二逼近当然也是 $A$ 自己（因为 $A$ 的秩本来就不超过2）。

$$A_2 = \sigma_1 u_1 v_1^T + \sigma_2 u_2 v_2^T = A + 0 = A$$

- 谱范数误差：$\|A - A_2\|_2 = 0$
- Frobenius范数误差：$\|A - A_2\|_F = 0$

**补充：** 如果问的是"用秩1/秩2去逼近一个秩更高的矩阵"，那才有非零误差。这里 $A$ 本身是秩1的，所以秩1和秩2逼近都是精确的。

让我们再确认一下 $\|A\|_F$：
$$\|A\|_F = \sqrt{1^2 + 1^2 + 1^2 + 1^2 + 1^2 + 1^2} = \sqrt{6} = \sigma_1$$
（和秩1矩阵的Frobenius范数公式一致）

---

## 第41题

**题目：** 设 $A \in \mathbb{R}^{m \times n}$，且 $A = U_r \Sigma_r V_r^T$ 是紧奇异值分解。证明 $AA^\dagger = U_r U_r^T$，$A^\dagger A = V_r V_r^T$。并说明 $AA^\dagger$ 与 $A^\dagger A$ 分别投影到哪些子空间。

**证明：**

紧SVD中，$U_r \in \mathbb{R}^{m \times r}$, $V_r \in \mathbb{R}^{n \times r}$ 满足 $U_r^T U_r = I_r$, $V_r^T V_r = I_r$，$\Sigma_r = \operatorname{diag}(\sigma_1, \dots, \sigma_r)$ 可逆。

伪逆由SVD给出：
$$A^\dagger = V_r \Sigma_r^{-1} U_r^T$$

**第一部分：证明 $AA^\dagger = U_r U_r^T$**

$$AA^\dagger = (U_r \Sigma_r V_r^T)(V_r \Sigma_r^{-1} U_r^T) = U_r \Sigma_r (V_r^T V_r) \Sigma_r^{-1} U_r^T$$

因为 $V_r^T V_r = I_r$，所以：
$$= U_r \Sigma_r \cdot I_r \cdot \Sigma_r^{-1} U_r^T = U_r (\Sigma_r \Sigma_r^{-1}) U_r^T = U_r I_r U_r^T = U_r U_r^T$$

✓

**第二部分：证明 $A^\dagger A = V_r V_r^T$**

$$A^\dagger A = (V_r \Sigma_r^{-1} U_r^T)(U_r \Sigma_r V_r^T) = V_r \Sigma_r^{-1} (U_r^T U_r) \Sigma_r V_r^T$$

因为 $U_r^T U_r = I_r$，所以：
$$= V_r \Sigma_r^{-1} \cdot I_r \cdot \Sigma_r V_r^T = V_r (\Sigma_r^{-1} \Sigma_r) V_r^T = V_r I_r V_r^T = V_r V_r^T$$

✓

**投影到哪些子空间：**

- $AA^\dagger = U_r U_r^T$ 是到 $\operatorname{Col}(U_r) = \operatorname{Col}(A)$（$A$ 的列空间）上的正交投影。
  因为 $U_r$ 的列是列空间的一组标准正交基。

- $A^\dagger A = V_r V_r^T$ 是到 $\operatorname{Col}(V_r) = \operatorname{Row}(A)$（$A$ 的行空间）上的正交投影。
  因为 $V_r$ 的列是行空间的一组标准正交基。

**几何意义：**
- $AA^\dagger$ 将任意向量投影到 $A$ 的列空间（即值域）
- $A^\dagger A$ 将任意向量投影到 $A$ 的行空间（即零空间的正交补）

---

## 第42题

**题目：** 设 $A \in \mathbb{R}^{m \times n}$ 满列秩。证明最小二乘解可以写为 $x^* = A^\dagger b$。进一步证明此时 $A^\dagger = (A^T A)^{-1} A^T$。

**证明：**

**第一部分：满列秩时 $A^\dagger = (A^T A)^{-1} A^T$**

设 $A$ 满列秩，即 $\operatorname{rank}(A) = n$。此时紧SVD为 $A = U_n \Sigma_n V_n^T$，其中 $V_n \in \mathbb{R}^{n \times n}$ 是正交方阵（因为秩为 $n$），$U_n \in \mathbb{R}^{m \times n}$ 满足 $U_n^T U_n = I_n$。

伪逆为：
$$A^\dagger = V_n \Sigma_n^{-1} U_n^T$$

现在看 $(A^T A)^{-1} A^T$：
$$A^T A = V_n \Sigma_n U_n^T U_n \Sigma_n V_n^T = V_n \Sigma_n^2 V_n^T$$

因此：
$$(A^T A)^{-1} = (V_n \Sigma_n^2 V_n^T)^{-1} = V_n (\Sigma_n^2)^{-1} V_n^T = V_n \Sigma_n^{-2} V_n^T$$

（因为 $V_n$ 是正交方阵，故可逆，且 $V_n^{-1} = V_n^T$）

于是：
$$(A^T A)^{-1} A^T = V_n \Sigma_n^{-2} V_n^T \cdot V_n \Sigma_n U_n^T = V_n \Sigma_n^{-2} \Sigma_n U_n^T = V_n \Sigma_n^{-1} U_n^T = A^\dagger$$

✓

**第二部分：最小二乘解可写为 $x^* = A^\dagger b$**

我们知道满列秩时最小二乘解为 $x^* = (A^T A)^{-1} A^T b$。

由第一部分的结论，$A^\dagger = (A^T A)^{-1} A^T$，因此：
$$x^* = A^\dagger b$$

✓

**补充说明：** 这个结论不仅在满列秩时成立，对一般的矩阵 $A$，最小二乘问题的最小范数解都是 $x^* = A^\dagger b$。当 $A$ 列满秩时，最小二乘解唯一，就是 $A^\dagger b$；当 $A$ 不列满秩时，最小二乘解不唯一，但其中范数最小的那个解还是 $A^\dagger b$。

证毕。✓

---

（全题解答完）

---

> 本内容由 Coze AI 生成，请遵循相关法律法规及《人工智能生成合成内容标识办法》使用与传播。
