"""
用playwright获取B站AI字幕
- 使用持久化用户数据目录保存登录态
- 第一次运行需要用户扫码登录
"""
import json
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

BVID = "BV16Btc6VEpE"
OUT_DIR = Path(r"D:\29469\Documents\notes\离散数学\原始材料")
USER_DATA_DIR = r"C:\Users\29469\.config\playwright-bilibili"
METADATA_PATH = OUT_DIR / "metadata.json"

def load_parts():
    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)["data"]
    return data["pages"]

def fetch_subtitles(page, cid, bvid):
    """调用B站API获取AI字幕"""
    url = f"https://api.bilibili.com/x/player/wbi/v2?cid={cid}&bvid={bvid}"
    resp = page.request.get(url)
    data = resp.json()
    if data.get("code") != 0:
        return None, f"API error: {data.get('message')}"
    subtitles = data.get("data", {}).get("subtitle", {}).get("subtitles", [])
    if not subtitles:
        return None, "No subtitles (may need login)"
    # 取第一个字幕（通常是AI字幕）
    sub_url = subtitles[0].get("subtitle_url", "")
    if sub_url.startswith("//"):
        sub_url = "https:" + sub_url
    # 下载字幕JSON
    sub_resp = page.request.get(sub_url)
    sub_data = sub_resp.json()
    # 解析字幕内容
    body = sub_data.get("body", [])
    lines = []
    for item in body:
        content = item.get("content", "")
        lines.append(content)
    return "\n".join(lines), None

def main():
    parts = load_parts()
    print(f"Total parts: {len(parts)}")
    
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sub_dir = OUT_DIR / "ai_subtitles"
    sub_dir.mkdir(exist_ok=True)
    
    with sync_playwright() as p:
        # 启动Chromium，使用持久化用户数据目录
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,  # 非headless，方便用户登录
            viewport={"width": 1280, "height": 720},
        )
        page = context.new_page()
        
        # 先检查登录态
        page.goto("https://api.bilibili.com/x/web-interface/nav")
        nav_data = page.evaluate("JSON.parse(document.body.innerText)")
        is_login = nav_data.get("data", {}).get("isLogin", False)
        print(f"Login status: {is_login}")
        
        if not is_login:
            print("需要登录B站。正在打开B站首页，请在浏览器中点击登录按钮扫码...")
            page.goto("https://www.bilibili.com/", wait_until="domcontentloaded")
            # 截图排查
            page.screenshot(path=str(OUT_DIR / "login_page.png"))
            print(f"页面已打开: {page.url}")
            print(f"页面标题: {page.title()}")
            # 轮询检测登录态，最多等180秒
            for i in range(180):
                time.sleep(1)
                try:
                    nav_resp = page.request.get("https://api.bilibili.com/x/web-interface/nav")
                    nav_data = nav_resp.json()
                    is_login = nav_data.get("data", {}).get("isLogin", False)
                    if is_login:
                        uname = nav_data.get("data", {}).get("uname", "")
                        print(f"登录成功: {uname}")
                        break
                except Exception as e:
                    pass
                if i % 15 == 0:
                    print(f"  等待登录... ({i}s) 请在浏览器中扫码登录")
            if not is_login:
                print("登录超时，退出")
                context.close()
                return
        
        # 批量获取字幕
        success = 0
        failed = []
        for i, part in enumerate(parts):
            page_num = part["page"]
            cid = part["cid"]
            title = part["part"]
            print(f"[{i+1}/{len(parts)}] P{page_num}: {title} (cid={cid})")
            
            content, err = fetch_subtitles(page, cid, BVID)
            if err:
                print(f"  FAILED: {err}")
                failed.append((page_num, title, err))
                continue
            
            # 保存字幕
            safe_title = title.replace("/", "_").replace("\\", "_").replace(":", "_")
            out_file = sub_dir / f"p{page_num:03d}_{cid}_{safe_title}.txt"
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  OK: {len(content)} chars -> {out_file.name}")
            success += 1
            
            # 避免请求过快
            time.sleep(0.5)
        
        context.close()
    
    print(f"\n=== Done ===")
    print(f"Success: {success}/{len(parts)}")
    if failed:
        print(f"Failed: {len(failed)}")
        for pn, title, err in failed:
            print(f"  P{pn}: {title} - {err}")

if __name__ == "__main__":
    main()
