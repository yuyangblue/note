# -*- coding: utf-8 -*-
import io, json, sys, re

path = r"D:\29469\Documents\notes\ppt_signal_zh\resp-pVR.json"
t = io.open(path, encoding="utf-8").read()
# find JSON block in stderr
start = t.find("{")
js = json.loads(t[start:])
err = js.get("error") or {}
msg = err.get("message")
print("type:", err.get("type"), "code:", err.get("code"))
try:
    report = json.loads(msg)
    print(json.dumps(report, ensure_ascii=False, indent=1)[:3000])
except Exception:
    print(msg[:3000])
