# Database (per-user data, minimal)

Dev/small: SQLite (WAL mode) — `users(id PK, lang, created)`, `orders(id, user_id, payload JSON, total, status)`, `kv(user_id, key, value)` for prefs. One file, backups by copy.
Growth: Postgres — same schema + `sessions`, `nonces`, `idempotency(client_key UNIQUE, result)`.

Rules:
- All money/state server-computed; store request + result for idempotency replay.
- Migrations: numbered SQL files `migrations/001_init.sql`, applied at boot in order, recorded in `_migrations` table. No ORM magic required; `aiosqlite`/`asyncpg` + plain SQL is fine.
- PII minimal: keep `user_id`, no phone unless the feature needs it (then encrypt at rest or don't store).
- Per-room data (games/groups): `rooms(chat_instance PK, state JSON, updated)` with row TTL cleanup job.
