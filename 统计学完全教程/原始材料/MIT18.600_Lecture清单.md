# MIT 18.600（Fall 2019，Scott Sheffield）讲义 Lecture 清单

- 课程：MIT 18.600 Probability and Random Variables（概率与随机变量）
- 教材：Sheldon Ross《A First Course in Probability》（第8版）——**注意：不是《All of Statistics》**
- 讲义位置：`D:\29469\Documents\notes\概率论与数理统计\原始材料\MIT18.600\`（Lecture1.pdf ~ Lecture39.pdf，共 38 个，缺 Lecture29）
- 用途：作为《统计学完全教程》第 1–5 章（概率部分）笔记的**讲义参考**；**视频主讲为 MIT 6.041SC 概率论导论**（B站上集 BV1JZhFzYEXH + 下集 BV1RXhAzaEva，对照见 `MIT6.041SC_B站Lecture对照.md`）
- 18.600 无官方视频（OCW 仅发布讲义；B站无搬运）

## Lecture 主题（从讲义首页提取）

| Lecture | 主题 | 对应《统计学完全教程》章节 |
|---|---|---|
| 1 | Permutations and combinations, Pascal's | 1.4 计数（排列组合） |
| 2 | Multinomial coefficients and more counting | 1.4 / 2.10 多项系数、多项分布 |
| 3 | What is probability? | 1.2–1.3 概率定义 |
| 4 | Axioms of probability | 1.3 概率公理 |
| 5 | Problems with all outcomes equally likely | 1.4 等可能结果 |
| 6 | Conditional probability | 1.6 条件概率 |
| 7 | Bayes' formula and independence | 1.5、1.7 独立与贝叶斯 |
| 8 | Discrete random variables | 2.2 分布函数、2.3 离散分布 |
| 9 | Expectations of discrete random variables | 3.1 期望定义 |
| 10 | Variance and standard deviation | 3.3 方差（亦引出 Chebyshev，见第 4 章） |
| 11 | Binomial random variables and repeated trials | 2.3 二项分布 |
| 12 | Poisson random variables | 2.3 泊松分布 |
| 13 | Lectures 1-12 Review | 复习 |
| 14 | More discrete random variables | 2.3 其他离散分布（几何等） |
| 15 | Poisson processes | 扩展（泊松过程，超出本书） |
| 16 | More discrete random variables | 2.3 其他离散分布 |
| 17 | Continuous random variables | 2.2、2.4 连续随机变量 |
| 18 | Uniform random variables | 2.4 均匀分布 |
| 19 | Normal random variables | 2.4 正态分布 |
| 20 | Exponential random variables | 2.4 指数分布 |
| 21 | More continuous random variables | 2.4 伽马/贝塔等 |
| 22 | Joint distribution functions | 2.5–2.6 二元/联合分布 |
| 23 | Sums of independent random variables | 2.11 随机变量之和 |
| 24 | Conditional probability, order statistics | 2.8 条件分布、顺序统计量 |
| 25 | Covariance and some conditional | 3.3 协方差 |
| 26 | Conditional expectation | 3.5 条件期望 |
| 27 | Moment generating functions | 3.6 矩母函数 |
| 28 | Lectures 17-27 Review | 复习 |
| 29 | （讲义缺失） | — |
| 30 | Weak law of large numbers | 5.3 弱大数定律 |
| 31 | Central limit theorem | 5.4 中心极限定理 |
| 32 | Strong law of large numbers and Jensen's | 5.3 强大数定律、4.2 Jensen 不等式 |
| 33 | Markov Chains | 扩展（马尔可夫链，超出本书） |
| 34 | Entropy | 扩展 |
| 35 | Martingales and the optional stopping | 扩展 |
| 36 | Risk Neutral Probability and Black-Scholes | 扩展 |
| 37–39 | Review: practice problems | 复习 |

## 各笔记参考来源对照速查（最终版）

| 笔记 | 课本 | 6.041SC 视频（B站，主看） | 18.600 Lecture（讲义，参考） |
|---|---|---|---|
| p01 第1章（上） | 1.1–1.4 | L1（上p1–p10）、L4（上p40–p48） | 1、3–5 |
| p02 第1章（下） | 1.5–1.7 | L2（上p22–p29）、L3（上p30–p39） | 6–7 |
| p03 第2章（一） | 2.1–2.2 | L5（上p49–p59）、L8（上p80–p88） | 8、17 |
| p04 第2章（二） | 2.3 | L5（上p49–p59） | 8、11–12、14、16 |
| p05 第2章（三） | 2.4 | L8（上p80–p88） | 17–21 |
| p06 第2章（四） | 2.5–2.8 | L6（上p61–p68）、L9（上p89–p98）、L10（上p100–p110） | 22–24 |
| p07 第2章（五） | 2.9–2.10 | L9（上p89–p98）、L12（上p121–p131） | 2、22 |
| p08 第2章（六） | 2.11–2.12 | L11（上p111–p119）、L12（上p121–p124） | 23 |
| p09 第3章（一） | 3.1–3.2 | L5（上p56–p59） | 9 |
| p10 第3章（二） | 3.3–3.4 | L6（上p62–p63）、L12（上p125–p131） | 10、25 |
| p11 第3章（三） | 3.5–3.6 | L13（上p132–p142） | 26–27 |
| p12 第4章 | 4.1–4.2 | L18（上p181–p182；S18.2/18.3） | 10、32（间接） |
| p13 第5章（上） | 5.1–5.3 | L18（上p183–p187） | 30、32 |
| p14 第5章（下） | 5.4–5.5 | L19（上p191–p197） | 31 |
| p15 第6章 | 6.1–6.3 | 18.650 Lecture 1–2（B站 p01–p02） | — |

> 6.041SC 细分版完整分P 对照见 `MIT6.041SC_B站Lecture对照.md`；6.041SC 教材为 Bertsekas（非 Ross、非《All of Statistics》）。
