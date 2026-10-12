# Screen pattern library (map to Refero components)

- Splash: logo + skeleton of first screen behind, `ready()` instantly, max 1.5s branded wait, then content (no spinners-forever).
- Auth/profile: avatar+name from validated initData, language + theme rows, logout. No passwords.
- List→detail: chips filter + skeleton rows → detail with gallery, facts table, single BottomButton action.
- Checkout: lines + server total + BottomButton "Pay X" with progress; success screen with receipt facts + [Back to shop].
- Booking: date strip + slot grid → form (closingConfirmation if dirty) → confirm with write-access opt-in reason.
- Paywall: 3 tiers max, prices server-side, Stars invoice on tap, restore on open.
- Game: lobby (`chat_instance`) → fullscreen canvas → results + leaderboard; pause on hide.
- Settings: theme follow, language, haptics toggle (stored CloudStorage), support row, version row.
Each pattern: build from the ONE Refero style's card/button/badge specs (see DESIGN-TOKENS.md), Telegram theme vars for surfaces.
