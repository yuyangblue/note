import io, os, re, sys

ROOT = r"D:\29469\Documents\notes"
BASE = os.path.join(ROOT, "统计学完全教程")

# 抓 [[...]]，允许 \| 作为表格内的别名分隔
PAT = re.compile(r"\[\[([^\[\]]+?)\]\]")


def parse(inner: str):
    s = inner
    # 表格里写成 \| 的别名分隔
    if "\\|" in s:
        s = s.replace("\\|", "\x00")
        target_part, _, label = s.partition("\x00")
        return target_part.strip(), _, label.strip()
    if "|" in s:
        target_part, _, label = s.rpartition("|")
        return target_part.strip(), _, label.strip()
    return s.strip(), None, None


def split_anchor(target: str):
    # 只按第一个 # 切（标题里一般不含 #）
    if "#" in target:
        p, a = target.split("#", 1)
        return p.strip(), a.strip()
    return target, None


def headings(path):
    hs = []
    for line in io.open(path, encoding="utf-8"):
        if line.startswith("#"):
            hs.append(line.lstrip("#").strip())
    return hs


bad, total, files = [], 0, {}
for dp, dn, fn in os.walk(BASE):
    dn[:] = [d for d in dn if d != "原始材料" and not d.startswith(".")]
    for f in fn:
        if not f.endswith(".md"):
            continue
        full = os.path.join(dp, f)
        rel = os.path.relpath(full, ROOT).replace("\\", "/")
        txt = io.open(full, encoding="utf-8").read()
        for m in PAT.finditer(txt):
            target, _, label = parse(m.group(1))
            if not target and not (m.group(1).startswith("#")):
                continue
            total += 1
            path, anchor = split_anchor(target)
            if not path:  # 同页锚点
                path = rel
            if not path.endswith(".md"):
                path = path + ".md"
            full2 = os.path.join(ROOT, path.replace("/", os.sep))
            if not os.path.exists(full2):
                bad.append(("NOFILE", rel, path))
                continue
            files[path] = files.get(path, 0) + 1
            if anchor:
                hs = headings(full2)
                if anchor not in hs:
                    bad.append(("NOANCHOR", rel, path + "#" + anchor))

print("链接总数", total, " 涉及文件", len(files))
print("坏链接", len(bad))
for b in bad:
    print(" ", b[0], "|", b[1], "->", b[2], ("| 近似候选: " + str([h for h in headings(os.path.join(ROOT, b[2].split('#')[0].replace('/', os.sep))) if h[:6] == b[2].split('#')[1][:6]])) if b[0] == "NOANCHOR" else "")
