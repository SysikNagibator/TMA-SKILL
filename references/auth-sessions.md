# Sessions on top of initData

initData is per-launch proof, not a session. For multi-request flows:

- Short session: after first valid initData, issue `session_id` (httpOnly? No cookies in WebView reliably — return `{session, exp}` and send as `X-Session` header alongside `Authorization: tma`). Bind session to `user_id` + app version; TTL 24h; refresh requires fresh initData (auth_date < 1h).
- Nonces for sensitive actions (pay, book, transfer): `POST /api/nonce` → `{nonce}` single-use 5min; action must present it. Prevents replay of captured requests.
- Never accept `user_id` from body/query — always from validated initData/session.
- Logout = drop session client-side + server blacklist; initData itself can't be revoked (short TTL is the mitigation).
- Third-party services (no bot token): Ed25519 check with Telegram pubkeys (see backend-security.md), same expiry rules.
