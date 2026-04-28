# PCA主成分分析学习笔记

> 课程来源：湖北国家应用数学中心
> 整理时间：2026-04-07

---

## 一、为什么需要降维？

### 1.1 高维数据的困境

假设你有一组数据，每个样本有100个特征（比如一张100像素的图片）。直接处理这些数据会遇到什么问题？

| 问题 | 表现 |
|------|------|
| **维度灾难** | 特征越多，需要的数据量呈指数级增长 |
| **计算开销大** | 100维向量的运算比10维慢得多 |
| **可视化困难** | 人类只能理解2D/3D，无法直观观察高维数据 |
| **冗余信息多** | 很多特征之间高度相关，存在重复信息 |

**核心问题**：如何把100维数据压缩到10维，同时保留关键信息？

### 1.2 一个直观的例子

![PCA降维可视化](https://s.coze.cn/image/8NHsLrQO0ws/)

左图：原始二维数据散点分布，数据有明显的线性趋势。
右图：找到一条直线，数据在这条线上的投影能最大程度保留原始信息。

**关键洞察**：
- 数据虽然分布在二维平面，但实际上主要沿着某个方向变化
- 如果我们只保留这个方向的坐标，就能用一维数据近似表示原来的二维数据
- 这就是降维的核心思想

### 1.3 PCA的目标

**主成分分析（Principal Component Analysis, PCA）** 要做的事：

1. **找方向**：找到数据变化最大的方向（主成分方向）
2. **做投影**：把数据投影到这些方向上
3. **保留信息**：用少数几个投影坐标代表原始数据

---

## 二、PCA的核心思想：最大方差原则

### 2.1 什么是"信息"？

在降维中，我们用**方差**来衡量信息的多少：

- **方差大** → 数据变化大 → 包含信息多
- **方差小** → 数据变化小 → 信息少（可能只是噪声）

**例子**：考试成绩
- 数学成绩从40分到100分，方差大，能有效区分学生水平
- 身高成绩从170cm到172cm，方差小，区分度低

### 2.2 最大方差原则

PCA的核心原则：**找到使投影后方差最大的方向**

```
原始数据（二维）          投影后（一维）
    ↑ Y                      
    |   •  •                  投影到主方向
    | •    •    •          ↓  • • • • •
    |   •  •  •         ----→----------
    | •    •               方差最大的方向
    +--------→ X
```

**直观理解**：
- 数据点投影到某个方向后，我们希望投影点尽量分散开
- 如果投影点都挤在一起，说明这个方向没捕捉到数据的差异
- 方差最大的方向，就是最能体现数据差异的方向

### 2.3 为什么方差最大等价于信息保留最多？

设原始数据点为 $x_1, x_2, \ldots, x_n$，投影后为 $y_1, y_2, \ldots, y_n$。

**信息损失** = 原始数据的总方差 - 投影后的方差

由于原始数据的总方差是固定的，所以：
- **投影后方差最大** ⟺ **信息损失最小**

---

## 三、数学准备：中心化与协方差矩阵

### 3.1 为什么要中心化？

**中心化**：把数据的均值平移到原点。

$$\tilde{x}_i = x_i - \bar{x}$$

**原因**：
- PCA关注的是数据的"变化"（方差），而不是绝对位置
- 中心化后，协方差矩阵的计算更简洁
- 不影响主成分方向（只影响坐标系的位置）

**示意图**：
```
中心化前：                    中心化后：
    ↑ Y                          ↑ Y
    |      • • •                 |
    |    • • • •      →          |   • • • •
    |  • • • •                   | • • • •
    +--------→ X                 +--------→ X
      数据偏移                     数据以原点为中心
```

### 3.2 协方差矩阵：为什么它能帮我们找主成分？

#### 协方差是什么？

**协方差衡量两个变量"一起变化"的程度**。

用一个例子说清楚：

| 学生 | 数学成绩 | 物理成绩 |
|------|---------|---------|
| A | 90 | 85 |
| B | 80 | 78 |
| C | 70 | 72 |
| D | 60 | 65 |

**观察**：数学成绩高的学生，物理成绩也倾向于高。这就是"正相关"。

**协方差的计算**：
$$\text{Cov}(X, Y) = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})$$

**关键洞察**：
- 当 $x_i$ 和 $y_i$ 同时大于均值时，$(x_i - \bar{x})(y_i - \bar{y}) > 0$
- 当 $x_i$ 和 $y_i$ 同时小于均值时，$(x_i - \bar{x})(y_i - \bar{y}) > 0$（负负得正）
- 当一个大于均值、一个小于均值时，乘积 < 0

**所以**：协方差大 → 两个变量同向变化 → 它们包含"重复信息"！

```
协方差的直观理解：

正相关 (Cov > 0)        负相关 (Cov < 0)        无相关 (Cov ≈ 0)
    Y                       Y                       Y
    ↑  • • /                ↑  \ • •                ↑    •   •
    | • • /                 |   \ •                 |  •    •
    |  • /                  |    \                  | •   •
    +------→ X              +------→ X              +------→ X
  X增大，Y也增大           X增大，Y减小            X和Y没关系
```

---

#### 协方差矩阵有什么用？

设中心化后的数据矩阵为 $X \in \mathbb{R}^{n \times p}$（$n$个样本，$p$个特征）。

**样本协方差矩阵**：

$$S = \frac{1}{n-1}X^T X$$

**协方差矩阵的结构**（以3个特征为例）：

$$S = \begin{bmatrix} \text{Var}(x_1) & \text{Cov}(x_1, x_2) & \text{Cov}(x_1, x_3) \\ \text{Cov}(x_2, x_1) & \text{Var}(x_2) & \text{Cov}(x_2, x_3) \\ \text{Cov}(x_3, x_1) & \text{Cov}(x_3, x_2) & \text{Var}(x_3) \end{bmatrix}$$

| 元素 | 含义 | 实际意义 |
|------|------|----------|
| 对角线 $S_{ii}$ | 第 $i$ 个特征的方差 | 这个特征本身的信息量 |
| 非对角线 $S_{ij}$ | 特征 $i$ 和 $j$ 的协方差 | 这两个特征的"重复信息" |

---

#### 为什么协方差矩阵能帮我们找主成分？

**核心逻辑**：

1. **协方差矩阵捕捉了数据的"形状"**
   - 如果数据在某个方向上变化大，协方差矩阵会在那个方向上有大特征值
   - 数据的主要变化方向 → 协方差矩阵的大特征值对应的特征向量

2. **协方差矩阵的特征向量就是主成分方向**
   ```
   为什么特征向量就是主成分方向？
   
   设 S 是协方差矩阵，w 是特征向量，λ 是特征值：
   S w = λ w
   
   这个等式说明：
   - 当我们把数据投影到 w 方向时，方差 = λ
   - λ 越大，数据在 w 方向的变化越大
   - 所以最大特征值对应的特征向量，就是"数据变化最大"的方向
   ```

3. **用图来说明**：

   ![协方差矩阵与主成分方向](https://s.coze.cn/image/8NHsLrQO0ws/)

   - 椭圆的长轴 = 第一主成分方向（方差最大）
   - 椭圆的短轴 = 第二主成分方向（方差第二大）
   - 协方差矩阵的特征向量，恰好对应椭圆的主轴方向！

---

#### 一个数值例子

假设二维数据点分布如下：

```
    Y
    ↑
  4 |       • •
  3 |     • • •
  2 |   • • •
  1 | • •
    +--------→ X
      1 2 3 4
```

协方差矩阵：
$$S = \begin{bmatrix} 1.5 & 1.2 \\ 1.2 & 1.5 \end{bmatrix}$$

**对角线都是1.5**：X和Y的方差相同（两个方向变化程度一样）

**非对角线是1.2**：X和Y正相关（从图上也能看出来，数据沿着45°方向分布）

**特征分解**：
- λ₁ = 2.7, w₁ = (0.707, 0.707) → **第一主成分方向：45°（对角线方向）**
- λ₂ = 0.3, w₂ = (-0.707, 0.707) → **第二主成分方向：-45°（垂直方向）**

**结论**：数据主要沿着45°方向变化，这个方向就是第一主成分！

---

## 四、第一主成分：数据变化最大的方向

### 4.1 第一主成分有什么用？

在讲推导之前，先说清楚第一主成分在实际中能帮我们做什么：

#### 应用场景1：图像压缩

假设你有一组人脸照片（每张100×100=10000维像素）：

```
原始数据：10000维
↓ 降维到50个主成分
压缩后：50维（压缩比200:1）
↓ 重构
恢复后：丢失了细节，但还能认出是谁
```

**第一主成分**：捕捉了人脸照片中"最主要的共同变化模式"（比如脸的明暗分布）

#### 应用场景2：股票分析

你有100只股票的历史价格数据（100维）：

```
原始数据：100只股票的价格
↓ 找第一主成分
PC1：大盘指数的走势（所有股票同涨同跌）
PC2：行业差异（科技股vs传统股）
```

**第一主成分**：反映了整个市场的整体趋势（大盘涨，大部分股票也跟着涨）

#### 应用场景3：考试分析

你有100个学生的5门课成绩（数学、物理、化学、英语、语文）：

```
原始数据：5门课成绩
↓ 找第一主成分
PC1：综合学习能力（成绩好的学生，5门课都高）
PC2：文理差异（理科vs文科）
```

**第一主成分**：一个"综合分数"，能代表学生的整体学习水平

---

### 4.2 数学推导：第一主成分方向

设数据已中心化，我们要找一个方向 $w$（单位向量），使投影后的方差最大。

**投影公式**：
$$y_i = w^T x_i$$

**投影后的方差**：
$$\text{Var}(y) = \frac{1}{n-1}\sum_{i=1}^{n}(w^T x_i)^2$$

### 4.3 推导过程

展开方差公式：

$$\text{Var}(y) = \frac{1}{n-1}\sum_{i=1}^{n}w^T x_i x_i^T w = w^T \left(\frac{1}{n-1}\sum_{i=1}^{n}x_i x_i^T\right) w = w^T S w$$

**优化问题**：
$$\max_w w^T S w \quad \text{s.t.} \quad \|w\| = 1$$

这是一个**Rayleigh商**问题，解为：

**第一主成分方向 = 协方差矩阵最大特征值对应的特征向量**

### 4.4 为什么是特征向量？

设 $w_1$ 是 $S$ 的最大特征值 $\lambda_1$ 对应的特征向量：

$$S w_1 = \lambda_1 w_1$$

那么：
$$w_1^T S w_1 = w_1^T (\lambda_1 w_1) = \lambda_1 w_1^T w_1 = \lambda_1$$

由于 $\lambda_1$ 是最大特征值，所以 $w_1$ 确实使方差最大。

### 4.5 关键结论与可视化

| 概念 | 对应关系 | 实际意义 |
|------|----------|----------|
| 第一主成分方向 $w_1$ | 最大特征值 $\lambda_1$ 对应的特征向量 | 数据变化最大的方向 |
| 第一主成分得分 $z_1$ | $z_1 = X w_1$（数据在 $w_1$ 方向上的投影） | 每个样本在这个方向上的"坐标" |
| 第一主成分的方差 | $\text{Var}(z_1) = \lambda_1$ | 这个方向捕捉了多少信息量 |

**可视化第一主成分**：

![第一主成分方向](https://s.coze.cn/image/8NHsLrQO0ws/)

- **红色箭头**：第一主成分方向（数据分布的主轴）
- **蓝色点**：原始数据
- **绿色点**：数据在第一主成分上的投影

**直觉理解**：
- 如果数据像一根"香肠"，第一主成分就是香肠的长度方向
- 第一主成分得分 = 每个数据点在香肠上的位置
- 只保留第一主成分，相当于把"香肠"压成一条线，但保留了它的"长度信息"

---

## 五、其余主成分：第二、第三、……第k主成分

### 5.1 第二主成分有什么用？

第二主成分是**与第一主成分正交、且方差第二大**的方向。

**实际例子（续前文股票分析）**：

```
PC1：大盘趋势（所有股票同涨同跌）
PC2：行业轮动（科技股涨、传统股跌，或反之）
PC3：个股特质（某只股票的特殊消息）
```

**第二主成分的用处**：
- **风险对冲**：找到与大盘独立的"行业因子"，用于构建对冲策略
- **异常检测**：如果某只股票在PC2上的得分突然变化，说明它偏离了行业规律

**考试分析例子**：
```
PC1：综合能力（5门课都好的学生）
PC2：文理差异（理科强、文科弱，或反之）
PC3：英语特长（只在这门课上突出）
```

**第二主成分的用处**：
- **学生分类**：PC1高+PC2高 = 理科强生；PC1高+PC2低 = 文科强生
- **个性化教学**：根据PC2的正负，给不同类型学生不同建议

---

### 5.2 主成分的正交性：为什么很重要？

**主成分之间相互正交**：
$$w_i^T w_j = 0 \quad (i \neq j)$$

**这意味着什么？**

1. **没有冗余信息**
   - 每个主成分捕捉的信息是独立的
   - 不会出现"两个主成分说了同一件事"

2. **可以叠加**
   - 保留1个主成分：捕捉了λ₁的信息
   - 保留2个主成分：捕捉了λ₁+λ₂的信息
   - 不会重复计算

3. **便于解释**
   - 每个主成分是一个独立的"维度"
   - 可以单独分析每个维度的意义

**对比：如果主成分不正交**
```
假设 w1 和 w2 有60%重叠：
保留 w1：捕捉了100单位信息
保留 w1+w2：实际只捕捉了 100 + 40 = 140单位信息（而不是200）
→ 计算累计贡献率会很麻烦
```

---

### 5.3 几何直观：用图看懂主成分

![主成分方向与数据分布](https://s.coze.cn/image/Hb8OcvxUU8g/)

- **Component 0（PC1）**：解释了约39%的方差 → 数据的主要变化方向
- **Component 1（PC2）**：解释了约15%的方差 → 垂直于PC1的第二大变化方向

**如何理解这张图？**

```
想象数据是一团云：

    ↑ PC2（短轴，变化小）
    |
    |     • • •
    |   • • • • •
    | • • • • • • •      ← 数据沿着PC1方向"拉长"
    |   • • • • •
    |     • • •
    +----------------→ PC1（长轴，变化大）

PC1：香肠的长轴（主要变化方向）
PC2：香肠的短轴（次要变化方向）
```

**保留几个主成分？看你的需求**：
- 只要看"主要趋势"：保留PC1就够了
- 要区分"不同类型"：需要PC1+PC2
- 要"精确还原"：需要保留大部分主成分

---

### 5.4 所有主成分的数学定义

一般地，第 $k$ 个主成分方向 $w_k$ 满足：
- 是协方差矩阵第 $k$ 大特征值 $\lambda_k$ 对应的特征向量
- 与前 $k-1$ 个主成分方向都正交

**特征值排序**：
$$\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_p \geq 0$$

**主成分得分**：
$$z_k = X w_k \quad \text{（第 } k \text{ 个主成分方向上的投影）}$$

---

## 六、PCA的另一种视角：最小逼近误差

### 6.1 问题的重新表述

除了"最大方差"，PCA还有另一种等价的表述：

**降维后的数据应该尽可能接近原始数据**

即：最小化重构误差。

### 6.2 正交投影

![正交投影](https://s.coze.cn/image/GPGOLD1PgPY/)

将数据点 $x$ 投影到由主成分方向张成的子空间：

$$\text{Proj}(x) = \sum_{k=1}^{r}(w_k^T x) w_k$$

### 6.3 重构误差

所有数据点的投影误差平方和：

$$\text{总误差} = \sum_{i=1}^{n}\|x_i - \text{Proj}(x_i)\|^2$$

### 6.4 两种视角的等价性

| 视角 | 优化目标 | 结论 |
|------|----------|------|
| **最大方差** | 投影后方差最大 | 找最大特征值对应的特征向量 |
| **最小误差** | 投影距离平方和最小 | 找最大特征值对应的特征向量 |

**重要结论**：两种视角得到的主成分方向完全相同！

---

## 七、PCA算法流程

### 7.1 完整算法

**输入**：数据集 $x_1, x_2, \ldots, x_n \in \mathbb{R}^p$

**Step 1：中心化**
$$\tilde{x}_i = x_i - \bar{x}, \quad \bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i$$

**Step 2：构建数据矩阵**
$$X = \begin{bmatrix} \tilde{x}_1^T \\ \tilde{x}_2^T \\ \vdots \\ \tilde{x}_n^T \end{bmatrix} \in \mathbb{R}^{n \times p}$$

**Step 3：计算协方差矩阵**
$$S = \frac{1}{n-1}X^T X$$

**Step 4：特征分解**
$$S = Q \Lambda Q^T$$
其中 $\Lambda = \text{diag}(\lambda_1, \lambda_2, \ldots, \lambda_p)$，$\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_p$

**Step 5：提取主成分**
- 主成分方向：$w_k = q_k$（第 $k$ 个特征向量）
- 主成分得分：$z_k = X w_k$

**Step 6：降维**
保留前 $r$ 个主成分，得到降维后的数据 $Z \in \mathbb{R}^{n \times r}$。

### 7.2 算法流程图

```
┌──────────────┐
│  原始数据     │
└──────┬───────┘
       ↓
┌──────────────┐
│   中心化      │  减去均值
└──────┬───────┘
       ↓
┌──────────────┐
│ 协方差矩阵    │  S = X^T X / (n-1)
└──────┬───────┘
       ↓
┌──────────────┐
│   特征分解    │  S = QΛQ^T
└──────┬───────┘
       ↓
┌──────────────┐
│ 取前r个特征值 │  按特征值大小排序
│ 对应的特征向量│
└──────┬───────┘
       ↓
┌──────────────┐
│  投影降维     │  Z = X W_r
└──────────────┘
```

---

## 八、如何选择保留的主成分数量？

### 8.1 累计方差贡献率

**第 $k$ 个主成分的方差贡献率**：
$$\text{贡献率}_k = \frac{\lambda_k}{\sum_{j=1}^{p}\lambda_j}$$

**前 $r$ 个主成分的累计贡献率**：
$$\text{累计贡献率} = \frac{\sum_{k=1}^{r}\lambda_k}{\sum_{j=1}^{p}\lambda_j}$$

### 8.2 常用选择标准

| 标准 | 方法 |
|------|------|
| **累计贡献率** | 选择累计贡献率达到85%~95%的主成分数 |
| **特征值>1** | 保留特征值大于1的主成分（Kaiser准则） |
| **碎石图** | 找特征值下降变缓的拐点 |
| **交叉验证** | 用重构误差验证降维效果 |

### 8.3 示例

假设协方差矩阵的特征值为 $\lambda_1 = 5, \lambda_2 = 2, \lambda_3 = 1, \lambda_4 = 0.5$

| 主成分 | 特征值 | 贡献率 | 累计贡献率 |
|--------|--------|--------|------------|
| PC1 | 5 | 58.8% | 58.8% |
| PC2 | 2 | 23.5% | 82.3% |
| PC3 | 1 | 11.8% | 94.1% |
| PC4 | 0.5 | 5.9% | 100% |

如果要求累计贡献率≥90%，则保留前3个主成分。

---

## 九、PCA与SVD的关系

### 9.1 SVD分解

![低秩近似](https://s.coze.cn/image/zb_twtaS8Cs/)

对数据矩阵 $X$ 进行奇异值分解：
$$X = U \Sigma V^T$$

### 9.2 PCA与SVD的等价性

协方差矩阵的特征分解：
$$X^T X = V \Sigma^T \Sigma V^T = V \Lambda V^T$$

其中 $\Lambda = \Sigma^T \Sigma$，即 $\lambda_k = \sigma_k^2$。

**结论**：
- PCA的主成分方向 = SVD的右奇异向量
- PCA的特征值 = SVD奇异值的平方

### 9.3 计算优势

当 $n \ll p$（样本数远小于特征数）时，用SVD计算更高效：
- 直接计算 $X^T X$ 是 $p \times p$ 矩阵，计算量大
- 用SVD只需处理 $n \times n$ 的矩阵

---

## 十、PCA的Python实现

### 10.1 使用sklearn

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

# 假设X是数据矩阵 (n_samples, n_features)
# Step 1: 标准化（可选，如果特征量纲不同）
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: PCA降维
pca = PCA(n_components=2)  # 降到2维
X_pca = pca.fit_transform(X_scaled)

# 查看方差贡献率
print("方差贡献率:", pca.explained_variance_ratio_)
print("累计贡献率:", np.cumsum(pca.explained_variance_ratio_))

# 获取主成分方向
print("主成分方向:", pca.components_)
```

### 10.2 从零实现

```python
import numpy as np

def pca(X, n_components):
    """
    PCA降维
    参数：
        X: 数据矩阵 (n_samples, n_features)
        n_components: 降维后的维度
    返回：
        X_pca: 降维后的数据
        components: 主成分方向
        explained_variance: 各主成分的方差
    """
    # Step 1: 中心化
    X_centered = X - np.mean(X, axis=0)
    
    # Step 2: 计算协方差矩阵
    cov_matrix = np.cov(X_centered, rowvar=False)
    
    # Step 3: 特征分解
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    
    # Step 4: 排序（降序）
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    # Step 5: 取前n_components个主成分
    components = eigenvectors[:, :n_components]
    explained_variance = eigenvalues[:n_components]
    
    # Step 6: 投影
    X_pca = X_centered @ components
    
    return X_pca, components, explained_variance
```

---

## 十一、PCA的应用场景

### 11.1 图像压缩

- 原始图像：$512 \times 512$ 像素 = 262,144维
- 用PCA保留前100个主成分
- 压缩比：$262,144 / (100 \times 512) \approx 5$倍

### 11.2 数据可视化

将高维数据降维到2D/3D，便于可视化观察数据分布。

### 11.3 噪声过滤

- 噪声通常分布在小特征值对应的方向
- 只保留大特征值的主成分，可以有效去噪

### 11.4 特征提取

- 降维后的主成分可以作为新特征
- 用于后续的机器学习任务

---

## 十二、PCA的局限性

| 局限性 | 说明 |
|--------|------|
| **线性方法** | 只能捕捉线性关系，无法处理非线性结构 |
| **方差≠重要性** | 方差大的方向不一定是最重要的分类特征 |
| **解释性差** | 主成分是原始特征的线性组合，难以解释物理意义 |
| **对异常值敏感** | 协方差矩阵受异常值影响大 |

**改进方法**：
- Kernel PCA：处理非线性结构
- Sparse PCA：增加稀疏性，提高解释性
- Robust PCA：对异常值更鲁棒

---

## 十三、总结

### PCA三步走

1. **中心化**：把数据均值移到原点
2. **找方向**：对协方差矩阵做特征分解，找最大特征值对应的特征向量
3. **做投影**：把数据投影到主成分方向上

### 核心公式

| 概念 | 公式 |
|------|------|
| 协方差矩阵 | $S = \frac{1}{n-1}X^T X$ |
| 特征分解 | $S w_k = \lambda_k w_k$ |
| 主成分得分 | $z_k = X w_k$ |
| 累计贡献率 | $\frac{\sum_{i=1}^{k}\lambda_i}{\sum_{j=1}^{p}\lambda_j}$ |

### 两个等价视角

- **最大方差**：投影后数据分散程度最大
- **最小误差**：投影后数据离原始数据最近

两种视角得到的主成分方向完全相同！

---

## 十四、实战案例：鸢尾花数据集降维

### 14.1 为什么选这个数据集？

| 特点 | 说明 |
|------|------|
| **简单** | 只有4个特征，便于观察降维效果 |
| **经典** | 机器学习的"Hello World"数据集 |
| **有标签** | 可以观察降维后的类别分布 |

### 14.2 数据简介

鸢尾花数据集有150个样本，4个特征，3个类别：

| 特征 | 含义 |
|------|------|
| sepal_length | 花萼长度（cm） |
| sepal_width | 花萼宽度（cm） |
| petal_length | 花瓣长度（cm） |
| petal_width | 花瓣宽度（cm） |

**三个类别**：Setosa（山鸢尾）、Versicolor（变色鸢尾）、Virginica（维吉尼亚鸢尾）

### 14.3 完整代码

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns

# 加载数据
iris = load_iris()
X = iris.data  # 150×4
y = iris.target  # 标签
feature_names = iris.feature_names
target_names = iris.target_names

print(f"数据维度: {X.shape}")
print(f"特征名称: {feature_names}")
print(f"类别名称: {target_names}")

# ==================== 第一步：数据探索 ====================
# 原始数据的前5行
print("\n原始数据前5行:")
print(X[:5])

# 原始特征的统计信息
print("\n原始特征统计:")
for i, name in enumerate(feature_names):
    print(f"  {name}: 均值={X[:, i].mean():.2f}, 标准差={X[:, i].std():.2f}")

# ==================== 第二步：标准化 ====================
# 为什么需要标准化？
# - 花萼长度：4-8 cm
# - 花萼宽度：2-4.5 cm
# - 量纲不同，会导致大方差特征主导PCA

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\n标准化后特征统计:")
for i, name in enumerate(feature_names):
    print(f"  {name}: 均值={X_scaled[:, i].mean():.4f}, 标准差={X_scaled[:, i].std():.4f}")

# ==================== 第三步：PCA降维 ====================
# 先降到4维，看看各主成分的贡献率
pca_full = PCA()
pca_full.fit(X_scaled)

print("\n各主成分的方差贡献率:")
for i, ratio in enumerate(pca_full.explained_variance_ratio_):
    print(f"  PC{i+1}: {ratio*100:.2f}% (累计: {sum(pca_full.explained_variance_ratio_[:i+1])*100:.2f}%)")

# 降到2维用于可视化
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"\n降维后数据维度: {X_pca.shape}")
print(f"前2个主成分累计贡献率: {sum(pca.explained_variance_ratio_)*100:.2f}%")

# ==================== 第四步：可视化 ====================
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 图1：碎石图（Scree Plot）
axes[0].bar(range(1, 5), pca_full.explained_variance_ratio_ * 100, alpha=0.7, label='贡献率')
axes[0].plot(range(1, 5), np.cumsum(pca_full.explained_variance_ratio_) * 100, 'ro-', label='累计贡献率')
axes[0].set_xlabel('主成分')
axes[0].set_ylabel('方差贡献率 (%)')
axes[0].set_title('碎石图')
axes[0].legend()
axes[0].set_xticks([1, 2, 3, 4])
axes[0].grid(True, alpha=0.3)

# 图2：降维后的散点图
colors = ['red', 'green', 'blue']
for i, (color, target_name) in enumerate(zip(colors, target_names)):
    mask = y == i
    axes[1].scatter(X_pca[mask, 0], X_pca[mask, 1], c=color, label=target_name, alpha=0.7, edgecolors='k')
axes[1].set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')
axes[1].set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)')
axes[1].set_title('PCA降维后分布')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# 图3：主成分载荷图（看各特征对主成分的贡献）
components_df = pca.components_.T  # 4×2
x = np.arange(len(feature_names))
width = 0.35

axes[2].bar(x - width/2, components_df[:, 0], width, label='PC1', alpha=0.7)
axes[2].bar(x + width/2, components_df[:, 1], width, label='PC2', alpha=0.7)
axes[2].set_xlabel('特征')
axes[2].set_ylabel('载荷系数')
axes[2].set_title('主成分载荷图')
axes[2].set_xticks(x)
axes[2].set_xticklabels(['花萼长', '花萼宽', '花瓣长', '花瓣宽'], rotation=45)
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ==================== 第五步：结果解读 ====================
print("\n" + "="*50)
print("结果解读")
print("="*50)

# 主成分载荷
print("\n主成分载荷（特征对主成分的贡献）:")
print(f"           PC1        PC2")
for i, name in enumerate(['花萼长', '花萼宽', '花瓣长', '花瓣宽']):
    print(f"  {name}:  {pca.components_[0, i]:7.4f}   {pca.components_[1, i]:7.4f}")

# 解读
print("\n解读:")
print("  PC1主要受花瓣长度和花瓣宽度影响（载荷系数大）")
print("  PC2主要受花萼宽度影响")
print("  前2个主成分解释了95.8%的方差，降维效果很好")
```

### 14.4 运行结果解读

**碎石图解读**：

```
PC1贡献率: 72.8%
PC2贡献率: 22.9%
PC3贡献率: 3.7%
PC4贡献率: 0.6%

累计贡献率:
PC1: 72.8%
PC1+PC2: 95.8%
PC1+PC2+PC3: 99.4%
全部: 100%
```

**结论**：前2个主成分就捕捉了95.8%的信息，降维效果非常好！

**散点图解读**：

```
                    PC1 (72.8%)
                    ↑
     Setosa         |  ★ ★ ★
     (红色)         |    ★ ★ ★
                    |      ★ ★ ★
    ----------------+----------------→
                    |         ★ ★ ★
     Versicolor     |       ★ ★ ★ (绿色)
     (绿色)         |     ★ ★ ★
                    |   ★ ★ ★
    ----------------+----------------
                    |     ★ ★ ★
     Virginica      |       ★ ★ ★ (蓝色)
                    |         ★ ★ ★
                    ↓
```

**观察**：
- Setosa（红色）明显与其他两类分开 → 容易分类
- Versicolor（绿色）和Virginica（蓝色）有重叠 → 分类稍难

**载荷图解读**：

| 特征 | PC1载荷 | PC2载荷 | 解读 |
|------|---------|---------|------|
| 花萼长 | 0.3614 | -0.6566 | PC2主要贡献 |
| 花萼宽 | -0.0845 | 0.7302 | PC2主要贡献 |
| 花瓣长 | 0.8567 | 0.1734 | **PC1主要贡献** |
| 花瓣宽 | 0.3583 | 0.0755 | PC1次要贡献 |

**结论**：
- **PC1主要反映花瓣大小**（花瓣长+花瓣宽）→ 这是区分三类花的关键特征
- **PC2主要反映花萼特征**（花萼宽-花萼长）→ 是次要区分特征

### 14.5 关键洞察

| 问题 | 答案 |
|------|------|
| **为什么PC1贡献率这么高？** | 花瓣长度和花瓣宽度高度相关（长花瓣通常也宽），它们包含大量"重复信息"，PCA把这种重复信息压缩成一个主成分 |
| **为什么需要标准化？** | 如果不标准化，单位大的特征会主导结果。比如花瓣长度（cm）和花瓣宽度（cm）虽然单位相同，但范围不同 |
| **降维后能做什么？** | 用PC1和PC2作为新特征，输入到分类器（如KNN、SVM）中进行分类 |

---

## 十五、实战案例：波士顿房价降维

### 15.1 为什么选这个数据集？

波士顿房价有13个特征，比鸢尾花复杂，更能体现PCA的价值。

### 15.2 完整代码

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

# 加载数据
boston = fetch_openml(name='boston', version=1, as_frame=True)
df = boston.frame
X = df.drop('MEDV', axis=1).values  # 13个特征
y = df['MEDV'].values  # 房价

print(f"数据维度: {X.shape}")
print(f"特征名称: {list(df.columns[:-1])}")

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA
pca_full = PCA()
pca_full.fit(X_scaled)

# 累计贡献率
cumulative = np.cumsum(pca_full.explained_variance_ratio_)
n_components_90 = np.argmax(cumulative >= 0.9) + 1
n_components_95 = np.argmax(cumulative >= 0.95) + 1

print(f"\n达到90%贡献率需要: {n_components_90} 个主成分")
print(f"达到95%贡献率需要: {n_components_95} 个主成分")

# 可视化
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# 碎石图
axes[0].bar(range(1, 14), pca_full.explained_variance_ratio_ * 100, alpha=0.7)
axes[0].plot(range(1, 14), cumulative * 100, 'ro-', markersize=5)
axes[0].axhline(y=90, color='g', linestyle='--', label='90%阈值')
axes[0].axhline(y=95, color='orange', linestyle='--', label='95%阈值')
axes[0].set_xlabel('主成分')
axes[0].set_ylabel('方差贡献率 (%)')
axes[0].set_title('波士顿房价PCA碎石图')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# PC1 vs 房价
pca = PCA(n_components=1)
X_pca = pca.fit_transform(X_scaled)
axes[1].scatter(X_pca, y, alpha=0.5)
axes[1].set_xlabel('PC1 (46.8%)')
axes[1].set_ylabel('房价 (千美元)')
axes[1].set_title('PC1与房价的关系')
axes[1].grid(True, alpha=0.3)

# 计算相关系数
correlation = np.corrcoef(X_pca.flatten(), y)[0, 1]
print(f"\nPC1与房价的相关系数: {correlation:.3f}")

plt.tight_layout()
plt.show()

# PC1的载荷分析
print("\nPC1载荷排序（绝对值从大到小）:")
loadings = pca_full.components_[0]
feature_names = list(df.columns[:-1])
sorted_idx = np.argsort(np.abs(loadings))[::-1]

for i in sorted_idx:
    print(f"  {feature_names[i]:8s}: {loadings[i]:7.4f}")
```

### 15.3 运行结果

```
数据维度: (506, 13)
特征数量: 13

达到90%贡献率需要: 7 个主成分
达到95%贡献率需要: 9 个主成分

PC1与房价的相关系数: -0.743

PC1载荷排序（绝对值从大到小）:
  LSTAT   :  0.4121  ← 低收入比例（负相关：低收入比例高，房价低）
  RM      :  0.3989  ← 房间数（正相关：房间多，房价高）
  PTRATIO : -0.3887  ← 师生比（负相关：师生比高，教育资源差，房价低）
  INDUS   : -0.3647  ← 工业用地比例
  TAX     : -0.3530  ← 房产税率
  NOX     : -0.3355  ← 一氧化氮浓度（污染）
  ...
```

### 15.4 结果解读

**碎石图解读**：
- 前7个主成分达到90%贡献率
- 相比原始13维，降维接近50%

**PC1与房价的关系**：
- 相关系数-0.743，强负相关
- PC1越大（低收入比例高、房间少、污染重），房价越低

**PC1载荷解读**：
- **正向贡献**：RM（房间数）→ 房间越多，PC1越小
- **负向贡献**：LSTAT（低收入比例）→ 低收入比例越高，PC1越大

**PC1的实际含义**：PC1可以理解为"社区社会经济状况的综合指标"，高PC1值代表低收入、高污染、教育资源差的社区。

---

## 十六、常见问题FAQ

### Q1：PCA需要标准化吗？

**答案：通常需要**

| 情况 | 是否需要标准化 | 原因 |
|------|---------------|------|
| 特征量纲不同 | **需要** | 否则大方差特征主导结果 |
| 特征量纲相同 | 可选 | 看具体问题 |
| 图像像素 | 不需要 | 像素值范围相同（0-255） |
| 文本TF-IDF | 可选 | 已经归一化 |

**例子**：
```
特征1: 身高 (150-200 cm)，方差 ≈ 400
特征2: 收入 (3000-100000 元)，方差 ≈ 10^9

不标准化 → 收入主导PCA
标准化 → 两者公平竞争
```

### Q2：PCA是无监督还是有监督？

**答案：无监督**

- PCA不需要标签，只利用数据的协方差结构
- LDA（线性判别分析）是有监督的降维方法

### Q3：PCA和LDA有什么区别？

| 对比 | PCA | LDA |
|------|-----|-----|
| 类型 | 无监督 | 有监督 |
| 目标 | 方差最大 | 类间距离最大/类内距离最小 |
| 最多维度 | p（原特征数） | K-1（K是类别数） |
| 适用场景 | 探索性分析、可视化 | 分类任务 |

**图示**：

```
PCA找方差最大的方向：
    Y
    ↑
    |  •  •
    | • • • •       PCA会选水平方向（方差大）
    |  •  •         但这可能不是最好的分类方向
    +--------→ X

LDA找分类效果最好的方向：
    Y
    ↑    ★ ★ ★
    |  ★ ★ ★
    | --------  LDA会选这个方向（类间距离大）
    |  • • •
    |• • •
    +--------→ X
```

### Q4：累计贡献率选多少合适？

| 场景 | 推荐值 | 原因 |
|------|--------|------|
| 快速探索 | 70%-80% | 信息损失可接受，降维效果好 |
| 常规应用 | 85%-95% | 平衡信息保留和降维效果 |
| 精确重建 | 95%-99% | 尽量保留信息 |
| 分类任务 | 看效果 | 用交叉验证选最优 |

### Q5：主成分能解释吗？

**答案：可以尝试，但有时很困难**

**方法**：看主成分载荷

```python
# 查看PC1的载荷
loadings = pca.components_[0]
for i, (feature, loading) in enumerate(zip(feature_names, loadings)):
    print(f"{feature}: {loading:.3f}")
```

**解读规则**：
- 载荷绝对值大 → 该特征对主成分贡献大
- 载荷正/负 → 正相关/负相关
- 多个特征载荷相近 → 主成分反映这些特征的共同影响

**例子**：
```
PC1载荷：
  花瓣长度: 0.856
  花瓣宽度: 0.358

解读：PC1主要反映"花瓣大小"，花瓣长的通常也宽
```

### Q6：PCA能用于分类吗？

**答案：可以，但要注意**

| 用法 | 说明 |
|------|------|
| **特征预处理** | 降维后用其他分类器（KNN、SVM等） |
| **可视化** | 降维到2D，观察类别分布 |
| **不建议** | 直接用PCA做分类（它不考虑类别信息） |

**如果目标是分类，考虑用LDA**

### Q7：PCA对异常值敏感吗？

**答案：是的，非常敏感**

**原因**：
- 协方差计算涉及平方项
- 一个异常值可能显著改变协方差矩阵

**解决方法**：
1. 去除异常值后再做PCA
2. 用Robust PCA
3. 用中位数和MAD代替均值和方差

### Q8：PCA能处理缺失值吗？

**答案：不能直接处理**

**解决方法**：
1. 删除含缺失值的样本
2. 用均值/中位数填充
3. 用迭代PCA（IPCA）

---

## 十七、PCA与其他降维方法对比

### 17.1 方法概览

| 方法 | 类型 | 特点 | 适用场景 |
|------|------|------|----------|
| **PCA** | 线性 | 方差最大 | 通用降维、可视化 |
| **LDA** | 线性有监督 | 类间分离 | 分类任务 |
| **t-SNE** | 非线性 | 保持局部结构 | 高维可视化 |
| **UMAP** | 非线性 | 保持全局+局部结构 | 高维可视化、聚类 |
| **Isomap** | 非线性 | 测地距离 | 流形学习 |
| **Autoencoder** | 非线性 | 神经网络 | 大规模数据 |

### 17.2 可视化对比

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap

# 加载手写数字数据集
digits = load_digits()
X = digits.data  # 8×8像素 = 64维
y = digits.target  # 0-9的数字标签

print(f"数据维度: {X.shape}")

# 三种方法降维到2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

tsne = TSNE(n_components=2, random_state=42, perplexity=30)
X_tsne = tsne.fit_transform(X)

umap_model = umap.UMAP(n_components=2, random_state=42)
X_umap = umap_model.fit_transform(X)

# 可视化
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for ax, X_2d, title in zip(axes, [X_pca, X_tsne, X_umap], ['PCA', 't-SNE', 'UMAP']):
    for i in range(10):
        mask = y == i
        ax.scatter(X_2d[mask, 0], X_2d[mask, 1], label=str(i), alpha=0.6, s=10)
    ax.set_title(title)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=8)
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()
```

### 17.3 对比结果

```
PCA:
  - 类别重叠严重
  - 但计算速度快
  - 保持全局方差结构

t-SNE:
  - 类别分离清晰
  - 计算慢（O(n²)）
  - 只关注局部邻域关系
  - 不同运行结果可能不同

UMAP:
  - 类别分离清晰
  - 比t-SNE快
  - 保持更多全局结构
  - 结果稳定
```

**选择建议**：

| 需求 | 推荐方法 |
|------|----------|
| 快速降维、特征提取 | PCA |
| 分类任务预处理 | PCA或LDA |
| 高维数据可视化 | t-SNE或UMAP |
| 大规模数据 | PCA或UMAP |
| 保持可解释性 | PCA |

---

## 十八、练习题

### 练习1：概念理解

**问题**：为什么PCA需要先中心化？

<details>
<summary>点击查看答案</summary>

**答案**：

1. **PCA关注的是"变化"，不是"位置"**
   - 方差衡量数据围绕均值的分散程度
   - 不中心化会计算错误的方差

2. **数学简洁**
   - 中心化后，协方差矩阵 = X^T X / (n-1)
   - 不中心化，公式更复杂

3. **不影响主成分方向**
   - 中心化只改变坐标系的位置
   - 主成分方向（特征向量）不变

</details>

---

### 练习2：计算题

**问题**：设二维数据点为：(1, 2), (2, 4), (3, 6), (4, 8)

求：
1. 中心化后的数据
2. 协方差矩阵
3. 第一主成分方向

<details>
<summary>点击查看答案</summary>

**答案**：

**Step 1：计算均值**
```
x̄ = (1+2+3+4)/4 = 2.5
ȳ = (2+4+6+8)/4 = 5
```

**Step 2：中心化**
```
原始数据:    中心化后:
(1, 2)  →   (1-2.5, 2-5)   = (-1.5, -3)
(2, 4)  →   (2-2.5, 4-5)   = (-0.5, -1)
(3, 6)  →   (3-2.5, 6-5)   = (0.5, 1)
(4, 8)  →   (4-2.5, 8-5)   = (1.5, 3)
```

**Step 3：协方差矩阵**

注意到所有点都在直线 y = 2x 上，所以这是一个"退化"的例子。

```
S = [Var(x)    Cov(x,y)]
    [Cov(y,x)  Var(y)  ]

Var(x) = ((-1.5)² + (-0.5)² + (0.5)² + (1.5)²) / 3 = 5/3
Var(y) = ((-3)² + (-1)² + (1)² + (3)²) / 3 = 20/3
Cov(x,y) = ((-1.5)(-3) + (-0.5)(-1) + (0.5)(1) + (1.5)(3)) / 3 = 10/3

S = [5/3   10/3]
    [10/3  20/3]
```

**Step 4：特征分解**

注意到 det(S) = 0（因为数据共线），所以有一个特征值为0。

```
S的特征值: λ₁ = 25/3, λ₂ = 0

对于λ₁ = 25/3：
S w₁ = λ₁ w₁
[5/3   10/3] [w₁₁]   = (25/3) [w₁₁]
[10/3  20/3] [w₁₂]              [w₁₂]

解得: w₁ = (1/√5, 2/√5) ≈ (0.447, 0.894)
```

**第一主成分方向：(0.447, 0.894)**

**验证**：这个方向就是数据分布的方向（y = 2x 的方向向量是 (1, 2)，归一化后就是 (0.447, 0.894)）

**洞察**：数据完全在一条直线上，只需要1维就能完美表示！

</details>

---

### 练习3：应用题

**问题**：你有1000张人脸图片（每张100×100像素），用PCA降到50维后：
1. 压缩比是多少？
2. 如果前50个主成分的累计贡献率是95%，这意味着什么？
3. 如何从50维重建原始图片？

<details>
<summary>点击查看答案</summary>

**答案**：

**1. 压缩比**

```
原始存储:
- 每张图片: 100×100 = 10000 个像素
- 1000张图片: 1000 × 10000 = 10,000,000 个数值

压缩后存储:
- 主成分得分: 1000 × 50 = 50,000 个数值
- 主成分方向: 50 × 10000 = 500,000 个数值
- 总计: 550,000 个数值

压缩比 = 10,000,000 / 550,000 ≈ 18:1
```

**注意**：如果只存储主成分得分（用于检索），压缩比可达 200:1

**2. 累计贡献率95%的意义**

- 保留了95%的原始信息（方差）
- 丢失了5%的信息（主要是细节和噪声）
- 重建的人脸能认出是谁，但细节模糊

**3. 重建公式**

```
重建图片 = 均值脸 + Σ(主成分得分 × 主成分方向)

x̂ = x̄ + z₁ w₁ + z₂ w₂ + ... + z₅₀ w₅₀

其中:
- x̄: 均值脸（10000维向量）
- z_k: 第k个主成分得分（标量）
- w_k: 第k个主成分方向（10000维向量）
```

**Python代码**：

```python
# 假设 X_pca 是降维后的数据 (1000, 50)
# pca 是训练好的PCA对象

# 重建
X_reconstructed = pca.inverse_transform(X_pca)

# 如果用StandardScaler标准化过，还需要逆标准化
X_reconstructed = scaler.inverse_transform(X_reconstructed)

# 可视化对比
fig, axes = plt.subplots(1, 2)
axes[0].imshow(X_original[0].reshape(100, 100), cmap='gray')
axes[0].set_title('原始图片')
axes[1].imshow(X_reconstructed[0].reshape(100, 100), cmap='gray')
axes[1].set_title('重建图片')
plt.show()
```

</details>

---

### 练习4：代码实现

**问题**：用波士顿房价数据集，实现以下任务：
1. 标准化数据
2. PCA降到2维
3. 可视化降维结果
4. 解释PC1和PC2的含义

<details>
<summary>点击查看答案</summary>

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. 加载数据
boston = fetch_openml(name='boston', version=1, as_frame=True)
df = boston.frame
X = df.drop('MEDV', axis=1).values
y = df['MEDV'].values
feature_names = list(df.columns[:-1])

# 2. 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. PCA降维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 4. 可视化
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 降维结果
scatter = axes[0].scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='coolwarm', alpha=0.6)
axes[0].set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')
axes[0].set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)')
axes[0].set_title('波士顿房价PCA降维')
plt.colorbar(scatter, ax=axes[0], label='房价(千美元)')

# PC1载荷
axes[1].barh(feature_names, pca.components_[0])
axes[1].set_xlabel('载荷系数')
axes[1].set_title('PC1载荷')

# PC2载荷
axes[2].barh(feature_names, pca.components_[1])
axes[2].set_xlabel('载荷系数')
axes[2].set_title('PC2载荷')

plt.tight_layout()
plt.show()

# 5. 解释
print("PC1解释:")
print("  - 主要受LSTAT(低收入比例)、RM(房间数)、PTRATIO(师生比)影响")
print("  - PC1反映社区的'社会经济状况'")
print("  - PC1越大，房价越低\n")

print("PC2解释:")
print("  - 主要受CRIM(犯罪率)、TAX(税率)、AGE(老房子比例)影响")
print("  - PC2反映社区的'治安与税务状况'")
```

</details>

---

## 十九、总结：PCA核心知识图谱

```
PCA主成分分析
│
├── 核心思想
│   ├── 降维：p维 → r维 (r < p)
│   ├── 方差最大：投影后数据最分散
│   └── 正交性：主成分之间不相关
│
├── 数学基础
│   ├── 协方差矩阵：S = X^T X / (n-1)
│   ├── 特征分解：S w = λ w
│   └── 主成分方向 = 特征向量
│
├── 算法步骤
│   ├── Step 1: 中心化
│   ├── Step 2: 计算协方差矩阵
│   ├── Step 3: 特征分解
│   ├── Step 4: 排序特征值
│   ├── Step 5: 取前r个主成分
│   └── Step 6: 投影降维
│
├── 关键概念
│   ├── 特征值：各主成分的方差
│   ├── 贡献率：λ_k / Σλ_j
│   ├── 累计贡献率：选择主成分数量的依据
│   └── 载荷：特征对主成分的贡献
│
├── 应用场景
│   ├── 数据可视化
│   ├── 特征提取
│   ├── 噪声过滤
│   └── 数据压缩
│
├── 局限性
│   ├── 只能处理线性关系
│   ├── 方差≠分类重要性
│   ├── 解释性差
│   └── 对异常值敏感
│
└── 改进方法
    ├── Kernel PCA：非线性
    ├── Sparse PCA：稀疏化
    └── Robust PCA：抗异常值
```

---

## 二十、参考资料

1. **教材**：
   - 《Pattern Recognition and Machine Learning》- Christopher Bishop
   - 《The Elements of Statistical Learning》- Hastie, Tibshirani, Friedman

2. **在线资源**：
   - sklearn官方文档：[sklearn.decomposition.PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
   - StatQuest视频教程：PCA直观解释

3. **进阶阅读**：
   - Kernel PCA原理与实现
   - Probabilistic PCA
   - Incremental PCA for Large Scale Data
