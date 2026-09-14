# 教材补充：Bootstrap 自助法（对应教材第8章）

> 来源：《统计学完全教程》(All of Statistics, L. Wasserman) 第8章。
> 定位：**笔记库完全没有的一整章**（国内本科课程一般不教）。Bootstrap 是 Efron (1979) 发明的、用重抽样估计标准误和置信区间的通用方法，是"任何统计量都能算标准误"的万能钥匙。与第7章 plug-in 方法衔接：复杂泛函（中位数、相关系数、偏度）的标准误没有解析公式，就用 Bootstrap。

## 目录

- [一、 问题与两步思想](#一问题与两步思想)
- [二、 模拟的原理：大数定律](#二模拟的原理大数定律)
- [三、 Bootstrap 方差估计步骤](#三bootstrap-方差估计步骤)
- [四、 两种近似的来源](#四两种近似的来源)
- [五、 三种 Bootstrap 置信区间](#五三种-bootstrap-置信区间)
- [六、 例子与伪代码](#六例子与伪代码)
- [七、 Jackknife 刀切法（附录）](#七jackknife-刀切法附录)
- [本节重点](#本节重点)

---

## 一、 问题与两步思想

设 $T_n=g(X_1,\dots,X_n)$ 是统计量（数据的任意函数）。想要 $V_F(T_n)$——方差，下标 $F$ 强调**方差通常依赖未知分布 $F$**（如 $\bar X_n$ 的方差 $\sigma^2/n$ 中 $\sigma^2=\int(x-\mu)^2dF(x)$ 依赖 $F$）。

**Bootstrap 两步**：
- **第1步（plug-in）**：用经验分布 $\widehat F_n$ 替换未知 $F$，目标是 $V_{\widehat F_n}(T_n)$；
- **第2步（模拟）**：用重抽样模拟逼近 $V_{\widehat F_n}(T_n)$。

两步示意：
```
真实世界:  F  →  X₁,…,Xₙ  →  Tₙ = g(X₁,…,Xₙ)
Bootstrap: F̂ₙ →  X₁*,…,Xₙ* →  Tₙ* = g(X₁*,…,Xₙ*)
```

## 二、 模拟的原理：大数定律

从分布 $G$ 抽 $Y_1,\dots,Y_B$ iid，由大数定律：
$$\frac1B\sum_{j=1}^B Y_j\xrightarrow{p}\mathbb E(Y),\qquad \frac1B\sum_{j=1}^B(Y_j-\bar Y)^2\xrightarrow{p}V(Y)\quad(B\to\infty)$$
模拟里 $B$ 可以取任意大（如 1000、10000），所以样本均值和样本方差可以非常精确地逼近期望和方差。

## 三、 Bootstrap 方差估计步骤

**关键观察**：$\widehat F_n$ 在每个数据点放质量 $1/n$，所以**从 $\widehat F_n$ 抽一个观测 = 从原始数据随机等概率抽一个点**；抽 $n$ 个即**有放回抽 $n$ 个**。

**算法**：
1. 从 $X_1,\dots,X_n$ **有放回**抽 $n$ 个：$X_1^*,\dots,X_n^*\sim\widehat F_n$；
2. 计算 $T_b^*=g(X_1^*,\dots,X_n^*)$；
3. 重复 1-2 共 $B$ 次，得 $T_{,1}^*,\dots,T_{,B}^*$；
4. Bootstrap 方差估计：
$$V_{\rm boot}=\frac1B\sum_{b=1}^{B}\Big(T_{,b}^*-\frac1B\sum_{r=1}^{B}T_{,r}^*\Big)^2,\qquad \widehat{\text{se}}_{\rm boot}=\sqrt{V_{\rm boot}}$$

**伪代码（估计中位数的标准误）**：
```
T ← median(X)
for b in 1..B:
    Xstar ← 从 X 有放回抽 n 个
    Tboot[b] ← median(Xstar)
se ← sqrt(variance(Tboot))
```

## 四、 两种近似的来源

$$V_F(T_n)\ \overset{\text{近似1}}{\approx}\ V_{\widehat F_n}(T_n)\ \overset{\text{近似2}}{\approx}\ V_{\rm boot}$$

- 近似1：用 $\widehat F_n$ 替 $F$，**$n$ 越大越准**（Glivenko–Cantelli：$\widehat F_n$ 一致逼近 $F$）；
- 近似2：用有限次模拟替期望，**$B$ 越大越准**（大数定律，可任意小误差）。

## 五、 三种 Bootstrap 置信区间

设 $\theta=T(F)$，$\hat\theta_n=T(\widehat F_n)$，bootstrap 复制 $\hat\theta_{,1}^*,\dots,\hat\theta_{,B}^*$，$q_\beta^*$ 为它们的 $\beta$ 样本分位数：

**方法1：正态区间（Normal）**
$$\hat\theta_n\pm z_{\alpha/2}\,\widehat{\text{se}}_{\rm boot}$$
只在 $T_n$ 分布接近正态时准确。

**方法2：枢轴区间（Pivotal）**：枢轴 $R_n=\hat\theta_n-\theta$，用 $R_b^*=\hat\theta_{,b}^*-\hat\theta_n$ 的分位数：
$$C_n=\big(2\hat\theta_n-q_{1-\alpha/2}^*,\ \ 2\hat\theta_n-q_{\alpha/2}^*\big)$$
推导：$\mathbb P(\hat\theta_n-q_{1-\alpha/2}^*\le\theta\le\hat\theta_n-q_{\alpha/2}^*)=\mathbb P(q_{\alpha/2}^*\le R\le q_{1-\alpha/2}^*)\approx1-\alpha$。

**方法3：百分位区间（Percentile）**
$$C_n=\big(q_{\alpha/2}^*,\ q_{1-\alpha/2}^*\big)$$
论证（附录）：若存在单调正态化变换 $U=m(\hat\theta)$（无需知道它），则分位数在变换下保持，区间覆盖 $1-\alpha$。

> 三种区间同级精度（都是近似 $1-\alpha$）；小样本时可能有差异。还有更精确的方法（BCa 等）本书不讲。

## 六、 例子与伪代码

**例（两组中位数差，血浆胆固醇）**：两样本分别重抽样：
```
th.hat ← median(x2) - median(x1)
for b in 1..B:
    xx1 ← 从 x1 有放回抽 n1 个
    xx2 ← 从 x2 有放回抽 n2 个
    Tboot[b] ← median(xx2) - median(xx1)
```
点估计 18.5，$\widehat{\text{se}}=7.42$，三种 95% 区间都**不含 0** → 第二组胆固醇显著更高。

**例（相关系数，法学院数据）**：样本相关 $\hat\rho=0.776$，Bootstrap 直方图就是 $\hat\rho$ 抽样分布的逼近，$\widehat{\text{se}}=0.137$；正态区间 $(0.51,1.00)$、百分位 $(0.46,0.96)$。

**例（生物等效性，FDA）**：$\theta=\bar Y/\bar Z$ 的 plug-in 估计 $-0.071$，Bootstrap 95% 区间 $(-0.24,0.15)$ **不完全落在 FDA 要求 $(-0.2,0.2)$ 内** → 未证明生物等效。

## 七、 Jackknife 刀切法（附录）

更省算力的留一法：$T_{(-i)}$=删掉第 $i$ 个观测后的统计量，$\bar T_n=\frac1n\sum T_{(-i)}$：
$$V_{\rm jack}=\frac{n-1}{n}\sum_{i=1}^{n}\big(T_{(-i)}-\bar T_n\big)^2$$
一致估计方差（$V_{\rm jack}/V\to1$），但**对样本分位数不适用**（Bootstrap 可以）。

---

## 本节重点

> - **思想**：$\widehat F_n$ 替 $F$（plug-in）+ 重抽样替期望（大数定律）。
> - **做法**：有放回抽 $n$ 个 → 算统计量 → 重复 $B$ 次 → 样本方差/分位数。
> - **三种区间**：Normal（$\hat\theta\pm z\widehat{\text{se}}$）、Pivotal（$2\hat\theta-q_{1-\alpha/2}^*,\ 2\hat\theta-q_{\alpha/2}^*$）、Percentile（$q_{\alpha/2}^*,\ q_{1-\alpha/2}^*$）。
> - **适用范围**：任何统计量（中位数、相关系数、偏度、两样本差……），无需解析标准误公式。
> - **局限**：$n$ 小时不准（如 $\text{Uniform}(0,\theta)$ 的 $\hat\theta=X_{\max}$ 情形 Bootstrap 很差）；习题7给出 $P(\hat\theta^*=\hat\theta)\approx0.632$。
> - **Jackknife**：留一法，省算力，但对分位数失效。
