# -*- coding: utf-8 -*-
"""Extract run-level text streams per block via element walk (no string regex)."""
import io, os, json
import xml.etree.ElementTree as ET

os.chdir(r"D:\29469\Documents\notes\ppt_signal_zh")
tree = ET.parse("source.xml")
root = tree.getroot()
ns = "{https://www.larkoffice.com/sml/2.0}"
SKIP = {"bew", "bei", "beC"}

def local(elem):
    return elem.tag.split("}")[-1]

def walk_runs(elem, out):
    """Append span/br runs from children (recursing containers like strong)."""
    for child in elem:
        tag = local(child)
        if tag == "span":
            out.append({"tag": "span", "text": "".join(child.itertext())})
        elif tag == "br":
            out.append({"tag": "br", "text": ""})
        elif tag in ("strong", "em", "u", "s", "sub", "sup"):
            walk_runs(child, out)
        else:
            # unknown container: if it has text, record as span; else recurse
            t = "".join(child.itertext())
            if t:
                out.append({"tag": "span", "text": t})
            else:
                walk_runs(child, out)

out = []
for s in root.findall(ns + "slide"):
    sid = s.get("id")
    blocks = []
    for sh in s.iter(ns + "shape"):
        bid = sh.get("id")
        if bid in SKIP:
            continue
        ps = []
        for p in sh.iter(ns + "p"):
            runs = []
            walk_runs(p, runs)
            ps.append(runs)
        if ps:
            blocks.append({"id": bid, "ps": ps})
    out.append({"slide_id": sid, "blocks": blocks})

with io.open("runs.json", "w", encoding="utf-8", newline="\n") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

for page in out:
    print("=== ", page["slide_id"])
    for b in page["blocks"]:
        lines = []
        for p in b["ps"]:
            line = "".join(x["text"] if x["tag"] == "span" else "⏎" for x in p)
            lines.append(line)
        print("  ", b["id"], "::", " / ".join(lines)[:220])
