# Refero workflow (MANDATORY)

Source: `https://styles.refero.design/` — 2000+ AI-readable design systems. Each style page has Preview + `DESIGN.md` (Copy.md) + Tailwind v4 + CSS variables + tokens.

## Why mandatory

Refero gives the AI real product taste (colors, type, spacing, components, do/don't) instead of inventing generic slop. The skill hard-fails without this step.

## Steps (agent executes, not the user)

1. Open `https://styles.refero.design/`, search by task character:
   - fintech/bank → `Mercury`, `Ramp`, `Brex`
   - devtool/productivity → `Linear`, `Raycast`, `Vercel`
   - food/lifestyle → coffee/lifestyle styles, `ElevenLabs` warm cream editorial
   - game/crypto → neon dark styles
   - beauty/editorial → magazine/cream styles
2. Open the style page `/style/<id>`, switch tab to `DESIGN.md`, copy full markdown (or Tailwind v4 / CSS vars if building with Tailwind).
3. Create `webapp/DESIGN-TOKENS.md` in the project:
```md
# DESIGN-TOKENS
- Refero style: <Name> (<url>)
- Why it fits: <1 sentence>
- Palette mapping:
  - Refero Void #08090a → tg bg dark / ...
  - Refero Acid Lime #e4f222 → brand CTA (BottomButton color)
  - text mapping: Paper #fff → tg text dark ...
- Type: <fonts, scale, tracking, weights>
- Radii: cards 12 / buttons 6 / pills 9999 (from style, do not invent)
- Spacing ladder: 4/8/12/24/96
- Do / Don't (copied, max 7 each)
- Telegram adaptation: base surfaces replaced with --tg-theme-* so light+dark work; Refero accent kept for 1 CTA only.
```
4. Implement tokens as CSS vars + Tailwind theme (if Tailwind):
```css
:root {
  --brand-cta: #e4f222; /* Refero Acid Lime */
  --radius-card: 12px; --radius-btn: 6px;
  --bg: var(--tg-theme-bg-color);
  --text: var(--tg-theme-text-color);
  /* ... + full Refero palette as --ref-* for accents */
}
```
5. Build components using style's component prompts (hero headline, screenshot card, CTA button, nav bar, badges — Refero lists exact px/weights).
6. Obey style's Don't list (e.g. Linear: no bold 700+, no decorative gradients, max 12px card radius, hairline borders not shadows, mono only for IDs).

## Example (Linear)

- Canvas Void `#08090a`, card Carbon `#0f1011`, hairline Graphite `#23252a`, text Paper `#fff` / Mist `#d0d6e0` / Fog `#8a8f98`, single CTA Acid Lime `#e4f222`.
- Inter Variable 400–590 only, tracking −0.022em on display, radii 6/12/9999, 0.5px borders, 8/12/24/96 spacing.
- Telegram adaptation: light theme → paper becomes `#fff` canvas via tg vars, CTA stays lime; dark → exact Linear tokens.

## Fail conditions

- No `DESIGN-TOKENS.md` → fail.
- Two Refero styles mixed → fail (pick ONE).
- Refero accent used for 5 different buttons/decorations → fail (one primary action per view).
- DESIGN.md copied but Telegram dark/light broken → fail (adaptation required).
