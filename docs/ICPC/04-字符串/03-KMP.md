# 03 KMP

> KMP 算法在 O(n+m) 时间内完成字符串匹配，核心是 next 数组（前缀函数）——利用已匹配的信息，避免暴力匹配中不必要的回溯。

## 目录

- [1. 暴力匹配的问题](#1-暴力匹配的问题)
- [2. next 数组（前缀函数）](#2-next-数组前缀函数)
- [3. KMP 匹配过程](#3-kmp-匹配过程)
- [4. 最小循环节](#4-最小循环节)
- [5. 常见应用](#5-常见应用)
- [洛谷题](#洛谷题)

---

## 1. 暴力匹配的问题

### 大白话引入

文本串 T = "ababcabcabab"，模式串 P = "abcabx"。

暴力做法：T 的每个位置都尝试匹配 P，不匹配就 P 整体右移一位，T 的指针回溯。最坏情况 O(n·m)。

**问题在哪？** 比如匹配到 "abcab" 后发现第6位不匹配，暴力做法会把 P 右移一位从头开始比。但我们已经知道前5位是 "abcab"——其中 "ab" 既是前缀又是后缀！所以 P 可以直接右移到 "ab" 对齐的位置，不需要从头比。

这就是 KMP 的核心：**利用已匹配部分的公共前后缀信息，跳过不可能匹配的位置。**

---

## 2. next 数组（前缀函数）

### 核心定义

**next[i]** = 模式串 P 的前 i+1 个字符（P[0..i]）中，**最长的相等真前缀和真后缀的长度**。

> 真前缀/真后缀：不包含整个字符串本身的前缀/后缀。

比如 P = "abcab"：
- next[0] = 0（单个字符没有真前后缀）
- next[1] = 0（"ab"：前缀"a"，后缀"b"，不相等）
- next[2] = 0（"abc"：无公共前后缀）
- next[3] = 1（"abca"：前缀"a"=后缀"a"，长度1）
- next[4] = 2（"abcab"：前缀"ab"=后缀"ab"，长度2）

### 思维启发：怎么算 next 数组

暴力算每个 next[i] 要 O(m²)。但可以用**递推**：

假设已经算出 next[0..i-1]，现在算 next[i]。
- 设 j = next[i-1]，表示 P[0..i-1] 的最长公共前后缀长度是 j
- 如果 P[j] == P[i]，那么 next[i] = j + 1（在原来的基础上多匹配一个字符）
- 如果 P[j] != P[i]，就回退 j = next[j-1]，继续比较，直到 j=0 还不匹配则 next[i]=0

**为什么回退到 next[j-1]？** 因为 P[0..j-1] 本身也有公共前后缀，回退到它的最长公共前后缀长度，是"下一个可能匹配的位置"。

### C++ 代码：计算 next 数组

```cpp
#include <bits/stdc++.h>
using namespace std;

// 计算 next 数组（前缀函数）
// next[i] = P[0..i] 的最长相等真前缀和真后缀的长度
vector<int> compute_next(const string& P) {
    int m = P.size();
    vector<int> nxt(m, 0);
    for (int i = 1; i < m; i++) {
        int j = nxt[i - 1];  // 前一个位置的最长公共前后缀长度
        // 不匹配就回退，直到j=0
        while (j > 0 && P[i] != P[j]) {
            j = nxt[j - 1];
        }
        // 匹配成功，长度+1
        if (P[i] == P[j]) {
            j++;
        }
        nxt[i] = j;
    }
    return nxt;
}

int main() {
    string P = "abcab";
    vector<int> nxt = compute_next(P);
    cout << "P = " << P << endl;
    cout << "next: ";
    for (int i = 0; i < (int)P.size(); i++) {
        cout << nxt[i] << " ";
    }
    cout << endl;
    // 预期: 0 0 0 1 2

    P = "ababab";
    nxt = compute_next(P);
    cout << "\nP = " << P << endl;
    cout << "next: ";
    for (int x : nxt) cout << x << " ";
    cout << endl;
    // 预期: 0 1 2 3 4 5

    P = "aaaa";
    nxt = compute_next(P);
    cout << "\nP = " << P << endl;
    cout << "next: ";
    for (int x : nxt) cout << x << " ";
    cout << endl;
    // 预期: 0 1 2 3

    return 0;
}
```

> **坑：** next 数组的下标含义容易混——`next[i]` 是 P[0..i]（长度 i+1 的前缀）的最长公共前后缀长度。回退时是 `j = next[j-1]` 不是 `next[j]`（因为 j 是长度，长度为 j 的前缀最后一个下标是 j-1）。变量名常用 `nxt` 避免和 C++ 的 `next` 冲突。

---

## 3. KMP 匹配过程

### 思维启发

有了 next 数组，匹配时：
- 用 i 遍历文本串 T，j 表示当前已匹配的模式串长度
- 如果 T[i] == P[j]，i++, j++
- 如果 j == m（模式串全部匹配），找到了一个匹配位置，记录后 j = next[j-1] 继续找下一个
- 如果 T[i] != P[j] 且 j > 0，j = next[j-1]（利用公共前后缀回退，不用从头开始）
- 如果 j == 0 还不匹配，i++

**关键：i 永远不回溯！** 这就是 KMP 比暴力快的原因。

### C++ 代码：KMP 完整匹配

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> compute_next(const string& P) {
    int m = P.size();
    vector<int> nxt(m, 0);
    for (int i = 1; i < m; i++) {
        int j = nxt[i - 1];
        while (j > 0 && P[i] != P[j]) j = nxt[j - 1];
        if (P[i] == P[j]) j++;
        nxt[i] = j;
    }
    return nxt;
}

// KMP 匹配：返回 P 在 T 中所有出现的起始位置（0-indexed）
vector<int> kmp_match(const string& T, const string& P) {
    vector<int> positions;
    int n = T.size(), m = P.size();
    if (m == 0 || m > n) return positions;

    vector<int> nxt = compute_next(P);
    int j = 0;  // 当前已匹配的模式串长度
    for (int i = 0; i < n; i++) {
        // 不匹配就回退
        while (j > 0 && T[i] != P[j]) {
            j = nxt[j - 1];
        }
        // 匹配成功
        if (T[i] == P[j]) {
            j++;
        }
        // 找到完整匹配
        if (j == m) {
            positions.push_back(i - m + 1);  // 起始位置
            j = nxt[j - 1];  // 继续找下一个匹配（允许重叠）
        }
    }
    return positions;
}

int main() {
    string T = "ababcababab";
    string P = "abab";

    vector<int> nxt = compute_next(P);
    cout << "next数组: ";
    for (int x : nxt) cout << x << " ";
    cout << endl;

    vector<int> pos = kmp_match(T, P);
    cout << "\"" << P << "\" 在 \"" << T << "\" 中出现位置: ";
    for (int p : pos) cout << p << " ";
    cout << endl;
    // T = a b a b c a b a b a b
    //     0 1 2 3 4 5 6 7 8 9 10
    // "abab" 出现在位置 0 (abab), 6 (abab), 8? 
    // 位置6: T[6..9] = b a b a? 不对
    // 让我重新数: T = a(0) b(1) a(2) b(3) c(4) a(5) b(6) a(7) b(8) a(9) b(10)
    // "abab": 位置0 (a b a b ✓), 位置5? T[5..8]=a b a b ✓, 位置7? T[7..10]=a b a b ✓
    // 所以是 0, 5, 7

    // 另一个测试
    T = "aaaaa";
    P = "aa";
    pos = kmp_match(T, P);
    cout << "\"aa\" 在 \"aaaaa\" 中出现位置: ";
    for (int p : pos) cout << p << " ";
    cout << endl;
    // 预期: 0 1 2 3（允许重叠匹配）

    return 0;
}
```

> **坑：** 找到匹配后 `j = next[j-1]` 是为了继续找重叠匹配（如 "aaaa" 中找 "aa"）。如果不需要重叠匹配，可以设 j=0。匹配位置是 `i - m + 1`（i 是文本串当前下标，m 是模式串长度）。时间复杂度 O(n+m)，因为 i 只增不减，j 每次回退但总增加量不超过 n。

---

## 4. 最小循环节

### 核心公式

如果字符串 S 长度为 n，且 n % (n - next[n-1]) == 0，那么 S 的最小循环节长度是 **n - next[n-1]**，循环次数是 n / (n - next[n-1])。

**推导：** next[n-1] 是整个串的最长公共前后缀长度。如果前缀=后缀，说明串可以由一个子串重复构成。去掉公共前后缀后剩下的部分就是最小循环节。

例子：
- S = "abcabcabc"，n=9，next[8]=6（前缀"abcabc"=后缀"abcabc"），n-next[8]=3，9%3==0，最小循环节="abc"，重复3次
- S = "ababab"，n=6，next[5]=4，n-next[5]=2，6%2==0，最小循环节="ab"
- S = "abcab"，n=5，next[4]=2，n-next[4]=3，5%3≠0，没有完整循环节

### C++ 代码

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> compute_next(const string& P) {
    int m = P.size();
    vector<int> nxt(m, 0);
    for (int i = 1; i < m; i++) {
        int j = nxt[i - 1];
        while (j > 0 && P[i] != P[j]) j = nxt[j - 1];
        if (P[i] == P[j]) j++;
        nxt[i] = j;
    }
    return nxt;
}

// 求最小循环节，返回 {循环节长度, 循环次数}，如果不能完整循环返回 {-1, 1}
pair<int, int> min_period(const string& s) {
    int n = s.size();
    vector<int> nxt = compute_next(s);
    int len = n - nxt[n - 1];  // 最小循环节长度
    if (n % len == 0) {
        return {len, n / len};
    }
    return {-1, 1};  // 不能完整循环
}

int main() {
    string tests[] = {"abcabcabc", "ababab", "aaaa", "abcab", "abababa"};
    for (const string& s : tests) {
        auto [len, cnt] = min_period(s);
        if (len != -1) {
            cout << s << ": 最小循环节=" << s.substr(0, len)
                 << ", 长度=" << len << ", 重复" << cnt << "次" << endl;
        } else {
            cout << s << ": 无完整循环节" << endl;
        }
    }
    return 0;
}
```

---

## 5. 常见应用

| 应用 | 做法 |
|------|------|
| 字符串匹配 | KMP 标准匹配，O(n+m) |
| 求每个前缀的最长公共前后缀 | next 数组本身 |
| 最小循环节 | n - next[n-1]，判断 n%len==0 |
| 字符串是否由某子串重复构成 | 最小循环节判断 |
| 求最短回文串（在前面补字符） | 反转+KMP，求 s+#+rev(s) 的 next |
| AC 自动机 | KMP 的多模式串扩展（trie + fail指针，fail类似next） |

---

## 洛谷题

| 题号 | 题目 | 难度 | 提示 |
|------|------|------|------|
| P3375 | 【模板】KMP字符串匹配 | ⭐ 入门 | 纯KMP模板：输出所有匹配位置+next数组 |
| P4391 | [BOI2009] Radio Transmission 无线传输 | ⭐ 普及- | 最小循环节：n - next[n-1] |
| P2375 | [NOI2014] 动物园 | ⭐⭐⭐ 提高+/省选 | next数组进阶：统计每个前缀不重叠的公共前后缀数量 |
| P3435 | [POI2006] OKR-Periods of Words | ⭐⭐ 普及+/提高 | 利用next数组求所有前缀的最大周期 |
| P4824 | [USACO15FEB] Censoring S | ⭐⭐ 普及+/提高 | KMP+栈：匹配到模式串就删除，删除后继续匹配 |
| P3193 | [HNOI2008] GT考试 | ⭐⭐⭐ 提高+/省选 | KMP+矩阵快速幂DP：next数组构建状态转移 |

> **本节重点**：
> - next[i] = P[0..i] 的最长相等真前缀和真后缀长度
> - 计算 next：递推，不匹配时 j = next[j-1] 回退
> - KMP匹配：i不回溯，j不匹配时回退到 next[j-1]，O(n+m)
> - 找到匹配后 j = next[j-1] 继续找重叠匹配
> - 最小循环节 = n - next[n-1]，需 n % len == 0
> - **常见坑**：next数组下标含义搞混（next[i]对应长度i+1的前缀）；回退写成next[j]而不是next[j-1]；匹配位置计算错误（i-m+1不是i-m）；最小循环节忘记判断n%len==0
