# 深度学习与高等代数常用LaTeX符号速查表

## 1. 集合论与逻辑符号

| 描述 | LaTeX代码 | 效果 |
| ------ |------ |------ |
| 属于 | `x \in A` | $x \in A$ |
| 不属于 | `x \notin A` | $x \notin A$ |
| 包含于 | `A \subseteq B` | $A \subseteq B$ |
| 真包含于 | `A \subset B` | $A \subset B$ |
| 包含 | `A \supseteq B` | $A \supseteq B$ |
| 真包含 | `A \supset B` | $A \supset B$ |
| 并集 | `A \cup B` | $A \cup B$ |
| 交集 | `A \cap B` | $A \cap B$ |
| 差集 | `A \setminus B` | $A \setminus B$ |
| 补集 | `A^c` | $A^c$ |
| 空集 | `\emptyset` | $\emptyset$ |
| 任意 | `\forall x` | $\forall x$ |
| 存在 | `\exists y` | $\exists y$ |
| 逻辑与 | `A \land B` | $A \land B$ |
| 逻辑或 | `A \lor B` | $A \lor B$ |
| 逻辑非 | `\lnot A` | $\lnot A$ |
| 等价 | `A \iff B` | $A \iff B$ |
| 蕴含 | `A \implies B` | $A \implies B$ |

## 2. 线性代数与矩阵

| 描述 | LaTeX代码 | 效果 |
| ------ |------ |------ |
| 向量 | `\mathbf{v}` | $\mathbf{v}$ |
| 矩阵 | `\mathbf{W}` | $\mathbf{W}$ |
| 转置 | `A^\top` | $A^\top$ |
| 点积 | `a \cdot b` | $a \cdot b$ |
| 叉积 | `a \times b` | $a \times b$ |
| 张量积 | `A \otimes B` | $A \otimes B$ |
| 矩阵求逆 | `A^{-1}` | $A^{-1}$ |
| 矩阵行列式 | `\det(A)` | $\det(A)$ |
| 矩阵迹 | `\operatorname{tr}(A)` | $\operatorname{tr}(A)$ |
| 范数 | `| x |_2` | $\| x \|_2$ |
| Frobenius范数 | `| A |_F` | $\| A \|_F$ |
| 矩阵维度 | `A \in \mathbb{R}^{m \times n}` | $A \in \mathbb{R}^{m \times n}$ |
| 单位矩阵 | `I` 或 `I_n` | $I$ 或 $I_n$ |
| 零矩阵 | `\mathbf{0}` | $\mathbf{0}$ |

## 3. 微积分与优化

| 描述 | LaTeX代码 | 效果 |
| ------ |------ |------ |
| 偏导数 | `\frac{\partial y}{\partial x}` | $\frac{\partial y}{\partial x}$ |
| 梯度 | `\nabla f` | $\nabla f$ |
| 拉普拉斯算子 | `\Delta u` | $\Delta u$ |
| 无穷 | `\infty` | $\infty$ |
| 求和 | `\sum_{i=1}^{n} x_i` | $\sum_{i=1}^{n} x_i$ |
| 极限 | `\lim_{x \to 0} f(x)` | $\lim_{x \to 0} f(x)$ |
| 积分 | `\int_a^b f(x) dx` | $\int_a^b f(x) dx$ |
| 损失函数 | `\mathcal{L}(\theta)` | $\mathcal{L}(\theta)$ |
| 目标函数 | `J(\theta)` | $J(\theta)$ |
| 梯度下降 | `\theta \gets \theta - \alpha \nabla_\theta \mathcal{L}` | $\theta \gets \theta - \alpha \nabla_\theta \mathcal{L}$ |
| Hessian矩阵 | `\mathbf{H}` | $\mathbf{H}$ |
| 海森矩阵 | `\nabla^2 f` | $\nabla^2 f$ |

## 4. 概率与统计

| 描述 | LaTeX代码 | 效果 |
| ------ |------ |------ |
| 概率 | `P(A)` 或 `\Pr(A)` | $P(A)$ |
| 条件概率 | `P(A \mid B)` | $P(A \mid B)$ |
| 联合概率 | `P(A, B)` | $P(A, B)$ |
| 期望 | `\mathbb{E}[X]` | $\mathbb{E}[X]$ |
| 条件期望 | `\mathbb{E}[X \mid Y]` | $\mathbb{E}[X \mid Y]$ |
| 方差 | `\operatorname{Var}(X)` | $\operatorname{Var}(X)$ |
| 标准差 | `\sigma_X` | $\sigma_X$ |
| 协方差 | `\operatorname{Cov}(X, Y)` | $\operatorname{Cov}(X, Y)$ |
| 相关系数 | `\rho_{X,Y}` | $\rho_{X,Y}$ |
| 独立 | `X \perp\!\!\!\perp Y` | $X \perp\!\!\!\perp Y$ |
| 正态分布 | `\mathcal{N}(\mu, \sigma^2)` | $\mathcal{N}(\mu, \sigma^2)$ |
| 伯努利分布 | `\text{Bern}(p)` | $\text{Bern}(p)$ |
| 二项分布 | `\text{Bin}(n,p)` | $\text{Bin}(n,p)$ |
| 均匀分布 | `\text{Unif}(a,b)` | $\text{Unif}(a,b)$ |
| 概率密度函数 | `p(x)` | $p(x)$ |
| 累积分布函数 | `F(x)` | $F(x)$ |

## 5. 常用函数与运算符

| 描述 | LaTeX代码 | 效果 |
| ------ |------ |------ |
| 最大值 | `\max(x)` | $\max(x)$ |
| 最小值 | `\min(x)` | $\min(x)$ |
| 上确界 | `\sup S` | $\sup S$ |
| 下确界 | `\inf S` | $\inf S$ |
| sigmoid函数 | `\sigma(x)` | $\sigma(x)$ |
| ReLU函数 | `\text{ReLU}(x)` | $\text{ReLU}(x)$ |
| Softmax函数 | `\operatorname{softmax}(z)` | $\operatorname{softmax}(z)$ |
| 对数 | `\log(x)` | $\log(x)$ |
| 自然对数 | `\ln(x)` | $\ln(x)$ |
| 指数 | `\exp(x)` | $\exp(x)$ |
| 绝对值 | `\lvert x \rvert` | $\lvert x \rvert$ |
| 向上取整 | `\lceil x \rceil` | $\lceil x \rceil$ |
| 向下取整 | `\lfloor x \rfloor` | $\lfloor x \rfloor$ |
| 指示函数 | `\mathbb{I}[condition]` | $\mathbb{I}[condition]$ |

## 6. 常用字母变体

| 描述 | LaTeX代码 | 效果 |
| ------ |------ |------ |
| 黑板粗体 (数域) | `\mathbb{R}` | $\mathbb{R}$ |
| `\mathbb{C}` | $\mathbb{C}$ |  |
| `\mathbb{N}` | $\mathbb{N}$ |  |
| `\mathbb{Z}` | $\mathbb{Z}$ |  |
| 花体 | `\mathcal{F}` | $\mathcal{F}$ |
| `\mathcal{L}` | $\mathcal{L}$ |  |
| `\mathcal{N}` | $\mathcal{N}$ |  |
| 哥特体 | `\mathfrak{g}` | $\mathfrak{g}$ |
| 粗体希腊字母 | `\boldsymbol{\alpha}` | $\boldsymbol{\alpha}$ |
| `\boldsymbol{\beta}` | $\boldsymbol{\beta}$ |  |
| `\boldsymbol{\theta}` | $\boldsymbol{\theta}$ |  |

## 7. 深度学习专用符号

| 描述 | LaTeX代码 | 效果 |
| ------ |------ |------ |
| 神经网络层 | `h^{(l)}` | $h^{(l)}$ |
| 权重矩阵 | `W^{(l)}` | $W^{(l)}$ |
| 偏置向量 | `b^{(l)}` | $b^{(l)}$ |
| 激活值 | `a^{(l)}` | $a^{(l)}$ |
| 卷积操作 | `f \ast g` | $f \ast g$ |
| 批量归一化 | `\text{BN}(x)` | $\text{BN}(x)$ |
| Dropout | `\text{Dropout}(x)` | $\text{Dropout}(x)$ |
| LSTM门 | `i_t`, `f_t`, `o_t` | $i_t$, $f_t$, $o_t$ |
| 注意力机制 | `\text{Attention}(Q,K,V)` | $\text{Attention}(Q,K,V)$ |
| 嵌入向量 | `\mathbf{e}_i` | $\mathbf{e}_i$ |
| 位置编码 | `\text{PE}(pos)` | $\text{PE}(pos)$ |

## 使用说明

1. **字体建议**：
    - 矩阵和向量建议使用粗体：`\mathbf{A}` 或 `\boldsymbol{\alpha}`
    - 函数名称建议使用文本格式：`\text{ReLU}`
2. **括号使用**：
    - 自动调整大小：`\left( \frac{a}{b} \right)`
    - 手动调整大小：`\big(`, `\Big(`, `\bigg(`, `\Bigg(`
3. **空格控制**：
    - 小空格：`\,`
    - 中等空格：`\:`
    - 大空格：`\;`
    - 负空格：`\!`
4. **常用组合**：
    - 矩阵乘法：`A \mathbf{x} = \mathbf{b}`
    - 特征值分解：`A = Q \Lambda Q^{-1}`
    - 奇异值分解：`A = U \Sigma V^\top`

这份速查表涵盖了深度学习和高等代数中最常用的LaTeX符号，建议收藏以备日常使用。

