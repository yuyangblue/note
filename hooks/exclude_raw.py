"""构建钩子：定制 MkDocs 站点生成。

1. 从站点中排除所有「原始材料」目录（B站字幕、素材、jsonl 等非笔记内容）。
2. 为每个课程目录（docs 下的一级目录）自动生成 index.md 落地页，
   作为导航 tab 的入口，并展示课程统计与快速入口。
3. 修正自动导航标题：index.md 显示为「首页」。
"""

from mkdocs.structure.files import File, file_sort_key

# 课程目录 -> 图标（未匹配的课程用默认图标）
COURSE_ICONS = {
    "ICPC": "⚔️",
    "离散数学": "🧩",
    "概率论与数理统计": "🎲",
    "计算机系统导论": "🖥️",
    "一些讲座": "🎤",
}


def on_files(files, config):
    """排除原始材料，并为每个顶层课程目录生成虚拟 index.md。"""
    # 1. 排除原始材料
    keep = []
    for f in files._files:
        if "/原始材料/" in "/" + f.src_path.replace("\\", "/") + "/":
            continue
        keep.append(f)

    # 2. 按顶层目录分组
    top_dirs = {}
    for f in keep:
        parts = f.src_path.replace("\\", "/").split("/")
        if len(parts) >= 2 and parts[0] != "index.md":
            top_dirs.setdefault(parts[0], []).append(f)

    # 3. 为每个顶层课程目录生成 index.md（仅当目录含笔记且无 index 时）
    for dirname, fs in top_dirs.items():
        pages = [f for f in fs if f.is_documentation_page()]
        if not pages or any(f.name == "index.md" for f in pages):
            continue
        keep.append(File.generated(
            config, f"{dirname}/index.md",
            content=build_course_index(dirname, fs),
        ))

    files._files = keep
    return files


def build_course_index(dirname: str, fs) -> str:
    """生成课程落地页 Markdown 内容。"""
    pages = [f for f in fs if f.is_documentation_page()]
    notes = [f for f in pages if f.name != "index.md"]
    icon = COURSE_ICONS.get(dirname, "📄")

    # 拆成「一级子目录」与「顶层文件」两组（用于快速入口）
    subdirs, seen = [], set()
    topfiles = []
    for f in sorted(notes, key=file_sort_key):
        src = f.src_path.replace("\\", "/")
        rel_src = src[len(dirname) + 1:]
        url = f.url
        rel_url = url[len(dirname) + 1:] if url.startswith(dirname + "/") else url
        if "/" not in rel_src:
            title = f.name.replace("_", " ").replace("-", " ")
            topfiles.append((title, rel_url))
        else:
            sub = rel_src.split("/")[0]
            if sub in seen or sub == "原始材料":
                continue
            seen.add(sub)
            first = None
            for sf in sorted(
                (x for x in notes if x.src_path.replace("\\", "/").startswith(dirname + "/" + sub + "/")),
                key=file_sort_key,
            ):
                sf_url = sf.url
                first = sf_url[len(dirname) + 1:] if sf_url.startswith(dirname + "/") else sf_url
                break
            subdirs.append((sub, first))

    # 顶层文件排序：学习路线 / 清单 / 入门 类优先，其余按文件名
    priority_kw = ("学习路线", "清单", "入门", "目录", "总览")
    topfiles.sort(key=lambda t: (0 if any(k in t[0] for k in priority_kw) else 1, t[0]))
    entries = subdirs + topfiles

    lines = [f"# {icon} {dirname}", ""]
    lines.append(f"> 本课程共收录 **{len(notes)}** 篇笔记，全部内容按主题整理。")
    lines.append("")

    if entries:
        first_link = entries[0][1]
        lines.append(f'<a class="md-button md-button--primary" href="{first_link}">🚀 从第一篇开始</a>')
        lines.append("")
        lines.append("## 📑 快速入口")
        lines.append("")
        lines.append('<div class="course-list">')
        lines.append("")
        for title, rel in entries:
            lines.append(f'<p><a href="{rel}"><strong>{title}</strong></a></p>')
        lines.append("")
        lines.append("</div>")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("> 💡 左侧导航栏可按章节浏览全部笔记，顶部支持全文搜索。")
    lines.append("")
    return "\n".join(lines)


def on_nav(nav, config, files):
    for item in nav.items:
        if getattr(item, "is_page", False) and item.file.src_path == "index.md":
            item.title = "首页"
    return nav
