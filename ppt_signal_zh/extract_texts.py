# -*- coding: utf-8 -*-
import io, re, os, json
import xml.etree.ElementTree as ET

os.chdir(r"D:\29469\Documents\notes\ppt_signal_zh")
tree = ET.parse("source.xml")
root = tree.getroot()
ns = "{https://www.larkoffice.com/sml/2.0}"

slides = root.findall(ns + "slide")
print("slide_count:", len(slides))

out = []
for s in slides:
    sid = s.get("id")
    texts = []
    for sh in s.iter(ns + "shape"):
        bid = sh.get("id")
        # collect paragraph texts
        parts = []
        for p in sh.iter(ns + "p"):
            t = "".join(p.itertext())
            if t.strip():
                parts.append(t.strip())
        if parts:
            texts.append({"id": bid, "text": " | ".join(parts)})
    out.append({"slide_id": sid, "texts": texts})

with io.open("page_texts.json", "w", encoding="utf-8", newline="\n") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

# Print compact summary: slide id + first 120 chars of concatenated text
for page in out:
    joined = " || ".join(t["text"] for t in page["texts"])
    print(page["slide_id"], "|", joined[:150])
