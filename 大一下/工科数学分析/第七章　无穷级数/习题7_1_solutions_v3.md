
# 工科数学分析基础（下册·第三版，马知恩/王绵森）—— 习题 7.1 解答

> 范围：习题 7.1（pp. 285–289）  
> 题号：(A) 组：3、8、12、14、15、16、18；(B) 组：3、4  
> 说明：第 16、18 题的题面已根据补充资料补全。

---

## 0. 做题技巧速查（应试必备）

7.1 习题考察的全部是**判别级数敛散性**或**用敛散性求和**。下面 7 条是题目里**反复出现**的核心套路。

### 选判别法的总原则

**第一步永远是看 $a_n\to 0$**——否则直接发散。然后按下表对号入座：

| 看到什么                                          | 用什么方法                               | 对应题号                                |
| --------------------------------------------- | ----------------------------------- | ----------------------------------- |
| 几何级数 / 裂项 / 望远镜                               | **定义法**（直接算部分和）                     | A3(1)(2)(3)(4)                      |
| 通项含 $\sin,\cos,\tan,\ln(1+\cdot),e^{\cdot}-1$ | **等价无穷小** + 比阶到 $1/n^p$             | A8(2)(4)、A12(8)(9)(10)、A14(4)(6)    |
| 通项含 $n!,a^n$、组合数                              | **检比法**                             | A12(5)(11)、A14(1)、A16(1)            |
| 整体 $n$ 次方 $(\cdots)^n$                        | **检根法**                             | A12(13)                             |
| 多项式有理式 $\sim 1/n^p$                           | **比较法 II（比阶）**                      | A12(2)(3)(4)(7)、A14(2)(5)           |
| 交错级数 $(-1)^{n-1}a_n$，$a_n\downarrow 0$        | **Leibniz 准则**                      | A14(2)(3)(4)(6)、A15(3)(4)、A18(3)(4) |
| 变号、含绝对值约束 $\|a_n\|\le b_n$，$\sum b_n$ 收敛      | **绝对收敛准则**                          | A18(1)(2)                           |
| 求和精度要求 $\|R_n\|<\varepsilon$                  | **Leibniz 余项 $\|R_n\|\le a_{n+1}$** | A17                                 |
| 含未知函数 / 待定参数                                  | **Taylor 展开 + 比阶**                  | B3、B4                               |

---

### 技巧一：用定义直接算部分和（基础题）

**适用**：几何级数、裂项级数、望远镜级数。

**三种凑法**：
1. **几何级数**：识别 $\sum aq^n$，$\|q\|<1$ 收敛于 $\dfrac{a}{1-q}$。
2. **部分分式**：$\dfrac{1}{(an+b)(an+c)}=\dfrac{1}{c-b}\Bigl(\dfrac{1}{an+b}-\dfrac{1}{an+c}\Bigr)$。
3. **望远镜**：$a_n=b_{n+1}-b_n$ 或 $a_n=b_{n+1}-2b_n+b_{n-1}$（A3(3) 二阶差分）。

**应试要点**：把 $S_N$ 写成"裂项相加 → 中间消掉 → 只剩头尾"的形式。

**对应题目**：A3(1)~(4)。

---

### 技巧二：必要条件秒杀（$a_n\not\to 0\Rightarrow$ 发散）

很多题**看似复杂，其实通项不趋于 0**，直接发散。

**常用极限**：
- $(1+\tfrac{1}{n})^n\to e$（A8(1)）
- $2^n\sin\dfrac{\pi}{2^n}\to\pi$（A8(2)）
- $n^2\ln(1+\tfrac{x}{n^2})\to x$（A8(4)）
- $\sqrt n\cot\dfrac{1}{n}\sim\sqrt n\cdot n\to\infty$（A12(12)）
- $\sqrt n/(1+1/n)^n\sim\sqrt n/e\to\infty$

> **应试套路**：拿到题先**算极限 $\lim a_n$**，是 $\ne 0$ 立判发散，不用继续分析。

**对应题目**：A8(1)(2)(4)、A12(12)、A15(1)。

---

### 技巧三：等价无穷小 + 比阶到 $\sum 1/n^p$

**核心**：把 $a_n$ 写成 $a_n\sim\dfrac{c}{n^p}$，立判：$p>1$ 收敛、$p\le 1$ 发散。

**七大常用等价无穷小**（$t=t_n\to 0$ 时）：
| 函数 | 等价 |
|---|---|
| $\sin t$ | $t$ |
| $\tan t$ | $t$ |
| $1-\cos t$ | $\tfrac{t^2}{2}$ |
| $\ln(1+t)$ | $t$ |
| $e^t-1$ | $t$ |
| $(1+t)^\alpha-1$ | $\alpha t$ |
| $\sqrt[n]{a}-1=e^{\ln a/n}-1$ | $\tfrac{\ln a}{n}$ |

**比阶速查例**：

| 通项 | 化简后 | 结论 |
|---|---|---|
| $\sin\dfrac{\pi}{3^n}\cdot n$ | $\sim\dfrac{n\pi}{3^n}$（几何主导） | 收敛 |
| $1-\cos\dfrac{\pi}{n}$ | $\sim\dfrac{\pi^2}{2n^2}$ | 收敛 |
| $n\ln(1+\dfrac{2}{n^3})$ | $\sim\dfrac{2}{n^2}$ | 收敛 |
| $\sqrt[n]{a}-1$ | $\sim\dfrac{\ln a}{n}$ | 发散 |
| $\dfrac{\sqrt{n+2}-\sqrt{n-2}}{n^\alpha}$ | $\sim\dfrac{2}{n^{\alpha+1/2}}$ | $\alpha>\tfrac12$ 收敛 |

> **应试要诀**：分子分母同阶 → 算 $p$；不同阶 → 直接舍小项保大项。

**对应题目**：A8(2)、A12(2)(3)(4)(7)(8)(9)(10)、A14(4)(6)、A15(2)。

---

### 技巧四：检比法 / 检根法

**检比法**：$a_n>0$，$\lim\dfrac{a_{n+1}}{a_n}=\lambda$。$\lambda<1$ 收敛、$\lambda>1$ 发散、$\lambda=1$ 失效。

**检根法**：$\lim\sqrt[n]{a_n}=\lambda$，结论同上。

**选哪个的信号**：
- 通项含 **$n!,\,a^n$、组合数、双阶乘** → 检比法（约分容易）；
- 通项是 **整体 $n$ 次方 $(\cdots)^n$** → 检根法（开方易得极限）；
- 通项 $\sim$ 几何级数 $r^n$ → 两者都行。

**含参数题的标准套路**：写出 $\lim\dfrac{a_{n+1}}{a_n}=g(x)$，分别讨论 $g(x)<1,\,>1,\,=1$ 三种情况（如 A12(11) $x/e$、A14(6) $\|x\|$）。

> ⚠ **$\lambda=1$ 时检比/检根失效**——这时回到比阶或更精细的判别法（Raabe / 对数法）。

**对应题目**：A12(5)(10)(11)(13)、A14(1)(6)、A16(1)、A18(2)。

---

### 技巧五：交错级数 + Leibniz 准则

**Leibniz 三件套**：交错级数 $\sum(-1)^{n-1}a_n$（$a_n>0$）若
1. $a_n$ 单调减；
2. $a_n\to 0$

则**收敛**，且**余项 $\|S-S_n\|\le a_{n+1}$**。

**判断单调减的三种方法**：
1. **直接比较** $a_n,a_{n+1}$（最朴素）；
2. **取导**：把 $a_n$ 看成 $f(n)$，$f'(x)<0$（A14(3)：$f(x)=x-\ln x$ 单增 ⇒ $1/(n-\ln n)$ 单减）；
3. **分析增减**：$\ln(2+1/n)$ 单减 + $\sqrt{9n^2-4}$ 单增 ⇒ 商单减（A15(4)、A18(4)）。

**条件收敛 vs 绝对收敛**：
- $\sum\|a_n\|$ 收敛 ⇒ **绝对收敛**（如 A14(1)(5)、A18(1)(2)）；
- $\sum\|a_n\|$ 发散 + Leibniz 收敛 ⇒ **条件收敛**（如 A14(2)(3)(4)(6)$\|x\|=1$、A18(3)(4)）。

**对应题目**：A14(2)(3)(4)(6)、A15(3)(4)、A17、A18(3)(4)。

---

### 技巧六：含参数级数的标准讨论流程

题目形如 $\sum a_n(x)$，要求**对所有 $x$ 讨论敛散性**。

**通用 4 步走**：

1. **写出 $\|a_n(x)\|$ 的等价**（通常带 $\|x\|$）；
2. **检比法**算 $\lim\dfrac{\|a_{n+1}\|}{\|a_n\|}=g(\|x\|)$；
3. **分三段讨论**：
   - $g(\|x\|)<1$：绝对收敛；
   - $g(\|x\|)>1$：通项 $\not\to 0$，发散；
   - $g(\|x\|)=1$（临界）：检比法失效，**回到原级数代入边界值**单独算。
4. **临界点细分**：分别看 $x=$ 正边界、负边界，是否满足 Leibniz。

**典型**：A14(6) $\sum x^n\tan\tfrac{1}{\sqrt n}$
- $\|x\|<1$ 绝对收敛；$\|x\|>1$ 发散；
- $x=1$：$\sim\sum 1/\sqrt n$ 发散；
- $x=-1$：交错且 $\tan(1/\sqrt n)\downarrow 0$，Leibniz 收敛 ⇒ 条件收敛。

**对应题目**：A12(11)(14)、A14(6)、A16(1)。

---

### 技巧七：Taylor 展开 + 比阶（处理含 $f$、$f'$、$f''$ 的抽象题）

B 组常见题型：已知 $f$ 在 $0$ 附近的极限信息，判别 $\sum f(\tfrac{1}{n})$ 的敛散性。

**标准思路**：
1. 用题目条件**确定 $f(0)=0, f'(0)=0$ 等**；
2. 在 $0$ 处作 **Taylor 展开**到合适阶：
   $$f(x)=f(0)+f'(0)x+\tfrac{f''(0)}{2}x^2+o(x^2);$$
3. 代入 $x=\tfrac{1}{n}$，看主项阶数；
4. 与 $\sum 1/n^p$ 比阶。

**典型**：B3 $\lim_{x\to 0}f(x)/x=0$ + $f$ 有二阶连续导数 ⇒ $f(0)=0, f'(0)=0$ ⇒ $f(\tfrac{1}{n})=O(1/n^2)$ ⇒ **绝对收敛**。

**对应题目**：B3、B4。

---

### 应试速查总流程

```
拿到级数 ∑a_n
   ↓
① 算 lim a_n → ≠0 直接发散；=0 继续
   ↓
② 看通项类型：
   ├─ 望远镜/几何/裂项     → 定义法直接算部分和
   ├─ 含 sin,cos,ln(1+·)等 → 等价无穷小 + 比阶
   ├─ 含 n!,a^n,组合数     → 检比法
   ├─ 整体 (…)^n           → 检根法
   ├─ 多项式 ~ 1/n^p       → 比较法 II
   ├─ 交错 (-1)^{n-1}a_n   → 先看 ∑|a_n| 绝对收敛？否则 Leibniz
   ├─ 含参数 x             → 检比 + 三段讨论 + 临界点细分
   └─ 含抽象 f             → Taylor 展开 + 比阶
```

---


## (A) 3. 用级数收敛的定义判别敛散性，并对收敛级数求其和

### (1) $\displaystyle\sum_{n=0}^{\infty}\frac{3^n+1}{q^n}\;(|q|>3)$

将级数拆开：
$$\sum_{n=0}^{\infty}\frac{3^n+1}{q^n}=\sum_{n=0}^{\infty}\left(\frac{3}{q}\right)^{n}+\sum_{n=0}^{\infty}\left(\frac{1}{q}\right)^{n}.$$
因 $|q|>3$，故 $|3/q|<1$ 且 $|1/q|<1$，两几何级数均收敛。
$$S=\frac{1}{1-3/q}+\frac{1}{1-1/q}=\frac{q}{q-3}+\frac{q}{q-1}.$$

**结论：收敛，和为 $\dfrac{q}{q-3}+\dfrac{q}{q-1}$.**

### (2) $\displaystyle\sum_{n=0}^{\infty}\frac{1}{(3n+1)(3n+4)}$

部分分式：$\dfrac{1}{(3n+1)(3n+4)}=\dfrac{1}{3}\!\left(\dfrac{1}{3n+1}-\dfrac{1}{3n+4}\right)$.

裂项求和：
$$S_N=\frac{1}{3}\sum_{n=0}^{N}\left(\frac{1}{3n+1}-\frac{1}{3n+4}\right)=\frac{1}{3}\left(1-\frac{1}{3N+4}\right)\to\frac{1}{3}.$$

**结论：收敛，和为 $\dfrac{1}{3}$.**

### (3) $\displaystyle\sum_{n=1}^{\infty}\left(\sqrt{n+2}-2\sqrt{n+1}+\sqrt{n}\right)$

记 $b_n=\sqrt{n+1}-\sqrt{n}$，则通项 $a_n=b_{n+1}-b_n$。于是
$$S_N=\sum_{n=1}^{N}(b_{n+1}-b_n)=b_{N+1}-b_1=\big(\sqrt{N+2}-\sqrt{N+1}\big)-(\sqrt{2}-1).$$
当 $N\to\infty$，$\sqrt{N+2}-\sqrt{N+1}=\dfrac{1}{\sqrt{N+2}+\sqrt{N+1}}\to 0$。故
$$S_N\to 1-\sqrt{2}.$$

**结论：收敛，和为 $1-\sqrt{2}$.**

### (4) $\displaystyle\sum_{n=1}^{\infty}\ln\frac{n}{n+1}$

$\ln\dfrac{n}{n+1}=\ln n-\ln(n+1)$，故
$$S_N=\sum_{n=1}^{N}[\ln n-\ln(n+1)]=-\ln(N+1)\to-\infty.$$

**结论：发散.**

---

## (A) 8. 利用级数的性质判别敛散性

### (1) $\displaystyle\sum_{n=1}^{\infty}\dfrac{\sqrt n}{(1+1/n)^n}$

$(1+1/n)^n\to e$，故 $a_n\sim\dfrac{\sqrt n}{e}\to+\infty$，通项不趋于 0。**发散.**

### (2) $\displaystyle\sum_{n=1}^{\infty}2^n\sin\dfrac{\pi}{2^n}$

由 $\sin x\sim x\,(x\to 0)$：$a_n=2^n\sin(\pi/2^n)\to\pi\neq 0$。**发散.**

### (3) $\displaystyle\sum_{n=1}^{\infty}\!\left(\dfrac{1}{n}-\dfrac{1}{2^n}\right)$

$\sum 1/n$ 发散（调和），$\sum 1/2^n$ 收敛。**收敛级数与发散级数之差仍发散**。**发散.**

### (4) $\displaystyle\sum_{n=1}^{\infty}n^2\ln\!\left(1+\dfrac{x}{n^2}\right)\;(x\in\mathbb R)$

由 $\ln(1+t)=t-\dfrac{t^2}{2}+O(t^3)$：
$$n^2\ln\!\left(1+\frac{x}{n^2}\right)=x-\frac{x^2}{2n^2}+O\!\left(\frac1{n^4}\right)\to x.$$
- 当 $x\neq 0$：通项不趋于 0，**发散**；
- 当 $x=0$：每项为 0，**收敛，和为 0**。

---

## (A) 12. 判别下列正项级数的敛散性

### (1) $\displaystyle\sum\dfrac{1}{3^n+2}$
$\dfrac{1}{3^n+2}<\dfrac{1}{3^n}$，由比较判别法，**收敛**。

### (2) $\displaystyle\sum\dfrac{n^{n+1}}{(n+1)^{n+2}}$
$a_n=\dfrac{1}{n+1}\cdot\dfrac{1}{(1+1/n)^{n+1}}\sim\dfrac{1}{e\,n}$，与调和级数同阶，**发散**。

### (3) $\displaystyle\sum\dfrac{\sqrt{n+2}-\sqrt{n-2}}{n^{\alpha}}$
$\sqrt{n+2}-\sqrt{n-2}=\dfrac{4}{\sqrt{n+2}+\sqrt{n-2}}\sim\dfrac{2}{\sqrt n}$，
所以 $a_n\sim\dfrac{2}{n^{\alpha+1/2}}$.

**当 $\alpha>1/2$ 时收敛，$\alpha\le 1/2$ 时发散**。

### (4) $\displaystyle\sum\dfrac{\sqrt n}{n^2-\ln n}$
$a_n\sim\dfrac{1}{n^{3/2}}$，**收敛**。

### (5) $\displaystyle\sum\dfrac{2^n n^2}{n!}$
$\dfrac{a_{n+1}}{a_n}=\dfrac{2(n+1)^2}{n^2(n+1)}=\dfrac{2(n+1)}{n^2}\to 0<1$，由比值判别法，**收敛**。

### (6) $\displaystyle\sum\dfrac{n^3\bigl[\sqrt 2+(-1)^n\bigr]}{3^n}$
$0\le a_n\le\dfrac{(\sqrt 2+1)n^3}{3^n}$，而 $\sum n^3/3^n$ 由比值法收敛，故**收敛**。

### (7) $\displaystyle\sum_{n=0}^{\infty}\dfrac{1}{\sqrt{n^2+1}}$
$a_n\sim 1/n$，**发散**。

### (8) $\displaystyle\sum\left(1-\cos\dfrac{\pi}{n}\right)$
$1-\cos(\pi/n)\sim\dfrac{\pi^2}{2n^2}$，**收敛**。

### (9) $\displaystyle\sum n\ln\!\left(1+\dfrac{2}{n^3}\right)$
$\ln(1+2/n^3)\sim 2/n^3$，故 $a_n\sim 2/n^2$，**收敛**。

### (10) $\displaystyle\sum n\sin\dfrac{\pi}{3^n}$
$\sin(\pi/3^n)\sim\pi/3^n$，$a_n\sim n\pi/3^n$，由比值法 $\dfrac{a_{n+1}}{a_n}\to\dfrac13<1$，**收敛**。

### (11) $\displaystyle\sum n!\left(\dfrac{x}{n}\right)^n\;(x>0)$
$$\frac{a_{n+1}}{a_n}=\frac{x}{(1+1/n)^n}\to\frac{x}{e}.$$
- $0<x<e$：**收敛**；
- $x>e$：**发散**；
- $x=e$：由 Stirling 公式 $n!\sim\sqrt{2\pi n}\,(n/e)^n$，得 $a_n=n!(e/n)^n\sim\sqrt{2\pi n}\to\infty$，**发散**。

### (12) $\displaystyle\sum\dfrac{1}{\sqrt n}\cot\dfrac{1}{n}$
$\cot(1/n)=\dfrac{\cos(1/n)}{\sin(1/n)}\sim n$ ($n\to\infty$)，故 $a_n\sim\sqrt n\to+\infty$，通项不趋于 0。**发散**。

> 注：若题目原意为 $\dfrac{1}{\sqrt n\,\cot(1/n)}$ 或 $\dfrac{1}{\sqrt n}\tan\dfrac{1}{n}$，则 $a_n\sim 1/n^{3/2}$，**收敛**。OCR 不清，请核对原书。

### (13) $\displaystyle\sum\left(2n\tan\dfrac{1}{n}\right)^{n/3}$
$n\tan(1/n)\to 1$，故 $2n\tan(1/n)\to 2$。
$$\sqrt[n]{a_n}=\bigl(2n\tan(1/n)\bigr)^{1/3}\to 2^{1/3}>1.$$
由根值判别法，**发散**。

### (14) $\displaystyle\sum\dfrac{\alpha^n}{1+\alpha^{2n}}\;(\alpha>0)$
- $\alpha=1$：$a_n=\tfrac12$，**发散**；
- $0<\alpha<1$：$a_n\le\alpha^n$，**收敛**；
- $\alpha>1$：$a_n\le\alpha^n/\alpha^{2n}=(1/\alpha)^n$，**收敛**。

**综上：$\alpha\neq 1$ 时收敛，$\alpha=1$ 时发散.**

---

## (A) 14. 判别敛散性，对收敛级数说明绝对收敛或条件收敛

### (1) $\displaystyle\sum(-1)^n\dfrac{1\cdot 3\cdots(2n-1)}{3^n\,n!}$
设 $|a_n|=\dfrac{(2n-1)!!}{3^n\,n!}$，
$$\frac{|a_{n+1}|}{|a_n|}=\frac{2n+1}{3(n+1)}\to\frac{2}{3}<1.$$
由比值法 $\sum|a_n|$ 收敛。**绝对收敛**。

### (2) $\displaystyle\sum\dfrac{(-1)^{n-1}}{\sqrt{2n-1}}$
$|a_n|\sim 1/\sqrt{2n}$，$\sum|a_n|$ 发散；$|a_n|$ 递减且趋于 0，由 Leibniz 准则收敛。**条件收敛**。

### (3) $\displaystyle\sum(-1)^{n-1}\dfrac{1}{n-\ln n}$
$|a_n|\sim 1/n$，$\sum|a_n|$ 发散。
设 $f(x)=x-\ln x$，$f'(x)=1-1/x>0\;(x>1)$，故 $\{n-\ln n\}$ 单增，从而 $|a_n|$ 单减到 0，Leibniz 收敛。**条件收敛**。

### (4) $\displaystyle\sum(-1)^{n-1}(\sqrt[n]{a}-1)\;(a>0,\,a\neq 1)$
$\sqrt[n]{a}-1=e^{(\ln a)/n}-1\sim\dfrac{\ln a}{n}$，$\sum|a_n|$ 发散。
- 若 $a>1$：$\sqrt[n]{a}>1$ 单减到 1，故 $\sqrt[n]{a}-1$ 单减到 0；
- 若 $0<a<1$：$\sqrt[n]{a}<1$ 单增到 1，故 $|\sqrt[n]{a}-1|$ 单减到 0。

由 Leibniz 准则收敛。**条件收敛**。

### (5) $\displaystyle\sum\dfrac{(-1)^{n-1}}{n(\sqrt n+1)}$
$|a_n|\sim 1/n^{3/2}$，$\sum|a_n|$ 收敛。**绝对收敛**。

### (6) $\displaystyle\sum x^n\tan\dfrac{1}{\sqrt n}\;(x\in\mathbb R)$
$\tan(1/\sqrt n)\sim 1/\sqrt n$，$|a_n|\sim|x|^n/\sqrt n$.
- $|x|<1$：由比值法或比较法，**绝对收敛**；
- $|x|>1$：通项 $\to\infty$，**发散**；
- $x=1$：$\sum\tan(1/\sqrt n)\sim\sum 1/\sqrt n$，**发散**；
- $x=-1$：$\sum(-1)^n\tan(1/\sqrt n)$，$\tan(1/\sqrt n)$ 单减到 0，由 Leibniz 收敛；而 $\sum\tan(1/\sqrt n)$ 发散，**条件收敛**。

---

## (A) 15. 是否交错？是否满足 Leibniz？是否收敛？

### (1) $\displaystyle\sum_{n=2}^{\infty}\!\left(\dfrac{1}{\sqrt n-1}-\dfrac{1}{\sqrt n+1}\right)$
通分：$\dfrac{1}{\sqrt n-1}-\dfrac{1}{\sqrt n+1}=\dfrac{2}{n-1}>0$。**不是交错级数**；与调和级数同阶，**发散**。

### (2) $\displaystyle\sum[1+(-1)^n]\dfrac{1}{n}\sin\dfrac{1}{n}$
$1+(-1)^n=\begin{cases}2,&n\text{ 偶}\\0,&n\text{ 奇}\end{cases}$，所有项非负，**不是交错级数**。取偶项 $n=2k$，原级数 $=\sum\dfrac{1}{k}\sin\dfrac{1}{2k}\sim\sum\dfrac{1}{2k^2}$，**收敛**。

### (3) $\displaystyle\sum(-1)^{n-1}\dfrac{1}{\sqrt[4]{n}}$
**是交错级数**；$\dfrac{1}{\sqrt[4]{n}}$ 单减到 0，**满足 Leibniz**，**收敛（条件收敛）**。

### (4) $\displaystyle\sum(-1)^{n+1}\dfrac{\ln(2+1/n)}{\sqrt{9n^2-4}}$
**是交错级数**；
$|a_n|=\dfrac{\ln(2+1/n)}{\sqrt{9n^2-4}}$：分子 $\ln(2+1/n)$ 单减且趋于 $\ln 2$，分母 $\sqrt{9n^2-4}$ 单增，故 $|a_n|$ 单减到 0。**满足 Leibniz**，**收敛**。
又 $|a_n|\sim\dfrac{\ln 2}{3n}$，$\sum|a_n|$ 发散，故**条件收敛**。

---

## (A) 16. 判别下列级数的敛散性

### (1) $\displaystyle\sum_{n=1}^{\infty}\frac{a^n}{n^p}\;(p>0,\,|a|\ne 1)$

通项 $u_n=\dfrac{a^n}{n^p}$。先看 $\sum|u_n|=\sum\dfrac{|a|^n}{n^p}$，用**检比法**：
$$\frac{|u_{n+1}|}{|u_n|}=|a|\cdot\Bigl(\frac{n}{n+1}\Bigr)^p\to|a|.$$

- **$|a|<1$**：检比极限 $<1\Rightarrow\sum|u_n|$ 收敛 $\Rightarrow$ 原级数**绝对收敛**。
- **$|a|>1$**：通项 $|u_n|=\dfrac{|a|^n}{n^p}\to+\infty$，不满足 $u_n\to 0$ ⇒ **发散**。

**结论**：$|a|<1$ 时绝对收敛；$|a|>1$ 时发散。

### (2) $\displaystyle a-\frac{b}{2}+\frac{a}{3}-\frac{b}{4}+\cdots+\frac{a}{2n-1}-\frac{b}{2n}+\cdots\;(a^2+b^2\ne 0)$

记 $H_n=\sum_{k=1}^{n}\dfrac{1}{k}=\ln n+\gamma+o(1)$（$\gamma$ 为 Euler–Mascheroni 常数）。

**部分和**：
$$
S_{2n}=\sum_{k=1}^{n}\Bigl(\frac{a}{2k-1}-\frac{b}{2k}\Bigr)
=a\sum_{k=1}^{n}\frac{1}{2k-1}-b\sum_{k=1}^{n}\frac{1}{2k}.
$$

利用 $\sum_{k=1}^{n}\dfrac{1}{2k-1}=H_{2n}-\dfrac{1}{2}H_n$ 和 $\sum_{k=1}^{n}\dfrac{1}{2k}=\dfrac{1}{2}H_n$：
$$
S_{2n}=a\bigl(H_{2n}-\tfrac{1}{2}H_n\bigr)-\tfrac{b}{2}H_n=a\,H_{2n}-\tfrac{a+b}{2}H_n.
$$

代入 $H_n=\ln n+\gamma+o(1),\;H_{2n}=\ln(2n)+\gamma+o(1)=\ln n+\ln 2+\gamma+o(1)$：
$$
S_{2n}=a\bigl[\ln n+\ln 2+\gamma\bigr]-\tfrac{a+b}{2}\bigl[\ln n+\gamma\bigr]+o(1)
=\boxed{\;a\ln 2+\tfrac{a-b}{2}(\ln n+\gamma)+o(1).\;}
$$

讨论：

- **$a=b$**（且 $\ne 0$）：发散项 $\tfrac{a-b}{2}(\ln n+\gamma)$ 消失，$S_{2n}\to a\ln 2$；又 $S_{2n+1}=S_{2n}+\dfrac{a}{2n+1}\to a\ln 2$，故级数**收敛于 $a\ln 2$**。
- **$a\ne b$**：发散项 $\tfrac{a-b}{2}\ln n\to\pm\infty$，$S_{2n}$ 无极限 ⇒ **发散**。

**结论**：当且仅当 $a=b\ne 0$ 时收敛，和为 $a\ln 2$；其余情形发散。

> 当 $a=b=1$ 时退化为 $1-\tfrac12+\tfrac13-\tfrac14+\cdots=\ln 2$，正是经典调和级数交错形式。

---

## (A) 17. 近似求和（误差 $<10^{-3}$）

**题目**：计算 $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}\dfrac{1}{(2n-1)!}$ 的近似值，使绝对误差 $<10^{-3}$。

**识别**：原级数 $=\sin 1$（由 $\sin x=\sum(-1)^{n-1}\dfrac{x^{2n-1}}{(2n-1)!}$ 取 $x=1$）。

**Leibniz 余项估计**：交错级数取前 $n$ 项的误差
$$|R_n|\le|a_{n+1}|=\frac{1}{(2n+1)!}.$$

要使 $|R_n|<10^{-3}$，取
$$\frac{1}{(2n+1)!}<10^{-3}\Rightarrow(2n+1)!>1000.$$

试算：$5!=120,\;7!=5040$。故取 $2n+1=7\Rightarrow n=3$ 即可（$1/5040\approx 1.98\times 10^{-4}<10^{-3}$）。

**前 3 项求和**：
$$
S_3=1-\frac{1}{3!}+\frac{1}{5!}=1-\frac{1}{6}+\frac{1}{120}=\frac{120-20+1}{120}=\frac{101}{120}\approx 0.8417.
$$

> 真值 $\sin 1\approx 0.84147$，误差 $\approx 1.98\times 10^{-4}$，符合要求。

**结论**：$S\approx\dfrac{101}{120}\approx 0.842$。

---

## (A) 18. 判定下列级数是绝对收敛还是条件收敛

### (1) $\displaystyle\sum_{n=1}^{\infty}\frac{\cos(n!)}{n\sqrt n}$

绝对值估计：$\Bigl|\dfrac{\cos(n!)}{n\sqrt n}\Bigr|\le\dfrac{1}{n^{3/2}}$。

由 $p=3/2>1$，$\sum\dfrac{1}{n^{3/2}}$ 收敛 ⇒ 由比较判别法 $\sum\bigl|\dfrac{\cos(n!)}{n\sqrt n}\bigr|$ 收敛。

**结论**：**绝对收敛**。

### (2) $\displaystyle\sum_{n=1}^{\infty}(-1)^{\frac{n(n+1)}{2}}\frac{n}{2^n}$

绝对值 $\dfrac{n}{2^n}$，用**检比法**：
$$\frac{(n+1)/2^{n+1}}{n/2^n}=\frac{n+1}{2n}\to\frac{1}{2}<1.$$

故 $\sum\dfrac{n}{2^n}$ 收敛 ⇒ 原级数**绝对收敛**。

> 符号 $(-1)^{n(n+1)/2}$ 按 $-,-,+,+,-,-,+,+,\cdots$ 周期 $4$ 变号；既然绝对值级数收敛，符号怎么变都不影响。

**结论**：**绝对收敛**。

### (3) $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}\frac{1}{\sqrt[4]{n}}$

绝对值级数 $\sum\dfrac{1}{n^{1/4}}$：$p=1/4<1$，**发散**。

原级数是交错级数，$\dfrac{1}{\sqrt[4]{n}}\downarrow 0$，由 **Leibniz 准则**收敛。

**结论**：**条件收敛**。（与 (A)15(3) 同题。）

### (4) $\displaystyle\sum_{n=1}^{\infty}(-1)^{n+1}\frac{\ln(2+1/n)}{\sqrt{9n^2-4}}$

**绝对值级数**：当 $n\to\infty$，
$$\frac{\ln(2+1/n)}{\sqrt{9n^2-4}}\sim\frac{\ln 2}{3n}.$$

由比较判别法 II（$\lambda=\ln 2/3>0$ 有限）+ 调和级数发散 ⇒ 绝对值级数**发散**。

**原级数（交错）**：
- $a_n=\dfrac{\ln(2+1/n)}{\sqrt{9n^2-4}}$；
- $\ln(2+1/n)$ 随 $n$ 增大而减小（$1/n\downarrow$），$\sqrt{9n^2-4}$ 单调增 ⇒ $a_n\downarrow$；
- $a_n\to 0$。

由 **Leibniz 准则**收敛。

**结论**：**条件收敛**。（与 (A)15(4) 同题。）

---

## 汇总表

| 题目 | 结论 |
|---|---|
| 16 (1) | $\|a\|<1$ 绝对收敛；$\|a\|>1$ 发散 |
| 16 (2) | $a=b\ne 0$ 收敛于 $a\ln 2$；$a\ne b$ 发散 |
| 17 | $S\approx\dfrac{101}{120}\approx 0.842$（取 3 项即可） |
| 18 (1) | 绝对收敛 |
| 18 (2) | 绝对收敛 |
| 18 (3) | 条件收敛 |
| 18 (4) | 条件收敛 |

---

## (B) 3. 关于 $\sum f(1/n)$ 的绝对收敛性

**题目**：设 $f(x)$ 在 $x=0$ 的某一邻域内具有二阶连续导数，且 $\displaystyle\lim_{x\to 0}\dfrac{f(x)}{x}=0$。证明级数 $\displaystyle\sum_{n=1}^{\infty}f\!\left(\dfrac{1}{n}\right)$ 绝对收敛。

**证明**：
由 $f$ 在 $0$ 处连续及 $\lim_{x\to0}f(x)/x=0$，必有 $f(0)=0$（否则 $f(x)/x\to\infty$）。又
$$f'(0)=\lim_{x\to 0}\frac{f(x)-f(0)}{x}=\lim_{x\to0}\frac{f(x)}{x}=0.$$
由 Taylor 公式（带 Lagrange 余项）：在 $0$ 的某邻域内存在 $\xi$（介于 $0$ 与 $x$ 之间）使
$$f(x)=f(0)+f'(0)x+\frac{f''(\xi)}{2}x^2=\frac{f''(\xi)}{2}x^2.$$
因 $f''$ 在 $0$ 处连续，存在邻域 $|x|<\delta$ 与常数 $M>0$ 使得 $|f''(\xi)|\le M$。

故当 $n>1/\delta$ 时，
$$\left|f\!\left(\frac{1}{n}\right)\right|\le\frac{M}{2n^2}.$$
由比较判别法及 $\sum 1/n^2$ 收敛，知 $\sum\bigl|f(1/n)\bigr|$ 收敛，即原级数**绝对收敛**。 $\blacksquare$

---

## (B) 4. 判别下列级数的敛散性

### (1) $\displaystyle\sum\dfrac{\ln n}{n^{1+\alpha}}\;(\alpha>0)$
取 $\beta=\alpha/2>0$。当 $n$ 充分大时 $\ln n<n^{\beta}$，故
$$\frac{\ln n}{n^{1+\alpha}}<\frac{1}{n^{1+\alpha-\beta}}=\frac{1}{n^{1+\alpha/2}},\quad 1+\alpha/2>1.$$
由比较判别法，**收敛**。

### (2) $\displaystyle\sum\dfrac{1}{n\ln(5+n^3)}$
当 $n\to\infty$，$\ln(5+n^3)\sim 3\ln n$，故
$$a_n\sim\frac{1}{3\,n\ln n}.$$
由积分判别法：$\displaystyle\int_2^{\infty}\dfrac{dx}{x\ln x}=\ln\ln x\Big|_2^{\infty}=\infty$，所以 $\sum 1/(n\ln n)$ 发散，原级数**发散**。

### (3) $\displaystyle\sum\!\left(\dfrac{\alpha^n}{n+1}\right)^{n}\;(\alpha>0)$
用根值判别法：
$$\sqrt[n]{a_n}=\frac{\alpha^n}{n+1}.$$
- 若 $0<\alpha\le 1$：$\alpha^n$ 有界，分母趋于无穷，$\sqrt[n]{a_n}\to 0<1$，**收敛**；
- 若 $\alpha>1$：$\dfrac{\alpha^n}{n+1}\to+\infty>1$，**发散**。

**综上：$0<\alpha\le 1$ 收敛；$\alpha>1$ 发散.**

### (4) $\displaystyle\sum\tan\!\bigl(\sqrt{n^2+1}\,\pi\bigr)$
$\sqrt{n^2+1}=n\sqrt{1+1/n^2}=n+\dfrac{1}{2n}+O(1/n^3)$，故
$$\sqrt{n^2+1}\,\pi=n\pi+\frac{\pi}{2n}+O(1/n^3).$$
由 $\tan(n\pi+\theta)=\tan\theta$，
$$\tan(\sqrt{n^2+1}\,\pi)=\tan\!\left(\frac{\pi}{2n}+O(1/n^3)\right)\sim\frac{\pi}{2n}.$$
与调和级数同阶，**发散**。

### (5) $\sqrt 3+\sqrt{3-\sqrt 6}+\sqrt{3-\sqrt{6+\sqrt 6}}+\cdots$
设辅助数列 $c_0=0$，$c_{n+1}=\sqrt{6+c_n}$（$n\ge 0$，并约定 $c_1=\sqrt 6$）。
则第 $n$ 项为 $a_n=\sqrt{3-c_{n-1}}$。

**先证 $c_n\uparrow 3$**：由 $c=\sqrt{6+c}\Rightarrow c^2-c-6=0\Rightarrow c=3$；由归纳法 $0\le c_n<3$ 且单调递增，故 $c_n\to 3$。

**收敛速度**：令 $\varepsilon_n=3-c_n>0$，则
$$\varepsilon_{n+1}=3-\sqrt{9-\varepsilon_n}=\frac{\varepsilon_n}{3+\sqrt{9-\varepsilon_n}}\le\frac{\varepsilon_n}{3+\sqrt{9-\varepsilon_1}}<\frac{\varepsilon_n}{5}.$$
故 $\varepsilon_n\le\varepsilon_1\cdot 5^{-(n-1)}$，即 $\varepsilon_n=O(5^{-n})$。

于是
$$a_n=\sqrt{\varepsilon_{n-1}}=O\!\left(\bigl(\tfrac1{\sqrt 5}\bigr)^{n}\right).$$
为公比小于 1 的几何级数所控，由比较判别法**收敛**。

---

## 附：缺失题目说明

OCR中（A）组**第 16 题、第 18 题**的题面缺失（在 287 页与 288 页交界处被跳过），无法给出解答。请将这两题题面补充给我，我再补齐解答到本文档。

---

