# Local run without domain — any working HTTPS tunnel

Problem: Telegram opens Mini Apps ONLY via public HTTPS with a valid cert. `http://localhost` is rejected by BotFather; self-signed `https://localhost` shows a white screen on Android/iOS.

Solution: bot polls locally (no HTTPS needed), frontend is exposed via a tunnel. ANY working tunnel is acceptable — agent picks one and documents it.

## Options

| Tool | Command → URL | Account | Notes |
|---|---|---|---|
| **cloudflared (preferred)** | `cloudflared tunnel --url http://localhost:5173` → `https://xxx.trycloudflare.com` | none | Clean HTTPS, no interstitial, works in WebView everywhere |
| ngrok | `ngrok http 5173` (or `--domain=xxx.ngrok.app 5173`) | required (authtoken) | Free without static domain shows warning page → breaks WebView; use static domain |
| localtunnel | `npx localtunnel --port 5173` → `https://xxx.loca.lt` | none | Desktop OK, mobile password page breaks WebView — desktop-only fallback |
| vite basic-ssl / mkcert | `https://localhost:5173` | — | Desktop/macOS/Web after cert exception ONLY, never mobile |

## Windows (PowerShell)

```powershell
winget install --id Cloudflare.cloudflared -e --silent
cd webapp; npm i; npm run dev -- --host --port 5173
.\scripts\start-tunnel.ps1 -Port 5173   # prints https://xxx.trycloudflare.com
curl -I https://xxx.trycloudflare.com  # must be 200
$env:BOT_TOKEN="123:AA"; $env:WEBAPP_URL="https://xxx.trycloudflare.com"
python scripts/set-menu-button.py
cd ..\bot; pip install -r requirements.txt; $env:BOT_TOKEN="123:AA"; $env:WEBAPP_URL="https://..."; python main.py
```

## Linux / macOS (bash)

```bash
# cloudflared: brew install cloudflared / apt install / binary from developers.cloudflare.com
cd webapp && npm i && npm run dev -- --host --port 5173 &
bash scripts/start-tunnel.sh 5173   # prints public URL
curl -I https://xxx.trycloudflare.com
BOT_TOKEN=123:AA WEBAPP_URL=https://xxx.trycloudflare.com python scripts/set-menu-button.py
cd ../bot && pip install -r requirements.txt && BOT_TOKEN=123:AA WEBAPP_URL=https://... python main.py
```

ngrok fallback: `ngrok config add-authtoken <TOKEN>; ngrok http --domain=<static> 5173`. localtunnel fallback: `npx localtunnel --port 5173`.

## Gotchas

- Tunnel URL CHANGES on every restart (trycloudflare). Always re-run `set-menu-button.py` + resend inline button.
- Telegram caches app pages. After new build: swipe-close app, wait 10s, reopen. Use `?v=N` during debug.
- Vite: `server.host=true`, fixed port, `base:'./'` in config or white screen on `?startapp`.
- Test-env allows HTTP/IP but is slow/buggy — prefer prod + tunnel for local dev.
- cloudflared uses outbound TLS 443 — works behind NAT, no port forwarding.

## Diagnostics

| Symptom | Cause | Fix |
|---|---|---|
| BotFather "Bot domain invalid" | http/localhost/self-signed | give tunnel https URL |
| White screen on Android, Desktop OK | self-signed / loca.lt pwd / ngrok interstitial | switch to cloudflared URL |
| `initData` empty | opened in browser, not TG | open via bot button; `mockTelegramEnv` dev-only |
| `hash mismatch` | validating Unsafe / double-decoding | validate raw `initData` as-is, exclude `hash` pre-sort |
| Old build opens | TG cache / stale URL | `?v=`, new tunnel + setChatMenuButton |
| Tunnel 502 | frontend down / wrong port | `curl http://localhost:5173` locally |
| CTA hidden by keyboard | pinned to `viewportHeight` | pin to `viewportStableHeight` + safe-area |

## WebView debugging (mandatory evidence)

Desktop Beta → Experimental → Enable webview inspecting → Inspect. Android → `chrome://inspect`. iOS → Safari Develop. Fallback `eruda.init()` dev-only, strip in prod. Agent must attach log excerpt proving the app booted (`ready()`, version, no JS errors).
