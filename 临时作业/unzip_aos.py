# -*- coding: utf-8 -*-
"""把课程归档 zip 解压到目标目录，并拍平最外层 <repo>-<branch>/ 目录。"""
import os
import sys
import zipfile

zip_path, destdir = sys.argv[1], sys.argv[2]
z = zipfile.ZipFile(zip_path)
names = [n for n in z.namelist() if not n.endswith("/")]
z.extractall(destdir)
z.close()
first = names[0].split("/")[0]
root = os.path.join(destdir, first)
if os.path.isdir(root) and os.path.abspath(root) != os.path.abspath(destdir):
    for entry in os.listdir(root):
        src = os.path.join(root, entry)
        dst = os.path.join(destdir, entry)
        if os.path.exists(dst):
            continue
        os.rename(src, dst)
print("extracted %d files -> %s" % (len(names), destdir))
for d, _, fs in os.walk(destdir):
    rel = os.path.relpath(d, destdir)
    if rel == ".":
        continue
    print("  %s: %d files" % (rel, len(fs)))
