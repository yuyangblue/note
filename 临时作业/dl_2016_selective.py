# -*- coding: utf-8 -*-
"""按学习路径，从 2016 归档仓库挑选必要文件下载（跳过手写扫描笔记）。"""
import json
import os
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

TREE = r"D:\29469\Documents\notes\临时作业\aos_2016_tree.json"
DEST = r"C:\Users\29469\Desktop\All of Statistics 统计部分\02_2016归档_作业与解答"
RAW = "https://raw.githubusercontent.com/cyber-rhythms/cmu-36-705-intermediate-statistics-fall-2016/master/"

SKIP_PREFIX = ("self-study-scanned-notes/",)
KEEP_DIRS = (
    "course-lecture-notes/",
    "assignment-questions/",
    "assignment-solutions/",
    "self-study-completed-assignments/",
    "self-study-completed-practice-exams/",
    "practice-exams/",
)
KEEP_FILES = (
    "README.md",
    "36-705-lecture-summaries.pdf",
    "cmu-36-705-intermediate-statistics-fall-2016-syllabus.pdf",
    "cmu-36-705-intermediate-statistics-fall-2016-course-page.html",
)

tree = json.load(open(TREE, encoding="utf-8"))["tree"]
paths = []
for it in tree:
    p = it["path"]
    if it["type"] != "blob" or any(p.startswith(s) for s in SKIP_PREFIX):
        continue
    if p.startswith(KEEP_DIRS) or p in KEEP_FILES:
        paths.append(p)


def get(p):
    dest = os.path.join(DEST, *p.split("/"))
    if os.path.exists(dest) and os.path.getsize(dest) > 100:
        return ("skip", p, os.path.getsize(dest))
    url = RAW + urllib.parse.quote(p)
    err = None
    for i in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            if len(data) < 50:
                raise ValueError("too small")
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as f:
                f.write(data)
            return ("ok", p, len(data))
        except Exception as e:
            err = e
            time.sleep(1 + i)
    return ("FAIL", p, str(err))


res = []
with ThreadPoolExecutor(max_workers=8) as ex:
    for f in as_completed([ex.submit(get, p) for p in paths]):
        res.append(f.result())

for status in ("ok", "skip", "FAIL"):
    group = [r for r in res if r[0] == status]
    print("%s: %d" % (status, len(group)))
    if status == "FAIL":
        for r in group:
            print("  ", r[1], r[2])
print("TOTAL_FILES_EXPECTED=%d" % len(paths))
total = sum(os.path.getsize(os.path.join(DEST, *p.split("/")))
            for p in paths if os.path.exists(os.path.join(DEST, *p.split("/"))))
print("TOTAL_BYTES=%d (%.1f MB)" % (total, total / 1048576.0))
