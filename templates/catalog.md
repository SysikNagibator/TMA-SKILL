# catalog — list + filters + detail + share

Screens: List (search + chips, skeleton rows) → Detail (photo, facts, BottomButton "Share" via `shareMessage` prepared / `shareToStory`).
API: `GET /api/items?q=&tag=`, `POST /api/share` → `PreparedInlineMessage` id → `shareMessage(id)`.
Share text server-rendered (no client injection).
