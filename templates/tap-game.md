# tap-game — fullscreen game + leaderboard

Screens: Lobby (`chat_instance` room, `?startapp=room_X`) → Game (fullscreen `requestFullscreen`, canvas dpr≤2, pause on `isActive=false`, landscape if needed) → Results + leaderboard.
API: `POST /api/score` (server validates rate/anti-cheat, never trusts client total), `GET /api/top?room=`.
Motion: haptic per milestone only; `prefers-reduced-motion` → static mode; poster fallback if WebGL missing.
Groups: key state by `chat_instance`; test with 2 users same link.
