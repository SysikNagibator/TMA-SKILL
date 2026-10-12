# Production webhooks (leaving polling)

Polling is for local dev. Prod with traffic → webhook:

1. Public HTTPS backend (VPS + Caddy/certbot, or PaaS). `POST /bot/<secret-path>` (long random path = poor-man's secret).
2. `setWebhook(url, secret_token=<random>)`; verify `X-Telegram-Bot-Api-Secret-Token` on every hit; `drop_pending_updates` on deploy if queue poisoned.
3. aiogram: `SimpleRequestHandler` + `setup_application`; grammY: `webhookCallback`. Graceful shutdown drains updates.
4. Keep a `USE_WEBHOOK` env switch — local stays polling, prod switches. Never commit the secret path/token.
5. Mini App frontend URL in prod = stable domain (not tunnel); update MenuButton + direct-link app URL in BotFather once, document it.
