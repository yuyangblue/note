---
AIGC:
  Label: "1",
  "ContentProducer":   "00191310104MAC2G6EG4100000003",
  "ContentPropagator": "00191310104MAC2G6EG4100000003",
  "ProduceID":         "u-4dc2a7-22130fc0-013d-4384-a938-f4011a280ce5",
  "PropagateID":       "u-4dc2a7-22130fc0-013d-4384-a938-f4011a280ce5",
  "ReservedCode1":     "",
  "ReservedCode2":     "",
---
# Beta 函数与 Gamma 函数速查手册

> 适用于工科数学分析 / 数学分析 / 高等数学中"含参变量反常积分"一章。  
> 本文按 **公式 → 性质 → 关系 → 使用方法 → 题型模板 → 易错点** 的顺序整理，便于做题查阅。

---

## 一、基本定义

### 1.1 Gamma 函数（第二类欧拉积分）

$$
\Gamma(s)=\int_0^{+\infty} x^{s-1}e^{-x}\,dx,\qquad s>0
$$

- **定义域**：$(0,+\infty)$；通过递推可延拓到 $\mathbb{R}\setminus\{0,-1,-2,\dots\}$。
- **几何意义**：把"阶乘"从整数推广到了实数（甚至复数）。

### 1.2 Beta 函数（第一类欧拉积分）

$$
B(p,q)=\int_0^1 x^{p-1}(1-x)^{q-1}\,dx,\qquad p>0,\ q>0
$$

- **定义域**：$(0,+\infty)\times(0,+\infty)$。

---

## 二、核心性质与公式

### 2.1 Gamma 函数

| 性质 | 公式 |
|---|---|
| 递推公式 | $\Gamma(s+1)=s\,\Gamma(s)$ |
| 整数值 | $\Gamma(n+1)=n!$，$\Gamma(1)=1$ |
| 半整数值 | $\Gamma\!\left(\tfrac12\right)=\sqrt{\pi}$ |
| 一般半整数 | $\Gamma\!\left(n+\tfrac12\right)=\dfrac{(2n-1)!!}{2^n}\sqrt{\pi}$ |
| 定义域延拓 | $\Gamma(s)=\dfrac{\Gamma(s+m+1)}{(s+m)(s+m-1)\cdots(s+1)\,s}$ |

### 2.2 Beta 函数

| 性质 | 公式 |
|---|---|
| 对称性 | $B(p,q)=B(q,p)$ |
| 递推（对 $q$） | $B(p,q)=\dfrac{q-1}{p+q-1}B(p,q-1)\quad(q>1)$ |
| 递推（双边） | $B(p,q)=\dfrac{(p-1)(q-1)}{(p+q-1)(p+q-2)}B(p-1,q-1)\quad(p,q>1)$ |

### 2.3 Beta 函数的三种等价积分表示

| 编号 | 形式 | 适用代换 |
|---|---|---|
| ① | $B(p,q)=\displaystyle\int_0^1 x^{p-1}(1-x)^{q-1}dx$ | 标准定义 |
| ② | $B(p,q)=2\displaystyle\int_0^{\pi/2}\sin^{2q-1}\!\varphi\,\cos^{2p-1}\!\varphi\,d\varphi$ | $x=\cos^2\varphi$ |
| ③ | $B(p,q)=\displaystyle\int_0^{+\infty}\dfrac{t^{p-1}}{(1+t)^{p+q}}dt$ | $x=\dfrac{t}{1+t}$ |

### 2.4 余元公式

$$
\Gamma(p)\,\Gamma(1-p)=\frac{\pi}{\sin(p\pi)},\qquad 0<p<1
$$

由此得：$B(p,1-p)=\dfrac{\pi}{\sin(p\pi)}$。

### 2.5 Beta 与 Gamma 的桥梁公式（最重要！）

$$
\boxed{\;B(p,q)=\dfrac{\Gamma(p)\,\Gamma(q)}{\Gamma(p+q)}\;}
$$

> **几乎所有 Beta 函数的题，最后都通过这个公式翻译成 Gamma，再用阶乘 / 半整数公式算出数值。**

---

## 三、几个必背的具体值

| 表达式 | 值 |
|---|---|
| $\Gamma(1)$ | $1$ |
| $\Gamma(2)$ | $1$ |
| $\Gamma(n+1)$ | $n!$ |
| $\Gamma(\tfrac12)$ | $\sqrt{\pi}$ |
| $\Gamma(\tfrac32)$ | $\tfrac{\sqrt\pi}{2}$ |
| $\Gamma(\tfrac52)$ | $\tfrac{3\sqrt\pi}{4}$ |
| $\Gamma(\tfrac72)$ | $\tfrac{15\sqrt\pi}{8}$ |
| $B(1,1)$ | $1$ |
| $B(\tfrac12,\tfrac12)$ | $\pi$ |

---

## 四、做题流程（4 步识别法）

### 第 1 步：看积分区间和被积函数特征

| 积分区间 | 关键特征 | 优先选用 |
|---|---|---|
| $[0,1]$ | 含 $(1-x)$ | Beta 形式 ① |
| $[0,\pi/2]$ | 含 $\sin^m\!x\,\cos^n\!x$ | Beta 形式 ② |
| $[0,+\infty)$ | 含 $e^{-x^k}$ | Gamma |
| $[0,+\infty)$ | 含 $\dfrac{1}{(1+x)^k}$ | Beta 形式 ③ |
| $[0,a]$ | 含 $\sqrt{a^2-x^2}$ 类根式 | 先三角代换，再用 Beta |

### 第 2 步：对号入座做代换

| 目标 | 常用代换 |
|---|---|
| 消根号 / 调指数 | $t=x^k$ |
| 把 $(1-x)$ 翻到第一项 | $t=1-x$ |
| 有限区间 $\leftrightarrow$ 无限区间 | $x=\dfrac{t}{1+t}$ |
| 三角形态 | $x=\sin^2\theta$ 或 $\cos^2\theta$ |

### 第 3 步：读出参数 $p,q$（或 $s$）

把代换后的式子和标准形式逐项比对，**列方程**解出参数。

### 第 4 步：化为 Γ 求数值

用 $B(p,q)=\dfrac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$ 全部翻成 Γ，再用阶乘 / 半整数 / 余元公式算出数值。

---

## 五、6 个高频题型模板

### 模板 1：$\displaystyle\int_0^{+\infty} x^{n}e^{-x^k}dx$ —— Gamma 型

**代换** $t=x^k$：
$$
\int_0^{+\infty}x^n e^{-x^k}dx=\frac{1}{k}\,\Gamma\!\left(\frac{n+1}{k}\right)
$$

**例**：$\displaystyle\int_0^{+\infty}e^{-x^2}dx=\tfrac12\Gamma(\tfrac12)=\dfrac{\sqrt\pi}{2}$。

---

### 模板 2：$\displaystyle\int_0^{\pi/2}\sin^m\!x\,\cos^n\!x\,dx$ —— 三角型

$$
\boxed{\int_0^{\pi/2}\sin^m\!x\,\cos^n\!x\,dx=\tfrac12 B\!\left(\tfrac{m+1}{2},\tfrac{n+1}{2}\right)=\frac{\Gamma\!\left(\tfrac{m+1}{2}\right)\Gamma\!\left(\tfrac{n+1}{2}\right)}{2\,\Gamma\!\left(\tfrac{m+n+2}{2}\right)}}
$$

**例**：$\displaystyle\int_0^{\pi/2}\sin^5\!x\cos^6\!x\,dx=\tfrac12 B(3,\tfrac72)=\tfrac{\Gamma(3)\Gamma(7/2)}{2\Gamma(13/2)}=\dfrac{8}{693}$。

---

### 模板 3：$\displaystyle\int_0^1 x^{\alpha}(1-x^k)^{\beta}dx$ —— 幂×幂型

**代换** $t=x^k$：
$$
\int_0^1 x^\alpha(1-x^k)^\beta dx=\frac{1}{k}B\!\left(\tfrac{\alpha+1}{k},\,\beta+1\right)
$$

**例**：$\displaystyle\int_0^1 x^3\sqrt{1-x^2}\,dx=\tfrac12 B(2,\tfrac32)=\dfrac{2}{15}$。

---

### 模板 4：$\displaystyle\int_0^{+\infty}\dfrac{x^{\alpha}}{(1+x)^{\beta}}dx$ —— 有理型

直接对比 Beta 形式 ③，参数为：
$$
p=\alpha+1,\quad q=\beta-\alpha-1
$$
（收敛条件：$\alpha>-1,\ \beta-\alpha-1>0$）

**例**：$\displaystyle\int_0^{+\infty}\dfrac{\sqrt x}{(1+x)^2}dx=B(\tfrac32,\tfrac12)=\dfrac{\pi}{2}$。

---

### 模板 5：$\displaystyle\int_0^{+\infty}\dfrac{dx}{1+x^n}$ —— 余元公式型

代换 $t=x^n$ 后化为 Beta，再用余元公式：
$$
\int_0^{+\infty}\frac{dx}{1+x^n}=\frac{\pi}{n\sin(\pi/n)}
$$

**例**：$n=3$ 时结果是 $\dfrac{2\pi}{3\sqrt 3}$。

---

### 模板 6：几何 / 物理量积分中出现的 Beta

凡是化简到 $\displaystyle\int_0^{\pi/2}\sin^a\!\theta\,\cos^b\!\theta\,d\theta$ 形态，**直接套模板 2**，不要硬展开。

**例**：极坐标曲线 $r^2=\sin\theta\cos\theta$ 所围面积
$$
A=\int_0^{\pi/2}\sin\theta\cos\theta\,d\theta=\tfrac12 B(1,1)=\tfrac12.
$$

---

## 六、综合演示题

> **求** $\displaystyle I=\int_0^{+\infty}\dfrac{x^{1/3}}{(1+x)^2}\,dx$

**Step 1** 识别：区间 $[0,+\infty)$、形如 $\dfrac{x^\alpha}{(1+x)^\beta}$ → **模板 4**。  
**Step 2** 对比 Beta 形式 ③：$\alpha=\tfrac13,\ \beta=2$。  
**Step 3** 解参数：$p=\tfrac43,\ q=\tfrac23$（均 $>0$，收敛）。  
**Step 4** 化简：
$$
I=B\!\left(\tfrac43,\tfrac23\right)=\frac{\Gamma(4/3)\Gamma(2/3)}{\Gamma(2)}=\tfrac13\Gamma(1/3)\Gamma(2/3)=\tfrac13\cdot\frac{\pi}{\sin(\pi/3)}=\dfrac{2\pi}{3\sqrt 3}.
$$

---

## 七、易错点提醒

1. **指数偏移 1**：Beta、Gamma 中都是 $x^{p-1}$，不是 $x^p$，对比时一定细看。  
2. **忘换 Jacobian**：$x=t^k\Rightarrow dx=k\,t^{k-1}dt$，常被遗漏。  
3. **上下限**：代换后区间是否仍匹配标准形式？  
4. **收敛性**：用公式前确认 $p>0,q>0$（或 $s>0$）；否则原积分发散，套公式得到的"值"无意义。  
5. **奇偶性陷阱**：$\int_0^{\pi/2}\sin^m\!x\cos^n\!x\,dx$ 公式仅当 $m,n>-1$ 时收敛。  

---

## 八、做题清单（建议贴在草稿本上）

```
□ 1. 看积分区间：[0,1]? [0,π/2]? [0,+∞)?
□ 2. 找特征因子：(1−x)? sin·cos? e^{−x^k}? 1/(1+x)^k?
□ 3. 选代换：t = x^k / 1−x / x/(1+x) / sin²θ
□ 4. 列方程解 p, q（或 s），确认均 > 0
□ 5. 用 B(p,q) = Γ(p)Γ(q)/Γ(p+q) 全部翻成 Γ
□ 6. 用递推 / 半整数 / 余元公式算最终值
□ 7. 数值合理性自检
```

---

## 九、一句话总结

> **Beta / Gamma 函数不是用来"证"的，而是用来"查表 + 套公式"快速求积分的工具。**  
> 做题三件套：**识别形态 → 对号代换 → 翻成 Γ 算数值**。

