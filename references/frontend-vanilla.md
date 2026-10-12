# Vanilla TS frontend (no framework)

For landing-like apps: zero deps, one `tg.ts` wrapper (~60 lines).

```ts
export const tg = (window as any).Telegram?.WebApp;
export const inTelegram = !!tg?.initData;
export function boot() {
  if (!tg) { document.body.innerHTML = '<p>Open this app inside Telegram.</p>'; return false; }
  tg.ready();
  paint(); tg.onEvent?.('themeChanged', paint);
  tg.onEvent?.('viewportChanged', layout);
  return true;
}
function paint() {
  const t = tg.themeParams ?? {};
  const root = document.documentElement.style;
  root.setProperty('--bg', t.bg_color ?? '#fff');
  root.setProperty('--text', t.text_color ?? '#111');
  tg.setHeaderColor?.(t.bg_color); tg.setBackgroundColor?.(t.bg_color);
}
function layout() {
  document.documentElement.style.setProperty('--stable-h',
    (tg.viewportStableHeight ?? window.innerHeight) + 'px');
}
export async function api(path: string, body?: unknown) {
  const res = await fetch(path, { method: body ? 'POST' : 'GET',
    headers: { 'Content-Type': 'application/json',
      ...(tg?.initData ? { Authorization: `tma ${tg.initData}` } : {}) },
    ...(body ? { body: JSON.stringify(body) } : {}) });
  if (!res.ok) throw new Error(`API ${res.status}`);
  return res.json();
}
export const haptic = {
  tap: () => tg?.HapticFeedback?.selectionChanged(),
  go: () => tg?.HapticFeedback?.impactOccurred('medium'),
  ok: () => tg?.HapticFeedback?.notificationOccurred('success'),
  err: () => tg?.HapticFeedback?.notificationOccurred('error'),
};
```

BackButton: `tg.BackButton.show/hide` + `onEvent('backButtonClicked')`, mirror your hash router. MainButton: `tg.MainButton.setParams/onClick/showProgress/hideProgress`. Same rules as React: no mock in prod, theme from live params, stable-height footer.
