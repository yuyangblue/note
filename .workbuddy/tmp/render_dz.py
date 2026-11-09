import pymupdf, sys, os
src = r"D:/29469/Documents/notes/计算方法与优化/原始材料/CM+Opt_手写笔记电子整理版.pdf"
out = r"D:/29469/Documents/notes/.workbuddy/tmp/dz"
os.makedirs(out, exist_ok=True)
doc = pymupdf.open(src)
print("pages:", doc.page_count)
pages = [int(x) for x in sys.argv[1:]]
for p in pages:
    pg = doc[p-1]
    pix = pg.get_pixmap(dpi=150)
    fn = os.path.join(out, f"p{p:02d}.png")
    pix.save(fn)
    print(fn, pix.width, pix.height, os.path.getsize(fn))
