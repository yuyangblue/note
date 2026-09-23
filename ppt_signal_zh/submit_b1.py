# -*- coding: utf-8 -*-
"""Submit batch parts to online slides, save responses."""
import io, os, subprocess, json

os.chdir(r"D:\29469\Documents\notes\ppt_signal_zh")
PRES = "NVAAsrqRMlxzD6d6aLPcA8KUnvc"
pages = ["pVR","pVi","pVm","pVd","pVe","pVf","pVq","pVx","pVY"]

for sid in pages:
    pf = "parts-%s.json" % sid
    if not os.path.exists(pf):
        print("SKIP", sid, "no parts file"); continue
    r = subprocess.run(
        ["lark-cli", "slides", "+replace-slide",
         "--presentation", PRES, "--slide-id", sid, "--parts", "@" + pf],
        capture_output=True, text=True, encoding="utf-8")
    payload = (r.stderr if r.stderr.strip() else r.stdout)
    out = "stdout:\n" + r.stdout + "\nstderr:\n" + r.stderr
    with io.open("resp-%s.json" % sid, "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    try:
        js = json.loads(payload)
        ok = js.get("ok")
        rev = (js.get("data") or {}).get("revision_id")
        err = (js.get("error") or {}).get("code")
        issues = (js.get("data") or {}).get("issues")
        iss_summary = ""
        if isinstance(issues, dict):
            s = issues.get("summary") or {}
            iss_summary = "issues: e=%s w=%s i=%s status=%s" % (s.get("error_count"), s.get("warning_count"), s.get("info_count"), s.get("status"))
        print(sid, "ok=", ok, "rev=", rev, "err=", err, iss_summary)
    except Exception as e:
        print(sid, "PARSE FAIL:", e, "| stdout_head:", out[:200])
