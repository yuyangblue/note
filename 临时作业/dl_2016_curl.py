# -*- coding: utf-8 -*-
"""用 curl 通道并发补齐 2016 归档中缺失的文件。"""
import json
import os
import subprocess
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

TREE = r"D:\29469\Documents\notes\临时作业\aos_2016_tree.json"
DEST = r"C:\Users\29469\Desktop\All of Statistics 统计部分\02_2016归档_作业与解答"
RAW = "https://raw.githubusercontent.com/cyber-rhythms/cmu-36-705-intermediate-statistics-fall-2016/master/"

SKIP_PREFIX = ("self-study-scanned-notes/",)
KEEP_DIRS = (
    "course-lecture-notes/", "assignment-questions/", "assignment-solutions/",
    "self-study-completed-assignments/", "self-study-completed-practice-exams/",
    "practice-exams/",
)
KEEP_FILES = (
    "README.md", "36-705-lecture-summaries.pdf",
    "cmu-36-705-intermediate-statistics-fall-2016-syllabus.pdf",
    "cmu-36-705-intermediate-statistics-fall-2016-course-page.html",
)

tree = json.load(open(TREE, encoding="utf-8"))["tree"]
paths = [it["path"] for it in tree
         if it["type"] == "blob"
         and not any(it["path"].startswith(s) for s in SKIP_PREFIX)
         and (it["path"].startswith(KEEP_DIRS) or it["path"] in KEEP_FILES)]


def get(p):
    dest = os.path.join(DEST, *p.split("/"))
    if os.path.exists(dest) and os.path.getsize(dest) > 100:
        return ("skip", p)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    url = RAW + urllib.parse.quote(p)
    r = subprocess.run(
        ["curl", "-sL", "--retry", "2", "--max-time", "90", "-o", dest, url],
        capture_output=True, text=True)
    if r.returncode == 0 and os.path.exists(dest) and os.path.getsize(dest) > 100:
        return ("ok", p)
    return ("FAIL", p + " :: " + r.stderr.strip()[:120])


res = []
with ThreadPoolExecutor(max_workers=6) as ex:
    for f in as_completed([ex.submit(get, p) for p in paths]):
        res.append(f.result())

for s in ("ok", "skip", "FAIL"):
    g = [r for r in res if r[0] == s]
    print("%s: %d" % (s, len(g)))
    if s == "FAIL":
        for r in g:
            print("  ", r[1])
print("EXPECTED=%d" % len(paths))
total = sum(os.path.getsize(os.path.join(DEST, *p.split("/")))
            for p in paths if os.path.exists(os.path.join(DEST, *p.split("/"))))
print("TOTAL=%.1f MB" % (total / 1048576.0))
