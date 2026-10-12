# Design System — zero AI slop

## Banned (hard fail)

1. `linear-gradient(135deg,#667eea,#764ba2)` or any default purple-blue gradient.
2. Default Inter, grey `#6B7280` on white, everything centered.
3. Hero "Welcome to SuperApp ✨🚀" + 3 identical Feature cards.
4. Emojis as UI icons (🎯💰⚡️). Emojis allowed only as user content, never as chrome.
5. Glassmorphism everywhere, purple blobs/noise background, AI-stock illustrations.
6. Lorem ipsum, EN placeholders in RU apps, `MM/DD/YYYY` for RU users.
7. Lone spinner for every load, no skeletons / empty / error / offline states.
8. Shipping without a Refero style (see `refero-workflow.md`) — hard fail.

## Principle: 1 app = 1 story

One sentence before code: "This is ___ for ___, core action ___ in ___ seconds."
Example: "Coffee checkout for a barista, pay in 10s with one thumb."

Derive: hero screen = 1 number/product/map (not a carousel of everything), 1 brand accent + Telegram palette (not 5 accents), 2 adjectives (e.g. "warm, bold" / "strict, banking") — check every decision against them.

## Palette: Telegram first, Refero second

Base always from live `themeParams` so dark/light both work:

```css
:root {
  --bg: var(--tg-theme-bg-color, #fff);
  --text: var(--tg-theme-text-color, #111);
  --hint: var(--tg-theme-hint-color, #999);
  --link: var(--tg-theme-link-color, #2481cc);
  --btn: var(--tg-theme-button-color, #2481cc);
  --btn-text: var(--tg-theme-button-text-color, #fff);
  --secondary: var(--tg-theme-secondary-bg-color, #f4f4f5);
  --section: var(--tg-theme-section-bg-color, #fff);
  --sep: var(--tg-theme-section-separator-color, rgba(0,0,0,.08));
}
```

Rules:
- Refero accent maps onto `--btn` / one action color. Keep Telegram system blue unless the brand really needs its own (cafe, game).
- Contrast AA ≥ 4.5:1 in BOTH schemes.
- No decorative gradients. Allowed only: photo overlay `black 40%→0%` for legibility, or 1 brand gradient from the logo angle.
- Destructive = `--tg-theme-destructive-text-color`. Elevation via 1px `sep` borders + one modal shadow `0 8px 24px rgba(0,0,0,.08)`, not shadow spam.

Starter mappings (pick ONE, never mix):
- Food/cafe: cream `#F6EFE6` + ink `#1C1410` + caramel `#C67C2E`
- Fintech: `#0B0E11` + `#EAECEF` + `#0ECB81`/`#F6465D`, tabular numbers
- Game: `#0A0A14` + neon lime `#C6FF4A` or amber `#FFB020`, rest monochrome
- Beauty: `#FAF6F0` + `#1A1A1A` + dusty rose `#C48B7A`
- Then overwrite with the chosen Refero tokens in `webapp/DESIGN-TOKENS.md`.

## Typography (Cyrillic required for RU apps)

- Pair: characterful headings + neutral body. Proven Cyrillic pairs: `Unbounded/Manrope`, `Inter Tight/Golos Text`, system `-apple-system` + `Golos` for banks.
- Scale: 28/22/17/15/13, headings 700 −1% tracking, body 15/1.45, captions 13 hint.
- Numbers: `font-variant-numeric: tabular-nums` for prices/balances.
- Max 2 weights per screen. Buttons 15–16 semibold, no all-caps except sport/game.
- RU details: `ё`, «», — (not `"` and `-`).

## Grid & components

- 8pt grid, one radius scale 12/16/20. Cards `section_bg`, 1px `sep` dividers.
- Mobile-first 390×844. Primary CTA in thumb zone above MainButton. Pin footers to `viewportStableHeight + safe-area`, never to jumping `viewportHeight`.
- Mandatory states: skeleton shimmer (~1.2s), empty (what to do + button), error (what + retry), offline.
- Icons: Lucide / SVG stroke 1.8, 20–22px. Real photos in one grade (grain/duotone under palette), no mixed stock.

## Motion & 3D

- Base: 180ms `cubic-bezier(.2,.8,.2,1)` enter, 120ms press `scale .97`, transform/opacity only, 60fps.
- Haptics in sync: `selection_changed` tabs, `impact_medium` main CTA, `notification_success/error` finals. Never on scroll.
- 3D only for: game core, configurator (car/furniture/skin), hero wow-product. Never for forms/lists/balances.
- Budget: three.js `lazy()`, `dpr=min(dpr,2)`, `antialias:false` on weak devices, pause when `isActive=false`, static poster fallback, respect `prefers-reduced-motion` + Telegram low-perf User-Agent class.
- One success Lottie max, not confetti on every tap.

## Telegram patterns

- Paint header/bg/bottomBar from theme. No white header on dark theme.
- BottomButton = ONE final action ("Pay 450 ₽") with loader. SecondaryButton = alternative.
- BackButton.show() on nested, hide() on root. `closingConfirmation` on dirty forms.
- `requestWriteAccess`/`requestContact`/geo only on explicit tap with "why" explanation.

## 5-second "not slop?" test

1. Remove logo — still recognizable? No → redo.
2. Greyscale screenshot — hierarchy readable? No → fix size/weight.
3. Telegram dark theme — readable? No → fix vars.
4. Remove all UI emojis — better? Yes → keep it that way.
5. Show to a non-tech user: clear where to tap in 3s? No → simplify.
