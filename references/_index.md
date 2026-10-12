# References index — all guides

Core (linked from SKILL.md):
- `design-system.md` — zero-slop rules, Telegram-first palette, type, grid, motion
- `refero-workflow.md` — MANDATORY Refero taste step (DESIGN.md → DESIGN-TOKENS.md)
- `telegram-api.md` — WebApp init, theme, viewport/safe-area, buttons, haptics, launch paths, debugging
- `backend-security.md` — initData HMAC validation, aiogram polling bot, holes
- `local-run.md` — any-tunnel local HTTPS run (Win/Linux/Mac), diagnostics
- `payments-stars-ton.md` — Stars + TON Connect essentials
- `groups-multiplayer.md` — shared chat context, rooms by chat_instance
- `checklist.md` — HARD blocking checklist incl. behavior rules

Frontend:
- `frontend-react.md` — React + @tma.js/sdk-react patterns
- `frontend-vanilla.md` — dependency-free vanilla TS wrapper
- `vite-config.md` — Vite setup for Mini Apps (host, base, https, build)
- `tailwind-refero.md` — Tailwind v4 theme from Refero DESIGN.md + tg vars
- `motion.md` — animation system, haptics choreography, Lottie, reduced motion
- `threejs.md` — three.js inside Telegram WebView (budget, pause, fallback)
- `media-fonts.md` — images, SVG icons, Cyrillic fonts, loading strategy
- `i18n.md` — RU/EN strings, plurals, dates, currency
- `a11y.md` — accessibility in mobile WebView

Backend:
- `aiogram-recipes.md` — FSM, keyboards, web_app buttons, answerWebAppQuery, invoices
- `grammy.md` — Node.js alternative bot
- `api-design.md` — REST contract over `Authorization: tma`
- `auth-sessions.md` — sessions/nonces on top of initData
- `database.md` — SQLite/Postgres per-user data, minimal migrations
- `webhooks-prod.md` — leaving polling: production webhooks
- `admin.md` — admin routes, feature flags, support tools

Quality & Ship:
- `testing.md` — QA matrix: devices, themes, 2-user rooms, payments sandbox
- `performance.md` — mobile perf budget, bundle, images, low-end Android
- `errors-logs.md` — error UX, server logging without leaking secrets
- `copywriting.md` — RU/EN microcopy, empty/error states that don't sound like a bot
- `design-patterns.md` — screen pattern library mapped to Refero components
- `deploy-prod.md` — domain, HTTPS, hosting, BotFather prod wiring
- `troubleshooting.md` — white screens, cache, old clients, tunnel failures
- `store-promo.md` — Main Mini App, previews, screenshots, featuring

Rule: if a guide answers the question, follow it. If two guides conflict, core guides win.
