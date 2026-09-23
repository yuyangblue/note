# -*- coding: utf-8 -*-
"""Extract span-level text runs per slide (excluding template blocks bew/bei/beC)."""
import io, os, json
import xml.etree.ElementTree as ET

os.chdir(r"D:\29469\Documents\notes\ppt_signal_zh")
tree = ET.parse("source.xml")
root = tree.getroot()
ns = "{https://www.larkoffice.com/sml/2.0}"
SKIP = {"bew", "bei", "beC"}

out = []
for s in root.findall(ns + "slide"):
    sid = s.get("id")
    blocks = []
    for sh in s.iter(ns + "shape"):
        bid = sh.get("id")
        if bid in SKIP:
            continue
        spans = []
        for p in sh.iter(ns + "p"):
            for el in p.iter():
                if el.tag in (ns + "span", ns + "strong", ns + "br"):
                    if el.tag == ns + "br":
                        spans.append({"kind": "br"})
                    else:
                        t = "".join(el.itertext())
                        # nested strong inside span etc: keep deepest text
                        spans.append({"kind": el.tag.split("}")[1], "text": t})
        if spans:
            blocks.append({"id": bid, "spans": spans})
    out.append({"slide_id": sid, "blocks": blocks})

with io.open("spans.json", "w", encoding="utf-8", newline="\n") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

for page in out:
    print("=== ", page["slide_id"])
    for b in page["blocks"]:
        joined = "".join(x.get("text", "<br>") for x in b["spans"])
        print("  ", b["id"], "|", joined[:200])
