# Stars payments + TON Connect

## Telegram Stars (digital goods, subscriptions)

Flow: backend creates invoice link → frontend `openInvoice(url)` → `invoiceClosed` event → backend verifies via Bot API.

```python
# backend: createInvoiceLink(amount_stars, payload) via Bot API, return URL
# frontend:
window.Telegram.WebApp.openInvoice(invoiceUrl);
tg.onEvent('invoiceClosed', ({status}) => { /* paid|cancelled|failed|pending */ });
```

Rules:
- Prices/tiers computed server-side from `payload`, never from frontend.
- Subscriptions: Stars recurring tiers; gifts: spend app Stars balance via `sendGift`. Check Bot API changelog for exact methods (8.0+).
- Successful Stars apps with Main Mini App + media previews may be featured in the Mini App Store — upload quality previews via BotFather.
- Test with test-env + test Stars before prod.

## TON Connect (wallets)

- Manifest `webapp/public/tonconnect-manifest.json` (name, url = prod/tunnel https URL, iconUrl). Never commit private keys.
- Frontend `@tonconnect/ui` (`TonConnectUIProvider`, `useTonConnect`), backend verifies wallet proof / tx via TON API.
- Template `templates/ton/` has manifest + connect button + proof request stub.
- On local run the manifest URL must equal the tunnel URL — update it together with MenuButton.

## Common pitfalls

- `openInvoice` called outside user gesture → ignored. Call inside click handler.
- Invoice URL for another bot → fails. One bot = one Stars receiver.
- TON proof without `auth_date` freshness → replay. Apply same expiry as initData.
