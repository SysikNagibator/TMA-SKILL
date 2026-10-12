# ton — wallet connect + gated content

Files: `public/tonconnect-manifest.json` (`{name, url: <tunnel-or-prod https>, iconUrl}`), connect button (`@tonconnect/ui`), proof request, gated screen.
Flow: Connect → `requestProof` → backend verifies via TON API + `auth_date` freshness → unlock.
Local: manifest `url` MUST equal tunnel URL — update together with MenuButton on every restart.
Secrets: no private keys in repo; verify server-side.
