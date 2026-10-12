# dashboard — stats + charts + settings

Screens: Stats (1 hero number + sparkline, tabular) → Breakdown list → Settings (theme follow-system toggle stored in CloudStorage/DeviceStorage).
API: `GET /api/stats` (per validated user), no cross-user leaks.
Charts: lightweight SVG/canvas, no heavy BI libs on mobile; reduce motion on low-perf User-Agent.
