# -*- coding: utf-8 -*-
import io, json, sys
import xml.etree.ElementTree as ET

parts = json.load(io.open(r"D:\29469\Documents\notes\ppt_signal_zh\parts-pVR.json", encoding="utf-8"))
for p in parts:
    bid = p["block_id"]
    repl = p["replacement"]
    print("== block", bid, "len", len(repl))
    try:
        ET.fromstring(repl)
        print("   XML OK")
    except Exception as e:
        print("   XML ERROR:", e)
    if bid == "bet":
        print(repl[:1200])
