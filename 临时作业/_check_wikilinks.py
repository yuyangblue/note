"""端到端校验 docs 下的 [[wikilink]]：复用 hooks/exclude_raw.py 的真实函数。

1. 用假 mkdocs 模块导入钩子；
2. 造出 docs 下全部文档页 + 静态文件；
3. 对每篇文档调用 on_page_markdown，统计笔记链接 / 图片各自的解析结果。
"""
import importlib.util
import os
import posixpath
import sys
import types

ROOT = r"D:\29469\Documents\notes"
DOCS = os.path.join(ROOT, "docs")

mk = types.ModuleType("mkdocs")
mk_utils = types.ModuleType("mkdocs.utils")
mk_utils.get_relative_url = lambda path, other: posixpath.relpath(path, posixpath.dirname(other))
mk_struct = types.ModuleType("mkdocs.structure")
mk_files = types.ModuleType("mkdocs.structure.files")
mk_files.File = object
mk_files.file_sort_key = lambda f: f.src_path
sys.modules.update({
    "mkdocs": mk, "mkdocs.utils": mk_utils,
    "mkdocs.structure": mk_struct, "mkdocs.structure.files": mk_files,
})
spec = importlib.util.spec_from_file_location("excl", os.path.join(ROOT, "hooks", "exclude_raw.py"))
hook = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook)


class F:
    def __init__(self, src_path):
        self.src_path = src_path.replace("\\", "/")
        self.name = os.path.splitext(os.path.basename(src_path))[0]
        self.is_doc = src_path.endswith(".md")
        self.url = self.src_path[:-3] + ".html" if self.is_doc else self.src_path
        self.file = self  # mkdocs 的 Page 有 .file 属性，钩子据此算相对链接

    def is_documentation_page(self):
        return self.is_doc


class Files:
    def __init__(self, items):
        self._items = items

    def documentation_pages(self):
        return [f for f in self._items if f.is_doc]

    def __iter__(self):
        return iter(self._items)


items = []
for dp, dn, fn in os.walk(DOCS):
    dn[:] = [d for d in dn if d != "原始材料" and not d.startswith(".")]
    for f in fn:
        items.append(F(os.path.relpath(os.path.join(dp, f), DOCS)))
files = Files(items)
pages = files.documentation_pages()
print(f"docs 下：文档页 {len(pages)} 篇，静态文件 {len(items) - len(pages)} 个")

stat = {"link_ok": 0, "link_miss": 0, "img_ok": 0, "img_miss": 0, "self_anchor": 0}
miss_link, miss_img = [], []
converted = []
for pg in pages:
    txt = open(os.path.join(DOCS, pg.src_path), encoding="utf-8").read()
    if "[[" not in txt:
        continue
    out = hook.on_page_markdown(txt, pg, None, files)
    for m in hook.WIKILINK_RE.finditer(txt):
        inner = m.group("inner")
        bang = bool(m.group("bang"))
        if not bang and inner.startswith("#"):
            stat["self_anchor"] += 1
            continue
    for line in out.split("\n"):
        if "](<" in line and ("概率论MIT/" in line or "统计学完全教程/" in line):
            converted.append((pg.src_path, line.strip()[:170]))
    # 统计残留
    for m in hook.WIKILINK_RE.finditer(out):  # 只看转换后
        inner = m.group("inner")
        if inner.startswith("#"):
            stat["self_left"] = stat.get("self_left", 0) + 1
        elif m.group("bang"):
            stat["img_miss"] += 1
            miss_img.append((pg.src_path, inner))
        else:
            stat["link_miss"] += 1
            miss_link.append((pg.src_path, inner))

total_in = sum(
    1 for pg in pages
    for m in hook.WIKILINK_RE.finditer(open(os.path.join(DOCS, pg.src_path), encoding="utf-8").read())
    if m.group("bang") or not m.group("inner").startswith("#")
)
stat["link_ok"] = 0
print("\n转换后仍残留 [[ ]] 的：")
print(f"  笔记链接 {stat['link_miss']} 条  示例: {miss_link[:3]}")
print(f"  图片     {stat['img_miss']} 条  示例: {[m[1] for m in miss_img[:5]]}")
print(f"  同页锚点 {stat['self_anchor']} 条（由 markdown 直接渲染）")

print("\n两套笔记互链的转换样例：")
for src, line in converted[:6]:
    print(f"  [{os.path.basename(src)}] {line}")

for name in ("概率论MIT", "统计学完全教程"):
    n = [p for p in pages if p.src_path.startswith(f"数学/{name}/")]
    print(f"\ndocs/数学/{name}: {len(n)} 篇")
