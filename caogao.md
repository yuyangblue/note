# 由这三个级数可以「再走一步」得到的经典展开

这三个式子是基础原料。对它们做**变量代换**（$x\mapsto -x$、$x\mapsto x^2$、$x\mapsto -x^2$）和**逐项积分**，就能立刻得到 $\ln(1+x)$、$\arctan x$、$\arcsin x$ 等一系列经典级数。下面分别推一遍。

---

## 一、从 $\dfrac{1}{1+x}$ 出发

### 1. 换 $x\to -x$，得几何级数

$$
\frac{1}{1-x}=\sum_{n=0}^{\infty}x^{n},\qquad |x|<1.
$$

### 2. 对 $\dfrac{1}{1+x}$ 逐项积分 → $\ln(1+x)$

$$
\ln(1+x)=\int_{0}^{x}\frac{dt}{1+t}=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{n+1}x^{n+1}=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}x^{n},\quad x\in(-1,1].
$$

### 3. 换 $x\to x^{2}$ → $\dfrac{1}{1+x^{2}}$，再积分 → $\arctan x$

$$
\frac{1}{1+x^{2}}=\sum_{n=0}^{\infty}(-1)^{n}x^{2n},
$$
$$
\arctan x=\int_{0}^{x}\frac{dt}{1+t^{2}}=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1}x^{2n+1},\quad x\in[-1,1].
$$
特别地，取 $x=1$ 得到 **Leibniz 公式**：
$$
\frac{\pi}{4}=1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\cdots.
$$

---

## 二、从 $\sqrt{1+x}$ 出发

### 1. 换 $x\to -x^{2}$，得 $\sqrt{1-x^{2}}$

$$
\sqrt{1-x^{2}}=1-\frac{1}{2}x^{2}-\sum_{n=2}^{\infty}\frac{(2n-3)!!}{(2n)!!}x^{2n},\qquad |x|\le 1.
$$

（把 $(-1)^{n-1}$ 与 $(-x^2)^n$ 中的 $(-1)^n$ 相乘，得到 $(-1)^{2n-1}=-1$，因此除首项外**全部带负号**。）

### 2. 积分 → 圆面积公式的级数版本

$$
\int_{0}^{x}\sqrt{1-t^{2}}\,dt=\frac{1}{2}\bigl(x\sqrt{1-x^{2}}+\arcsin x\bigr),
$$
对应级数为
$$
\int_{0}^{x}\sqrt{1-t^{2}}\,dt=x-\frac{x^{3}}{6}-\sum_{n=2}^{\infty}\frac{(2n-3)!!}{(2n)!!\,(2n+1)}x^{2n+1}.
$$

---

## 三、从 $\dfrac{1}{\sqrt{1+x}}$ 出发（最有用）

### 1. 换 $x\to -x^{2}$，得 $\dfrac{1}{\sqrt{1-x^{2}}}$

把 $(-1)^{n}(-x^{2})^{n}=(-1)^{n}(-1)^{n}x^{2n}=x^{2n}$，**所有负号消失**：
$$
\boxed{\,\frac{1}{\sqrt{1-x^{2}}}=1+\sum_{n=1}^{\infty}\frac{(2n-1)!!}{(2n)!!}\,x^{2n}=\sum_{n=0}^{\infty}\frac{(2n)!}{4^{n}(n!)^{2}}x^{2n},\quad |x|<1.\,}
$$

（这里用到 $(2n-1)!!\,(2n)!!=(2n)!$，且 $(2n)!!=2^{n}n!$。）

### 2. 积分 → $\arcsin x$ 的级数

$$
\arcsin x=\int_{0}^{x}\frac{dt}{\sqrt{1-t^{2}}}=\sum_{n=0}^{\infty}\frac{(2n-1)!!}{(2n)!!\,(2n+1)}\,x^{2n+1},\quad x\in[-1,1].
$$

或写成
$$
\arcsin x=\sum_{n=0}^{\infty}\frac{(2n)!}{4^{n}(n!)^{2}(2n+1)}\,x^{2n+1}=x+\frac{x^{3}}{6}+\frac{3x^{5}}{40}+\frac{15x^{7}}{336}+\cdots.
$$

特别地，取 $x=\tfrac12$ 可算 $\pi/6$；取 $x=1$ 可算 $\pi/2$（虽然收敛极慢）。

---

## 四、一张图总结「再走一步」的脉络

$$
\begin{array}{ccc}
\dfrac{1}{1+x} & \xrightarrow{\ x\to x^{2}\ } & \dfrac{1}{1+x^{2}}\xrightarrow{\ \int\ }\arctan x \\[4pt]
\Big\downarrow\int & & \\[4pt]
\ln(1+x) & & \\[10pt]
\dfrac{1}{\sqrt{1+x}} & \xrightarrow{\ x\to -x^{2}\ } & \dfrac{1}{\sqrt{1-x^{2}}}\xrightarrow{\ \int\ }\arcsin x \\[10pt]
\sqrt{1+x} & \xrightarrow{\ x\to -x^{2}\ } & \sqrt{1-x^{2}}\xrightarrow{\ \int\ }\tfrac12\bigl(x\sqrt{1-x^{2}}+\arcsin x\bigr)
\end{array}
$$

---

## 五、几点提醒

1. **逐项积分的合法性**：幂级数在收敛区间内部一致收敛（对任一闭子区间），所以可以逐项积分；积分后收敛半径不变，但**端点收敛性**可能改善（例如 $\ln(1+x)$ 在 $x=1$ 处收敛、$\arctan x$ 在 $x=\pm 1$ 处收敛）。
2. **系数化简的小技巧**：
   - $(2n)!!=2^{n}\,n!$；
   - $(2n-1)!!=\dfrac{(2n)!}{2^{n}\,n!}$；
   - 因此 $\dfrac{(2n-1)!!}{(2n)!!}=\dfrac{(2n)!}{4^{n}(n!)^{2}}=\dfrac{1}{4^{n}}\dbinom{2n}{n}$。
3. **统一记号**：所有这些都不过是 $\alpha=\pm 1,\ \pm\tfrac12$ 的广义二项式级数，再加上「代换 + 积分」两种操作；掌握这两步，几乎所有常见初等函数的麦克劳林级数都能现场推出。