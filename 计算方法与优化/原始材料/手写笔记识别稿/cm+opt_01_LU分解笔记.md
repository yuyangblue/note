# LU 分解（Doolittle 直接三角分解）笔记

> 来源：手写笔记 `cm+opt_lu.pdf`（共 2 页）。
> 本笔记逐页忠实转录原文内容与批注，公式保持原样；括号内为原文旁注。

---

## 第 1 页

对 $A$ 作带状划分（列带与行带示意）：

- 列带：$a_{1j}\ (j\ge 1)$；$a_{2j}\ (j\ge 2)$；$\cdots$；$a_{kj}\ (k\le j)$；$\cdots$；末尾 $a_{n-1,n}$、$a_{nn}$。
- 行带：$a_{i1}\ (i>1)$；$a_{i2}\ (i>2)$；$\cdots$；$a_{ik}\ (i>k)$；$\cdots$；$a_{n,n-1}$。

即（原文图示）：

$$
A=\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1k} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2k} & \cdots & a_{2n}\\
\vdots & \vdots & & \vdots & & \vdots\\
a_{k1} & a_{k2} & \cdots & a_{kk} & \cdots & a_{kn}\\
\vdots & \vdots & & \vdots & & \vdots\\
a_{n1} & a_{n2} & \cdots & a_{nk} & \cdots & a_{nn}
\end{bmatrix}
$$

### 逐步比较元素（原文左侧推导）

第 (1) 步：

$$
\begin{cases}
a_{1j} = u_{1j} & (j\ge 1)\\[2pt]
a_{i1} = l_{i1}\,u_{11} & (i>1)
\end{cases}
$$

$\vdots$

第 $(k)$ 步：

$$
\begin{cases}
a_{kj} = \displaystyle\sum_{s=1}^{k-1} l_{ks}\,u_{sj} + u_{kj} & (j\ge k)\\[6pt]
a_{ik} = \displaystyle\sum_{s=1}^{k-1} l_{is}\,u_{sk} + l_{ik}\,u_{kk} & (i>k)
\end{cases}
$$

$\vdots$

于是得到（原文红色结论）：

$$
\Longrightarrow\quad
\begin{cases}
\displaystyle u_{kj} = a_{kj} - \sum_{s=1}^{k-1} l_{ks}\,u_{sj} & (j\ge k)\\[6pt]
\displaystyle l_{ik} = \Big(a_{ik} - \sum_{s=1}^{k-1} l_{is}\,u_{sk}\Big)\Big/u_{kk} & (i>k)
\end{cases}
$$

### 分解结果（原文右侧图示）

$$
L=\begin{bmatrix}
1 & & & & \\
l_{21} & 1 & & & \\
l_{31} & l_{32} & 1 & & \\
\vdots & \vdots & & \ddots & \\
l_{n1} & l_{n2} & \cdots & l_{n,n-1} & 1
\end{bmatrix},
\qquad
U=\begin{bmatrix}
u_{11} & u_{12} & \cdots & u_{1k} & \cdots & u_{1n}\\
 & u_{22} & \cdots & u_{2k} & \cdots & u_{2n}\\
 & & \ddots & \vdots & & \vdots\\
 & & & u_{kk} & \cdots & u_{kn}\\
 & & & & \ddots & \vdots\\
 & & & & & u_{nn}
\end{bmatrix}
$$

### 计算步骤（原文下方，蓝色/黑色批注）

**第 1 步：**

$$
u_{1j} = a_{1j}\,;\qquad l_{i1} = a_{i1}/u_{11}
$$

**第 2 步：**

$$
u_{2j} = a_{2j} - \sum_{s=1}^{1} l_{2s}\,u_{sj}
$$

（旁注：求和项 $l_{2s}u_{sj}$ ←「L 矩阵第 1 列」×「U 矩阵第 1 行」，即 $l_{21}\,u_{1j}$。）

$$
l_{i2} = \Big(a_{i2} - \sum_{s=1}^{1} l_{is}\cdot u_{s2}\Big)\Big/u_{22}
$$

（旁注：求和项 $l_{is}u_{s2}$ ←「L 矩阵第 1 列」×「U 矩阵第 1 行」，即 $l_{i1}\,u_{12}$。）

**第 3 步：**

$$
u_{3j} = a_{3j} - \sum_{s=1}^{2} l_{3s}\,u_{sj}
$$

（旁注：求和项 ←「L 矩阵第 1～2 列」×「U 矩阵第 1～2 行」。）

$$
l_{i3} = \Big(a_{i3} - \sum_{s=1}^{2} l_{is}\cdot u_{s3}\Big)\Big/u_{33}
$$

（旁注：求和项 ←「L 矩阵第 1～2 列」×「U 矩阵第 1～2 行」。）

---

## 第 2 页

**第 $k$ 步：**

$$
u_{kj} = a_{kj} - \sum_{s=1}^{k-1} l_{ks}\,u_{sj}
$$

（旁注：$l_{ks}$ ←「L 矩阵第 $1\sim k-1$ 列」；$u_{sj}$ ←「U 矩阵第 $1\sim k-1$ 行」。）

$$
l_{ik} = \Big(a_{ik} - \sum_{s=1}^{k-1} l_{is}\,u_{sk}\Big)\Big/u_{kk}
$$

（旁注：求和项 ←「L 矩阵第 $1\sim k-1$ 列」×「U 矩阵第 $1\sim k-1$ 行」。）

$\vdots$

**第 $n$ 步：**

$$
u_{nj}\quad (j = n)
$$

---

## 整理者说明

- 原文为手写笔记，本笔记按原文顺序逐行转录；箭头、波浪线等强调记号未逐一复现，只以文字批注形式保留其含义。
- 原文反复强调的规律：**计算 $u_{kj}$ 时，求和项由「L 的前 $k-1$ 列」与「U 的第 $j$ 列（即前 $k-1$ 行）」对应元素乘积组成；计算 $l_{ik}$ 时，求和项由「L 的第 $i$ 行（即前 $k-1$ 列）」与「U 的前 $k-1$ 行（第 $k$ 列）」对应元素乘积组成。**
