# -*- coding: utf-8 -*-
"""下载 All of Statistics 统计部分配套课程资源到桌面文件夹。"""
import os
import time
import urllib.request
import zipfile
import io
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = r"C:\Users\29469\Desktop\All of Statistics 统计部分"
MAIN = os.path.join(BASE, "01_主线_Wasserman_36-705_Fall2020")
ARCH = os.path.join(BASE, "02_2016归档_作业与解答")
DEEP = os.path.join(BASE, "03_查漏_36-705_Fall2019_Siva")
LATE = os.path.join(BASE, "04_后半本_MIPT_11讲")

W = "https://www.stat.cmu.edu/~larry/=stat705/"
S = "https://www.stat.cmu.edu/~siva/teaching/705/"

jobs = []


def add(url, dest):
    jobs.append((url, dest))


# 主线：27 份 Lecture Notes
for n in range(1, 28):
    name = {11: "Lecture11a.pdf", 12: "Lecture12a.pdf"}.get(n, "Lecture%d.pdf" % n)
    add(W + name, os.path.join(MAIN, "LectureNotes", "L%02d.pdf" % n))

# 主线：13 套 Homework + syllabus
for n in range(1, 14):
    name = "homework1.pdf" if n == 1 else "Homework%d.pdf" % n
    add(W + name, os.path.join(MAIN, "Homework", "HW%02d.pdf" % n))
add(W + "syllabus.pdf", os.path.join(MAIN, "syllabus.pdf"))

# 查漏：36-705 Fall 2019
for n in range(1, 37):
    add(S + "lec%d.pdf" % n, os.path.join(DEEP, "lec%02d.pdf" % n))
add(S + "syllabus.pdf", os.path.join(DEEP, "syllabus.pdf"))


def fetch(item):
    url, dest = item
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        return ("skip", dest, os.path.getsize(dest))
    err = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            if len(data) < 800:
                raise ValueError("response too small: %d bytes" % len(data))
            if data[:4] != b"%PDF":
                raise ValueError("not a PDF")
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as f:
                f.write(data)
            return ("ok", dest, len(data))
        except Exception as e:
            err = e
            time.sleep(1 + attempt)
    return ("FAIL", url, str(err))


def fetch_zip(url, destdir, label):
    """下载 GitHub repo 压缩包并解压到 destdir。"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=180) as r:
            data = r.read()
        z = zipfile.ZipFile(io.BytesIO(data))
        os.makedirs(destdir, exist_ok=True)
        z.extractall(destdir)
        # 把最外层 <repo>-<branch>/ 里的东西提到 destdir 下
        root = os.path.join(destdir, z.namelist()[0].split("/")[0])
        if os.path.isdir(root) and root != destdir:
            for entry in os.listdir(root):
                src = os.path.join(root, entry)
                dst = os.path.join(destdir, entry)
                if not os.path.exists(dst):
                    os.rename(src, dst)
            try:
                os.rmdir(root)
            except OSError:
                pass
        return ("ok", label, len(data))
    except Exception as e:
        return ("FAIL", label, str(e))


results = []
with ThreadPoolExecutor(max_workers=8) as ex:
    futs = {ex.submit(fetch, j): j for j in jobs}
    for f in as_completed(futs):
        results.append(f.result())

# GitHub 归档（2016 版 slides / 作业 / 解答 / 摘要）
for branch in ("master", "main"):
    r = fetch_zip(
        "https://codeload.github.com/cyber-rhythms/cmu-36-705-intermediate-statistics-fall-2016/zip/refs/heads/" + branch,
        ARCH, "2016 archive (%s)" % branch)
    if r[0] == "ok":
        results.append(r)
        break
else:
    results.append(r)

# MIPT 11 讲（书后半本速览）
for branch in ("main", "master"):
    r = fetch_zip(
        "https://codeload.github.com/vladimir-molotkov/msai-statistics/zip/refs/heads/" + branch,
        LATE, "MIPT repo (%s)" % branch)
    if r[0] == "ok":
        results.append(r)
        break
else:
    results.append(r)

ok = [r for r in results if r[0] == "ok"]
skip = [r for r in results if r[0] == "skip"]
fail = [r for r in results if r[0] == "FAIL"]
print("OK=%d SKIP=%d FAIL=%d" % (len(ok), len(skip), len(fail)))
for r in fail:
    print("FAIL:", r[1], "|", r[2])
total = 0
for root, dirs, files in os.walk(BASE):
    for fn in files:
        total += os.path.getsize(os.path.join(root, fn))
print("TOTAL_BYTES=%d (%.1f MB)" % (total, total / 1048576.0))
for d in (MAIN, ARCH, DEEP, LATE):
    n = sum(len(f) for _, _, f in os.walk(d)) if os.path.isdir(d) else 0
    print("DIR %s -> %d files" % (os.path.basename(d), n))
