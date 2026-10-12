# Troubleshooting (extended diagnostics)

| Symptom | Check | Fix |
|---|---|---|
| White screen everywhere | `dist/index.html` absolute `/assets/`? JS error in logs? | `base:'./'`, fix error, rebuild |
| White only on mobile | self-signed/loca.lt/ngrok-free? | switch to cloudflared URL |
| Old build opens | Telegram cache | `?v=N`, swipe-close, wait 10s |
| `initData` empty | opened in browser | open via bot button; mock dev-only |
| `hash mismatch` | validating Unsafe / double-decode | raw string, exclude `hash` pre-sort |
| BottomButton invisible | `is_visible` never set / hidden route | setParams per screen |
| BackButton dead | no `backButtonClicked` handler | wire router, check unmount off() |
| Keyboard covers CTA | pinned to `viewportHeight` | pin to `viewportStableHeight` + safe-area |
| Tunnel 502 | frontend down / wrong port | `curl localhost:PORT`, `start-tunnel` port match |
| Bot silent | wrong token / polling conflict (2 instances) | one instance, check `getMe` |
| Stars invoice fails | currency not XTR / wrong bot | backend-created link, user gesture tap |
| TON proof fails | manifest URL ≠ app URL | update manifest with tunnel URL |

Always: version log line on splash (`app v, tg v, platform`) — halves debugging time.
