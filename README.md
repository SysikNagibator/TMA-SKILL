# TMA-SKILL

A skill for AI coding agents (Claude Code, OpenCode, Cursor): build premium, Telegram-native **Telegram Mini Apps** with zero AI slop — mandatory Refero design taste, correct WebApp API, `initData` auth, Stars / TON / groups support, and local HTTPS-tunnel run without a domain.

## Install

Clone this repo into your skills folder and rename it to `tma-skill`:

- Claude Code: `~/.claude/skills/tma-skill/`
- OpenCode: `.opencode/skills/tma-skill/` (or add path via `skills.paths`)
- Cursor: `.cursor/skills/tma-skill/`

```bash
git clone https://github.com/SysikNagibator/TMA-SKILL.git tma-skill
```

## Layout

- `SKILL.md` — entrypoint: hard rules, workflows (new app / local run / 3D)
- `references/` — 25+ guides, start at `_index.md` (design, API, backend, quality, deploy)
- `scripts/` — tunnel starters (ps1/sh), MenuButton setter, initData validator
- `templates/` — base, shop, booking, tap-game, catalog, dashboard, ton
