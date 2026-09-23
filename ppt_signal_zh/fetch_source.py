# -*- coding: utf-8 -*-
import subprocess, io, os

os.chdir(r"D:\29469\Documents\notes\ppt_signal_zh")
r = subprocess.run(
    ["lark-cli", "slides", "+xml-get",
     "--presentation", "NVAAsrqRMlxzD6d6aLPcA8KUnvc",
     "--output", "./source.xml", "--json"],
    capture_output=True, text=True, encoding="utf-8")
with io.open("source-response.json", "w", encoding="utf-8", newline="\n") as f:
    f.write(r.stdout)
print("rc:", r.returncode)
print("stdout_head:", r.stdout[:400])
print("stderr_head:", r.stderr[:400])
print("xml_size:", os.path.getsize("source.xml") if os.path.exists("source.xml") else -1)
