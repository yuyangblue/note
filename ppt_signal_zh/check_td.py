# -*- coding: utf-8 -*-
import io, json, xml.etree.ElementTree as ET

parts = json.load(io.open(r"D:\29469\Documents\notes\ppt_signal_zh\parts-pVP-td.json", encoding="utf-8"))
for p in parts:
    r = p["replacement"]
    try:
        root = ET.fromstring(r)
        print("OK", p["block_id"], "root=", root.tag)
    except Exception as e:
        print("BAD", p["block_id"], str(e)[:200])
        print(r[:400])
        print("---")
