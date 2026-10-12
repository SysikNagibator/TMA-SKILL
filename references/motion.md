# Motion system + haptics

Tokens (from Refero style, else defaults): `--dur-fast:120ms; --dur:180ms; --dur-slow:250ms; --ease:cubic-bezier(.2,.8,.2,1)`.
- Enter: fade+translateY(8px) var(--dur) var(--ease). Press: `scale(.97)` 120ms. Modal: slide-up from bottom. Page: slide/fade, never flip/rotate.
- Animate `transform`/`opacity` only. 60fps or cut it.
- Skeletons: shimmer 1.2s pulse on cards/rows; spinners only for <1s waits inside buttons (BottomButton `showProgress`).
- Haptics score: tab/select → `selectionChanged`; primary CTA press → `impact_medium`; success → `notification_success`; error → `notification_error`. Nothing on scroll/typing/toggles.
- `prefers-reduced-motion: reduce` → disable enter animations, parallax, Lottie autoplay (show first frame).
- Lottie: one success animation max per flow, <100KB, no autoplay loops on screens.
- BottomSheet conflict: if the app has its own vertical swipe (stories, sheets), call `disableVerticalSwipes()` for that screen only, re-enable on exit.
