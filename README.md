**English** | [Русский](README-ru.md)

# TMA-SKILL

![TMA-SKILL-EN](https://files.catbox.moe/gh3h4o.png)

A skill for AI coding agents — **Claude Code, OpenCode, Cursor** — that makes them build premium, Telegram-native **Telegram Mini Apps** instead of generic AI slop.

With this skill, the agent ships Mini Apps with real product taste, a correct WebApp API integration, secure `initData` auth, Stars / TON / group features — and runs the whole thing **locally on your PC without a domain** (public HTTPS tunnel + polling bot), verified inside real Telegram clients.

## Why this skill exists

Out of the box, AI agents generate Mini Apps that are instantly recognizable as slop: the same purple-blue gradient, three grey cards, a "Welcome to..." hero, emoji icons — and broken in half the places that matter (white screen on mobile, dead BackButton, unvalidated `initData`, `localhost` URLs that never open in Telegram).

TMA-SKILL fixes that with blocking rules the agent cannot skip:

- **No AI slop** — banned patterns, Telegram-first palette, Cyrillic-safe typography, mandatory UI states.
- **Mandatory design taste** — before any CSS, the agent picks ONE style from [styles.refero.design](https://styles.refero.design/) (2,000+ AI-readable design systems) and implements its tokens via `DESIGN.md`.
- **Correct Telegram API** — `ready()` first, live theme, `viewportStableHeight` pinning, safe-area, BackButton routing, BottomButton discipline, targeted haptics.
- **Secure by default** — raw `initData` validated via HMAC on every call, tokens stay in backend `.env`, never printed or committed.
- **Local run without a domain** — the agent starts the frontend, exposes it via any working HTTPS tunnel (cloudflared / ngrok / localtunnel), binds the URL to the bot, and proves it opens in Telegram.
- **No improvisation** — exactly what was asked, nothing "bonus". Unclear → the agent asks instead of guessing.
- **Self-verification** — WebView logs, dark/light checks, real-client testing. No evidence → no delivery.

## Install (15+ IDEs and agents)

```bash
git clone https://github.com/SysikNagibator/TMA-SKILL.git tma-skill
```

| Agent / IDE | Where to put it |
|---|---|
| Claude Code | `~/.claude/skills/tma-skill/` |
| OpenCode | `.opencode/skills/tma-skill/` (or `skills.paths` in `opencode.json`) |
| Cursor | `.cursor/skills/tma-skill/` (+ optional rule in `.cursor/rules/`) |
| Windsurf | `.windsurf/skills/tma-skill/` (+ line in `.windsurf/rules.md`) |
| Gemini CLI | `~/.gemini/skills/tma-skill/` |
| Codex CLI | `~/.codex/skills/tma-skill/` |
| Cline (VS Code) | `skills/tma-skill/` in workspace + `.clinerules` pointer |
| Roo Code (VS Code) | `skills/tma-skill/` in workspace + `.roorules` pointer |
| Aider | `--read tma-skill/SKILL.md` (or `read:` in `.aider.conf.yml`) |
| Continue | `docs:` entry in `~/.continue/config.yaml` |
| GitHub Copilot | `AGENTS.md` snippet in your repo (see below) |
| JetBrains AI / Junie | same `AGENTS.md` snippet |
| Zed | `AGENTS.md` in project root |
| v0 / Lovable / Bolt | paste Refero DESIGN.md + mobile/theme prompt (frontend only) |
| Any other agent | "Read `SKILL.md`, then `references/_index.md`, follow strictly" |

Step-by-step copy-paste setups live in [`install/ADAPTERS.md`](install/ADAPTERS.md) — including the `AGENTS.md` snippet for Copilot/JetBrains/Zed.

The skill activates on triggers like `telegram mini app`, `tg webapp`, `launch locally`, `no domain`, `stars payments`, `ton connect`.

## How the agent works with it

1. **New Mini App** — clarifies the core action, picks a Refero style into `webapp/DESIGN-TOKENS.md`, scaffolds from the closest template in `templates/`, implements the mandatory API minimum, passes the hard checklist.
2. **Local run on your PC** — `npm run dev` → tunnel (`scripts/start-tunnel.ps1` / `.sh`) → `scripts/set-menu-button.py` binds the HTTPS URL to MenuButton + test button → `bot/main.py` polls → verified in Desktop + mobile clients.
3. **3D / animation** — only when it serves the core action, on a strict perf budget (lazy three.js, pause in background, poster fallback, reduced-motion respected).

## What's inside

- `SKILL.md` — entrypoint: triggers, 8 hard rules, the three workflows, sources.
- `references/` — **27 guides** with an index at `_index.md`:
  - Core: design-system, refero-workflow, telegram-api, backend-security, local-run, payments-stars-ton, groups-multiplayer, checklist.
  - Frontend: React + sdk-react, vanilla TS, Vite config, Tailwind-from-Refero, motion, three.js, media/fonts, i18n, a11y.
  - Backend: aiogram recipes, grammY, API design, sessions, database, production webhooks, admin/flags.
  - Ship: testing matrix, performance budget, errors/logs, copywriting, screen patterns, prod deploy, troubleshooting, store promo.
- `scripts/` — `start-tunnel.ps1` / `start-tunnel.sh` (cloudflared → ngrok → localtunnel fallback), `set-menu-button.py` (MenuButton + test button), `validate-initdata.py` (offline signature check).
- `templates/` — runnable starters: `base` (bot + webapp skeleton), `shop`, `booking`, `tap-game`, `catalog`, `dashboard`, `ton`.

## Default stack

- Frontend: Vite + React + TS + `@tma.js/sdk` (complex apps) or vanilla TS (landing-like). Agent may switch the frontend if justified.
- Bot: Python `aiogram 3`, long polling locally, webhooks prod-only.
- Tunnel: any working one (cloudflared preferred — no account, clean HTTPS).
- Debug: Desktop Beta webview inspect, Android `chrome://inspect`, iOS Safari inspector, `eruda` dev-only.

## Sources the skill is built on

- [`core.telegram.org/bots/webapps`](https://core.telegram.org/bots/webapps) — init, ThemeParams, buttons, haptics, storage, validation.
- [`docs.telegram-mini-apps.com`](https://docs.telegram-mini-apps.com/platform/about) — init-data, auth, theming, viewport, app links, debugging.
- [Mini Apps 2.0 overview](https://telegram.org/blog/fullscreen-miniapps-and-more) — fullscreen, safe-area, homescreen, Stars.
- [styles.refero.design](https://styles.refero.design/) — mandatory design taste (DESIGN.md systems).
- Cloudflare quick tunnels, ngrok docs, community localhost practices.

## License

Free to use, fork, and remix for building Telegram Mini Apps. If you remix it into your own skill, a credit link back is appreciated but not required.
