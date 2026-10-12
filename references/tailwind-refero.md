# Tailwind v4 theme from Refero + Telegram

Refero style pages export a Tailwind v4 `@theme` block — paste it, then add the Telegram bridge:

```css
@import "tailwindcss";
@theme {
  /* pasted Refero tokens, e.g. Linear: */
  --color-void: #08090a; --color-carbon: #0f1011;
  --color-acid-lime: #e4f222;
  --radius-card: 12px; --radius-btn: 6px;
}
/* Telegram live bridge (wins over Refero surfaces so both themes work) */
:root {
  --bg: var(--tg-theme-bg-color, var(--color-void));
  --text: var(--tg-theme-text-color, #fff);
  --hint: var(--tg-theme-hint-color, #8a8f98);
  --cta: var(--color-acid-lime);          /* Refero accent = the ONE CTA color */
}
```

Usage: surfaces `bg-(--bg) text-(--text)`, borders hairline per Refero (`border-white/10`), CTA `bg-(--cta)`. Never `bg-gradient-to-br from-violet-500` etc.
Dark/light: Telegram swaps `--tg-theme-*` live; Refero neutrals stay for accents/decor only. If the Refero style is light (cream editorial), map its paper → light tg bg and pick its ink for dark tg bg; keep the accent identical in both.
