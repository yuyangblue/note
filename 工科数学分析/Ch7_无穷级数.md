# Ch7 无穷级数

## §7.1 常数项级数

### 引例
庄子无穷二分、芝诺悖论

**问题：**
1. 无穷多项相加是否存在"和"
2. 是否满足结合律、交换律

**例子：** $\{(-1)^n\}$: $-1+1-1+1+\cdots+(-1)^n+\cdots$ 不具有结合律

### 7.1.1 概念、性质、收敛原理

#### 定义 1.1
对数列 $\{u_n\}$，定义：
- **数项级数**：$u_1+u_2+\cdots+u_n+\cdots = \sum_{n=1}^{\infty} u_n$
- **部分和**：$u_1+u_2+\cdots+u_n = \sum_{k=1}^{n} u_k = S_n$

若极限 $\lim_{n\to\infty} S_n$ 存在，则称级数 $\sum u_n$ **收敛**，极限值称为**级数和**；
若极限 $\lim_{n\to\infty} S_n$ 不存在，则称级数 $\sum u_n$ **发散**。

---

#### 例1：讨论等比级数 $\sum_{n=0}^{\infty} q^n$ 的敛散性

**解：**
当 $q \neq 1$ 时，部分和 $S_n = \frac{1-q^n}{1-q}$

- 若 $|q| < 1$，则 $q^n \to 0$，从而 $S_n \to \frac{1}{1-q}$，级数**收敛**
- 若 $|q| > 1$，则 $S_n \to \infty$，级数**发散**
- 若 $q = 1$，则 $S_n = n \to \infty$，**发散**
- 若 $q = -1$，则 $\lim_{n\to\infty} S_n$ 不存在，**发散**

**综上所述**：级数 $\sum q^n$ 在 $|q| < 1$ 时收敛，$|q| \geq 1$ 时发散

---

#### 例2：讨论级数 $\sum_{n=1}^{\infty} \frac{1}{n(n+1)}$ 的敛散性

**解：**
$$S_n = \sum_{k=1}^{n} \frac{1}{k(k+1)} = \sum_{k=1}^{n} \left(\frac{1}{k} - \frac{1}{k+1}\right) = 1 - \frac{1}{n+1} \to 1$$

级数**收敛**

---

### 性质

#### 性质1
设 $\sum a_n = A$，$\sum b_n = B$，其中 $A, B$ 均为有限数

**(1)(2) 线性性质**：若 $k_1, k_2$ 为常数，则
$$\sum_{n=1}^{\infty} (k_1 a_n + k_2 b_n) = k_1 \sum_{n=1}^{\infty} a_n + k_2 \sum_{n=1}^{\infty} b_n$$

**(3)** 若 $a_n \leq b_n$，则 $\sum a_n \leq \sum b_n$，$A_n \leq B_n$

#### 性质2
在级数中，任意删去、添加或改变有限项，不改变该级数的敛散性。

#### 性质3
**(1)** 若级数 $\sum u_n$ 收敛，则 $\lim_{n\to\infty} u_n = S_n - S_{n-1} \to 0$

**(2)** 级数 $\sum u_n$ 收敛 $\iff$ 余项 $R_n = \sum_{k=n+1}^{\infty} u_k \to 0$

$\iff \sum_{n=1}^{\infty} u_n = \sum_{k=1}^{n} u_k + R_n = S_n + R_n$

级数 $\sum u_n$ 收敛 $\iff \sum_{n=1}^{\infty} u_n = \lim_{n\to\infty} S_n$

#### 性质4
收敛级数满足加法结合律：若级数 $\sum u_n$ 收敛，则不改变各项次序任意添加括号所得新级数也收敛，且和不变。

**证明：** 设 $\sum u_n$ 收敛，和为 $S$。记 $u_1+u_2+\cdots+u_{n_1} = v_1$

$u_{n_1+1}+u_{n_1+2}+\cdots+u_{n_2} = v_2$

$u_{n_{k-1}+1}+u_{n_{k-1}+2}+\cdots+u_{n_k} = v_k$，$\cdots$，$\sum_{k=1}^{\infty} v_k$

下面证明 $\sum_{k=1}^{\infty} v_k = S$。由 $v_k$ 的定义：

$v_1+v_2+\cdots+v_k = u_1+u_2+\cdots+u_{n_k} = S_{n_k}$

因为 $\lim_{n\to\infty} S_n = S$，所以 $\lim_{k\to\infty} S_{n_k} = S$ $\square$

---

#### 定理 1.1（柯西准则）
级数 $\sum u_n$ 收敛 $\iff$ 对任何 $\varepsilon > 0$，存在 $N > 0$，当 $m > n > N$ 时，$\left|\sum_{k=n+1}^{m} u_k\right| = |S_m - S_n| < \varepsilon$

---

#### 例3：讨论调和级数 $\sum_{n=1}^{\infty} \frac{1}{n}$ 的敛散性

**方法一：** 用欧拉常数。已知 $\lim_{n\to\infty} \left(1+\frac{1}{2}+\cdots+\frac{1}{n} - \ln n\right) = \gamma$

对充分大的 $n$，有 $S_n = 1+\frac{1}{2}+\cdots+\frac{1}{n} > \ln n + \gamma - \frac{\varepsilon}{2} = \ln n \to +\infty$

**方法二：** 取 $\varepsilon = \frac{1}{2}$，对任何正整数 $N$，取 $m = 2n$，$n > N$，

有 $\sum_{k=n+1}^{m} \frac{1}{k} > n \cdot \frac{1}{2n} = \frac{1}{2}$

由柯西准则，级数**发散** $\square$

---

#### 例4：$\sum_{n=1}^{\infty} \frac{1}{n^2}$ 收敛

**证明：** 因为 $\sum_{k=n+1}^{m} \frac{1}{k^2} < \sum_{k=n+1}^{m} \frac{1}{(k-1)k} = \sum_{k=n+1}^{m} \left(\frac{1}{k-1} - \frac{1}{k}\right) = \frac{1}{n} - \frac{1}{m} < \frac{1}{n}$

所以对任何 $\varepsilon > 0$，存在 $N > 0$，当 $m > n > N$ 时，$\frac{1}{n} < \varepsilon$

从而 $\sum_{k=n+1}^{m} \frac{1}{k^2} < \varepsilon$

因此，级数**收敛**

---

#### 例5：$\sum_{n=1}^{\infty} \frac{1}{n^p}$（$p > 0$）—— p-级数

**方法一：** $S_n = \sum_{k=1}^{n} \frac{1}{k^p}$ 关于 $n$ 严格增，则 $S_n$ 收敛 $\iff$ $S_n$ 有上界

- **① 当 $p \leq 1$ 时**：$S_n \geq \sum_{k=1}^{n} \frac{1}{k} \to +\infty$，**发散**
- **② 当 $p > 1$ 时**，下面证明：$S_n \leq C + \lambda S_n$，$C > 0$，$\lambda \in (0,1)$

  从而解出 $S_n \leq \frac{C}{1-\lambda}$

  因为 $S_{2n} = 1 + \frac{1}{2^p} + \frac{1}{3^p} + \cdots + \frac{1}{(2n-2)^p} + \frac{1}{(2n-1)^p} + \frac{1}{(2n)^p}$

  $< 1 + 2\left(\frac{1}{2^p} + \frac{1}{4^p} + \cdots + \frac{1}{(2n)^p}\right)$

  $= 1 + 2^{1-p}\left(1 + \frac{1}{2^p} + \cdots + \frac{1}{n^p}\right)$

  $= 1 + 2^{1-p} S_n$

  所以 $S_n < S_{2n} < 1 + 2^{1-p} S_n \Rightarrow S_n < \frac{1}{1-2^{1-p}}$

**方法二：** 因为 $\sum_{k=2}^{n} = \sum_{k=2}^{n} \int_{k-1}^{k} \frac{1}{k^p} dx < \sum_{k=2}^{n} \int_{k-1}^{k} \frac{1}{x^p} dx = \int_{1}^{n} \frac{1}{x^p} dx$

$\sum_{k=2}^{n} \frac{1}{k^p} = \sum_{k=2}^{n} \int_{k}^{k+1} \frac{1}{k^p} dx > \sum_{k=2}^{n} \int_{k}^{k+1} \frac{dx}{x^p} = \int_{2}^{n+1} \frac{dx}{x^p}$

所以 $\int_{2}^{n+1} \frac{dx}{x^p} < \sum_{k=2}^{n} \frac{1}{k^p} < \int_{1}^{n} \frac{dx}{x^p}$

由 $\int_{1}^{+\infty} \frac{dx}{x^p}$ 在 $p > 1$ 时收敛，$p \leq 1$ 时发散

知原级数在 $p > 1$ 时收敛，$p \leq 1$ 时发散

---

### 7.1.2 正项级数

$\sum u_n$，$u_n \geq 0$，部分和 $S_n$ 单增

#### 定理 1.2
正项级数 $\sum u_n$ 收敛 $\iff$ 部分和 $\{S_n\}$ 存在上界

---

## 一、比较判别法

#### 定理 1.3
设 $\sum u_n$ 与 $\sum v_n$ 都是正项级数，且 $u_n \leq v_n$

- 则 $\sum v_n$ 收敛 $\Rightarrow$ $\sum u_n$ 收敛
- $\sum u_n$ 发散 $\Rightarrow$ $\sum v_n$ 发散

**常用比较级数：** $\sum q^n$，$\sum \frac{1}{n^p}$

---

#### 例6
**(1)** $\sum_{n=1}^{\infty} \frac{1}{n^2-n+1}$  
**(2)** $\sum_{n=1}^{\infty} \frac{n}{2^n}$

**(1)** 当 $n \geq 2$ 时，$n^2-n+1 > (n-1)^2$，$\frac{1}{n^2-n+1} < \frac{1}{(n-1)^2}$

$\sum_{n=2}^{\infty} \frac{1}{(n-1)^2}$ 收敛，原级数**收敛**

**(2) 方法一：** 因为 $\lim_{n\to\infty} \frac{n}{(\sqrt{2})^n} = 0$，所以当 $n$ 充分大时，

$\frac{n}{2^n} = \frac{n}{(\sqrt{2})^n} \cdot \frac{1}{(\sqrt{2})^n} < \left(\frac{1}{\sqrt{2}}\right)^n$

由 $\sum \left(\frac{1}{\sqrt{2}}\right)^n$ 收敛，知原级数**收敛**

**方法二：** 当 $n \geq 4$ 时，$2^n = (1+1)^n > C_n^3 = \frac{n(n-1)(n-2)}{6} > \frac{n^3}{24}$

$\frac{n}{2^n} < \frac{24}{n^2}$，因为 $\sum \frac{1}{n^2}$ 收敛，所以原级数**收敛**

---

#### 定理 1.4（比较判别法的极限形式）
设 $\sum u_n$ 与 $\sum v_n$ 为正项级数，$v_n > 0$，且 $\lim_{n\to\infty} \frac{u_n}{v_n} = l$

- **(i)** 当 $0 < l < +\infty$ 时，$\sum u_n$ 与 $\sum v_n$ 同敛散（$u_n \sim l \cdot v_n$，同阶）
- **(ii)** 当 $l = 0$ 时，$\sum v_n$ 收敛 $\Rightarrow$ $\sum u_n$ 收敛（$u_n = o(v_n)$，高阶）
- **(iii)** 当 $l = +\infty$ 时，$\sum u_n$ 发散 $\Rightarrow$ $\sum v_n$ 发散

**证明：**
**(i)** 由定义，对任何 $\varepsilon > 0$，存在 $N > 0$，当 $n > N$ 时，$\left|\frac{u_n}{v_n} - l\right| < \varepsilon$，$l-\varepsilon < \frac{u_n}{v_n} < l+\varepsilon$

取 $\varepsilon = \frac{l}{2}$，有 $\frac{l}{2} \cdot v_n < u_n < \frac{3}{2} l \cdot v_n$

由比较判别法，结论 $\checkmark$

**(ii)** 此时，$u_n < \varepsilon \cdot v_n$，由比较判别法 $\checkmark$

**(iii)** $n > N$ 时，$\frac{u_n}{v_n} > 1$，$u_n > v_n$，由比较 $\cdots$

---

#### 例7：$\sum_{n=1}^{\infty} \sin\frac{1}{n}$

**解：** 当 $n \to \infty$ 时，$\sin\frac{1}{n} \sim \frac{1}{n}$，$\sum \frac{1}{n}$ 发散，**发散**

---

#### 例8：$\sum_{n=1}^{\infty} \frac{1}{2^n-n}$

**方法一：** 因为 $\lim_{n\to\infty} \frac{\frac{1}{2^n-n}}{\frac{1}{2^n}} = \lim_{n\to\infty} \frac{2^n}{2^n-n} = 1$

$\sum \frac{1}{2^n}$ 收敛，原级数**收敛**

**方法二：** 因为 $\lim_{n\to\infty} \frac{n}{2^n} = 0$，所以当 $n$ 充分大时，$2^{n-1} > n$

从而 $\frac{1}{2^n-n} < \frac{1}{2^{n-1}}$，$\sum \frac{1}{2^{n-1}}$ 收敛，原级数**收敛**

---

#### 例9：$\sum_{n=1}^{\infty} \left(e - \left(1+\frac{1}{n}\right)^n\right)$

**解：** $u_n = e - e^{n\ln(1+\frac{1}{n})} = \left(1+\frac{1}{n}\right)^n \left[e^{1-n\ln(1+\frac{1}{n})} - 1\right]$

$\sim e \cdot \left[1 - n\ln\left(1+\frac{1}{n}\right)\right]$

$= e \cdot \left[1 - n\left(\frac{1}{n} - \frac{1}{2n^2} + o\left(\frac{1}{n^2}\right)\right)\right]$

$= e \cdot \left[\frac{1}{2n} + o\left(\frac{1}{n^2}\right)\right] \sim \frac{e}{2n}$

$\sum \frac{1}{n}$ 发散，原**发散**

**注：** 在比较判别法中以 p 级数 $\sum \frac{1}{n^p}$ 为比较级数

---

### 推论1（柯西判别法）
设 $\sum u_n$ 为正项级数

- **(i)** 若存在常数 $p > 1$，$\lambda > 0$，使 $n^p \cdot u_n \leq \lambda$，则 $\sum u_n$ **收敛**
- **(ii)** 若存在 $\lambda > 0$ s.t. $n \cdot u_n \geq \lambda$，则 $\sum u_n$ **发散**

### 推论2（柯西判别法的极限形式）
设 $\sum u_n$ 为正项级数，且 $\lim_{n\to\infty} n^p \cdot u_n = \lambda$

- **(i)** 当 $p > 1$ 且 $0 \leq \lambda < +\infty$ 时，$\sum u_n$ **收敛**
- **(ii)** 当 $p \leq 1$ 且 $0 < \lambda \leq +\infty$ 时，$\sum u_n$ **发散**

### 推论3（比值比较判别法）
设 $\sum u_n$，$\sum v_n$ 都是正项级数，且存在正整数 $N$，当 $n > N$ 时，$\frac{u_{n+1}}{u_n} \leq \frac{v_{n+1}}{v_n}$

- 则 $\sum v_n$ 收敛 $\Rightarrow$ $\sum u_n$ 收敛
- $\sum u_n$ 发散 $\Rightarrow$ $\sum v_n$ 发散

**证明：** 当 $n > N$ 时，因为

$$\frac{u_n}{u_{n+1}} = \frac{u_n}{u_{n-1}} \cdot \frac{u_{n-1}}{u_{n-2}} \cdots \frac{u_{N+2}}{u_{N+1}}$$

$$\leq \frac{v_n}{v_{n-1}} \cdot \frac{v_{n-1}}{v_{n-2}} \cdots \frac{v_{N+2}}{v_{N+1}} = \frac{v_n}{v_{N+1}} \cdot \frac{u_n}{u_{N+1}} \leq \frac{v_n}{v_{N+1}}$$

由比较 $\checkmark$ $\square$

---

## 二、积分判别法 $\Leftarrow \sum \frac{1}{n^p}$

#### 定理 1.5
设 $f(x)$ 定义在 $[a, +\infty)$ 上，非负，且在任何有限区间 $[a, A]$ 上可积，任取严格增且趋于 $+\infty$ 的数列 $\{a_n\}$（$a_1 = a$），令 $u_n = \int_{a_n}^{a_{n+1}} f(x) dx$

则正项级数 $\sum u_n$ 与 $\int_{a}^{+\infty} f(x) dx$ 同时收敛或同时发散于 $+\infty$

且 $\sum_{n=1}^{\infty} u_n = \int_{a}^{+\infty} f(x) dx$

**特别地**，当 $f(x)$ 单减时，$\sum_{n=[a]+1}^{\infty} f(n)$ 与 $\int_{a}^{+\infty} f(x)$ 同敛散

**证明：** $\sum u_n$ 部分和 $S_n = \int_{a}^{a_{n+1}} f(x) dx$

依 $\{a_n\}$ 的选取，有 $[a, +\infty) = \bigcup_{n=1}^{\infty} [a_n, a_{n+1})$

对 $\forall A > a$，存在 $n \in \mathbb{N}^+$ 使 $a_n \leq A < a_{n+1}$，于是

$S_{n-1} \leq \int_{a}^{A} f(x) dx \leq S_n$

当 $\{S_n\}$ 有界时，$\sum u_n$ 收敛，由迫敛性 $\int_{a}^{+\infty} f(x) dx = \sum_{n=1}^{\infty} u_n$

当 $\{S_n\}$ 无界时，$\sum u_n = +\infty$，由迫敛性 $\int_{a}^{+\infty} f(x) dx = +\infty$

**特别地**，当 $f(x)$ 单减时，取 $a_n = n$，则 $n \geq \max\{a, 1\}$ 时，

$f(n+1) \leq u_n = \int_{n}^{n+1} f(x) dx \leq f(n)$

由比较 $\sum f(n)$ 与 $\sum u_n$ 同敛散，从而与 $\int_{a}^{+\infty} f(x) dx$ 同敛散

---

#### 例10：$\sum_{n=1}^{\infty} \frac{1}{n^p}$

因为 $f(x) = \frac{1}{x^p}$ 在 $[1, +\infty)$ 上非负、严格减，又因为在 $p > 1$ 时收敛，$0 < p \leq 1$ 时发散

所以 $\sum \frac{1}{n^p}$ 在 $p > 1$ 时收敛，$0 < p \leq 1$ 时发散

---

## 三、比式判别法

#### 定理 1.6
设 $\sum u_n$ 为正项级数，存在正整数 $N$ 以及常数 $d$，当 $n > N$ 时，有：

- **(i)** $\frac{u_{n+1}}{u_n} \leq d < 1$，则 $\sum u_n$ **收敛**
- **(ii)** $\frac{u_{n+1}}{u_n} \geq 1$，则 $\sum u_n$ **发散**

**注：** 在比值比较判别法中取 $v_n = d^n$

### 推论（比式判别法的极限形式）
$\lim_{n\to\infty} \frac{u_{n+1}}{u_n} = d$

- **(i)** 当 $0 \leq d < 1$ 时，$\sum u_n$ **收敛**
- **(ii)** 当 $d > 1$ 时，$\sum u_n$ **发散**

**证明：** $0$，$\exists N_0$，$n > N$，$\frac{u_{n+1}}{u_n} < d+\varepsilon$

若 $0 \leq d < 1$，取 $\varepsilon \in (0, 1-d)$，$d+\varepsilon < 1$

由比较 $\cdots$ 收敛

若 $1 < d < +\infty$，则 $\cdots$，$\varepsilon$ **发散**

**注：** 若 $d = +\infty$，则 $n > N$ 时，$\frac{u_{n+1}}{u_n} > 1$，$\sum u_n$ **发散** $\square$

**注：** 当 $d = 1$ 时，一般无法判定，例如 p 级数 $\sum \frac{1}{n^p}$

---

#### 例12：$\sum_{n=1}^{\infty} \frac{a^n}{n!}$，其中常数 $a > 0$

**解：** $\lim_{n\to\infty} \frac{u_{n+1}}{u_n} = \lim_{n\to\infty} \frac{a}{n+1} = 0$

比式，级数**收敛**

---

#### 例13：$\sum_{n=1}^{\infty} \frac{n!}{n^n}$

**解：** $\lim_{n\to\infty} \frac{u_{n+1}}{u_n} = \lim_{n\to\infty} \frac{(n+1)!}{(n+1)^{n+1}} \cdot \frac{n^n}{n!} = \lim_{n\to\infty} \frac{1}{(1+\frac{1}{n})^n} = \frac{1}{e} < 1$

由比式 method，级数**收敛**

---

## 四、根式判别法

#### 定理 1.7
设 $\sum u_n$ 为正项级数，且存在正整数 $N$ 与常数 $c > 0$，当 $n > N$ 时：

- **(i)** 若 $\sqrt[n]{u_n} \leq c < 1$，则 $\sum u_n$ **收敛**（$u_n < c^n$）
- **(ii)** 若 $\sqrt[n]{u_n} \geq 1$，则 $\sum u_n$ **发散**

### 推论（根式判别法的极限形式）
因为 $f \downarrow$，所以 $\cdots$

$\sum u_n$ 在 $c < 1$ 时收敛，$c > 1$ 时发散

**注：** 当 $c = 1$ 时，一般无法判定

---

#### 例14：$\sum_{n=1}^{\infty} \frac{1}{2^{n+(-1)^n}}$

**解：** 因为 $\lim_{n\to\infty} \sqrt[n]{u_n} = \lim_{n\to\infty} \frac{1}{2} \sqrt[n]{2+(-1)^n} = \frac{1}{2} < 1$

所以级数**收敛**

（因为 $1 \leq 2+(-1)^n \leq 3$，$1 \leq \sqrt[n]{2+(-1)^n} \leq \sqrt[n]{3} \to 1$）

**注：** $\sqrt[n]{u_n} = \left(\frac{u_n}{u_{n-1}} \cdot \frac{u_{n-1}}{u_{n-2}} \cdots \frac{u_2}{u_1} \cdot u_1\right)^{\frac{1}{n}}$

$\lim_{n\to\infty} \frac{u_{n+1}}{u_n} = d \Rightarrow \lim_{n\to\infty} \sqrt[n]{u_n} = d$

**根式判别法 $\geq$ 比式判别法**

---

## 五、其他判别法

### 1. 在比较判别法中

- **①** $u_n \leq \frac{1}{n^p} \iff \ln u_n \leq -p\ln n \iff \frac{-\ln u_n}{\ln n} \geq p$
- **②** $u_n \geq \frac{1}{n} \iff \ln u_n \geq -\ln n \iff \frac{-\ln u_n}{\ln n} \leq 1$

#### 对数判别法
设正项级数 $\sum u_n$ 满足 $n \geq N$ 时：

- **(i)** $\frac{-\ln u_n}{\ln n} \geq$ 常数 $p > 1$，则 $\sum u_n$ **收敛**
- **(ii)** $\frac{-\ln u_n}{\ln n} \leq 1$，则 $\sum u_n$ **发散**

#### 对数判别法的极限形式
设正项级数 $\sum u_n$ 满足 $\lim_{n\to\infty} \frac{-\ln u_n}{\ln n} = p$

则 $\sum u_n$ 在 $p > 1$ 时收敛，$p < 1$ 时发散

---

#### 例15
**(1)** $\sum_{n=2}^{\infty} \frac{1}{n(\ln n)^p}$（$p > 0$）

因为 $\lim_{n\to\infty} \frac{-\ln u_n}{\ln n} = \lim_{n\to\infty} \frac{\ln(n(\ln n)^p)}{\ln n} = \lim_{n\to\infty} \frac{\ln n + p\ln\ln n}{\ln n} = 1$

当 $p \geq 1$ 时，$\lambda = 0$ **发散**

$0 < p < 1$ 时，$\lambda = +\infty$ **收敛**

---

### 2. 在比式判别法中

设 $= d + o(1)$

当 $d = 1$ 时，比式判别法失效，需 $o(1)$ 更精确的信息

例如：$\frac{a_n}{n+1} = \left(1+\frac{1}{n}\right)^p = 1 + \frac{p}{n} + o\left(\frac{1}{n^2}\right)$

$= (1+\frac{1}{n})^p = 1 + \frac{p}{n} + o\left(\frac{1}{n}\right)$

$\frac{a_{n+1}}{a_n} = 1 - \frac{p}{n} + o\left(\frac{1}{n^2}\right)$

一般地，$= 1 + o\left(\frac{1}{n}\right)$（$n \to \infty$）

---

### 拉贝判别法
设 $\sum u_n$ 为正项级数，且存在 $N_0$ 以及 $\cdots$

当 $n > N$ 时：

- **(i)** $n\left(1 - \frac{u_{n+1}}{u_n}\right) \geq p > 1$ 时，$\sum u_n$ **收敛**
- **(ii)** $n\left(1 - \frac{u_{n+1}}{u_n}\right) \leq 1$ 时，$\sum u_n$ **发散**

**证明：**

**(i)** 取 $p > q > 1$，令 $v_n = \frac{1}{n^q}$

因为 $q > 0$，所以 $\frac{v_{n+1}}{v_n} = \left(1+\frac{1}{n}\right)^{-q} = 1 - \frac{q}{n} + o\left(\frac{1}{n^2}\right)$

又因为 $\sum v_n$ 收敛，所以由比值比较判别法

$\frac{u_{n+1}}{u_n} \leq \frac{v_{n+1}}{v_n}$，$\sum u_n$ **收敛**

**(ii)** 取 $n = \cdots$，因为 $v_n$ 发散，$\cdots$，$\sum u_n$ **发散**

---

### 拉贝判别法的极限形式
设 $\sum u_n$ 为正项级数，且

$$\lim_{n\to\infty} n\left(1 - \frac{u_{n+1}}{u_n}\right) = r$$

则 $\sum u_n$ 在 $r > 1$ 时收敛，$r < 1$ 时发散

**注：** 当 $r = 1$ 时，无法判定

---

#### 例
$$\frac{n+1}{n} = 1 - \frac{1}{n} - \frac{p}{n\ln n} + o\left(\frac{1}{n^2}\right)$$

$n\ln n$

---

## 欧拉求和公式

设 $f(x)$ 在 $[a, +\infty)$（$a > 0$）上非负、单减有界

则对每个正整数 $N > a$，都有

$$\sum_{k=[a]+1}^{N} f(k) = \int_{a}^{N} f(x) dx + O(1)$$

**证明：** $\sum f(k) - \int f(x) dx = \cdots$

因为 $f \downarrow$，所以 $\cdots$

$\sum_{k=2}^{N} f(k) - \int_{1}^{N} f(x) dx = O(1)$

---
