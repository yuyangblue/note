# -*- coding: utf-8 -*-
"""逐个解压官方作业解答 rar，带超时保护，避免单个坏包卡死。"""
import os
import subprocess

D = r"C:\Users\29469\Desktop\All of Statistics 统计部分\02_2016归档_作业与解答\assignment-solutions"
SEVENZ = r"C:\Program Files\7-Zip\7z.exe"

for fn in sorted(f for f in os.listdir(D) if f.lower().endswith(".rar")):
    src = os.path.join(D, fn)
    dst = os.path.join(D, os.path.splitext(fn)[0])
    os.makedirs(dst, exist_ok=True)
    if any(f for f in os.listdir(dst) if not f.endswith(".rar")):
        print("skip", fn)
        continue
    try:
        r = subprocess.run([SEVENZ, "x", "-y", "-o" + dst, src],
                           capture_output=True, text=True, timeout=25)
        got = [f for f in os.listdir(dst) if os.path.isfile(os.path.join(dst, f))]
        print("%s rc=%d -> %s" % (fn, r.returncode, got if got else r.stdout[-160:].replace("\n", " ")))
    except subprocess.TimeoutExpired:
        print("TIMEOUT", fn)
    except Exception as e:
        print("ERROR", fn, e)

n = sum(len([f for f in fs]) for _, _, fs in os.walk(D))
print("total files under assignment-solutions:", n)
