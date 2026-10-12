# HARD checklist (all must be YES)

## Design (no slop)
- [ ] No purple-blue gradient, default-Inter cards, "Welcome" hero, emoji icons, full-glass, lorem?
- [ ] `webapp/DESIGN-TOKENS.md` exists with ONE Refero style + URL + mapping to tg-theme?
- [ ] Do/Don't from Refero obeyed (radii, weights, one CTA color)?
- [ ] Dark + light Telegram themes readable, AA contrast, vars from `--tg-theme-*`?
- [ ] Skeleton/empty/error/offline states, not a single spinner?
- [ ] 390px thumb zone, footer pinned to `viewportStableHeight` + safe-area?
- [ ] Motion 120–250ms, haptics in sync, `prefers-reduced-motion` respected?
- [ ] 3D only if serving core action, lazy, paused in background, poster fallback?

## API correctness
- [ ] `telegram-web-app.js?64` + `ready()` first, `isVersionAtLeast` gates?
- [ ] `themeChanged`/`viewportChanged` handled, header/bg/bottomBar painted?
- [ ] BackButton nested-only routing, BottomButton final-only + loader?
- [ ] `closingConfirmation` on dirty forms, swipes not breaking gestures?
- [ ] WriteAccess/Contact/Geo only on explicit tap with reason?
- [ ] Tested in real Telegram clients (not just browser)?

## Security
- [ ] Raw `initData` in `Authorization: tma` on every call, HMAC + `auth_date` validated?
- [ ] No `initDataUnsafe` for rights/money? Token only in backend `.env`, never `dist/`?
- [ ] Prices/rights server-computed, CORS not `*`+cookies, no initData in prod console?

## Local run
- [ ] Frontend `:5173` 200 locally, tunnel https URL 200 publicly, tool documented?
- [ ] MenuButton + inline `web_app` point at CURRENT tunnel URL (re-run after restart)?
- [ ] Bot polling answers `/start`, app opens from MenuButton AND phone?
- [ ] Manifest (TON) URL updated if used? Cache busted (`?v=`)?

## Verification evidence (mandatory)
- [ ] WebView logs attached (inspect/chrome://inspect/Safari/eruda-dev) with zero JS errors?
- [ ] Dark + light screenshots or described checks?
- [ ] Payments/groups flows tested if in scope (invoice status / 2-user room)?

## Behavior (no extras, no lectures)
- [ ] Built exactly what was asked — zero unrequested screens/features?
- [ ] Ambiguities were asked, not guessed?
- [ ] User-provided tokens were USED (not refused/preached), kept in `.env`, never printed/committed?

ANY NO → fix. Do not deliver.
