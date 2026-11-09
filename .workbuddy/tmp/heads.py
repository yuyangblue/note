import pymupdf
doc = pymupdf.open(r"D:/29469/Documents/notes/计算方法与优化/原始材料/CM+Opt_手写笔记电子整理版.pdf")
for i, pg in enumerate(doc, 1):
    d = pg.get_text("dict")
    for b in d["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                if s["size"] >= 13 and s["text"].strip():
                    print(f"p{i:02d} [{s['size']:.1f}] {s['text'].strip()}")
