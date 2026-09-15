# LECTURE 14：贝叶斯推断入门

（本译稿为 MIT 6.041SC Lecture 14 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 14：贝叶斯推断入门**

- 整体概况
  - 动机、应用
  - 问题类型（假设检验、估计等）
- 通用框架
  - 贝叶斯法则 → 后验（4 种形式）
  - 点估计（MAP、LMS）
  - 性能指标（错误概率；均方误差）
  - 示例

---

## 第 2 页

**推断：整体概况**

（图示：三个方框——"现实世界"、"概率论（分析）"、"推断/统计学"；"现实世界"产出"数据"流向"推断/统计学"；"推断/统计学"通过"模型"支持"概率论（分析）"；"概率论（分析）"通过"预测"与"决策"作用于"现实世界"）

---

## 第 3 页

**推断的过去与现在**

- 过去：
  - 10 名患者接受了治疗：3 人死亡
  - 10 名患者未接受治疗：5 人死亡
  - 因此……
- 现在：
  - 大数据
  - 大模型
  - 大型计算机

---

## 第 4 页

**应用领域示例**

- 实验的设计与解读
  - 民意调查

（图示：美国大选相关统计与地图——"州统计（含华盛顿特区）：17 个坚定民主党、23 个坚定共和党、11 个摇摆州；选举人票统计：237 票可能投给民主党、191 票可能投给共和党、110 票摇摆"，图注"奥巴马/拜登 | 罗姆尼/瑞安"。底部版权声明：来源未知，版权所有，该内容不包含在我们的知识共享许可中，详见 https://ocw.mit.edu/help/faq-fair-use）

---

## 第 5 页

**应用领域示例**

- 营销、广告
- 推荐系统
  - Netflix 竞赛

（图示：一个数独样式的 9×9 网格，格内分布数字 1–5 与紫色问号占位符）

---

## 第 6 页

**应用领域示例**

- 金融

（图示：标普 500 指数图，截至 2007 年 3 月 30 日，指数 1200–1500 曲线与成交量柱状图，时间轴 2006 年 5 月–2007 年 3 月，成交量轴以十亿为单位 0.0–6.0。底部版权声明：来源未知，版权所有，该内容不包含在我们的知识共享许可中，详见 https://ocw.mit.edu/help/faq-fair-use）

---

## 第 7 页

**应用领域示例**

- 生命科学
  - 基因组学
  - 系统生物学
  - 神经科学，等等，等等

（图示：左为基因组图谱（Ideogram/Contig/Unigene/基因序列/基因符号等列，X 染色体区带 Xp22.33–Xq28 及对应基因名）；右为细胞信号通路图（生存因子、趋化因子/激素/递质、生长因子、细胞外基质等配体，经 RTK、GPCR、整合素等受体，激活 PI3K/Akt、Ras/MAPK、Wnt、NF-κB 等通路，调控基因表达、细胞增殖与凋亡）。图注：本图为公有领域图片，来源：Wikimedia）

---

## 第 8 页

**应用领域示例**

- 海洋的建模与监测
- 全球气候的建模与监测
- 污染的建模与监测
- 解读物理实验数据
- 解读天文学数据

---

## 第 9 页

**应用领域示例**

- 信号处理
  - 通信系统（含噪声……）
  - 语音处理与理解
  - 图像处理与理解
  - 目标跟踪
  - 定位系统（如 GPS）
  - 异常事件检测

---

## 第 10 页

**模型构建与推断未观测变量**

- $X = aS + W$
- 模型构建：
  - 已知"信号" $S$，观测 $X$
  - 推断 $a$
- 变量估计：
  - 已知 $a$，观测 $X$
  - 推断 $S$

（图示：同第 2 页的"现实世界—推断/统计学—概率论（分析）"关系图）

---

## 第 11 页

**假设检验与估计**

- 假设检验：
  - 未知量取若干个可能值之一
  - 目标是错误决策的概率很小
  - 它是飞机还是一只鸟？
- 估计：
  - 数值型未知量
  - 目标是得到一个"接近"真实但未知值的估计

---

## 第 12 页

**贝叶斯推断框架**

- 未知 $\Theta$（视为随机变量）
  - 先验分布 $p_\Theta$ 或 $f_\Theta$
- 观测 $X$
  - 观测模型 $p_{X \mid \Theta}$ 或 $f_{X \mid \Theta}$
- 使用适当版本的贝叶斯法则
  - 求 $p_{\Theta \mid X}(\cdot \mid X = x)$ 或 $f_{\Theta \mid X}(\cdot \mid X = x)$
- 先验从何而来？
  - 对称性
  - 已知取值范围
  - 先前的研究
  - 主观或任意的

（图示：流程图——先验 $p_\Theta$ → 观测过程 → 观测值 $x$ → 后验计算 → 后验 $p_{\Theta \mid X}(\cdot \mid X = x)$；先验经条件分布 $p_{X \mid \Theta}$ 与观测过程相连）

---

## 第 13 页

**贝叶斯推断的输出**

- 完整的答案是后验分布：
  - PMF $p_{\Theta \mid X}(\cdot \mid x)$ 或 PDF $f_{\Theta \mid X}(\cdot \mid x)$

（图示：左为离散 PMF 示意图与连续 PDF 示意图；右为"奥巴马选举人票分布"直方图，标注"罗姆尼 14.62%、84.59% 奥巴马、0.79% 平局"，横轴为选举人票数（0–500，标记 270），纵轴为概率（0%–6%）。底部版权声明：来源未知，版权所有，该内容不包含在我们的知识共享许可中，详见 https://ocw.mit.edu/help/faq-fair-use）

（图示：流程图——先验 $p_\Theta$ →（条件分布 $p_{X \mid \Theta}$ 经观测过程）→ 观测值 $x$ → 后验计算 → 后验 $p_{\Theta \mid X}(\cdot \mid X = x)$ → 点估计、误差分析、等等）

---

## 第 14 页

**贝叶斯推断中的点估计**

- 完整的答案是后验分布：
  - PMF $p_{\Theta \mid X}(\cdot \mid x)$ 或 PDF $f_{\Theta \mid X}(\cdot \mid x)$

（图示：左为离散 PMF 竖线图与连续 PDF 双峰曲线图）

- 估计值：$\hat{\theta} = g(x)$（一个数）
- 估计子：$\hat{\Theta} = g(X)$（一个随机变量）
- 最大后验概率（MAP）：
  - $p_{\Theta \mid X}(\theta^* \mid x) = \max_\theta p_{\Theta \mid X}(\theta \mid x)$
  - $f_{\Theta \mid X}(\theta^* \mid x) = \max_\theta f_{\Theta \mid X}(\theta \mid x)$
- 条件期望：$E[\Theta \mid X = x]$（LMS：最小均方）

---

## 第 15 页

**离散 $\Theta$，离散 $X$**

- $\Theta$ 的取值：备择假设

（图示：后验 $p_{\Theta \mid X}(\theta \mid x)$ 柱状图，$\theta = 1, 2, 3$ 处概率分别为 $0.1, 0.6, 0.3$）

- MAP 准则：$\hat{\theta} = $（讲义留白）
- $p_{\Theta \mid X}(\theta \mid x) = \dfrac{p_\Theta(\theta) p_{X \mid \Theta}(x \mid \theta)}{p_X(x)}$
- $p_X(x) = \sum_{\theta'} p_\Theta(\theta') p_{X \mid \Theta}(x \mid \theta')$
- 条件错误概率：$P(\hat{\theta} \ne \Theta \mid X = x)$
  - 在 MAP 准则下最小
- 整体错误概率：
  - $P(\hat{\Theta} \ne \Theta) = \sum_x P(\hat{\Theta} \ne \Theta \mid X = x) p_X(x)$
  - $= \sum_\theta P(\hat{\Theta} \ne \Theta \mid \Theta = \theta) p_\Theta(\theta)$

---

## 第 16 页

**离散 $\Theta$，连续 $X$**

- 标准示例：
  - 发送信号 $\Theta \in \{1, 2, 3\}$
  - $X = \Theta + W$
  - $W \sim N(0, \sigma^2)$，与 $\Theta$ 独立
  - $f_{X \mid \Theta}(x \mid \theta) = f_W(x - \theta)$

（图示：后验 $p_{\Theta \mid X}(\theta \mid x)$ 柱状图，$\theta = 1, 2, 3$ 处概率分别为 $0.1, 0.6, 0.3$）

- MAP 准则：$\hat{\theta} = $（讲义留白）
- $p_{\Theta \mid X}(\theta \mid x) = \dfrac{p_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta)}{f_X(x)}$
- $f_X(x) = \sum_{\theta'} p_\Theta(\theta') f_{X \mid \Theta}(x \mid \theta')$
- 条件错误概率：$P(\hat{\theta} \ne \Theta \mid X = x)$
  - 在 MAP 准则下最小
- 整体错误概率：
  - $P(\hat{\Theta} \ne \Theta) = \int P(\hat{\Theta} \ne \Theta \mid X = x) f_X(x) dx$
  - $= \sum_\theta P(\hat{\Theta} \ne \theta \mid \Theta = \theta) p_\Theta(\theta)$

---

## 第 17 页

**连续 $\Theta$，连续 $X$**

- 线性正态模型
  - 带噪信号的估计
  - $X = \Theta + W$
  - $\Theta$ 和 $W$：独立正态
  - 多维版本（多个正态参数，多个观测）
- 均匀分布参数的估计
  - $X$：$[0, \Theta]$ 上的均匀分布
  - $\Theta$：$[0, 1]$ 上的均匀分布
- $f_{\Theta \mid X}(\theta \mid x) = \dfrac{f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta)}{f_X(x)}$
- $f_X(x) = \int f_\Theta(\theta') f_{X \mid \Theta}(x \mid \theta') d\theta'$
- $\hat{\Theta} = g(X)$
- 关注：
  - $E[(\hat{\Theta} - \Theta)^2 \mid X = x]$
  - $E[(\hat{\Theta} - \Theta)^2]$

---

## 第 18 页

**推断一枚硬币的未知偏置与贝塔分布**

- 标准示例：
  - 硬币偏置 $\Theta$；先验 $f_\Theta(\cdot)$
  - 固定 $n$；$K$ = 正面次数
- 假设 $f_\Theta(\cdot)$ 在 $[0,1]$ 上均匀
  - $f_{\Theta \mid K}(\theta \mid k) = $（讲义留白）
  - $= \dfrac{1}{d(n,k)} \theta^k (1-\theta)^{n-k}$
  - "参数为 $(k+1, n-k+1)$ 的贝塔分布"
- 若先验是贝塔分布：$f_\Theta(\theta) = \dfrac{1}{c} \theta^\alpha (1-\theta)^\beta$
  - $f_{\Theta \mid K}(\theta \mid k) = $（讲义留白）
- $f_{\Theta \mid K}(\theta \mid k) = \dfrac{f_\Theta(\theta) p_{K \mid \Theta}(k \mid \theta)}{p_K(k)}$
- $p_K(k) = \int f_\Theta(\theta') p_{K \mid \Theta}(k \mid \theta') d\theta'$

---

## 第 19 页

**推断一枚硬币的未知偏置：点估计**

- 标准示例：
  - 硬币偏置 $\Theta$；先验 $f_\Theta(\cdot)$
  - 固定 $n$；$K$ = 正面次数
- 假设 $f_\Theta(\cdot)$ 在 $[0,1]$ 上均匀
  - $f_{\Theta \mid K}(\theta \mid k) = \dfrac{1}{d(n,k)} \theta^k (1-\theta)^{n-k}$
- MAP 估计：
  - $\hat{\theta}_{MAP} = $（讲义留白）
  - $\hat{\Theta}_{MAP} = $（讲义留白）
- $\int_0^1 \theta^\alpha (1-\theta)^\beta d\theta = \dfrac{\alpha! \beta!}{(\alpha+\beta+1)!}$
- $E[\Theta \mid K = k] = $（讲义留白）

---

## 第 20 页

**总结**

- 问题数据：$p_\Theta(\cdot)$，$p_{X \mid \Theta}(\cdot \mid \cdot)$
- 给定 $X$ 的值 $x$：求，例如，$p_{\Theta \mid X}(\cdot \mid x)$
  - 使用适当版本的贝叶斯法则
- 估计子 $\hat{\Theta} = g(X)$ ｜ 估计值 $\hat{\theta} = g(x)$
- MAP：$\hat{\theta}_{MAP} = g_{MAP}(x)$，最大化 $p_{\Theta \mid X}(\theta \mid x)$
- LMS：$\hat{\theta}_{LMS} = g_{LMS}(x) = E[\Theta \mid X = x]$
- 估计子 $\hat{\Theta}$ 的性能评估
  - $P(\hat{\Theta} \ne \Theta \mid X = x)$ ｜ $E[(\hat{\Theta} - \Theta)^2 \mid X = x]$
  - $P(\hat{\Theta} \ne \Theta)$ ｜ $E[(\hat{\Theta} - \Theta)^2]$

---

## 第 21 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
