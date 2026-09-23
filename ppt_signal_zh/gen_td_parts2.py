# -*- coding: utf-8 -*-
"""Regenerate pVP td parts via XML parser (robust)."""
import io, re, json, xml.etree.ElementTree as ET

NS = "https://www.larkoffice.com/sml/2.0"
ET.register_namespace("", NS)

t = io.open(r"D:\29469\Documents\notes\ppt_signal_zh\readback.xml", encoding="utf-8").read()
m = re.search(r'<slide\b[^>]*\bid="pVP"[^>]*>.*?</slide>', t, re.S)
st = m.group(0)
slide_el = ET.fromstring(st)

TR = {
    "bwS": "编号", "bwn": "名称", "bwZ": "默认动作", "bwB": "对应事件",
    "bwq": "终止", "bwx": "用户键入 ctrl-c",
    "bwK": "终止", "bwP": "终止程序（无法覆盖或忽略）",
    "bwz": "终止", "bwQ": "段违规",
    "bwp": "终止", "bwr": "定时器信号",
    "bwW": "忽略", "bwd": "子进程停止或终止",
}

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

parts = []
for td in slide_el.iter("td"):
    tid = td.get("id")
    if tid not in TR:
        continue
    # find first text span
    done = False
    for span in td.iter("span"):
        if span.text and span.text.strip():
            span.text = TR[tid]
            done = True
            break
    if not done:
        print("NO SPAN", tid)
        continue
    x = ET.tostring(td, encoding="unicode")
    x = re.sub(r'xmlns(:\w+)?="[^"]*"\s*', "", x, count=1)
    parts.append({"action": "block_replace", "block_id": tid, "replacement": x})

with io.open(r"D:\29469\Documents\notes\ppt_signal_zh\parts-pVP-td.json", "w", encoding="utf-8", newline="\n") as f:
    json.dump(parts, f, ensure_ascii=False)
print("parts:", len(parts))
# verify well-formed
for p in parts:
    try:
        ET.fromstring(p["replacement"])
        print("OK", p["block_id"])
    except Exception as e:
        print("BAD", p["block_id"], str(e)[:120])
