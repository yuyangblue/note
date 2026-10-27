import importlib.util, os, posixpath, sys, types, re

ROOT = r"D:\29469\Documents\notes"
DOCS = os.path.join(ROOT, "docs")

mk = types.ModuleType("mkdocs")
mu = types.ModuleType("mkdocs.utils")
mu.get_relative_url = lambda p, o: posixpath.relpath(p, posixpath.dirname(o))
mf = types.ModuleType("mkdocs.structure.files")
mf.File = object
mf.file_sort_key = lambda f: f.src_path
sys.modules.update({
    "mkdocs": mk, "mkdocs.utils": mu,
    "mkdocs.structure": types.ModuleType("mkdocs.structure"),
    "mkdocs.structure.files": mf,
})
spec = importlib.util.spec_from_file_location("hook", os.path.join(ROOT, "hooks", "exclude_raw.py"))
hook = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook)


class F:
    def __init__(self, p):
        self.src_path = p.replace("\\", "/")
        self.name = os.path.splitext(os.path.basename(p))[0]
        self.is_doc = p.endswith(".md")
        self.url = self.src_path[:-3] + ".html" if self.is_doc else self.src_path
        self.file = self

    def is_documentation_page(self):
        return self.is_doc


items = []
for dp, dn, fn in os.walk(DOCS):
    dn[:] = [d for d in dn if d != "原始材料" and not d.startswith(".")]
    for f in fn:
        items.append(F(os.path.relpath(os.path.join(dp, f), DOCS)))


class Files:
    def __init__(self, i):
        self._i = i

    def documentation_pages(self):
        return [x for x in self._i if x.is_doc]

    def __iter__(self):
        return iter(self._i)


fs = Files(items)
targets = [f for f in items if f.is_doc and "统计学完全教程/作业/" in f.src_path]
print("作业 目录下文档数：", len(targets))
leftover = 0
for pg in targets:
    txt = open(os.path.join(DOCS, pg.src_path), encoding="utf-8").read()
    out = hook.on_page_markdown(txt, pg, None, fs)
    rest = re.findall(r"\[\[[^\]]+\]\]", out)
    leftover += len(rest)
    if rest:
        print("残留", pg.src_path, rest[:3])
    # 抽查转换结果
    conv = re.findall(r"\]\(<[^>]+>\)", out)
    if pg.src_path.endswith("00-复习总览.md"):
        print("总览转换出的链接数：", len(conv))
        for c in conv[:4]:
            print("   ", c)
print("残留 [[ ]] 总数：", leftover)
