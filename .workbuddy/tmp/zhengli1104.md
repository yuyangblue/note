# 幂法的加速与收缩方法 · 整理版逐字稿

2026 年 11 月 4 日课堂。原文为语音转写，本稿逐句校订：改正转写错误（"密码法／密码迭代"→幂法、"法密法／法律法"→反幂法、"拉姆达"→$\lambda$、"锐意商／瑞利杀／润商"→瑞利商、"密集"→幂法、"颅顶"→收缩、"direction 方法"→Wielandt 方法等），删去重复与口头填充，按板书补全推导。板书照片在 `桌面\计算方法与优化\计算方法与优化课程实录\11.04\`，共 17 张。

这一讲的主线是：幂法只能算一个特征值（按模最大的或按模最小的），而且 $|\lambda_2/\lambda_1|$ 接近 1 时慢得没法用。于是要做三件事——**移动原点**改变比值、**换一个估计特征值的方式**（瑞利商）、**把已经算出来的特征值剥掉**，让下一个顶上来。

## 一、为什么需要加速

先把问题摆清楚。幂法收敛速度由比值 $r=|\lambda_2/\lambda_1|$ 决定，$r\to1$ 时每步只把误差压一点点，要几十上百步才收敛。反幂法同理，比值是 $|\lambda_{n-1}/\lambda_n|$。

加速的思路只有一个：**不改迭代格式，改矩阵**，让新的比值比原来小。

## 二、原点位移：把原点搬到特征值旁边

### 2.1 矩阵层面

设 $A\in\mathbb{R}^{n\times n}$，特征值按模排好：

$$
|\lambda_1|>|\lambda_2|\ge|\lambda_3|\ge\cdots\ge|\lambda_{n-1}|>|\lambda_n|.
$$

取一个实数 $\mu$，作

$$
B=A-\mu I .
$$

这一步在矩阵上做的事很具体：**对角元每一个都减去 $\mu$，非对角元一个都不动**。于是 $B$ 的特征值是

$$
\lambda_1-\mu,\ \lambda_2-\mu,\ \dots,\ \lambda_n-\mu,
$$

特征向量和 $A$ 完全一样（因为 $A\vec x=\lambda\vec x$ 两边减去 $\mu\vec x$ 就是 $B\vec x=(\lambda-\mu)\vec x$）。

再取逆，$(A-\mu I)^{-1}$ 的特征值是

$$
\frac{1}{\lambda_1-\mu},\ \frac{1}{\lambda_2-\mu},\ \dots,\ \frac{1}{\lambda_n-\mu}.
$$

关键就在这一步。如果我们取 $\mu$ 非常靠近 $\lambda_n$，那么 $\lambda_n-\mu$ 是一个很小的数，它的倒数 $1/(\lambda_n-\mu)$ 就变成**按模最大**的那个特征值。于是拿 $(A-\mu I)^{-1}$ 去做幂法（也就是反幂法），主特征值就是 $1/(\lambda_n-\mu)$，反解出 $\lambda_n$ 就得到了最小的特征值。

$\mu$ 越靠近 $\lambda_n$，$|\lambda_n-\mu|$ 越小，$1/(\lambda_n-\mu)$ 越大，和其他特征值的差距拉得越开，收敛越快。这就是**原点位移**这个名字的来历——相当于把坐标原点搬到 $\mu$ 那个位置去看整条实轴。

### 2.2 收敛速度

原来用反幂法算 $\lambda_n$，收敛比值是

$$
\frac{|\lambda_n|}{|\lambda_{n-1}|}.
$$

加了位移之后，收敛比值变成

$$
\frac{|\lambda_n-\mu|}{|\lambda_{n-1}-\mu|}.
$$

为什么这个更小？在实轴上画一下就清楚了。把 $\lambda_n$ 和 $\lambda_{n-1}$ 标在轴上，原来量的是它们到 $0$ 的距离之比；把原点搬到 $\mu$ 之后，量的是它们到 $\mu$ 的距离之比。因为 $\mu$ 紧挨着 $\lambda_n$，分子 $|\lambda_n-\mu|$ 缩得很厉害，分母 $|\lambda_{n-1}-\mu|$ 只是从 $|\lambda_{n-1}|$ 变成了 $|\lambda_{n-1}-\mu|$，缩得有限。所以比值一定变小。

极端情形：如果 $\mu$ 恰好取成 $\lambda_n$，那么 $|\lambda_n-\mu|=0$，比值是 $0$，**一步就收敛**。实际计算里 $\mu$ 只能取近似值，所以比值是个很小的正数，几步也能收敛。

同样的道理对幂法也成立，只是方向相反：想算按模最大的 $\lambda_1$，就取 $\mu$ 靠近 $\lambda_1$，让 $|\lambda_1-\mu|$ 远小于 $|\lambda_2-\mu|$ 等其余各项。

$$
\text{幂法：}\ \frac{|\lambda_2-\mu|}{|\lambda_1-\mu|},\qquad
\text{反幂法：}\ \frac{|\lambda_n-\mu|}{|\lambda_{n-1}-\mu|}.
$$

### 2.3 幂法与反幂法是对称的

这里要点一句：**原点位移对幂法和反幂法是同一套技术**，区别只在于把原点搬到哪一端。

由此还能推出一个求全部特征值的策略：先用反幂法（带位移）算出按模最小的 $\lambda_n$，再想办法把它从矩阵里去掉，剩下的矩阵最小的就是 $\lambda_{n-1}$，再算，再剥……一层层往上，直到全部算完。反过来，先算最大的再往下剥也一样。这个"去掉"的动作就是本讲后半的**收缩方法**。

课上还提到，实际计算里 $\mu$ 取多少也有讲究，甚至可以在迭代过程中动态调整。这一点在后面的 QR 方法里还会遇到（带原点位移的 QR 方法）。

## 三、瑞利商：换一个估计特征值的方式

### 3.1 定义与一个显然的事实

对任意非零向量 $\vec x\in\mathbb{R}^n$，定义

$$
\lambda(\vec x)=\frac{\vec x^{T}A\vec x}{\vec x^{T}\vec x}.
$$

这叫 $\vec x$ 的**瑞利商**。注意它对任意向量都有定义，随便给一个非零向量代进去都能算出一个数；问题是这个数有没有用。

先看一个特殊情形：如果 $\vec x$ 恰好是 $A$ 关于 $\lambda$ 的特征向量，那么 $A\vec x=\lambda\vec x$，代进去

$$
\lambda(\vec x)=\frac{\vec x^{T}(\lambda\vec x)}{\vec x^{T}\vec x}=\lambda\frac{\vec x^{T}\vec x}{\vec x^{T}\vec x}=\lambda .
$$

所以**在特征向量处，瑞利商精确等于特征值**。这一点从表达式上一眼能看出来。

### 3.2 当向量不是特征向量时

麻烦在于，幂法每一步得到的只是一个**近似** $\vec v$，它不是特征向量。这时特征值方程

$$
\vec x\,\lambda=A\vec x
$$

就不严格成立了——左边和右边差一截。

这个方程要看清它的形状。$\vec x$ 是已知的 $n$ 维向量，$\lambda$ 是未知的一个数，$A\vec x$ 是已知的 $n$ 维向量（把 $\vec x$ 代进去就能算出来）。所以这是

$$
\underbrace{\vec x}_{\text{系数矩阵 }n\times1}\cdot\underbrace{\lambda}_{\text{一个未知数}}=\underbrace{A\vec x}_{\text{右端项 }n\times1}.
$$

**$n$ 个方程、$1$ 个未知数**——一个超定方程组。如果 $\vec x$ 真是特征向量，它有精确解；否则无解。

无解不代表不能处理。处理超定方程组的常规办法是最小二乘：求 $\lambda$ 使 $\|A\vec x-\vec x\lambda\|_2$ 最小。

### 3.3 法方程给回瑞利商

把问题写成标准形式。用记号 $\vec b$ 表示系数向量（这里是 $\vec x$），$y$ 表示未知数（这里是 $\lambda$），$\vec c$ 表示右端（这里是 $A\vec x$），问题是

$$
\vec b\,y=\vec c .
$$

最小二乘的法方程是 $\vec b^{T}\vec b\,y=\vec b^{T}\vec c$。代回来：

$$
\vec x^{T}\vec x\,\lambda=\vec x^{T}A\vec x
\quad\Longrightarrow\quad
\lambda=\frac{\vec x^{T}A\vec x}{\vec x^{T}\vec x}.
$$

**绕一圈又回到了瑞利商。** 也就是说，瑞利商不是拍脑袋定义的，它就是"把近似的 $\vec x$ 代进特征值方程、用最小二乘求那个 $\lambda$"的解。

这一步的意义在于：它给了瑞利商一个解释，也给了它一个地位——它是**用当前向量能给出的最好的特征值估计**（在最小二乘意义下）。

和原来幂法的做法比一下：原来是把 $\vec v^{(k)}$ 里按模最大的那个分量直接拿出来当特征值。那是一个很粗糙的估计，只是利用了"规范化之后最大分量等于 $\lambda_1$"这个性质。瑞利商不一样——它用了**整个向量**的所有分量，而不是一个分量。这是它更准的原因。

要强调的是：**瑞利商迭代没有改变幂法的迭代方式，改变的是算特征值的方式**。$\vec v^{(k)}$ 还是那样一步一步乘出来的，只是在每一步，读特征值的公式从"取最大分量"换成了"算瑞利商"。

## 四、瑞利商为什么「最优」

上面说瑞利商是"最好的估计"，这话得证明。结论是：

$$
\lambda(\vec x)-\lambda_1=O\big(\|\vec x-\vec v_1\|^2\big),
$$

而幂法本身给的是 $\|\vec v^{(k)}-\vec v_1\|=O(|\lambda_2/\lambda_1|^k)$。两个一合，特征值的误差变成 $O(|\lambda_2/\lambda_1|^{2k})$——**误差被平方了**。这就是瑞利商加速的全部来源。

为什么会有平方？因为 $\lambda(\vec x)$ 在 $\vec v_1$ 处的**梯度是零**。一个函数在极值点附近，一阶项消失，误差就从一阶降到二阶。

### 4.1 梯度为零

设 $\vec v_1$ 是 $A$ 关于 $\lambda_1$ 的特征向量。把 $\lambda(\vec x)$ 在 $\vec v_1$ 处做多元泰勒展开：

$$
\lambda(\vec x)=\lambda(\vec v_1)+(\vec x-\vec v_1)^{T}\nabla\lambda(\vec v_1)+O\big(\|\vec x-\vec v_1\|_2^2\big).
$$

只要证明 $\nabla\lambda(\vec v_1)=\vec 0$，第一项之后的一阶项就整个消失。

求梯度。设分子 $N=\vec x^{T}A\vec x$、分母 $D=\vec x^{T}\vec x$，用商法则：

$$
\nabla\lambda(\vec x)
=\frac{\nabla(\vec x^{T}A\vec x)\cdot(\vec x^{T}\vec x)-(\vec x^{T}A\vec x)\cdot\nabla(\vec x^{T}\vec x)}{(\vec x^{T}\vec x)^2}.
$$

其中 $\nabla(\vec x^{T}A\vec x)=2A\vec x$（$A$ 对称时），$\nabla(\vec x^{T}\vec x)=2\vec x$。代入：

$$
\nabla\lambda(\vec x)
=\frac{2A\vec x\cdot(\vec x^{T}\vec x)-(\vec x^{T}A\vec x)\cdot2\vec x}{(\vec x^{T}\vec x)^2}
=\frac{2}{\vec x^{T}\vec x}\Big(A\vec x-\frac{\vec x^{T}A\vec x}{\vec x^{T}\vec x}\vec x\Big)
=\frac{2}{\vec x^{T}\vec x}\big(A\vec x-\lambda(\vec x)\vec x\big).
$$

括号里那一项，在 $\vec x=\vec v_1$ 时是 $A\vec v_1-\lambda_1\vec v_1=\vec 0$。所以

$$
\nabla\lambda(\vec v_1)=\vec 0 .
$$

### 4.2 误差变成平方

有了 $\nabla\lambda(\vec v_1)=\vec 0$，泰勒展开的一阶项整块消失，而且 $\lambda(\vec v_1)=\lambda_1$，于是

$$
\lambda(\vec x)-\lambda_1=O\big(\|\vec x-\vec v_1\|_2^2\big).
$$

再代入幂法的方向误差 $\|\vec v^{(k)}-\vec v_1\|_2=O(|\lambda_2/\lambda_1|^k)$：

$$
\lambda(\vec v^{(k)})-\lambda_1=O\Big(\big|\tfrac{\lambda_2}{\lambda_1}\big|^{2k}\Big).
$$

对比一下：

| 量 | 误差阶 |
| --- | --- |
| 幂法给的方向 $\vec v^{(k)}$ | $O(|\lambda_2/\lambda_1|^k)$ |
| 最大分量读出的特征值 | $O(|\lambda_2/\lambda_1|^k)$ |
| 瑞利商读出的特征值 | $O(|\lambda_2/\lambda_1|^{2k})$ |

**同样的迭代序列，只是换了读法，精度就翻了一倍。** 如果 $|\lambda_2/\lambda_1|=0.8$，迭代 $10$ 步方向上有 $0.8^{10}\approx0.107$ 的误差，瑞利商给出的特征值误差只有 $0.8^{20}\approx0.0115$，差一个数量级；迭代 $20$ 步差距拉到一个半数量级。

这个"误差平方"的现象不是瑞利商独有的——它其实是一般规律：**任何在极值点处一阶导数为零的估计量，都会把误差平方**。非线性方程那边的 Aitken 加速、Steffensen 迭代，本质上是同一件事。

## 五、两个加速算法

### 5.1 算法一：幂法套上瑞利商

既然特征值改用瑞利商来读，那规范化那一步就**不必再用无穷范数**了。

原来用无穷范数是有原因的：除以最大分量之后，最大分量恒等于 $1$，而这个数正好可以当作 $\lambda_1$ 的估计。现在特征值从瑞利商读，规范化就只剩下"控制长度别溢出"这一个作用，用哪个范数都行。用 $2$-范数更方便——因为瑞利商的分母是 $\vec x^{T}\vec x$，如果先让 $\|\vec v\|_2=1$，分母就等于 $1$，可以直接省掉。

算法：

给定 $\vec v^{(0)}$，对 $k=0,1,2,\dots$：

$$
\begin{cases}
\vec z^{(k+1)}=A\vec v^{(k)},\\[4pt]
\vec v^{(k+1)}=\dfrac{\vec z^{(k+1)}}{\|\vec z^{(k+1)}\|_2},\\[8pt]
\lambda^{(k+1)}=(\vec v^{(k+1)})^{T}A\vec v^{(k+1)} .
\end{cases}
$$

第 3 步因为 $\|\vec v^{(k+1)}\|_2=1$，分母为 $1$，所以只剩分子。

**一个计算上的优化**：注意第 1 步算 $A\vec v^{(k)}$，第 3 步又要算 $A\vec v^{(k+1)}$；而下一轮的第 1 步算的正是 $A\vec v^{(k+1)}$——**同一个矩阵向量乘被算了两次**。矩阵向量乘是这整个循环里最费时的运算，省一次很划算。

做法是引入一个中间向量记住它：

$$
\vec m^{(k+1)}=A\vec v^{(k)},\qquad
\vec v^{(k+1)}=\frac{\vec m^{(k+1)}}{\|\vec m^{(k+1)}\|_2},\qquad
\lambda^{(k+1)}=(\vec v^{(k+1)})^{T}\vec m^{(k+1)} .
$$

下一轮开头 $\vec z^{(k+2)}=A\vec v^{(k+1)}$ 直接就是新的 $\vec m$，不用再乘。于是每轮只做一次矩阵向量乘。

这类"把上一步算过的东西留下来"的优化，从原理上说不做也行，但从计算量上必须做——写实现的时候要习惯看一遍循环，找出哪一步可以复用到下一轮。

### 5.2 算法二：瑞利商迭代

把瑞利商和反幂法、原点位移三样结合起来，就是**瑞利商迭代**（Rayleigh quotient iteration）。

思路：反幂法要加速就得有原点位移值 $\mu$，而 $\mu$ 应该取靠近目标特征值的数；瑞利商正好每步都能给出一个特征值的估计，那就**用它当 $\mu$**。

给定 $\vec v^{(0)}$ 且 $\|\vec v^{(0)}\|_2=1$，对 $k=0,1,2,\dots$：

$$
\begin{cases}
\lambda^{(k)}=(\vec v^{(k)})^{T}A\vec v^{(k)},\\[4pt]
\text{解}\ \ (A-\lambda^{(k)}I)\vec z^{(k+1)}=\vec v^{(k)},\\[4pt]
\vec v^{(k+1)}=\dfrac{\vec z^{(k+1)}}{\|\vec z^{(k+1)}\|_2}.
\end{cases}
$$

第 2 步是解一个线性方程组，系数矩阵每轮都在变（因为 $\lambda^{(k)}$ 在变），这是它的主要代价。

它为什么快：如果 $\vec v^{(k)}$ 已经接近某个特征向量 $\vec v_j$，那么 $\lambda^{(k)}\approx\lambda_j$，于是 $A-\lambda^{(k)}I$ 有一个特征值 $\lambda_j-\lambda^{(k)}\approx0$，**它几乎是奇异的**；反幂法在这个矩阵上做迭代，主特征值是 $1/(\lambda_j-\lambda^{(k)})$，因为分母接近零，这个值极大，收敛极快。理论上它最终是**三次收敛**的（对称矩阵情形），比幂法加瑞利商的二阶还高一阶。

代价也明显：每步解一个线性方程组。实际实现时，如果每轮都重新做三角分解，代价很高；常见做法是只在 $\lambda^{(k)}$ 变化较大时才重新分解。

## 六、收缩方法：一次剥掉一个特征值

### 6.1 目标

幂法和它的各种加速版本，都只能算**一个**特征值——要么按模最大，要么按模最小。想算第二个、第三个怎么办？

思路是从特征多项式看。$A$ 的特征多项式是

$$
(x-\lambda_1)(x-\lambda_2)\cdots(x-\lambda_n)=0 .
$$

如果能把 $\lambda_1$ 这个根"变成零"，就相当于把因子 $(x-\lambda_1)$ 换成了 $x$：

$$
x\,(x-\lambda_2)\cdots(x-\lambda_n)=0 .
$$

这样剩下的根还是 $\lambda_2,\dots,\lambda_n$，但最大的是 $\lambda_2$ 了，幂法就能算它。算完再剥一次，$\lambda_3$ 顶上来。

所以收缩方法要解决的就是一件事：

> **给一个矩阵，把某个已知的特征值变成 $0$，同时不改变其余特征值。**

从空间的角度看，这相当于把 $n$ 维空间里对应 $\vec v_1$ 的那一维**拆掉**，剩下的 $n-1$ 维里做同样的问题。

### 6.2 前置：$A$ 与 $A^{T}$ 的特征向量正交

构造要用到一条性质。设 $\vec v_i$ 是 $A$ 关于 $\lambda_i$ 的特征向量，$\vec w_j$ 是 $A^{T}$ 关于 $\lambda_j$ 的特征向量，且 $\lambda_i\ne\lambda_j$，则

$$
\vec v_i^{T}\vec w_j=0 .
$$

证明只有四行。由 $A\vec v_i=\lambda_i\vec v_i$ 两边转置得 $\vec v_i^{T}A^{T}=\lambda_i\vec v_i^{T}$，再右乘 $\vec w_j$：

$$
\vec v_i^{T}A^{T}\vec w_j=\lambda_i\,\vec v_i^{T}\vec w_j .
$$

左边用 $A^{T}\vec w_j=\lambda_j\vec w_j$ 换掉：

$$
\lambda_j\,\vec v_i^{T}\vec w_j=\lambda_i\,\vec v_i^{T}\vec w_j
\quad\Longrightarrow\quad
(\lambda_j-\lambda_i)\,\vec v_i^{T}\vec w_j=0 .
$$

因为 $\lambda_i\ne\lambda_j$，只能是 $\vec v_i^{T}\vec w_j=0$。

这里要说清楚一件事：$A$ 和 $A^{T}$ 的**特征值相同**（特征多项式一样），但**特征向量不同**。上面这条说的是"$A$ 的第 $i$ 个特征向量"和"$A^{T}$ 的第 $j$ 个特征向量"在 $i\ne j$ 时正交。注意它不是通常说的"不同特征值的特征向量正交"——那个结论只对正规矩阵（比如对称矩阵）成立，一般矩阵不成立，所以这里要绕到 $A^{T}$ 上去。

### 6.3 构造 $B$ 与它的两条性质

取

$$
B=A-\lambda_1\vec v_1\vec x^{T},
$$

其中 $\vec x$ 待定，要求满足 $\vec x^{T}\vec v_1=1$。

这是一个**秩一修正**：$A$ 减掉一个秩一矩阵 $\lambda_1\vec v_1\vec x^{T}$。

**性质一：$B$ 有特征值 $0$。** 把 $B$ 作用在 $\vec v_1$ 上：

$$
B\vec v_1=A\vec v_1-\lambda_1\vec v_1\vec x^{T}\vec v_1
=\lambda_1\vec v_1-\lambda_1\vec v_1\cdot1
=\lambda_1\vec v_1\,(1-\vec x^{T}\vec v_1)=\vec 0 .
$$

所以 $\vec v_1$ 是 $B$ 关于特征值 $0$ 的特征向量。原来 $\lambda_1$ 那个位置被换成了 $0$。

**性质二：$B$ 的其余特征值不变。** 这次要看 $B^{T}$：

$$
B^{T}=(A-\lambda_1\vec v_1\vec x^{T})^{T}=A^{T}-\lambda_1\vec x\vec v_1^{T}.
$$

把它作用在 $A^{T}$ 的特征向量 $\vec w_i$（$i\ne1$）上：

$$
B^{T}\vec w_i=A^{T}\vec w_i-\lambda_1\vec x\,\vec v_1^{T}\vec w_i .
$$

由 6.2 那条正交性，$i\ne1$ 时 $\vec v_1^{T}\vec w_i=0$，第二项整个消失：

$$
B^{T}\vec w_i=A^{T}\vec w_i=\lambda_i\vec w_i .
$$

所以 $\lambda_i$（$i\ne1$）也是 $B^{T}$ 的特征值，而 $B^{T}$ 与 $B$ 特征值相同，于是 $B$ 的其余特征值就是 $\lambda_2,\dots,\lambda_n$。

两条合起来：$B$ 的特征值是 $0,\lambda_2,\dots,\lambda_n$。

另外还有一个附带结论：$B$ 有两个零化方向（一个是 $\vec v_1$ 被 $B$ 打成零），秩至多是 $n-1$。如果 $\lambda_1$ 是单根，$\operatorname{rank}(B)=n-1$。

### 6.4 特征向量怎么还原

问题来了：在 $B$ 上算出来的特征向量是 $B$ 的，不是 $A$ 的。要用回去就得把关系找出来。

$B$ 的特征向量记作 $\vec u_2,\dots,\vec u_n$（$n-1$ 个，对应 $\lambda_2,\dots,\lambda_n$），再加上 $\vec v_1$（对应 $0$）。

设 $A$ 的特征向量 $\vec v_i$ 可以写成

$$
\vec v_i=\alpha\vec u_i+\beta\vec v_1,\qquad i=2,3,\dots,n .
$$

这个假设是否成立，靠推出来的 $\alpha,\beta$ 能取到实数来验证。

把 $B$ 作用上去：

$$
B\vec v_i=(A-\lambda_1\vec v_1\vec x^{T})\vec v_i=A\vec v_i-\lambda_1\vec v_1\,(\vec x^{T}\vec v_i).
$$

代入 $\vec v_i=\alpha\vec u_i+\beta\vec v_1$，注意 $\vec x^{T}\vec v_1=1$：

$$
B\vec v_i=A\vec v_i-\lambda_1\vec v_1\big(\alpha\,\vec x^{T}\vec u_i+\beta\big)
=A\vec v_i-\alpha\lambda_1(\vec x^{T}\vec u_i)\vec v_1-\beta\lambda_1\vec v_1 .
$$

另一方面，由 $B\vec v_i=B(\alpha\vec u_i+\beta\vec v_1)=\alpha B\vec u_i+\beta B\vec v_1$，而 $B\vec u_i=\lambda_i\vec u_i$、$B\vec v_1=\vec 0$：

$$
B\vec v_i=\alpha\lambda_i\vec u_i .
$$

两边相等：

$$
A\vec v_i-\alpha\lambda_1(\vec x^{T}\vec u_i)\vec v_1-\beta\lambda_1\vec v_1=\alpha\lambda_i\vec u_i .
$$

再把 $A\vec v_i=\lambda_i\vec v_i=\lambda_i(\alpha\vec u_i+\beta\vec v_1)$ 代进左边：

$$
\lambda_i\alpha\vec u_i+\lambda_i\beta\vec v_1-\alpha\lambda_1(\vec x^{T}\vec u_i)\vec v_1-\beta\lambda_1\vec v_1=\alpha\lambda_i\vec u_i .
$$

两边的 $\alpha\lambda_i\vec u_i$ 消掉，剩下全在 $\vec v_1$ 方向上：

$$
\big[\beta(\lambda_i-\lambda_1)-\alpha\lambda_1(\vec x^{T}\vec u_i)\big]\vec v_1=\vec 0 .
$$

因为 $\vec v_1\ne\vec 0$，方括号里必须为零。取

$$
\alpha=\lambda_i-\lambda_1,\qquad \beta=\lambda_1(\vec x^{T}\vec u_i),
$$

等式就严格成立。于是

$$
\vec v_i=(\lambda_i-\lambda_1)\vec u_i+\lambda_1(\vec x^{T}\vec u_i)\,\vec v_1 .
$$

反过来解 $\vec u_i$：

$$
\vec u_i=\frac{1}{\lambda_i-\lambda_1}\vec v_i-\frac{\lambda_1(\vec x^{T}\vec u_i)}{\lambda_i-\lambda_1}\vec v_1 .
$$

这两个式子说明：**$B$ 的特征向量和 $A$ 的特征向量张成同一个二维平面**（由 $\vec u_i$ 和 $\vec v_1$ 撑起来）。要从 $\vec u_i$ 还原 $\vec v_i$，只需要知道 $\lambda_i$、$\lambda_1$、$\vec x$ 和 $\vec v_1$——这些在算 $B$ 的时候都有了。

代价是：每剥一层，还原就要多套一层公式。所以实际计算中，如果只要特征值不在乎特征向量，可以不做还原；要特征向量的话，剥了几层就得往回套几次。

### 6.5 $\vec x$ 怎么取：Wielandt 的选择

回到那个待定的 $\vec x$。理论上的要求只有一条：$\vec x^{T}\vec v_1=1$。满足它的 $\vec x$ 有无穷多个。

Wielandt 给了一个具体取法，好处是**不用另外算 $\vec x$，直接从 $A$ 里取一行**。

取 $A$ 的第 $k$ 行的转置，再除以一个数：

$$
\vec x=\frac{1}{\lambda_1 v_{1,k}}\,[a_{k1},a_{k2},\dots,a_{kn}]^{T},
$$

其中 $v_{1,k}$ 是 $\vec v_1$ 的第 $k$ 个分量。

验证 $\vec x^{T}\vec v_1=1$：

$$
\vec x^{T}\vec v_1=\frac{1}{\lambda_1v_{1,k}}\,[a_{k1},\dots,a_{kn}]\,\vec v_1
=\frac{1}{\lambda_1v_{1,k}}\,(A\vec v_1)_k
=\frac{1}{\lambda_1v_{1,k}}\cdot\lambda_1v_{1,k}=1 .
$$

中间一步用的是"$A$ 乘 $\vec v_1$ 的第 $k$ 个分量就是 $A$ 的第 $k$ 行乘 $\vec v_1$"，而 $A\vec v_1=\lambda_1\vec v_1$，所以那个分量等于 $\lambda_1v_{1,k}$。

$k$ 怎么选？理论上任意，只要 $v_{1,k}\ne0$ 就能放进分母。实际为了数值稳定，**取 $|\vec v_1|$ 中绝对值最大的分量所对应的位置**——分母最大，$1/v_{1,k}$ 最小，舍入误差的影响最小。

这个取法还有一个漂亮的副作用：$\vec x$ 是 $A$ 的某一行的倍数，而 $B=A-\lambda_1\vec v_1\vec x^{T}$ 的第 $k$ 行是

$$
B_{k\cdot}=A_{k\cdot}-\lambda_1v_{1,k}\,\vec x^{T}=A_{k\cdot}-A_{k\cdot}=\vec 0 .
$$

**第 $k$ 行整行变成零。** 于是 $B$ 的第 $k$ 行可以直接划掉，问题降成 $(n-1)\times(n-1)$。这正是"降阶"这个说法的实际内容。

### 6.6 一个完整例子

$$
A=\begin{pmatrix}
11 & -6 & 4 & -2\\
4 & 1 & 0 & 0\\
-9 & 9 & -6 & 5\\
-6 & 6 & -6 & 7
\end{pmatrix},
$$

它的四个特征值是 $5,4,3,1$。

**第一步，幂法求主特征值。** 幂法给出

$$
\lambda_1=5,\qquad \vec v_1=(1,1,0,0)^{T}.
$$

核对：$A\vec v_1=(11-6,\,4+1,\,-9+9,\,-6+6)^{T}=(5,5,0,0)^{T}=5\vec v_1$，对。

**第二步，定 $\vec x$。** $\vec v_1$ 的四个分量是 $1,1,0,0$，绝对值最大的是前两个，都等于 $1$。取 $k=1$，则 $v_{1,1}=1$：

$$
\vec x=\frac{1}{5\times1}\,[11,-6,4,-2]^{T}=(2.2,\,-1.2,\,0.8,\,-0.4)^{T}.
$$

**第三步，算 $B=A-\lambda_1\vec v_1\vec x^{T}$。** 注意 $\lambda_1\vec v_1\vec x^{T}=5\cdot(1,1,0,0)^{T}\cdot(2.2,-1.2,0.8,-0.4)$，只有前两行非零，且都等于 $[11,-6,4,-2]$：

$$
B=\begin{pmatrix}
11&-6&4&-2\\
4&1&0&0\\
-9&9&-6&5\\
-6&6&-6&7
\end{pmatrix}
-\begin{pmatrix}
11&-6&4&-2\\
11&-6&4&-2\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}
=\begin{pmatrix}
0&0&0&0\\
-7&7&-4&2\\
-9&9&-6&5\\
-6&6&-6&7
\end{pmatrix}.
$$

第一行整行是零，和 6.5 的结论一致。

**第四步，划掉第一行第一列，降成 $3\times3$：**

$$
B'=\begin{pmatrix}
7&-4&2\\
9&-6&5\\
6&-6&7
\end{pmatrix}.
$$

$B'$ 的特征值是 $4,3,1$。对它再用幂法：

$$
\lambda_2=4,\qquad \vec v_2'=(0,\tfrac12,1)^{T}.
$$

**第五步，还原特征向量。** 先把 $\vec v_2'$ 补回四维。因为划掉的是第 $1$ 行第 $1$ 列，补的就是第 $1$ 个分量，补零：

$$
\vec u_2=(0,\,0,\,\tfrac12,\,1)^{T}.
$$

再用 6.4 的公式 $\vec v_2=(\lambda_2-\lambda_1)\vec u_2+\lambda_1(\vec x^{T}\vec u_2)\vec v_1$：

$$
\vec x^{T}\vec u_2=2.2\times0+(-1.2)\times0+0.8\times\tfrac12+(-0.4)\times1=0.4-0.4=0,
$$

$$
\vec v_2=(4-5)\vec u_2+5\times0\cdot\vec v_1=(0,\,0,\,-\tfrac12,\,-1)^{T}.
$$

核对：$A\vec v_2=(0,0,-2,-4)^{T}=4\vec v_2$，对。

**往下继续。** 对 $B'$ 再剥一次，得到 $2\times2$ 的矩阵，特征值 $3,1$，幂法算出 $3$，再剥得 $1$。整个过程就是"算一个、剥一个、降一阶"。

注意一件事：每剥一次，后续的还原公式就多套一层。如果只要特征值，不管特征向量，那就省掉全部还原步骤，只要一路幂法加剥。

### 6.7 另一种收缩：相似变换

上面用的是秩一修正。还有一条路是**相似变换**。

目标同样是把 $\lambda_1$ 从这个矩阵里"隔出去"，但做法是找一个 $M$，使

$$
B=MAM^{-1}=\begin{pmatrix}\lambda_1 & \vec m\\ \vec 0 & B_1\end{pmatrix}.
$$

这样 $B$ 是分块上三角，它的特征值就是 $\lambda_1$ 加上 $B_1$ 的特征值，所以 $B_1$ 的特征值正好是 $\lambda_2,\dots,\lambda_n$。问题降成 $n-1$ 阶，而且不需要"补回"什么，因为相似变换不改变特征值，$B_1$ 直接就是新的问题。

$M$ 怎么取？想让 $B$ 的第一列除对角元外全为零，相当于要求

$$
B\vec e_1=\lambda_1\vec e_1,\qquad \vec e_1=(1,0,\dots,0)^{T}.
$$

而 $B=MAM^{-1}$，所以 $MAM^{-1}\vec e_1=\lambda_1\vec e_1$，两边左乘 $M^{-1}$：

$$
A\,(M^{-1}\vec e_1)=\lambda_1\,(M^{-1}\vec e_1).
$$

也就是说 $M^{-1}\vec e_1$ 必须是 $A$ 关于 $\lambda_1$ 的特征向量，即 $M^{-1}\vec e_1=\vec v_1$（差一个常数倍无妨），于是 $M\vec v_1=\vec e_1$。

这样的 $M$ 是存在的：取 $\vec v_1$ 和一个单位向量 $\vec e_1$，总能用初等变换（相当于把 $\vec v_1$ 那一段旋转到 $\vec e_1$ 方向）构造出来。构造好之后，$B$ 的第一列就只剩左上角那个 $\lambda_1$。

这条路比秩一修正"干净"——降阶之后不用还原特征向量，因为相似变换保特征值。代价是要把 $M$ 和 $M^{-1}$ 都乘出来，计算量大一些。

## 七、下次课

下一次讲**QR 迭代**。它的做法简单到只有两步：把矩阵做 QR 分解 $A=QR$，再把 $R$ 和 $Q$ 换位置乘起来得到新矩阵 $RQ$；对新矩阵再做 QR 分解，再交换乘起来……不断重复，最后几乎所有特征值都会出现在对角线上。

方法本身三句话能说完，但细节不少：怎么让它跑得快、带原点位移的 QR 怎么设计、上 Hessenberg 矩阵为什么要先约化、实矩阵出现复特征值时怎么用双步。这些下次讨论。

另外，这一讲说的原点位移、瑞利商估计，到 QR 那里会再出现一次——带原点位移的 QR 方法，那个位移量就是用瑞利商来取的。
