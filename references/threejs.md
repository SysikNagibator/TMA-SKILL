# three.js inside Telegram WebView

Allowed only when 3D serves the core action (game, configurator, hero product). Otherwise CSS/SVG.

```ts
const THREE = await import('three'); // lazy, separate chunk (see vite-config.md)
const renderer = new THREE.WebGLRenderer({ antialias: false, powerPreference: 'low-power' });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
```

- Pause loop on `visibilitychange` hidden, on `tg.onEvent('viewportChanged')` minimized, on `tg.isActive === false`. Resume on visible.
- Kill scene on route unmount (`geometry.dispose()`, `renderer.dispose()`); WebView GPU memory is tiny.
- Low-end Android (perf class in User-Agent, or `hardwareConcurrency <= 4`): reduce particles/shadows, or swap to static poster image.
- No postprocessing bloom stacks on mobile. One hemisphere + one directional light is usually enough.
- Fallback: `<img poster>` behind canvas; if WebGL context fails, poster stays and app still works.
- Respect `prefers-reduced-motion`: render one static frame, no autorotate.
