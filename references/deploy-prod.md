# Production deploy

Frontend: stable `https://app.example.com` (Vercel/Pages/VPS+Caddy). `base:'./'`, fresh `npm run build`, smoke `vite preview` + checklist.
Backend: VPS + Caddy (auto TLS) or PaaS; env `BOT_TOKEN/WEBAPP_URL/ADMIN_IDS`; SQLite→Postgres when needed; supervisor/systemd restarts; daily DB backup.
Telegram wiring (once, documented): BotFather → MenuButton URL = prod; direct-link app (`/newapp` → Edit link = prod); Main Mini App if bot IS the app; TON manifest `url` = prod; Stars provider token live.
Cutover from tunnel: replace URL everywhere (menu, inline, manifest), bump `?v=`, swipe-close cached apps, verify via testing.md matrix on prod.
