# -*- coding: utf-8 -*-
import io, json, glob, os
import xml.etree.ElementTree as ET

os.chdir(r"D:\29469\Documents\notes\ppt_signal_zh")
for pf in sorted(glob.glob("parts-*.json")):
    parts = json.load(io.open(pf, encoding="utf-8"))
    for p in parts:
        repl = p["replacement"]
        try:
            ET.fromstring(repl)
        except Exception as e:
            print(pf, p["block_id"], "ERR:", e)
            # show offending area
            msg = str(e)
            m = None
            import re
            m = re.search(r"line (\d+), column (\d+)", msg)
            if m:
                line, col = int(m.group(1)), int(m.group(2))
                lines = repl.split("\n")
                if line-1 < len(lines):
                    print("   ctx:", repr(lines[line-1][max(0,col-60):col+40]))
