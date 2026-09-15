import fitz

# --- textbook ch6 ---
doc = fitz.open(r"C:\Users\29469\Desktop\统计学完全教程_中文版.pdf")
print("textbook pages:", doc.page_count)
# TOC from book: ch6 starts at printed page 67; PDF offset: find by searching text
# printed page 67 -> search for chapter heading
found = None
for i in range(40, 120):
    txt = doc[i].get_text()
    if "第6章" in txt and ("模型" in txt or "统计推断" in txt):
        print("ch6 heading found at pdf page", i, "of", doc.page_count)
        found = i
        break
if found is None:
    print("ch6 heading not found in first pass")
