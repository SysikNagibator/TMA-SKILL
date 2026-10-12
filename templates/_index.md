# Templates index — start from the closest, never blank

| Template | Use when | Key screens | Backend |
|---|---|---|---|
| `base/` | any app, runnable skeleton | splash + profile + DESIGN-TOKENS | aiogram `/start` + validated `/api/me` |
| `shop/` | store, cart, checkout | catalog, product, cart, success | products, cart totals server-side, Stars invoice |
| `booking/` | salon, cafe table, consultations | slots, form, confirm | slot lock, `closingConfirmation`, write-access on confirm |
| `tap-game/` | clicker/game | game, leaderboard, fullscreen | anti-cheat totals, `chat_instance` lobby |
| `catalog/` | menu, portfolio, real estate | list, filters, detail + shareToStory | filters server-side, share prepared message |
| `dashboard/` | finance, habits, admin | stats, charts, settings | per-user aggregates, CloudStorage prefs |
| `ton/` | wallet-gated | connect, proof, gated content | TON proof verify |

Each file below = copy-paste skeleton. After copying: run Refero step (DESIGN-TOKENS.md), recolor BottomButton/CTA to Refero accent, wire `Authorization: tma` on every call.
