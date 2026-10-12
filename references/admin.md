# Admin, flags, support

- Admin gate: `ADMIN_IDS={...}` env; `/admin` command checks `user_id` in set (from validated initData/session, never client flag). Admin API under `/api/admin/*` with same check + audit log.
- Feature flags: `flags.json` or DB table (`new_paywall: {pct: 20}`) — percentage rollout by `user_id % 100`, kill-switch per feature. Flags evaluated server-side; client receives resolved values.
- Support bundle: `/api/me/debug` returns `{user_id, app_version, tg_version, platform}` for bug reports (no initData echo). Bot `/start` fallback works without the Mini App.
- Broadcasts: via bot `sendMessage` batches with rate limits (30/s), never from the Mini App client.
