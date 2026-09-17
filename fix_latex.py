# -*- coding: utf-8 -*-
"""修复笔记中的 LaTeX 公式渲染问题：
1. 块公式行去掉 4 空格缩进（pymdownx 只识别行首 $$）
2. 表格后的缩进文本行去掉缩进（避免被当作代码块）
3. 非代码块内的 \\\\( / \\\\) 双重转义还原为 \\( / \\)
"""
import os, re, sys

ROOTS = ["ICPC","数据结构","概率论与数理统计","离散数学","计算方法与优化",
         "计算机系统导论","C++学习","深度学习","一些讲座","大一下"]

def iter_md():
    for r in ROOTS:
        for dp, dn, fn in os.walk(r):
            if "原始材料" in dp:
                continue
            for f in fn:
                if f.endswith(".md"):
                    yield os.path.join(dp, f)

def is_fence(line):
    return line.lstrip().startswith("```") or line.lstrip().startswith("~~~")

def fix_file(path):
    with open(path, "r", encoding="utf-8") as fh:
        s = fh.read()
    lines = s.split("\n")
    out = []
    in_code = False
    c1 = c2 = c3 = c4 = 0
    for i, ln in enumerate(lines):
        if is_fence(ln):
            in_code = not in_code
        # 规则1：块公式行去缩进（行首4空格 + $$，且不在代码块内）
        if not in_code and re.match(r"^ {4}\$\$", ln):
            out.append(ln[4:])
            c1 += 1
            continue
        # 规则2：块级元素（标题/表格/分割线）之后的缩进文本去缩进（避免代码块化）
        if not in_code and re.match(r"^ {4}\S", ln):
            j = i - 1
            while j >= 0 and lines[j].strip() == "":
                j -= 1
            if j >= 0:
                up = lines[j].lstrip()
                is_list = re.match(r"^(?:[-*+]|\d+[.)])\s", up)
                is_block = up.startswith("#") or up.startswith("|") or re.match(r"^-{3,}$", up)
                if is_block and not is_list:
                    out.append(ln[4:])
                    c2 += 1
                    continue
        # 规则3：非代码块内 \\\\( -> \\( 、\\\\) -> \\)
        if not in_code and ("\\\\(" in ln or "\\\\)" in ln):
            new = ln.replace("\\\\(", "\\(").replace("\\\\)", "\\)")
            if new != ln:
                c3 += 1
            out.append(new)
            continue
        # 规则4：列表项内的单行块公式 $$...$$ -> $...$（避免 pymdownx 输出 $+span+$ 残留）
        if not in_code and re.match(r"^\$\$.+\$\$$", ln):
            prev_i = i - 1
            while prev_i >= 0 and lines[prev_i].strip() == "":
                prev_i -= 1
            next_i = i + 1
            while next_i < len(lines) and lines[next_i].strip() == "":
                next_i += 1
            prev_ind = prev_i >= 0 and lines[prev_i].startswith(" ")
            next_ind = next_i < len(lines) and lines[next_i].startswith(" ")
            if prev_ind or next_ind:
                out.append(ln[1:-1])
                c4 += 1
                continue
        out.append(ln)
    ns = "\n".join(out)
    if ns != s:
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(ns)
    return c1, c2, c3, c4

total = [0, 0, 0, 0]
changed = []
for p in iter_md():
    r = fix_file(p)
    if any(r):
        total[0] += r[0]; total[1] += r[1]; total[2] += r[2]; total[3] += r[3]
        changed.append((p, r))

print("changed files:", len(changed))
print("rules applied: indent-$$=%d, block-indent=%d, dbl-escape=%d, list-$$=%d" % tuple(total))
for p, r in changed:
    print("  %s -> %s" % (p, r))
