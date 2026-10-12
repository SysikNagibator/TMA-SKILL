# shop — catalog + cart + Stars checkout

Screens: Catalog (grid, skeleton cards, filters as chips) → Product (gallery, price tabular, BottomButton "Add 450 ₽") → Cart (qty steppers, server totals) → Success (Lottie once + `notification_success` + invoice if Stars).
Bot: `/start` + deep `?startapp=sku_123` → product screen. API: `GET /api/products`, `POST /api/cart/price` (ids only, server prices), `POST /api/invoice` → `openInvoice(url)` → `invoiceClosed`.
Refero: pick 1 food/fintech style; CTA = Refero accent; prices tabular; no emoji icons.
Anti-cheat: cart total recomputed server-side from ids.
