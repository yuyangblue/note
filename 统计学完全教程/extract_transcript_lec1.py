import fitz

doc = fitz.open(r"C:\Users\29469\Desktop\MIT18.650应用统计学\官方英文逐字稿PDF\01_Lec1_Introduction.pdf")
full = []
for i in range(doc.page_count):
    full.append(doc[i].get_text())
text = "\n".join(full)
with open(r"D:\29469\Documents\notes\统计学完全教程\原始材料\BV1hp4y1i77w\transcript_lec01.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("chars:", len(text))
# print head
print(text[:3000])
