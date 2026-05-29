# 课题六：极度稀疏矩阵的低秩补全与潜在特征发现

> **课程项目报告**
>
> 算法路线：Soft-Impute（核范数/SVD） + Alternating Least Squares（矩阵分解）
> 数据集：MovieLens-100k（原始缺失率 **93.7%**，满足题目"缺失率大于 80%"的要求）

---

## 摘要

本报告针对**极度稀疏矩阵的低秩补全与潜在特征发现**问题，以 MovieLens-100k 电影评分数据为实验对象（943 用户 × 1682 电影，仅 10 万条评分，原始缺失率 93.7%），系统实现了两种经典算法并进行对比实验：

1. **Soft-Impute**（Mazumder et al., 2010）：基于核范数正则化与奇异值软阈值的凸优化方法；
2. **ALS / Alternating Minimization**（Jain et al., 2013; Hardt, 2014）：基于双线性分解的非凸交替最小二乘方法。

实验覆盖了不同缺失率（50%–90%）、不同潜在秩（rank = 5, 10, 20, 30, 50）下的恢复误差（RMSE/MAE）对比，同时对完整矩阵进行了**奇异值谱分析**以验证低秩假设，并对分解出的潜在特征进行了**语义解释**。结果表明：Soft-Impute 在所有测试场景下均优于 ALS，且对秩的选择不敏感；ALS 在 rank 过高时会出现明显过拟合。奇异值谱的快速衰减有力支持了"用户-电影评分矩阵具有低秩结构"这一核心假设。

---

## 1. 问题背景

### 1.1 推荐系统与 Netflix 竞赛

在推荐系统中，用户-物品交互数据通常以矩阵形式组织：行代表用户，列代表物品，元素为用户对物品的评分。由于每个用户只会评价极少数物品，该矩阵极度稀疏。Netflix Prize（Bell & Koren, 2007）是这一问题的典型场景：约 48 万用户、1.8 万电影，总条目超 86 亿，但观测到的评分仅占约 1.2%。

### 1.2 低秩假设

Mazumder et al. (2010) 在论文第 1 节（Introduction）中指出：

> "...we assume that Z can be well represented by a matrix of low rank, that is, Z ≈ V_{m×k} G_{k×n}, where k ≪ min(n,m). In this recommender-system example, low rank structure suggests that movies can be grouped into a small number of 'genres', with G_{ℓj} the relative score for movie j in genre ℓ. Viewer i on the other hand has an affinity V_{iℓ} for genre ℓ..."

换言之，用户偏好并非独立：喜欢科幻的人通常也喜欢动作片；喜欢文艺片的人评分风格往往相似。这些**潜在特征**（latent features，如"商业片偏好"、"艺术片偏好"）决定了评分，使得评分矩阵可以用少量"潜在维度"来近似，即矩阵是**低秩**的。

### 1.3 问题形式化

设观测到的评分矩阵为 X ∈ ℝ^{m×n}，观测位置集合为 Ω ⊂ {1,…,m} × {1,…,n}。矩阵补全问题旨在恢复完整的低秩矩阵 Z：

$$
\min_{Z} \; \text{rank}(Z) \quad \text{s.t.} \quad \sum_{(i,j)\in\Omega}(X_{ij} - Z_{ij})^2 \le \delta.
\tag{1}
$$

其中 δ ≥ 0 为误差容忍参数。由于 rank(·) 的非凸性，问题 (1) 是组合困难的（Srebro & Jaakkola, 2003）。

---

## 2. 数学理论

### 2.1 奇异值分解（SVD）

对任意矩阵 M ∈ ℝ^{m×n}，其（完全）奇异值分解为：

$$
M = U \Sigma V^T = \sum_{i=1}^{r} \sigma_i u_i v_i^T,
\tag{2}
$$

其中 r = rank(M)，奇异值满足 σ₁ ≥ σ₂ ≥ … ≥ σ_r > 0，U、V 为正交矩阵。SVD 是提取矩阵主成分、潜在特征与低维结构的强大工具。

### 2.2 低秩近似（Eckart-Young-Mirsky 定理）

对目标秩 k < r，最优 Frobenius 范数低秩近似由截断 SVD 给出：

$$
M_k = \sum_{i=1}^{k} \sigma_i u_i v_i^T.
\tag{3}
$$

该定理保证了在完全观测情形下，截断 SVD 是最优的低秩逼近。然而，在矩阵补全问题中只有部分条目被观测，无法直接计算 SVD。

### 2.3 核范数松弛

Mazumder et al. (2010) 在第 1 节中将式 (1) 中的秩约束替换为**核范数**（nuclear norm）：

$$
\|Z\|_* = \sum_{i=1}^{r} \sigma_i(Z),
\tag{4}
$$

即 Z 的所有奇异值之和。核范数是 rank(·) 的有效凸松弛（Fazel, 2002; Candès & Recht, 2008; Recht et al., 2007）。由此得到凸优化问题：

$$
\min_{Z} \; \frac{1}{2}\|P_\Omega(X) - P_\Omega(Z)\|_F^2 + \lambda \|Z\|_*.
\tag{5}
$$

式 (5) 即 Mazumder et al. (2010) 论文中的**公式 (3)** 与**公式 (10)**。其中 P_Ω 为观测位置投影算子：

$$
[P_\Omega(Y)]_{ij} = \begin{cases} Y_{ij}, & (i,j)\in\Omega, \\ 0, & (i,j)\notin\Omega. \end{cases}
\tag{6}
$$

式 (6) 对应文献 [1] 第 3.1 节的公式 (7)。

---

## 3. 算法实现

### 3.1 Soft-Impute 算法

**来源**：Mazumder, Hastie & Tibshirani (2010), JMLR 11:2287–2322.
**核心章节**：第 3.2 节 Lemma 1（软阈值闭式解），第 3.3 节 Algorithm 1（完整迭代算法）。

#### 3.1.1 核心思想

Soft-Impute 是一种不动点迭代算法，其动机源于 EM 框架：每一步先用当前估计填补缺失值，再对填补后的矩阵做软阈值 SVD，从而得到低秩更新。Mazumder et al. (2010) 在第 3.3 节明确指出该算法"inspired by SVD-IMPUTE (Troyanskaya et al., 2001)—an EM-type iterative algorithm"。

#### 3.1.2 迭代公式

记 $Z^{old}$ 为当前迭代矩阵，则更新规则为（文献 [1] Algorithm 1, Step 2(a)i）：

$$
Z^{\text{new}} \;\leftarrow\; S_\lambda\!\left( P_\Omega(X) + P_\Omega^\perp(Z^{\text{old}}) \right).
\tag{7}
$$

其中 P_Ω^⊥ 为补投影算子（未观测位置保留，已观测位置置零），S_λ(·) 为**奇异值软阈值算子**。

#### 3.1.3 软阈值算子 S_λ

**文献 [1] 第 3.2 节 Lemma 1** 给出了如下闭式解：若 W = U·diag(d₁,…,d_r)·V^T 为 W 的 SVD，则

$$
S_\lambda(W) = U \cdot \text{diag}\bigl((d_1-\lambda)_+, \dots, (d_r-\lambda)_+\bigr) \cdot V^T,
\tag{8}
$$

其中 (t)_+ = max(t, 0)。该算子将小于 λ 的奇异值压缩至零，大于 λ 的奇异值收缩 λ，从而实现**自动秩选择**与**正则化**。

#### 3.1.4 收敛性

文献 [1] 第 4 节（Convergence Analysis）证明：Soft-Impute 产生的迭代序列使目标函数 (5) 单调递减，并渐近收敛到最优解；非渐近收敛速率为 O(1/k)。这与需要手动选择步长的通用一阶方法（如 Nesterov 加速梯度法）形成对比，也是该算法"最容易写、最容易解释"的优势所在。

#### 3.1.5 算法伪代码

```
Algorithm 1 SOFT-IMPUTE [Mazumder et al., 2010, Algorithm 1]
-----------------------------------------------------------------
1. Initialize Z^{old} = 0.
2. Do for λ₁ > λ₂ > ... > λ_K:
   (a) Repeat:
       i.   Z^{new} ← S_{λ_k}( P_Ω(X) + P_Ω^⊥(Z^{old}) )
       ii.  If ‖Z^{new}−Z^{old}‖_F / ‖Z^{old}‖_F < ε  exit.
       iii. Z^{old} ← Z^{new}
   (b) Assign Ẑ_{λ_k} ← Z^{new}.
3. Output the sequence of solutions Ẑ_{λ_1},...,Ẑ_{λ_K}.
```

在我们的实现中，为加速收敛，初始化采用全局均值矩阵而非零矩阵；λ 取为初始矩阵最大奇异值的 5%。

---

### 3.2 Alternating Least Squares (ALS)

**来源**：
- Jain, Netrapalli & Sanghavi (2013), *Low-rank Matrix Completion using Alternating Minimization*, STOC 2013. (arXiv:1212.0467)
- Hardt (2014), *Understanding Alternating Minimization for Matrix Completion*, FOCS 2014. (arXiv:1312.0925)

**核心章节**：文献 [2] 第 2 节（问题形式化与 Incoherence 条件）、Algorithm 1（AltMinSense 伪代码）；文献 [3] 第 1 节（基本更新公式 (4)）、Theorem 1.1（样本复杂度保证）。

#### 3.2.1 核心思想

与核范数方法不同，ALS 直接对目标矩阵进行**双线性参数化**：

$$
M \approx U V^T, \quad U \in \mathbb{R}^{m\times k}, \; V \in \mathbb{R}^{n\times k},
\tag{9}
$$

其中 k 为预设的潜在维度。整体优化问题是**非凸**的：

$$
\min_{U,V} \; \sum_{(i,j)\in\Omega} \bigl( M_{ij} - (UV^T)_{ij} \bigr)^2 + \lambda\bigl(\|U\|_F^2 + \|V\|_F^2\bigr).
\tag{10}
\tag{LRMC}
$$

式 (10) 即文献 [2] 中的 **(LRMC)** 问题形式化，也是文献 [3] 引言中讨论的优化目标。然而，若固定 U 优化 V（或反之），每个子问题都是凸的**正则化最小二乘**，可解析求解。这就是"交替"一词的含义。

#### 3.2.2 更新规则

**文献 [3] 第 1 节公式 (4)** 给出了 ALS 的基本更新步骤（以右因子为例）：

$$
Y_\ell = \arg\min_Y \bigl\| P_\Omega(A - X_{\ell-1} Y^\top) \bigr\|_F^2.
\tag{11}
$$

在我们的实现中，对每个用户 i（固定 V），其潜在向量 u_i 的闭式解为：

$$
u_i = \bigl( V_{\Omega_i}^T V_{\Omega_i} + \lambda I \bigr)^{-1} V_{\Omega_i}^T M_{i,\Omega_i},
\tag{12}
$$

其中 Ω_i 表示用户 i 评过分的电影集合。类似地，对每个电影 j（固定 U）：

$$
v_j = \bigl( U_{\Omega_j}^T U_{\Omega_j} + \lambda I \bigr)^{-1} U_{\Omega_j}^T M_{\Omega_j,j}.
\tag{13}
$$

这种逐行/逐列独立求解的策略使 ALS 具有天然的**并行性**，也是其"速度快、工业界常用"的根本原因（Netflix Prize 获胜方案即大量采用了此类矩阵分解技术）。

#### 3.2.3 理论保证

文献 [2] 的 **Theorem 2.2** 证明了：在矩阵满足非相干（incoherence）条件、观测条目均匀随机采样且数量足够多时，ALS 能以**几何速率**（geometric convergence）恢复真实矩阵，迭代复杂度为 O(log(1/ε))。文献 [3] 的 **Theorem 1.1** 进一步将样本复杂度要求降低了约秩的四次方，并证明了算法在**近线性时间** O(nk³ + |Ω|·k) 内运行。这些理论结果为 ALS 的广泛使用提供了坚实的数学基础。

#### 3.2.4 算法特点

| 特性 | Soft-Impute | ALS |
|------|-------------|-----|
| 优化问题 | 凸（核范数） | 非凸（双线性分解） |
| 超参数 | λ（软阈值） | k（秩）、λ（正则化） |
| 自动选秩 | 是（软阈值压缩小奇异值） | 否（需预设 k） |
| 每步瓶颈 | 低秩 SVD | 多个最小二乘 |
| 理论保证 | 全局最优 | 局部最优，需良好初始化 |
| 工业应用 | 学术研究、中小规模 | Netflix、大规模推荐系统 |

---

## 4. 数据集与实验设置

### 4.1 MovieLens-100k

本项目采用 GroupLens 实验室发布的 **MovieLens-100k** 数据集（Harper & Konstan, 2015）。该数据集是推荐系统领域最经典、最广泛使用的基准数据之一，具有"小、干净、好处理"的特点。

- **用户数**：943
- **电影数**：1682
- **总可能条目**：943 × 1682 = 1,586,126
- **实际评分数**：100,000
- **评分范围**：1–5 的整数
- **原始缺失率**：**93.70%**（满足题目"缺失率大于 80%"的要求）

### 4.2 评价指标

采用推荐系统领域标准的 **RMSE**（均方根误差）与 **MAE**（平均绝对误差）：

$$
\text{RMSE} = \sqrt{\frac{1}{|\Omega_{\text{test}}|} \sum_{(i,j)\in\Omega_{\text{test}}} (\hat{M}_{ij} - M_{ij})^2},
\qquad
\text{MAE} = \frac{1}{|\Omega_{\text{test}}|} \sum_{(i,j)\in\Omega_{\text{test}}} |\hat{M}_{ij} - M_{ij}|.
\tag{14}
$$

### 4.3 实验环境

- Python 3.14.3
- NumPy 2.4.4, SciPy 1.17.1, Matplotlib 3.10.9, Pandas 3.0.2
- 全部代码自主实现，未调用 fancyimpute / scikit-surprise 等外部库

---

## 5. 实验结果

### 5.1 单次运行基准测试

在 80%/20% 训练/测试划分下，两种算法的典型表现如下：

| 算法 | Test RMSE | Test MAE | 收敛迭代数 |
|------|-----------|----------|------------|
| Soft-Impute (λ=15, rank≤50) | **0.920** | **0.733** | 60 |
| ALS (k=10, λ=0.5) | 1.083 | 0.815 | 50 |

Soft-Impute 在 RMSE 和 MAE 上均显著优于 ALS，这与核范数方法具有全局最优保证的理论优势一致。

---

### 5.2 实验一：不同缺失率下的恢复效果

为了系统评估算法在极度稀疏场景下的鲁棒性，我们在原始观测条目上按不同比例（50%、70%、80%、90%）进一步隐藏部分评分，构造不同缺失率的训练集，剩余作为测试集。

**结果图表**：见 `results/exp_missing_rate.png`

| 缺失率 | Soft-Impute RMSE | Soft-Impute MAE | ALS RMSE | ALS MAE |
|--------|------------------|-----------------|----------|---------|
| 50% | 0.951 | 0.763 | 1.244 | 0.935 |
| 70% | 0.992 | 0.804 | 1.409 | 1.074 |
| 80% | 1.023 | 0.833 | 1.545 | 1.203 |
| 90% | 1.082 | 0.892 | 1.609 | 1.271 |

**分析**：
- 随着缺失率从 50% 上升至 90%，两种算法的误差均单调上升，符合直观：信息越少，恢复越困难。
- **Soft-Impute 的优势随缺失率增加而更加显著**。在 90% 缺失率下，Soft-Impute 的 RMSE 比 ALS 低 **32.8%**。这是因为核范数正则化通过软阈值自动选择有效秩，避免了 ALS 在高缺失率下因信息不足而导致的拟合困难。
- 两条曲线的斜率差异表明：Soft-Impute 对稀疏性的鲁棒性更强。

---

### 5.3 实验二：不同潜在秩（rank）的影响

固定 80%/20% 训练/测试划分，比较不同 rank（k = 5, 10, 20, 30, 50）对两种算法的影响。

**结果图表**：见 `results/exp_rank.png`

| rank k | Soft-Impute RMSE | Soft-Impute MAE | ALS RMSE | ALS MAE |
|--------|------------------|-----------------|----------|---------|
| 5 | 0.921 | 0.733 | 0.985 | 0.753 |
| 10 | 0.921 | 0.733 | 1.083 | 0.815 |
| 20 | 0.921 | 0.733 | 1.271 | 0.953 |
| 30 | 0.920 | 0.733 | 1.372 | 1.044 |
| 50 | 0.920 | 0.733 | 1.430 | 1.103 |

**分析**：
- **Soft-Impute 对 rank 几乎完全不敏感**：RMSE 稳定在 0.920 附近。这是因为软阈值算子 S_λ 自动将小于 λ 的奇异值置零，有效秩由数据本身和 λ 共同决定，而非人为预设。这一特性极大降低了调参难度。
- **ALS 的误差随 rank 增加而显著恶化**：从 k=5 时的 RMSE=0.985 上升到 k=50 时的 1.430。rank 增大使模型容量增加，但训练数据量不变，导致**过拟合**。这体现了非凸双线性分解的一个核心缺点：需要仔细选择 k。
- 该实验有力说明：在缺乏充足观测的情况下，盲目增加模型复杂度（rank）是有害的；核范数正则化通过"收缩小奇异值"自动实现了模型选择。

---

### 5.4 实验三：奇异值谱分析

对 MovieLens-100k 完整评分矩阵（缺失值以全局均值填充）进行 SVD，分析奇异值的衰减特性。

**结果图表**：见 `results/singular_spectrum.png`

**关键发现**：
- **奇异值快速衰减**：最大奇异值 σ₁ ≈ 4000，而前 10 个奇异值已降至约 30，前 100 个降至约 10，衰减呈现明显的指数型趋势。
- **低秩结构得到验证**：虽然第一个奇异值（对应全局均值项）能量占比极高，但除去均值项后，后续奇异值仍以较快速度衰减。这说明用户评分行为确实可以由少量潜在因子主导。
- 奇异值谱的快速衰减为矩阵补全问题的**适定性**（well-posedness）提供了经验证据：真实评分矩阵确实接近低秩，因此基于低秩假设的补全算法有望成功恢复缺失条目。

---

### 5.5 实验四：潜在特征发现与解释

通过 ALS 分解得到的物品潜在矩阵 V ∈ ℝ^{1682×10}，我们分析了前几个维度上得分最高/最低的电影，尝试解释每个维度的语义含义。

**完整结果**：见 `results/latent_features.txt`

**典型发现示例**：

- **维度 1**：正向最强电影包括 *FairyTale: A True Story*、*Spice World*、*Les Misérables*、*Angels and Insects*；负向最强包括 *Mr. Wrong*、*Kingpin*、*Threesome*。这一维度似乎区分了"**家庭/文艺剧情片**"与"**低俗喜剧/黑色幽默**"，可解释为"**严肃情感深度 vs. 轻松娱乐**"。

- **维度 2**：正向包括 *A Thin Line Between Love and Hate*、*The Stupids*、*Cabin Boy*；负向包括 *The Spitfire Grill*、*Transformers: The Movie*、*Michael Collins*。这一维度可能对应"**小众/另类风格 vs. 主流商业大片**"，即"**艺术/独立电影偏好**"。

- **维度 3**：正向包括 *Lost in Space*、*Naked*、*Everyone Says I Love You*；负向包括 *Down Periscope*、*Bio-Dome*、*Jury Duty*。这一维度似乎捕捉了"**科幻/奇幻/浪漫元素**"与"**纯搞笑闹剧**"之间的对比。

这些发现与 Mazumder et al. (2010) 在引言中的论述高度一致：低秩分解自动提取的潜在维度，对应着用户对不同"类型"（genres）或"风格"的隐含偏好。这正是题目所要求的"**潜在特征发现**"与"**解释分解出的潜在特征矩阵的意义**".

---

## 6. 结论

本项目以 MovieLens-100k 数据集为载体，围绕"极度稀疏矩阵的低秩补全与潜在特征发现"这一课题，完成了以下工作：

1. **理论层面**：系统梳理了低秩矩阵补全的数学基础，包括 SVD、低秩近似、核范数松弛，以及交替最小化的非凸优化框架；所有核心公式均严格标注了原始文献来源（Mazumder et al., 2010; Jain et al., 2013; Hardt, 2014）。

2. **算法层面**：从零实现了 **Soft-Impute** 与 **ALS** 两种经典算法，并在代码注释中明确标注了每个步骤对应的论文章节与公式编号。

3. **实验层面**：
   - 验证了数据集原始缺失率（93.7%）满足题目要求；
   - 在 50%–90% 缺失率范围内，Soft-Impute 始终优于 ALS，且在极度稀疏场景下优势更明显；
   - 发现 Soft-Impute 对人为预设的 rank 不敏感（自动秩选择），而 ALS 在 rank 过高时明显过拟合；
   - 通过奇异值谱分析，从经验上验证了评分矩阵的低秩结构；
   - 对分解出的潜在特征进行了语义解释，发现其对应"家庭/文艺 vs. 娱乐"、"独立/小众 vs. 主流商业"等可理解的观影偏好维度。

4. **工程层面**：全部代码使用纯 Python + NumPy/SciPy 实现，不依赖 fancyimpute / scikit-surprise 等现成库，确保了对算法原理的完全掌控；实验结果以高质量图表保存，可直接用于课程报告与课堂展示。

**最终推荐**：对于课程项目，Soft-Impute 作为"主算法"最为合适——它数学上优雅（凸优化、全局收敛）、实现上简洁（核心仅为 SVD + 软阈值）、效果上稳健（对超参数不敏感）。ALS 作为"对比算法"能很好体现非凸分解路线的优缺点，增加报告的深度与层次感。

---

## 参考文献

[1] **Rahul Mazumder, Trevor Hastie, and Robert Tibshirani.** "Spectral Regularization Algorithms for Learning Large Incomplete Matrices." *Journal of Machine Learning Research*, 11:2287–2322, 2010.
> 重点引用章节：Section 1 (Introduction), Section 3.2 (Lemma 1, 软阈值闭式解), Section 3.3 (Algorithm 1, SOFT-IMPUTE 伪代码), Section 4 (Convergence Analysis).

[2] **Prateek Jain, Praneeth Netrapalli, and Sujay Sanghavi.** "Low-rank Matrix Completion using Alternating Minimization." *Proceedings of the 45th Annual ACM Symposium on Theory of Computing (STOC)*, 2013. arXiv:1212.0467.
> 重点引用章节：Section 2 (问题形式化与 Incoherence 定义), Algorithm 1 (AltMinSense 伪代码), Theorem 2.2 (几何收敛保证).

[3] **Moritz Hardt.** "Understanding Alternating Minimization for Matrix Completion." *Proceedings of the 55th IEEE Annual Symposium on Foundations of Computer Science (FOCS)*, 2014. arXiv:1312.0925.
> 重点引用章节：Section 1 (Introduction, 基本更新公式 (4)), Theorem 1.1 (样本复杂度与恢复保证), Section 4 (交替最小二乘的鲁棒收敛分析).

[4] **F. Maxwell Harper and Joseph A. Konstan.** "The MovieLens Datasets: History and Context." *ACM Transactions on Interactive Intelligent Systems (TiiS)*, 5(4):Article 19, 2015.

[5] **Emmanuel J. Candès and Benjamin Recht.** "Exact Matrix Completion via Convex Optimization." *Foundations of Computational Mathematics*, 9(6):717–772, 2009.

[6] **Maryam Fazel.** "Matrix Rank Minimization with Applications." *PhD thesis, Stanford University*, 2002.

---

## 附录：项目文件结构

```
d:\高代/
├── ml-100k/ml-100k/          # MovieLens-100k 数据集
├── src/
│   ├── data_loader.py        # 数据加载与预处理
│   ├── soft_impute.py        # Soft-Impute 算法（含文献 [1] 详细引用）
│   ├── als.py                # ALS 算法（含文献 [2][3] 详细引用）
│   ├── metrics.py            # RMSE / MAE 评估指标
│   └── experiments.py        # 实验脚本与可视化
├── results/
│   ├── exp_missing_rate.png  # 实验一：缺失率对比图
│   ├── exp_rank.png          # 实验二：rank 对比图
│   ├── singular_spectrum.png # 实验三：奇异值谱分析图
│   └── latent_features.txt   # 实验四：潜在特征解释
├── main.py                   # 主运行脚本
└── report.md                 # 本报告
```

**运行方式**：
```bash
cd d:\高代
python main.py
```

全部实验在普通笔记本上约 **1–2 分钟**内完成。
