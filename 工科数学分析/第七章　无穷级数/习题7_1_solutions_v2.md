---
AIGC:
  Label: "1",
  "ContentProducer":   "00191310104MAC2G6EG4100000003",
  "ContentPropagator": "00191310104MAC2G6EG4100000003",
  "ProduceID":         "u-4dc2a7-899b9d5b-d79c-4ec9-b3bf-1b84a7500431",
  "PropagateID":       "u-4dc2a7-899b9d5b-d79c-4ec9-b3bf-1b84a7500431",
  "ReservedCode1":     "",
  "ReservedCode2":     "",
---

# 工科数学分析基础（下册·第三版，马知恩/王绵森）—— 习题 7.1 解答

> 范围：习题 7.1（pp. 285–289）  
> 题号：(A) 组：3、8、12、14、15、16、18；(B) 组：3、4  
> 说明：第 16、18 题的题面已根据补充资料补全。

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

