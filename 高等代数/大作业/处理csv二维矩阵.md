## 代码逐行详解

---

### 第一步：导入库

```python
import pandas as pd   # 数据处理
import numpy as np    # 矩阵运算
```

---

### 第二步：读取边列表

```python
url = "https://snap.stanford.edu/data/email-Eu-core.txt.gz"
df = pd.read_csv(url, sep=' ', header=None, names=['from', 'to'])
```

**文件内容是这样的**：
```
0 1
0 2
0 3
1 2
...
```

**解读**：
- `sep=' '` → 用空格分隔
- `header=None` → 文件没有标题行
- `names=['from', 'to']` → 给两列起名字

**读取后 df 变成**：

| from | to |
|------|-----|
| 0 | 1 |
| 0 | 2 |
| 0 | 3 |
| 1 | 2 |
| ... | ... |

**含义**：节点0 → 节点1，节点0 → 节点2，...

---

### 第三步：获取所有节点

```python
nodes = sorted(set(df['from']).union(set(df['to'])))
```

**拆解**：

```python
set(df['from'])           # {0, 1, 2, 3, ...}  所有起点
set(df['to'])             # {1, 2, 3, 4, ...}  所有终点
.union(...)               # {0, 1, 2, 3, 4, ...}  合并去重
sorted(...)               # [0, 1, 2, 3, 4, ...]  排序成列表
```

**结果**：`nodes = [0, 1, 2, 3, ..., 1004]`（共1005个节点）

---

### 第四步：建立节点编号映射

```python
n = len(nodes)  # n = 1005
node_to_idx = {node: i for i, node in enumerate(nodes)}
```

**为什么需要映射？**

原始节点ID可能是 `0, 1, 2, 100, 500...`（不连续），但邻接矩阵需要连续的 `0, 1, 2, 3...` 作为索引。

**映射结果**：

```python
node_to_idx = {
    0: 0,    # 节点0 → 矩阵第0行/列
    1: 1,    # 节点1 → 矩阵第1行/列
    2: 2,
    ...
    1004: 1004
}
```

---

### 第五步：初始化邻接矩阵

```python
A = np.zeros((n, n))  # 1005 × 1005 的全零矩阵
```

**初始状态**：

```
A = [
  [0, 0, 0, 0, ...],  # 第0行
  [0, 0, 0, 0, ...],  # 第1行
  [0, 0, 0, 0, ...],  # 第2行
  ...
]
```

---

### 第六步：填充矩阵

```python
for _, row in df.iterrows():
    i = node_to_idx[row['from']]
    j = node_to_idx[row['to']]
    A[i, j] = 1
```

**逐行拆解**：

```python
for _, row in df.iterrows():     # 遍历每一行
```

第一次循环：
```python
row = {'from': 0, 'to': 1}
i = node_to_idx[0]  # i = 0
j = node_to_idx[1]  # j = 1
A[0, 1] = 1         # 第0行第1列 = 1
```

第二次循环：
```python
row = {'from': 0, 'to': 2}
i = node_to_idx[0]  # i = 0
j = node_to_idx[2]  # j = 2
A[0, 2] = 1         # 第0行第2列 = 1
```

**图解**：

```
        列:  0  1  2  3  ...
行:
  0         [0, 1, 1, 0, ...]   ← 节点0 连向 节点1,2
  1         [0, 0, 0, 0, ...]
  2         [0, 0, 0, 0, ...]
  ...
```

---

### 第七步：输出结果

```python
print(A.shape)           # (1005, 1005)
print("非零元素:", np.sum(A))  # 25571
```

**验证**：
- `A.shape` → 矩阵大小 = 节点数 × 节点数
- `np.sum(A)` → 非零元素个数 = 边数（因为有向，每条边对应矩阵中一个1）

---

## 总结流程图

```
原始文件                 读取后 df                邻接矩阵 A
                      
0 1                from  to              A[0,1] = 1
0 2       →        0     1      →        A[0,2] = 1
0 3                0     2              A[0,3] = 1
1 2                0     3              A[1,2] = 1
...                1     2              ...
                   ...

    读取数据           映射索引              填充矩阵
```

---

## 一句话总结

**遍历每条边 (from, to)，在邻接矩阵对应位置 A[from, to] = 1**