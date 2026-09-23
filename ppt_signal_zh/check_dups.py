# -*- coding: utf-8 -*-
import io, os, json, collections
import xml.etree.ElementTree as ET

os.chdir(r"D:\29469\Documents\notes\ppt_signal_zh")
tree = ET.parse("source.xml")
root = tree.getroot()
ns = "{https://www.larkoffice.com/sml/2.0}"

# 1) duplicate ids across slides
seen = collections.defaultdict(list)
for s in root.findall(ns + "slide"):
    sid = s.get("id")
    for sh in s.iter(ns + "shape"):
        seen[sh.get("id")].append(sid)
dups = {k: v for k, v in seen.items() if len(v) > 1}
print("dup ids:", {k: v for k, v in dups.items()})
same_page = {k: v for k, v in dups.items() if len(set(v)) == 1}
print("dups within SAME page:", same_page)
