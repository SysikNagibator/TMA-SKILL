# base — runnable skeleton (copy this first)

```
bot/main.py requirements.txt .env (BOT_TOKEN WEBAPP_URL)
webapp/index.html (telegram-web-app.js?64) src/main.ts src/api.ts DESIGN-TOKENS.md
```

bot/requirements.txt: `aiogram>=3.0`
bot/.env: `BOT_TOKEN=123:AA\nWEBAPP_URL=https://xxx`

bot/main.py: /start → inline web_app button (see backend-security.md).
webapp/src/api.ts: `authFetch(path, body)` with `Authorization: tma ${retrieveRawInitData()}`.
webapp/src/main.ts: `ready()`, theme paint, BackButton router (root hides), BottomButton hidden until final screen, `viewportStableHeight` footer, skeleton on boot, `themeChanged`/`viewportChanged` listeners.
