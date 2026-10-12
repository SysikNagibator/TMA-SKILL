# Backend + security — initData, aiogram bot

Sources: `platform/init-data`, `platform/authorizing-user`, `bots/webapps#validating-data*`.

## Golden rule

`initDataUnsafe` is just a parsed query string from the WebView — forgeable via DevTools. Trust ONLY raw `initData` AFTER server validation.

## Client: send raw on every request

```ts
import { retrieveRawInitData } from '@tma.js/sdk';
fetch('https://xxx/api/orders', { method: 'POST',
  headers: { Authorization: `tma ${retrieveRawInitData()}`, 'Content-Type': 'application/json' },
  body: JSON.stringify({ cart }) });
```
Vanilla: `window.Telegram.WebApp.initData` (empty outside TG — handle it).

## Server: HMAC validation (required code)

1. Parse as query params, pop `hash`, keep `{k}={v}`.
2. Sort alphabetically, join `\n` → data_check_string.
3. `secret = HMAC_SHA256(key="WebAppData", msg=BOT_TOKEN)` (bytes, not hex!).
4. `calc = HMAC_SHA256(key=secret, msg=data_check_string)` hex.
5. `compare_digest(calc, hash)` + `auth_date` fresh (≤3600s–24h).

Python:

```python
import hmac, hashlib, time
from urllib.parse import parse_qsl
def validate_init_data(raw: str, bot_token: str, max_age: int = 3600) -> dict:
    pairs = dict(parse_qsl(raw, keep_blank_values=True))
    recv = pairs.pop('hash', None)
    if not recv: raise ValueError('no hash')
    s = '\n'.join(f'{k}={v}' for k, v in sorted(pairs.items()))
    secret = hmac.new(b'WebAppData', bot_token.encode(), hashlib.sha256).digest()
    calc = hmac.new(secret, s.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(calc, recv): raise ValueError('bad signature')
    if time.time() - int(pairs.get('auth_date', 0)) > max_age: raise ValueError('expired')
    return pairs
```

Node: same with `crypto`; or use `@tma.js/init-data-node` (`validate`+`parse`+`expiresIn`), Go `init-data-golang`. Local check script: `scripts/validate-initdata.py`.
Third-party (no token): Ed25519 with Telegram pubkeys prod `e7bf03a2...242d` / test `40055058...72ec`, payload `{bot_id}:WebAppData\n{sorted}`.

## aiogram 3 bot (default, polling locally)

```python
import os, asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
TOKEN = os.environ['BOT_TOKEN']
URL = os.environ['WEBAPP_URL']
bot, dp = Bot(TOKEN), Dispatcher()
@dp.message(CommandStart())
async def start(m: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Open app', web_app={'url': URL})]])
    await m.answer('Tap below 👇', reply_markup=kb)
async def main(): await dp.start_polling(bot)
if __name__ == '__main__': asyncio.run(main())
```

- Locally: long polling only. Webhook prod-only (needs HTTPS).
- Re-run `scripts/set-menu-button.py` on every tunnel URL change (MenuButton + test inline button).
- `answerWebAppQuery(query_id, result)` sends inline message as user + closes app; `query_id` lives minutes, don't cache.
- `KeyboardButton web_app` (reply keyboard) only if you need `sendData` without backend.

## Holes (hard fail if present)

- `user_id` from Unsafe into SQL → spoofing. Token in `dist/*.js` → bot hijack. Amounts/rights computed on frontend → recompute on server. `auth_date` unchecked → replay forever. CORS `*` + cookies → use `Authorization: tma` only, no cookies. Full initData logged in prod console → strip, keep `user.id/auth_date` server-side only.
