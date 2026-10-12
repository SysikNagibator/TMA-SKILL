# Media, icons, fonts

Images:
- Real photos in ONE grade (same grain/duotone as Refero style), WebP/AVIF, `loading="lazy"` below fold, explicit width/height (no CLS), `srcset` 1x/2x. Hero <150KB.
- No mixed stock packs. AI-generated only in one consistent style prompt, disclosed nowhere, invisible as AI.
- Avatars: Telegram `photo_url` when allowed; fallback initials circle (no grey silhouette clip-art).

Icons: Lucide (or inline SVG), stroke 1.8–2, 20–22px, `currentColor`. One icon family per app. Emojis never as chrome.

Fonts (Cyrillic is mandatory for RU):
- Heading + body pair from Refero style, but VERIFY Cyrillic subset (many display fonts lack `ё/ж/ф`). Fallbacks: `Unbounded/Manrope`, `Inter Tight/Golos Text`, system + `Golos`.
- `font-display: swap`, preload only 2 weights (400/700 or style's pair), subset `cyrillic+latin` via Google Fonts `&subset=` or self-hosted woff2.
- Numbers/prices: `font-variant-numeric: tabular-nums`.
- Never load >3 font files on mobile first paint.
