# 04 LCA（最近公共祖先）

> LCA（Lowest Common Ancestor）：树上两个节点的**最近公共祖先**——u 和 v 往上爬，第一个相遇的节点。
> 树论工具箱里的"扳手"：不解决具体问题，给其他算法提供"快速求树上两点路径"的能力。
> 最常用实现：**倍增**（binary lifting），O(n log n) 预处理，O(log n) 回答一次查询。
> 常与树上差分、树形 DP、Kruskal 重构树搭配。

## 目录
- [大白话引入](#大白话引入)
- [思维启发 & 思考流程](#思维启发--思考流程)
- [核心讲解](#核心讲解)
- [洛谷题](#洛谷题)

---

## 大白话引入

翻开家族族谱：问"张三和李四最近的共同祖先是谁"？两个人的爸爸、爷爷、太爷爷……往上数，**第一个重合的祖先**就是答案。

放到树上：树根是老祖宗，每个节点往上走只有一条路（到根）。给两个节点 u、v，**它们向上走的路径第一次交汇的那个点**，就是 LCA。

为什么需要它？很多树上问题都要"拆路径"：u 到 v 的唯一简单路径 = u 往上走到 LCA + LCA 往下走到 v。算路径长度、路径上的点权和、路径是否相交……全都先要 LCA。

> 类比：LCA 就像树形结构里的"公共接口"——两个子树的唯一连接点。树形 DP 里子树通过它合并，路径查询里路径通过它拆成两段。

---

## 思维启发 & 思考流程

**先想暴力**：两个节点同时往上爬，怎么知道在哪相遇？

1. 先让**深度深的那个往上跳**，跳到和浅的同一深度（不然一个在 5 楼一个在 1 楼，没法一起爬）；
2. 两个**一起往上跳**，第一次跳到同一个点，就是 LCA。

这个思路完全正确，问题只有一个：**一次跳一步太慢**。树深 n=5×10⁵，查询 q=5×10⁵，最坏 O(nq) 直接爆炸。

**怎么加速？——二进制拆分（倍增）**。

回想"跳台阶"：从第 100 层跳到第 0 层，一次跳 1 层要 100 步；但如果我有"跳 1、2、4、8、16、32、64 层"的跳法，把 100 拆成二进制 `100 = 64+32+4`，**3 步搞定**。

树上同理：预处理 `up[u][k]` = 从 u 往上跳 **2^k 步**到达的节点。任何步数都能用若干个 2^k 拼出来（二进制拆分），所以从 u 跳到任意祖先最多 log n 步。

**核心预处理公式**（关键中的关键）：

```
up[u][0] = u 的爸爸
up[u][k] = up[ up[u][k-1] ][k-1]    // 跳 2^k 步 = 先跳 2^(k-1) 步，再跳 2^(k-1) 步
```

这个递推用一次 DFS 就能填完：先知道爸爸（up[u][0]），然后 k 从小到大递推。

---

## 核心讲解

### 状态与预处理

- `depth[u]` = u 的深度（根的深度为 0）
- `up[u][k]` = u 往上跳 2^k 步的祖先；跳过头（超过根）记 0（0 是哨兵，表示"不存在"）

DFS 回溯时填表：先递归孩子算 depth，再在**进入节点时**就填好 up（因为 up[u][k] 只依赖祖先，不依赖子树）。

### 查询三步走（背下来）

```
lca(u, v):
1. 深度对齐：让深的 u 往上跳 depth[u]-depth[v] 步（二进制拆分 diff）
   特判：如果跳完 u == v，说明 v 本来就是 u 的祖先，直接返回 u
2. 一起跳：k 从大到小（LOG-1 → 0），如果 up[u][k] != up[v][k] 就都跳
   —— 保证跳完不会跳过 LCA（两人还在 LCA 下面）
3. 返回 up[u][0]（此时 u、v 恰好停在 LCA 的两个孩子上，爸爸就是 LCA）
```

**第 2 步为什么从大到小 + 不相等才跳？** 这是倍增的经典 trick：从大步到小步试探，只有"跳完两人还没相遇"才跳——保证最终两人**停在 LCA 的正下方**（LCA 的两个不同孩子），再往上一步就是 LCA。如果相等就跳，会直接跳过 LCA 甚至跳到根。

### 手算例子

链形树 `1-2-3-4-5`（1 是根，depth: 1=0, 2=1, 3=2, 4=3, 5=4）：

查询 `lca(4, 5)`：
1. depth[5]=4 > depth[4]=3，swap 让 u=5, v=4；diff=1 → u 跳 1 步到 4；u==v → 返回 4 ✓

查询 `lca(3, 5)`：
1. diff=2 → u=5 跳 2 步（二进制 10，k=1）→ 3；u==v → 返回 3 ✓

查询 `lca(2, 5)`：
1. diff=3 → u=5 跳 3 步（二进制 11：k=0 跳 1 步到 4，k=1 跳 2 步到 2）→ 2；u==v → 返回 2 ✓

### 完整代码：P3379 【模板】最近公共祖先（LCA）

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 500005;
const int LOG = 20;            // 2^19 = 524288 > 5e5，LOG 取 20 够用
vector<int> g[MAXN];           // 无向树
int depth[MAXN];
int up[MAXN][LOG];             // up[u][k] = u 往上跳 2^k 步到达的节点（0 = 越界哨兵）
int n, m, s;                   // s = 指定的根

void dfs(int u, int fa) {
    up[u][0] = fa;                                   // 跳 1 步 = 爸爸
    for (int k = 1; k < LOG; k++)                    // 跳 2^k = 先跳 2^(k-1) 再跳 2^(k-1)
        up[u][k] = up[up[u][k - 1]][k - 1];          // 注意：up[0][*] = 0，跳过头自动归 0
    for (int v : g[u]) {
        if (v == fa) continue;
        depth[v] = depth[u] + 1;
        dfs(v, u);
    }
}

int lca(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);             // 保证 u 更深
    // 第 1 步：u 跳到和 v 同一深度（diff 二进制拆分）
    int diff = depth[u] - depth[v];
    for (int k = 0; k < LOG; k++)
        if (diff >> k & 1) u = up[u][k];             // diff 的第 k 位是 1，就跳 2^k 步
    if (u == v) return u;                            // v 本来就是 u 的祖先
    // 第 2 步：一起跳，跳到 LCA 正下方（不相等才跳）
    for (int k = LOG - 1; k >= 0; k--)
        if (up[u][k] != up[v][k]) {                  // 跳完没相遇 → 安全，跳
            u = up[u][k];
            v = up[v][k];
        }
    return up[u][0];                                 // 再往上一步就是 LCA
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m >> s;
    for (int i = 1; i < n; i++) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    dfs(s, 0);                                       // 从指定根开始预处理
    while (m--) {
        int u, v;
        cin >> u >> v;
        cout << lca(u, v) << '\n';
    }
    return 0;
}
```

**坑**：
- `up[u][k] = up[up[u][k-1]][k-1]`：当 `up[u][k-1] = 0`（跳过头）时，`up[0][k-1] = 0`——**up[0] 整行必须是 0**，全局数组默认就是，别乱初始化
- 第 2 步必须**从大到小**枚举 k；从小到大会把小步跳完再跳大步，逻辑乱掉
- 深度对齐后要特判 `u == v`（一个点是另一个的祖先时），否则第 2 步会把祖先跳飞
- LOG 要取够：2^LOG > n，n=5×10⁵ 时 LOG=20

**复杂度分析**：预处理 O(n log n)，每次查询 O(log n)。n=q=5×10⁵ 时约 10⁷ 次操作，轻松过。

---

## 洛谷题

| 题号 | 题目 | 难度 | 提示 |
|------|------|------|------|
| P3379 | 【模板】最近公共祖先（LCA） | ⭐ 普及+/提高 | 倍增模板，背下来 |
| P3258 | [JLOI2014] 松鼠的新家 | ⭐ 普及+/提高 | LCA + 点差分 + 端点修正（起点终点重复算） |
| P3128 | [USACO15DEC] Max Flow | ⭐ 提高+ | LCA + 点差分模板：路径覆盖计数 |
| P3398 | 仓鼠找 sugar | ⭐ 普及+/提高 | 判断两路径是否相交：LCA 深度比较结论 |

---

### Tarjan 离线算法

**核心思想**：DFS 回溯时用并查集合并子树，离线处理所有查询。

**步骤**：
1. 把所有询问存到每个节点的邻接表（离线）
2. DFS 遍历树，标记已访问节点
3. 子树回溯时，用并查集把子树合并到父节点
4. 处理当前节点的询问：如果另一个点已访问，LCA = `find(另一个点)`

**复杂度**：均摊 O(1) 每次查询（并查集近似常数），但必须离线。

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 500005;
vector<int> g[MAXN];
vector<pair<int, int>> queries[MAXN];  // queries[u] = {(v, query_id)}
int ans[MAXN];
bool vis[MAXN];
int fa[MAXN];  // 并查集

int find(int x) {
    return fa[x] == x ? x : fa[x] = find(fa[x]);
}

void tarjan_lca(int u, int parent) {
    fa[u] = u;  // 初始化并查集
    
    for (int v : g[u]) {
        if (v == parent) continue;
        tarjan_lca(v, u);
        fa[v] = u;  // 子树回溯，合并到父节点
    }
    
    vis[u] = true;
    
    // 处理当前节点的所有询问
    for (auto& [v, id] : queries[u]) {
        if (vis[v]) {
            ans[id] = find(v);  // 另一个点已访问，LCA = find(v)
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int n, m, root;
    cin >> n >> m >> root;
    
    for (int i = 1; i < n; i++) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    
    for (int i = 1; i <= m; i++) {
        int u, v;
        cin >> u >> v;
        queries[u].push_back({v, i});
        queries[v].push_back({u, i});
    }
    
    tarjan_lca(root, 0);
    
    for (int i = 1; i <= m; i++) {
        cout << ans[i] << '\n';
    }
    
    return 0;
}
```

**适用场景**：所有询问已知（离线），且需要极快查询速度。

---

### 树剖（HLD）求 LCA

**核心思想**：重链剖分，每次跳过整条重链，O(log n) 查询。

**关键定义**：
- **重儿子**：子树大小最大的儿子
- **重链**：重儿子连成的链
- **链顶**：重链深度最浅的节点

**查询逻辑**：
1. 比较两点链顶深度，深的跳到链顶的父节点
2. 重复直到两点在同一条重链
3. 深度较小的点就是 LCA

**复杂度**：预处理 O(n)（两次 DFS），查询 O(log n)（常数比倍增小）。

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 500005;
vector<int> g[MAXN];
int parent_node[MAXN], depth[MAXN], sz[MAXN], heavy[MAXN];
int top[MAXN];  // 链顶

// 第一次 DFS：求父节点、深度、子树大小、重儿子
void dfs1(int u, int p, int d) {
    parent_node[u] = p;
    depth[u] = d;
    sz[u] = 1;
    heavy[u] = 0;
    int max_sz = 0;
    
    for (int v : g[u]) {
        if (v == p) continue;
        dfs1(v, u, d + 1);
        sz[u] += sz[v];
        if (sz[v] > max_sz) {
            max_sz = sz[v];
            heavy[u] = v;
        }
    }
}

// 第二次 DFS：求链顶
void dfs2(int u, int t) {
    top[u] = t;
    if (heavy[u]) {
        dfs2(heavy[u], t);  // 重儿子继承链顶
    }
    for (int v : g[u]) {
        if (v == parent_node[u] || v == heavy[u]) continue;
        dfs2(v, v);  // 轻儿子是新链顶
    }
}

int lca(int u, int v) {
    while (top[u] != top[v]) {
        // 链顶深的往上跳
        if (depth[top[u]] < depth[top[v]]) {
            v = parent_node[top[v]];
        } else {
            u = parent_node[top[u]];
        }
    }
    // 同一条重链，深度小的就是 LCA
    return depth[u] < depth[v] ? u : v;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int n, m, root;
    cin >> n >> m >> root;
    
    for (int i = 1; i < n; i++) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    
    dfs1(root, 0, 0);
    dfs2(root, root);
    
    while (m--) {
        int u, v;
        cin >> u >> v;
        cout << lca(u, v) << '\n';
    }
    
    return 0;
}
```

**为什么 O(log n)**：每跳一条重链，子树大小至少减半（最坏情况），所以最多跳 log n 次。

**对比**：
| 算法 | 预处理 | 查询 | 特点 |
|------|--------|------|------|
| 倍增 | O(n log n) | O(log n) | 在线，码量小 |
| Tarjan | O(n) | 均摊 O(1) | 离线，最快 |
| 树剖 | O(n) | O(log n) | 在线，常数小，支持修改 |

---

### 应用：树上距离查询

**公式**：`dist(u, v) = depth[u] + depth[v] - 2 * depth[lca(u, v)]`

**推导**：u 到 v 的路径 = u 到 LCA + LCA 到 v，用容斥思想。

```cpp
// 树上距离查询示意（需要配合上面的 LCA 模板使用）
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 500005;
int depth[MAXN];

// lca 函数占位定义（实际使用时用上面的倍增/Tarjan/树剖实现替换）
int lca(int u, int v) { return 0; }

// 树上距离查询
int dist(int u, int v) {
    return depth[u] + depth[v] - 2 * depth[lca(u, v)];
}

int main() { return 0; }  // 示意块不运行
```

**例题**：P1099 查询树上两点距离，直接套公式。

---

### 应用：树上差分（路径覆盖计数）

**问题**：给 u-v 路径上所有点/边 +1，最后问每个点/边被加了几次。

#### 点差分

**操作**：
```
diff[u] += 1
diff[v] += 1
diff[lca] -= 1
diff[parent[lca]] -= 1  // 防止 LCA 被多算
```

**推导**：
- 对 u 加 1：u 到根的路径上所有点 +1
- 对 v 加 1：v 到根的路径上所有点 +1
- 此时 u-v 路径上的点被加了 2 次，LCA 及以上被加了 2 次
- 对 lca 减 1：LCA 到根的路径上所有点 -1
- 此时 u-v 路径上的点被加了 1 次，但 LCA 及以上仍被加了 1 次
- 对 parent[lca] 减 1：parent[lca] 到根的路径上所有点 -1
- 最终只有 u-v 路径上的点被加了 1 次 ✓

**还原**：从叶子向根累加 `cnt[u] = diff[u] + Σ cnt[child]`

#### 边差分

**操作**（边权记在深度深的端点）：
```
diff[u] += 1
diff[v] += 1
diff[lca] -= 2  // 不用管 parent[lca]
```

**推导**：
- 边权记在深度深的端点：节点 u 的 diff 值代表 u 到 parent[u] 这条边的权值
- 对 u 加 1：u 到根的路径上所有边 +1
- 对 v 加 1：v 到根的路径上所有边 +1
- 此时 u-v 路径上的边被加了 2 次，LCA 及以上的边被加了 2 次
- 对 lca 减 2：LCA 到根的路径上所有边 -2
- 最终只有 u-v 路径上的边被加了 1 次 ✓
- 根节点没有父边，所以不用处理 parent[lca]

**还原**：同样从叶子向根累加

#### 代码实现

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;
vector<int> g[MAXN];
int diff[MAXN], cnt[MAXN];
int parent_node[MAXN], depth[MAXN];

void dfs_sum(int u, int p) {
    parent_node[u] = p;
    for (int v : g[u]) {
        if (v == p) continue;
        depth[v] = depth[u] + 1;
        dfs_sum(v, u);
        diff[u] += diff[v];  // 孩子的覆盖数累加到 u
    }
    cnt[u] = diff[u];
}

// 给 u-v 路径上所有点 +1
void add_path_point(int u, int v, int lca) {
    diff[u]++;
    diff[v]++;
    diff[lca]--;
    if (parent_node[lca]) {
        diff[parent_node[lca]]--;
    }
}

// 给 u-v 路径上所有边 +1
void add_path_edge(int u, int v, int lca) {
    diff[u]++;
    diff[v]++;
    diff[lca] -= 2;
}

int main() {
    // 读入树，预处理 LCA
    // 对每条路径调用 add_path_point 或 add_path_edge
    // dfs_sum 还原
    // 输出 cnt 数组
    return 0;
}
```

#### 例题

**P3128 [USACO15DEC] Max Flow** —— 给 K 条路径上所有点 +1，求最大覆盖次数。

**P3258 [JLOI2014] 松鼠的新家** —— 松鼠从 A1 走到 A2，再走到 A3...最后到 An。每到一个房间吃一块糖，问每个房间需要准备多少糖。
- 对每条路径 Ai 到 Ai+1 做点差分
- 但 Ai+1 这个点被算了两次（上一条路径的终点 + 下一条路径的起点），实际只吃一次
- 所以对 A2, A3, ..., An-1 这些中间点 diff 减 1（An 是终点不用减）

**P2680 [NOIP2015] 运输计划** —— 给定 M 条运输路径，可以把一条边的权值改为 0，求最小化最大路径长度。
- 二分答案 mid
- 把所有长度 > mid 的路径找出来，用边差分统计每条边被多少条超长路径覆盖
- 如果存在一条边被所有超长路径覆盖，且减去这条边后最大路径 ≤ mid，则可行
- 复杂度 O((N+M) log N)

---

> 下一篇（规划）：**05-树链剖分** —— LCA 的加强版，支持路径上带修改的查询（线段树 + 剖分序）
