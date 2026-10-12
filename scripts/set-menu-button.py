"""Set MenuButton WebApp + send test inline button. ENV: BOT_TOKEN, WEBAPP_URL, TEST_CHAT_ID (optional)."""
import os, sys, json, urllib.request
TOKEN = os.environ.get("BOT_TOKEN", "")
URL = os.environ.get("WEBAPP_URL", "")
CHAT = os.environ.get("TEST_CHAT_ID", "")
if not TOKEN or not URL.startswith("https://"):
    print("Need: BOT_TOKEN=<token> WEBAPP_URL=https://xxx (public tunnel URL)"); sys.exit(1)
def api(method, payload):
    req = urllib.request.Request(f"https://api.telegram.org/bot{TOKEN}/{method}",
        data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as r:
        out = json.loads(r.read())
    print(method, "->", out.get("ok"), out.get("description", ""))
    return out
api("setChatMenuButton", {"menu_button": {"type": "web_app", "text": "Open", "web_app": {"url": URL}}})
if CHAT:
    api("sendMessage", {"chat_id": CHAT, "text": "Mini App test 👇",
        "reply_markup": {"inline_keyboard": [[{"text": "Open app", "web_app": {"url": URL}}]]}})
else:
    print("TEST_CHAT_ID unset — MenuButton updated; send yourself an inline web_app button with the same URL.")
