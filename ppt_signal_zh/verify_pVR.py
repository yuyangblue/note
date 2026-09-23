# -*- coding: utf-8 -*-
import subprocess, io, os, re, json
os.chdir(r"D:\29469\Documents\notes\ppt_signal_zh")
r = subprocess.run(["lark-cli", "slides", "+xml-get", "--presentation",
                    "NVAAsrqRMlxzD6d6aLPcA8KUnvc", "--slide-id", "pVR",
                    "--output", "./rb-pVR.xml", "--json"],
                   capture_output=True, text=True, encoding="utf-8")
t = io.open("rb-pVR.xml", encoding="utf-8").read()
for bid in ("bet", "beX", "bei"):
    m = re.search(r'<shape\b[^>]*\bid="%s"[^>]*>.*?</shape>' % bid, t, re.S)
    if m:
        inner = re.sub(r"<[^>]+>", "", m.group(0))
        print(bid, "::", inner[:200])
