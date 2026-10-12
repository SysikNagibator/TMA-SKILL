[English](README.md) | **Русский**

# TMA-SKILL

![TMA-SKILL-RU](https://files.catbox.moe/zfeu61.png)

Скилл для ИИ-кодовых агентов — **Claude Code, OpenCode, Cursor** — который заставляет их делать премиальные, Telegram-нативные **Telegram Mini Apps** вместо обычного нейрослопа.

Со скиллом агент выпускает мини-аппы с настоящим вкусом, корректной интеграцией WebApp API, безопасной `initData`-авторизацией, фичами Stars / TON / групп — и запускает всё это **локально на твоём ПК без домена** (публичный HTTPS-туннель + polling-бот), с проверкой в реальных клиентах Telegram.

## Зачем этот скилл

Без скилла ИИ-агенты генерят мини-аппы, которые за секунду узнаются как слоп: тот же фиолетово-синий градиент, три серые карточки, hero «Welcome to...», эмодзи-иконки — и сломано всё важное (белый экран на мобиле, мёртвая BackButton, непроверенный `initData`, `localhost`-ссылки, которые в Telegram не открываются).

TMA-SKILL чинит это блокирующими правилами, которые агент не может пропустить:

- **Никакого нейрослопа** — запрещённые паттерны, Telegram-палитра, типографика с кириллицей, обязательные UI-состояния.
- **Вкус обязателен** — перед любым CSS агент выбирает ОДИН стиль с [styles.refero.design](https://styles.refero.design/) (2000+ дизайн-систем для ИИ) и внедряет его токены через `DESIGN.md`.
- **Корректный Telegram API** — сначала `ready()`, живая тема, пининг к `viewportStableHeight`, safe-area, роутинг BackButton, дисциплина BottomButton, точечные хаптики.
- **Безопасность по умолчанию** — сырой `initData` валидируется через HMAC на каждый запрос, токены только в backend-`.env`, нигде не светятся и не коммитятся.
- **Локальный запуск без домена** — агент сам стартует фронт, выставляет его через рабочий HTTPS-туннель (cloudflared / ngrok / localtunnel), привязывает URL к боту и доказывает, что открывается в Telegram.
- **Без самодеятельности** — ровно то, что просили, никаких «бонусных» фич. Непонятно — агент спрашивает, а не додумывает.
- **Самопроверка** — логи WebView, тёмная/светлая темы, тесты в реальных клиентах. Нет доказательств — работа не сдана.

## Установка (15+ IDE и агентов)

```bash
git clone https://github.com/SysikNagibator/TMA-SKILL.git tma-skill
```

| Агент / IDE | Куда класть |
|---|---|
| Claude Code | `~/.claude/skills/tma-skill/` |
| OpenCode | `.opencode/skills/tma-skill/` (или `skills.paths` в `opencode.json`) |
| Cursor | `.cursor/skills/tma-skill/` (+ опциональное правило в `.cursor/rules/`) |
| Windsurf | `.windsurf/skills/tma-skill/` (+ строка в `.windsurf/rules.md`) |
| Gemini CLI | `~/.gemini/skills/tma-skill/` |
| Codex CLI | `~/.codex/skills/tma-skill/` |
| Cline (VS Code) | `skills/tma-skill/` в воркспейсе + указатель в `.clinerules` |
| Roo Code (VS Code) | `skills/tma-skill/` в воркспейсе + указатель в `.roorules` |
| Aider | `--read tma-skill/SKILL.md` (или `read:` в `.aider.conf.yml`) |
| Continue | секция `docs:` в `~/.continue/config.yaml` |
| GitHub Copilot | сниппет `AGENTS.md` в твоём репо |
| JetBrains AI / Junie | тот же сниппет `AGENTS.md` |
| Zed | `AGENTS.md` в корне проекта |
| v0 / Lovable / Bolt | вставить Refero DESIGN.md + промпт про мобилу/темы (только фронт) |
| Любой другой агент | «Прочитай `SKILL.md`, потом `references/_index.md`, следуй строго» |

Пошаговые копипаст-инструкции — в [`install/ADAPTERS.md`](install/ADAPTERS.md) (на английском).

## Как агент с ним работает

1. **Новый мини-апп** — уточняет главное действие, выбирает Refero-стиль в `webapp/DESIGN-TOKENS.md`, собирается из ближайшего шаблона в `templates/`, внедряет обязательный минимум API, проходит жёсткий чеклист.
2. **Локальный запуск на ПК** — `npm run dev` → туннель (`scripts/start-tunnel.ps1` / `.sh`) → `scripts/set-menu-button.py` привязывает HTTPS-URL к MenuButton + тестовой кнопке → `bot/main.py` в polling → проверка в Desktop + мобильных клиентах.
3. **3D / анимации** — только если усиливают главное действие, со строгим бюджетом (ленивый three.js, пауза в фоне, постер-фолбэк, уважение к reduced-motion).

## Что внутри

- `SKILL.md` — вход: триггеры, 8 жёстких правил, три процесса, источники (на английском).
- `references/` — **27 гайдов**, оглавление в `_index.md`: дизайн, API, бэкенд, качество, деплой.
- `scripts/` — стартеры туннеля, установщик MenuButton, валидатор initData.
- `templates/` — рабочие стартеры: `base`, `shop`, `booking`, `tap-game`, `catalog`, `dashboard`, `ton`.

## Стек по умолчанию

- Фронт: Vite + React + TS + `@tma.js/sdk` (сложные аппы) или ванилла-TS (лендинги).
- Бот: Python `aiogram 3`, локально long polling, вебхуки только в проде.
- Туннель: любой рабочий (cloudflared предпочтителен — без аккаунта, чистый HTTPS).
- Дебаг: Desktop Beta webview inspect, Android `chrome://inspect`, iOS Safari inspector, `eruda` только в dev.

## Лицензия

Бесплатно: используй, форкай и пересобирай для своих Telegram Mini Apps. Если сделаешь свой скилл на основе — ссылка-кредит приветствуется, но не обязательна.
