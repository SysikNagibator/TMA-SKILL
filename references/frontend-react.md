# React frontend (@tma.js/sdk-react)

Packages: `@tma.js/sdk-react` (hooks) + `@tma.js/sdk` (core) + `@tma.js/init-data-node` (backend only).

```tsx
import { SDKProvider, useLaunchParams, useThemeParams, useMainButton, useBackButton, useHapticFeedback } from '@tma.js/sdk-react';

function Root() {
  return <SDKProvider acceptCustomStyles debug={import.meta.env.DEV}>
    <App />
  </SDKProvider>;
}

function ProductScreen({ onBack, onPay }) {
  const theme = useThemeParams();          // live theme, re-renders on themeChanged
  const back = useBackButton();            // {show, hide}
  const main = useMainButton();            // {setParams, showProgress, onClick...}
  const haptic = useHapticFeedback();
  useEffect(() => { back.show(); return () => back.hide(); }, []);
  useEffect(() => {
    main.setParams({ text: 'Pay 450 ₽', isVisible: true, backgroundColor: theme.buttonColor });
    const off = main.onClick(async () => { main.showProgress(); try { await onPay(); haptic.notificationOccurred('success'); } catch { haptic.notificationOccurred('error'); } finally { main.hideProgress(); } });
    return off;
  }, [theme]);
}
```

Rules:
- `mockTelegramEnv` ONLY in dev entry (`if (import.meta.env.DEV)`), never in prod bundle. Outside Telegram with no mock — render a "Open in Telegram" fallback screen, not a crash.
- Theme via `useThemeParams()` + CSS vars; never hardcode bg/text.
- Router (react-router/tanstack): BackButton mirrors history — show on depth>0, hide on root. Unsubscribe on unmount (the `off` functions).
- `retrieveRawInitData()` from `@tma.js/sdk` for the `Authorization: tma` header on every call.
- `isVersionAtLeast('8.0')` guard before fullscreen/safe-area hooks; old clients get non-fullscreen layout.
