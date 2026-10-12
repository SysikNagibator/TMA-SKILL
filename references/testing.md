# Testing & QA matrix

Per release (and mandatory for first publish):
1. Clients: Telegram Desktop + 1 Android + 1 iOS if reachable; log `tg.version/platform` from splash.
2. Themes: light + dark, each: contrast readable, header/bg/bottomBar painted, no white-on-white.
3. Entry points: MenuButton, inline button, direct `?startapp=` link, cold start + reopen (cache).
4. Flows: happy path, empty (new user), error (server 500/kill backend → friendly retry), offline (airplane → offline screen).
5. Money: Stars sandbox invoice paid/cancelled; double-tap BottomButton → single charge (idempotency).
6. Groups (if in scope): 2 users, same `?startapp=room_X`, shared state converges; third user in another room isolated.
7. WebView logs clean: zero JS errors (`chrome://inspect` / Safari / eruda-dev excerpt attached as evidence).
8. Old client: set `isVersionAtLeast` gates — features degrade, app never white-screens.
