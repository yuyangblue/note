import os, sys, json, time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = r"C:\Users\29469\.config\playwright-bilibili"
OUT_DIR = r"D:\29469\Documents\notes\.workbuddy\tmp_bili\ai_subtitles"
os.makedirs(OUT_DIR, exist_ok=True)

TARGETS = [
    ("BV1vgMw6XEJ3", 39651314597, "字符串"),
    ("BV1TcMH6hE8i", 39794771553, "KMP-next数组求解"),
    ("BV1wWNu6jESN", 39882916500, "KMP算法原理"),
]

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(USER_DATA_DIR, headless=True)
    page = ctx.new_page()
    page.goto("https://www.bilibili.com/", wait_until="domcontentloaded", timeout=60000)
    time.sleep(2)
    nav = page.evaluate("""
        fetch("https://api.bilibili.com/x/web-interface/nav", {credentials:"include"}).then(r => r.json())
    """)
    print("isLogin=", nav.get("data", {}).get("isLogin"), "uname=", nav.get("data", {}).get("uname"))
    if not nav.get("data", {}).get("isLogin"):
        ctx.close()
        sys.exit("NOT_LOGGED_IN")

    for bvid, cid, tag in TARGETS:
        player = page.evaluate(f"""
            fetch("https://api.bilibili.com/x/player/wbi/v2?bvid={bvid}&cid={cid}", {{credentials:"include"}}).then(r => r.json())
        """)
        subs = player.get("data", {}).get("subtitle", {}).get("subtitles", [])
        info = [{"lan": s.get("lan"), "ai_status": s.get("ai_status"), "url": s.get("subtitle_url")} for s in subs]
        print(f"--- {bvid} {tag}: {len(subs)} subs", json.dumps(info, ensure_ascii=False)[:400])
        if not subs:
            continue
        sub_url = "https:" + subs[0]["subtitle_url"]
        txt = page.evaluate(f"fetch('{sub_url}').then(r => r.text())")
        fname = os.path.join(OUT_DIR, f"{bvid}_{cid}_{tag}.json")
        with open(fname, "w", encoding="utf-8") as f:
            f.write(txt)
        # also dump plain text
        try:
            arr = json.loads(txt)
            lines = [it.get("content", "") for it in arr.get("body", arr if isinstance(arr, list) else [])]
        except Exception as e:
            lines = [f"PARSE_ERR {e}"]
        with open(os.path.join(OUT_DIR, f"{bvid}_{tag}.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"[OK] {bvid} {tag} lines={len(lines)}")
        time.sleep(0.5)
    ctx.close()
