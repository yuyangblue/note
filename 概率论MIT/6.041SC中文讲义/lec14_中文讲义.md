# LECTURE 14：贝叶斯推断导论

（本译稿为 MIT 6.041SC Lecture 14 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 14：贝叶斯推断导论**

- 整体概况
  - 动机、应用
  - 问题类型（假设检验、估计等）
- 通用框架
  - 贝叶斯法则 → 后验
    - （4 种版本）
  - 点估计（MAP、LMS）
  - 性能度量
    - （错误概率；均方误差）
  - 示例

---

## 第 2 页

**推断：整体概况**

（图示：三个方框——"Real world（现实世界）"、"Probability theory (Analysis)（概率论（分析））"、"Inference/Statistics（推断/统计）"，箭头标注：现实世界→Data（数据）→推断/统计→Models（模型）→概率论（分析）→Predictions（预测）与 Decisions（决策）→现实世界）

---

## 第 3 页

**推断：过去与现在**

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
  - 民意调查（polling）

（图示：右侧为美国大选地图，州以蓝色/浅灰/红色标注倾向，下方列出：STATE COUNTS（含华盛顿特区）——17 稳为民主党、23 稳为共和党、11 摇摆；ELECTORAL VOTE COUNTS——237 可能民主党、191 可能共和党、110 摇摆；图注 Obama/Biden | Romney/Ryan；版权声明：© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see https://ocw.mit.edu/help/faq-fair-use.）

---

## 第 5 页

**应用领域示例**

- 营销、广告
- 推荐系统
  - Netflix 竞赛

（图示：右侧为数独网格示意图，格内分布数字 1–5 与多个紫色问号占位格）

---

## 第 6 页

**应用领域示例**

- 金融

（图示：右侧为标普 500 指数走势图（as of 30-Mar-2007），纵轴 1500–1200，横轴 May06 至 Mar07，下方为成交量柱状图，单位 Billions，刻度 6.0/4.0/2.0/0.0；版权声明：© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see https://ocw.mit.edu/help/faq-fair-use.）

---

## 第 7 页

**应用领域示例**

- 生命科学
  - 基因组学
  - 系统生物学
  - 神经科学，等等，等等

（图示：左侧为基因组学数据表（Ideogram/Contig/HsUnig/Gene_seq/Symbol 各列，染色体位置 Xp22.32–Xq28 及基因符号）；右侧为细胞信号通路示意图（生长因子/细胞因子/趋化因子等细胞外因子经 RTK/GPCR/整合素等受体，激活 PI3K、MAPK、NF-κB、Wnt 等通路，调控基因调节、细胞增殖、细胞凋亡等）；图注：This image is in the public domain. Source: Wikimedia.）

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
  - 定位系统（例如 GPS）
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

（图示：右侧为"Real world（现实世界）—Data（数据）—Inference/Statistics（推断/统计）—Models（模型）—Probability theory (Analysis)（概率论（分析））—Predictions（预测）/Decisions（决策）"框图）

---

## 第 11 页

**假设检验与估计**

- 假设检验：
  - 未知量取少数几个可能值之一
  - 目标是使错误决策的概率小
- 是飞机还是鸟？

（图示：无）

- 估计：
  - 数值型未知量
  - 目标是得到一个"接近"真实但未知值的估计

---

## 第 12 页

**贝叶斯推断框架**

- 未知 $\Theta$
  - 被当作随机变量处理
  - 先验分布 $p_\Theta$ 或 $f_\Theta$
- 观测 $X$
  - 观测模型 $p_{X \mid \Theta}$ 或 $f_{X \mid \Theta}$
- 使用适当版本的贝叶斯法则
  - 求出 $p_{\Theta \mid X}(\cdot \mid X = x)$ 或 $f_{\Theta \mid X}(\cdot \mid X = x)$

（图示：左侧框图——先验 $p_\Theta$ 与条件 $p_{X \mid \Theta}$ → 观测过程 → 观测值 $x$ → 后验计算 → 后验 $p_{\Theta \mid X}(\cdot \mid X = x)$）

- 先验从何而来？
  - 对称性
  - 已知范围
  - 早期研究
  - 主观或任意设定

---

## 第 13 页

**贝叶斯推断的输出**

- 完整答案是后验分布：
  - PMF $p_{\Theta \mid X}(\cdot \mid x)$ 或 PDF $f_{\Theta \mid X}(\cdot \mid x)$

（图示：左侧为离散 PMF 竖线图与连续 PDF 曲线示意；右侧为奥巴马的选举人票分布柱状图——ROMNEY 14.62%、84.59% OBAMA、0.79% TIE，纵轴 PROBABILITY 6%–0%，横轴 NUMBER OF ELECTORAL VOTES 0–450，标注 270 线；版权声明：© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see https://ocw.mit.edu/help/faq-fair-use.）

（图示：底部流程图——先验 $p_\Theta$ 与条件 $p_{X \mid \Theta}$ → 观测过程 → $x$ → 后验计算 → $p_{\Theta \mid X}(\cdot \mid X = x)$ → 点估计 / 误差分析 等）

---

## 第 14 页

**贝叶斯推断中的点估计**

- 完整答案是后验分布：
  - PMF $p_{\Theta \mid X}(\cdot \mid x)$ 或 PDF $f_{\Theta \mid X}(\cdot \mid x)$

（图示：左侧为离散 PMF 竖线图与连续 PDF 曲线示意）

- 估计：$\hat{\theta} = g(x)$
  - （数值）
- 估计量：$\hat{\Theta} = g(X)$
  - （随机变量）
- 最大后验概率（MAP）：
  - $p_{\Theta \mid X}(\theta^* \mid x) = \max_\theta p_{\Theta \mid X}(\theta \mid x)$
  - $f_{\Theta \mid X}(\theta^* \mid x) = \max_\theta f_{\Theta \mid X}(\theta \mid x)$
- 条件期望：$\mathbb{E}[\Theta \mid X = x]$（LMS：最小均方）

---

## 第 15 页

**离散 $\Theta$，离散 $X$**

- $\Theta$ 的取值：备选假设

（图示：左侧为后验 $p_{\Theta \mid X}(\theta \mid x)$ 柱状图，$\theta$ 取 1、2、3 时后验分别为 0.1、0.6、0.3）

- MAP 准则：$\hat{\theta} = $（讲义留白）
- $p_{\Theta \mid X}(\theta \mid x) = \dfrac{p_\Theta(\theta) p_{X \mid \Theta}(x \mid \theta)}{p_X(x)}$
- $p_X(x) = \sum_{\theta'} p_\Theta(\theta') p_{X \mid \Theta}(x \mid \theta')$
- 条件错误概率：
  - $\text{P}(\hat{\theta} \neq \Theta \mid X = x)$
  - 在 MAP 准则下最小
- 整体错误概率：
  - $\text{P}(\hat{\Theta} \neq \Theta) = \sum_x \text{P}(\hat{\Theta} \neq \Theta \mid X = x) p_X(x)$
  - $= \sum_\theta \text{P}(\hat{\Theta} \neq \Theta \mid \Theta = \theta) p_\Theta(\theta)$

---

## 第 16 页

**离散 $\Theta$，连续 $X$**

- 标准示例：
  - 发送信号 $\Theta \in \{1, 2, 3\}$
  - $X = \Theta + W$
  - $W \sim N(0, \sigma^2)$，与 $\Theta$ 独立
  - $f_{X \mid \Theta}(x \mid \theta) = f_W(x - \theta)$

（图示：左侧为后验 $p_{\Theta \mid X}(\theta \mid x)$ 柱状图，$\theta$ 取 1、2、3 时后验分别为 0.1、0.6、0.3）

- MAP 准则：$\hat{\theta} = $（讲义留白）
- $p_{\Theta \mid X}(\theta \mid x) = \dfrac{p_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta)}{f_X(x)}$
- $f_X(x) = \sum_{\theta'} p_\Theta(\theta') f_{X \mid \Theta}(x \mid \theta')$
- 条件错误概率：
  - $P(\hat{\Theta} \neq \Theta \mid X = x)$
  - 在 MAP 准则下最小
- 整体错误概率：
  - $P(\hat{\Theta} \neq \Theta) = \int P(\hat{\Theta} \neq \Theta \mid X = x) f_X(x) \, dx$
  - $= \sum_\theta P(\hat{\Theta} \neq \theta \mid \Theta = \theta) p_\Theta(\theta)$

---

## 第 17 页

**连续 $\Theta$，连续 $X$**

- 线性正态模型
  - 含噪信号的估计
  - $X = \Theta + W$
  - $\Theta$ 与 $W$：独立正态
  - 多维版本（许多正态参数、许多观测）
- 估计均匀分布的参数
  - $X$：uniform$[0, \Theta]$
  - $\Theta$：uniform $[0, 1]$
- $\widehat{\Theta} = g(X)$
  - 关注：
    - $\mathbb{E}[(\widehat{\Theta} - \Theta)^2 \mid X = x]$
    - $\mathbb{E}[(\widehat{\Theta} - \Theta)^2]$
- $f_{\Theta \mid X}(\theta \mid x) = \dfrac{f_\Theta(\theta) f_{X \mid \Theta}(x \mid \theta)}{f_X(x)}$
- $f_X(x) = \int f_\Theta(\theta') f_{X \mid \Theta}(x \mid \theta') \, d\theta'$

---

## 第 18 页

**推断硬币的未知偏置与贝塔分布**

- 标准示例：
  - 具有偏置 $\Theta$ 的硬币；先验 $f_\Theta(\cdot)$
  - 固定 $n$；$K$ = 正面朝上的次数
- 假设 $f_\Theta(\cdot)$ 在 $[0,1]$ 上均匀
  - $f_{\Theta \mid K}(\theta \mid k) = $（讲义留白）
  - $= \dfrac{1}{d(n,k)} \theta^k (1-\theta)^{n-k}$
  - "贝塔分布，参数 $(k + 1, n - k + 1)$"
- 若先验是贝塔分布：$f_\Theta(\theta) = \dfrac{1}{c} \theta^\alpha (1-\theta)^\beta$
  - $f_{\Theta \mid K}(\theta \mid k) = $（讲义留白）
- $f_{\Theta \mid K}(\theta \mid k) = \dfrac{f_\Theta(\theta) p_{K \mid \Theta}(k \mid \theta)}{p_K(k)}$
- $p_K(k) = \int f_\Theta(\theta') p_{K \mid \Theta}(k \mid \theta') \, d\theta'$

---

## 第 19 页

**推断硬币的未知偏置：点估计**

- 标准示例：
  - 具有偏置 $\Theta$ 的硬币；先验 $f_\Theta(\cdot)$
  - 固定 $n$；$K$ = 正面朝上的次数
- 假设 $f_\Theta(\cdot)$ 在 $[0,1]$ 上均匀
  - $f_{\Theta \mid K}(\theta \mid k) = \dfrac{1}{d(n,k)} \theta^k (1-\theta)^{n-k}$
- $\int_0^1 \theta^\alpha (1-\theta)^\beta \, d\theta = \dfrac{\alpha! \beta!}{(\alpha+\beta+1)!}$
- MAP 估计：
  - $\hat{\theta}_{MAP} = $（讲义留白）
  - $\widehat{\Theta}_{MAP} = $（讲义留白）
- $E[\Theta \mid K = k] = $（讲义留白）

---

## 第 20 页

**总结**

- 问题数据：
  - $p_\Theta(\cdot)$，$p_{X \mid \Theta}(\cdot \mid \cdot)$
- 给定 $X$ 的值 $x$：
  - 求，例如，$p_{\Theta \mid X}(\cdot \mid x)$
  - 使用适当版本的贝叶斯法则
- 估计量 $\widehat{\Theta} = g(X)$
- 估计 $\widehat{\theta} = g(x)$
  - MAP：$\widehat{\theta}_{MAP} = g_{MAP}(x)$ 最大化 $p_{\Theta \mid X}(\theta \mid x)$
  - LMS：$\widehat{\theta}_{LMS} = g_{LMS}(x) = \mathbb{E}[\Theta \mid X = x]$
- 估计量 $\widehat{\Theta}$ 的性能评估
  - $\mathbb{P}(\widehat{\Theta} \neq \Theta \mid X = x)$
  - $\mathbb{E}[(\widehat{\Theta} - \Theta)^2 \mid X = x]$
  - $\mathbb{P}(\widehat{\Theta} \neq \Theta)$
  - $\mathbb{E}[(\widehat{\Theta} - \Theta)^2]$

---

## 第 21 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
