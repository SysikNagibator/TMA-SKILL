# API design over `Authorization: tma`

- Every request carries raw initData: `Authorization: tma <raw>`. Middleware validates (HMAC + expiry) and injects `{user_id, lang, chat_type, chat_instance, start_param}` into context. No cookies, no JWT parallel auth.
- REST shape: `GET /api/products`, `POST /api/cart/price {ids[]}` → `{lines[], total}` (server prices), `POST /api/book {slot_id}` → `201 {booking}` / `409 {error:'taken'}`. Errors: `{error:'code', message:'human RU/EN'}` + right HTTP status; frontend maps codes to localized copy (see copywriting.md).
- Idempotency: mutating calls take `client_key` (uuid per tap); server dedupes 24h — double-taps on BottomButton never double-charge.
- Pagination: cursor `?after=` for lists; rooms keyed by validated `chat_instance`, never client-sent room alone.
- Rate limits: game scores ≤ N/min per user; validation failures → 401 without details (no oracle).
- Versioning: `/api/v1/...` once prod users exist; tunnel-dev may stay unversioned.
