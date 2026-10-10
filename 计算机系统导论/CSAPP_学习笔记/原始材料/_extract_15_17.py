import zipfile, re, os

ZIP = r"C:\Users\29469\Desktop\translationCSAPP-master.zip"
OUT = r"D:\29469\Documents\notes\计算机系统导论\CSAPP_学习笔记\原始材料"

targets = {
    "Lecture 15  Exceptional Control Flow  Signals and Nonlocal Jumps.ass":
        ("Lecture15_Signals_中英精校.ass", "Lecture15_Signals_中英对照.txt"),
    "Lecture 17  Virtual Memory  Concepts.ass":
        ("Lecture17_VMConcepts_中英精校.ass", "Lecture17_VMConcepts_中英对照.txt"),
}

z = zipfile.ZipFile(ZIP)
for name, (ass_out, txt_out) in targets.items():
    src = f"translationCSAPP-master/subtitle/Chinese_English/{name}"
    data = z.read(src).decode("utf-8", errors="replace")
    with open(os.path.join(OUT, ass_out), "w", encoding="utf-8") as f:
        f.write(data)

    # Parse Dialogue lines, strip {...} tags
    cues = []
    for line in data.splitlines():
        if not line.startswith("Dialogue:"):
            continue
        # Dialogue: Marked=0,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
        parts = line.split(",", 9)
        if len(parts) < 10:
            continue
        start, end = parts[1], parts[2]
        text = parts[9]
        text = re.sub(r"\{[^}]*\}", "", text)
        text = text.replace("\\N", " ").replace("\\n", " ").strip()
        if text:
            cues.append((start, end, text))

    with open(os.path.join(OUT, txt_out), "w", encoding="utf-8") as f:
        for s, e, t in cues:
            f.write(f"[{s} -> {e}] {t}\n")
    print(f"{ass_out}: {len(cues)} cues")
