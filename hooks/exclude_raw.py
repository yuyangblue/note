"""构建钩子：从 MkDocs 中排除所有「原始材料」目录（B站字幕、素材、jsonl 等非笔记内容）。

在 files 阶段过滤，这样导航自动展开时也不会出现原始材料页面。
"""
import os


def on_files(files, config):
    keep = []
    for f in files._files:
        parts = f.src_path.split(os.sep)
        if "原始材料" in parts:
            continue
        keep.append(f)
    files._files = keep
    return files
