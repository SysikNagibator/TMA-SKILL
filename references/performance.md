# Performance budget (mobile first)

- First paint in WebView < 2s on mid Android: main bundle ≤ 200KB gzip (three.js/Lottie always lazy chunks), ≤ 3 font files, hero image <150KB WebP.
- Runtime: 60fps lists (virtualize >50 rows), no layout thrash (read `viewportStableHeight` once per stable event), images lazy + sized.
- Low-end detection: `hardwareConcurrency <= 4` or Telegram perf class low in User-Agent → disable blur/shadows-heavy decor, cap `dpr` at 1.5, static poster instead of 3D/Lottie.
- Network: one `initData`-authed bootstrap call, then per-screen fetches; cache GETs in memory per session; offline-first error copy.
- Measure: Desktop inspect Performance tab + Android remote profiling; attach numbers (first paint, bundle KB) in delivery notes.
