# LECTURE 2：条件作用与贝叶斯法则（Conditioning and Bayes' rule）

（本译稿为 MIT 6.041SC Lecture 2 讲义原图的逐页中文翻译，内容与英文原版一一对应，未添加或改写任何内容。）

---

## 第 1 页

**LECTURE 2：条件作用与贝叶斯法则**

- 条件概率
- 三个重要工具：
  - 乘法法则
  - 全概率定理
  - 贝叶斯法则（→ 推断）

---

## 第 2 页

**条件作用的思想**

- 用新信息修正模型
- 假设 12 个等可能结果
- $P(A) = 5/12$，$P(B) = 6/12$
- 若被告知 $B$ 已发生：
  - $P(A \mid B) = $（讲义留白）
  - $P(B \mid B) = $（讲义留白）

（图示：Ω 被划分为 A 独有 3/12、A∩B 2/12、B 独有 4/12、其余 3/12）

---

## 第 3 页

**条件概率的定义**

- $P(A \mid B)$ = "在 $B$ 已发生的条件下，$A$ 的概率"
- $P(A \mid B) = P(A \cap B) / P(B)$
- 仅在 $P(B) > 0$ 时定义

（图示：Ω 中 A∩B 为 2/12，B 独有为 4/12）

---

## 第 4 页

**示例：掷两次四面骰子**

- 令 $B$ 为事件：$\min(X, Y) = 2$
- 令 $M = \max(X, Y)$
- $P(M = 1 \mid B) = $（讲义留白）
- $P(M = 3 \mid B) = $（讲义留白）

（图示：4×4 网格，X = 第一次掷，Y = 第二次掷）

---

## 第 5 页

**条件概率具有普通概率的性质**

- $P(A \mid B) \ge 0$（假设 $P(B) > 0$）
- $P(\Omega \mid B) = $（讲义留白）
- $P(B \mid B) = $（讲义留白）
- 若 $A \cap C = \varnothing$，则 $P(A \cup C \mid B) = P(A \mid B) + P(C \mid B)$

---

## 第 6 页

**基于条件概率的模型**

- 事件 $A$：飞机正在上方飞行
- 事件 $B$：雷达屏幕上出现信号
- $P(A \cap B) = $（讲义留白）
- $P(B) = $（讲义留白）
- $P(A \mid B) = $（讲义留白）

（概率树：$P(A) = 0.05$，$P(A^c) = 0.95$；$P(B \mid A) = 0.99$、$P(B^c \mid A) = 0.01$、$P(B \mid A^c) = 0.10$、$P(B^c \mid A^c) = 0.90$，分别通向 $A \cap B$、$A \cap B^c$、$A^c \cap B$、$A^c \cap B^c$）

---

## 第 7 页

**乘法法则**

- $P(A \mid B) = P(A \cap B)/P(B)$
- $P(A \cap B) = P(B)P(A \mid B)$
- $= P(A)P(B \mid A)$
- $P(A^c \cap B \cap C^c) = $（讲义留白）

（概率树：A / A^c 分支 → B / B^c 分支，叶节点含 $A \cap B \cap C$、$A \cap B^c$、$A^c \cap B$、$A^c \cap B \cap C^c$、$A^c \cap B^c$）

---

## 第 8 页

**全概率定理**

- 将样本空间划分为 $A_1, A_2, A_3$
- 已知每个 $i$ 的 $P(A_i)$
- 已知每个 $i$ 的 $P(B \mid A_i)$
- $P(B) = $（讲义留白）
- $P(B) = \sum_i P(A_i)P(B \mid A_i)$

（图示：Ω 被划分为 $A_1, A_2, A_3$，$B$ 与各 $A_i$ 相交形成 $A_1 \cap B$、$A_2 \cap B$、$A_3 \cap B$；下方为对应的分支图）

---

## 第 9 页

**贝叶斯法则**

- 将样本空间划分为 $A_1, A_2, A_3$
- 已知每个 $i$ 的 $P(A_i)$ —— 初始"信念"
- 已知每个 $i$ 的 $P(B \mid A_i)$
- 在 $B$ 已发生的条件下修正的"信念"：
- $P(A_i \mid B) = $（讲义留白）
- $P(A_i \mid B) = \dfrac{P(A_i)P(B \mid A_i)}{\sum_j P(A_j)P(B \mid A_j)}$

---

## 第 10 页

**贝叶斯法则与推断**

- Thomas Bayes，长老会牧师（约 1701–1761）
- "贝叶斯定理"，死后发表
- 纳入新证据的系统性方法
- **贝叶斯推断**
  - 对观测事件 $B$ 的可能原因 $A_i$ 的初始信念 $P(A_i)$
  - 每个 $A_i$ 下的世界模型：$P(B \mid A_i)$
  - （图示：$A_i \xrightarrow{\text{模型 } P(B \mid A_i)} B$）
  - 得出结论（关于原因）
  - （图示：$B \xrightarrow{\text{推断 } P(A_i \mid B)} A_i$）

---

## 第 11 页

（MIT OpenCourseWare 版权声明页：本资源为 John Tsitsiklis 与 Patrick Jaillet 提供的个人学习资源，见 https://ocw.mit.edu/terms）
