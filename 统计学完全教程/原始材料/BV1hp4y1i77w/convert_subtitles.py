import json
import os

SRC = r"D:\29469\Documents\notes\统计学完全教程\原始材料\BV1hp4y1i77w\browser_ai_subtitles"
OUT = r"D:\29469\Documents\notes\统计学完全教程\原始材料\BV1hp4y1i77w\字幕纯文本"
os.makedirs(OUT, exist_ok=True)

for fname in sorted(os.listdir(SRC)):
    if not fname.endswith(".txt"):
        continue
    with open(os.path.join(SRC, fname), encoding="utf-8") as f:
        raw = f.read()
    try:
        data = json.loads(raw)
        segs = data.get("body", []) if isinstance(data, dict) else data
    except Exception:
        segs = []
    lines = []
    for seg in segs:
        if not isinstance(seg, dict):
            continue
        content = seg.get("content", "")
        t0 = seg.get("from", 0)
        m, s = divmod(int(t0), 60)
        lines.append(f"[{m:02d}:{s:02d}] {content}")
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(fname, "->", len(lines), "segments")
