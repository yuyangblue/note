"""一次性脚本：把两套概率统计笔记同步到 docs/数学/ 下（排除原始材料与脚本）。"""
import os
import shutil

ROOT = r"D:\29469\Documents\notes"
DEST = os.path.join(ROOT, "docs", "数学")

JOBS = [
    # (源目录, 目标目录名, 要排除的目录名, 要排除的文件后缀)
    ("概率论MIT", "概率论MIT", {"原始材料"}, set()),
    ("统计学完全教程", "统计学完全教程", {"原始材料"}, {".py", ".json"}),
]

IMG_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp"}

for src_name, dst_name, skip_dirs, skip_ext in JOBS:
    src = os.path.join(ROOT, src_name)
    dst = os.path.join(DEST, dst_name)
    if os.path.exists(dst):
        shutil.rmtree(dst)
    n_file = n_skip = 0
    for dp, dn, fn in os.walk(src):
        dn[:] = [d for d in dn if not d.startswith(".")]  # 原始材料也进去，但只取图片
        rel = os.path.relpath(dp, src)
        in_raw = "原始材料" in rel.split(os.sep)
        out = dst if rel == "." else os.path.join(dst, rel)
        os.makedirs(out, exist_ok=True)
        for f in fn:
            ext = os.path.splitext(f)[1].lower()
            if ext in skip_ext or (in_raw and ext not in IMG_EXT):
                n_skip += 1
                continue
            shutil.copy2(os.path.join(dp, f), os.path.join(out, f))
            n_file += 1
    print(f"{src_name}: 复制 {n_file} 个文件, 跳过 {n_skip} 个 -> docs/数学/{dst_name}")

# 汇总 md 数量
for name in ("概率论MIT", "统计学完全教程"):
    d = os.path.join(DEST, name)
    n = sum(1 for dp, dn, fn in os.walk(d) for f in fn if f.endswith(".md"))
    print(f"  docs/数学/{name} 下共 {n} 篇 md")
