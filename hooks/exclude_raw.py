"""构建钩子：定制 MkDocs 站点生成。

1. 从站点中排除所有「原始材料」目录（B站字幕、素材、jsonl 等非笔记内容）。
2. 站点按「分区 → 课程」两级组织：
   - 为每个课程目录生成 index.md 落地页（课程统计 + 快速入口）；
   - 为每个分区目录生成 index.md 落地页（课程卡片入口）。
3. 修正自动导航标题：index.md 显示为「首页」。
"""

from mkdocs.structure.files import File, file_sort_key

# 分区顺序与元数据（dict 保持插入顺序，决定分区展示顺序）
PARTITIONS = {
    "算法与数据结构": {
        "icon": "⚔️",
        "desc": "竞赛算法与数据结构：从复杂度、搜索到动态规划与图论的系统刷题路线。",
    },
    "数学": {
        "icon": "📐",
        "desc": "概率统计、离散数学与数值计算方法，公式推导全覆盖。",
    },
    "计算机与编程": {
        "icon": "🖥️",
        "desc": "计算机系统原理（程序执行、RISC-V、存储层次）与 C++ 语言学习。",
    },
    "人工智能": {
        "icon": "🤖",
        "desc": "深度学习课程笔记与前沿论文讲座翻译。",
    },
    "课程合集": {
        "icon": "🎓",
        "desc": "大一下学期各门课程的学习笔记合集。",
    },
}

# 课程 -> 图标（未匹配的课程用默认图标）
COURSE_ICONS = {
    "ICPC": "⚔️",
    "数据结构": "🧱",
    "概率论与数理统计": "🎲",
    "离散数学": "🧩",
    "计算方法与优化": "📐",
    "计算机系统导论": "🖥️",
    "C++学习": "💻",
    "深度学习": "🧠",
    "一些讲座": "🎤",
    "大一下": "🎓",
}

# 课程 -> 一句话简介（分区卡片与课程卡片复用）
COURSE_DESCS = {
    "ICPC": "数据结构与算法系统笔记：复杂度、搜索、动态规划、字符串、数学、图论七大部分，附洛谷题单与完整刷题路线。",
    "数据结构": "陈越《数据结构》课程笔记：线性结构、树、图、排序与散列查找十二讲，附 PTA 题目清单。",
    "概率论与数理统计": "随机事件、随机变量、数字特征、大数定律、数理统计、参数估计与假设检验，逐章整理含详细公式推导。",
    "离散数学": "集合、命题与谓词逻辑、关系、次序关系、函数、图论基础，经典教材章节式学习笔记。",
    "计算方法与优化": "数值计算方法系统笔记：误差分析、非线性方程求根、线性方程组、插值与拟合、数值积分、矩阵特征值与常微分方程。",
    "计算机系统导论": "程序结构与执行、RISC-V 指令系统与处理器、存储层次与链接，附带 Vivado / Verilog 硬件设计入门笔记。",
    "C++学习": "C++ 语言学习笔记：期末复习、二义性、线性群体、多对多实现与高级语言程序设计要点。",
    "深度学习": "深度学习课程笔记：线性回归、神经网络、损失函数、模型训练、梯度与初始化、正则化与模型评价。",
    "一些讲座": "讲座笔记与论文中文翻译：Functional Scaling Laws、Spend Less Fit Better 等深度学习方向前沿材料。",
    "大一下": "大一第二学期课程合集：工科数学分析、高等代数、机器学习、大数据解析与人工智能导引等。",
}


def is_raw(f) -> bool:
    """判断文件是否位于「原始材料」目录中。"""
    return "/原始材料/" in "/" + f.src_path.replace("\\", "/") + "/"


def on_files(files, config):
    """排除原始材料，并为分区与课程目录生成虚拟 index.md。"""
    # 1. 排除原始材料
    keep = [f for f in files._files if not is_raw(f)]

    # 2. 按「分区 → 课程」分组（仅统计文档页）
    by_part = {}
    for f in keep:
        if not f.is_documentation_page():
            continue
        src = f.src_path.replace("\\", "/")
        parts = src.split("/")
        if len(parts) >= 3 and parts[0] != "index.md":
            by_part.setdefault(parts[0], {}).setdefault(parts[1], []).append(f)

    # 3. 为每个课程目录生成落地页（仅当目录含笔记且无 index 时）
    for part in PARTITIONS:
        if part not in by_part:
            continue
        for course, fs in by_part[part].items():
            pages = [f for f in fs if f.is_documentation_page()]
            if not pages or any(f.src_path.endswith("/index.md") for f in pages):
                continue
            dirname = f"{part}/{course}"
            keep.append(File.generated(
                config, f"{dirname}/index.md",
                content=build_course_index(dirname, fs),
            ))

    # 4. 为每个分区生成落地页
    for part in PARTITIONS:
        if part not in by_part:
            continue
        keep.append(File.generated(
            config, f"{part}/index.md",
            content=build_partition_index(part, by_part[part]),
        ))

    files._files = keep
    return files


def build_partition_index(part: str, fs_by_course: dict) -> str:
    """生成分区落地页：课程卡片入口。"""
    meta = PARTITIONS.get(part, {"icon": "📂", "desc": ""})
    courses = list(fs_by_course.keys())

    total = 0
    for fs in fs_by_course.values():
        total += len([f for f in fs if f.is_documentation_page()])

    lines = [f"# {meta['icon']} {part}", ""]
    if meta["desc"]:
        lines.append(f"> {meta['desc']}")
        lines.append("")
    lines.append(f"本分区共收录 **{total}** 篇笔记，按课程整理如下。")
    lines.append("")
    lines.append('<div class="course-grid">')
    lines.append("")

    for course in courses:
        fs = fs_by_course[course]
        n = len([f for f in fs if f.is_documentation_page()])
        icon = COURSE_ICONS.get(course, "📄")
        desc = COURSE_DESCS.get(course, "")
        lines.append(f'<a class="course-card" href="{course}/">')
        lines.append(f'  <span class="course-icon">{icon}</span>')
        lines.append("  <span class=\"course-body\">")
        lines.append(f'    <span class="course-name">{course}</span>')
        if desc:
            lines.append(f'    <span class="course-desc">{desc}</span>')
        lines.append(f'    <span class="course-meta">{n} 篇笔记</span>')
        lines.append("  </span>")
        lines.append("</a>")
        lines.append("")

    lines.append("</div>")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("> 💡 点击左侧分区可展开课程，顶部支持全文搜索。")
    lines.append("")
    return "\n".join(lines)


def build_course_index(dirname: str, fs) -> str:
    """生成课程落地页 Markdown 内容。"""
    pages = [f for f in fs if f.is_documentation_page()]
    notes = [f for f in pages if f.name != "index.md"]
    icon = COURSE_ICONS.get(dirname.split("/")[-1], "📄")

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

    lines = [f"# {icon} {dirname.split('/')[-1]}", ""]
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
