# -*- coding: utf-8 -*-
"""Scan readback.xml for remaining English text (excluding template blocks, code, filenames)."""
import io, re, json

t = io.open(r"D:\29469\Documents\notes\ppt_signal_zh\readback.xml", encoding="utf-8").read()
# split into slides
slides = re.findall(r'<slide\b[^>]*>.*?</slide>', t, re.S)
print("slide count:", len(slides))

# English words heuristic: text runs that contain 2+ consecutive ASCII letters
pat = re.compile(r"[A-Za-z]{2,}")
SKIP_IDS = {"bew", "bei", "beC"}  # template blocks
keep = []
for s in slides:
    sid = re.search(r'\bid="([^"]+)"', s).group(1)
    for sm in re.finditer(r'<span\b[^>]*>([^<]*)</span>', s):
        txt = sm.group(1)
        if pat.search(txt):
            # locate block id: nearest preceding <shape ... id=
            head = s[:sm.start()]
            bidm = re.findall(r'<shape\b[^>]*\bid="([^"]+)"', head)
            bid = bidm[-1] if bidm else "?"
            keep.append((sid, bid, txt[:60]))

# dedupe and print
seen = set()
for sid, bid, txt in keep:
    k = (sid, bid, txt)
    if k in seen:
        continue
    seen.add(k)
    print(sid, bid, repr(txt))
