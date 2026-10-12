# Errors & logs

UX: every failure = human sentence + action. `409 taken` → "Slot just taken — pick another time" + [Choose]; `401` → silent re-auth via fresh initData, then retry once; network fail → offline illustration + [Retry]; 500 → "Something broke on our side" + [Retry] (never stack traces in UI).
Frontend: BottomButton `hideProgress` in `finally`, haptic error, keep form data. Log to console only in dev; prod console stays silent.
Backend: structured logs `{ts, user_id, route, code, ms}`; NEVER log raw initData, tokens, phones. Validation failures → counter + 401, no detail to client. Alert on 5xx spike / payment webhook failures.
