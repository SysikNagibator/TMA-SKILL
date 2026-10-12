# Telegram WebApp API — correct 100%

Sources: `core.telegram.org/bots/webapps`, `docs.telegram-mini-apps.com/platform/*`.

## Init (order matters)

```html
<head><script src="https://telegram.org/js/telegram-web-app.js?64"></script></head>
```

```js
const tg = window.Telegram.WebApp;
tg.ready(); // as early as possible — hides loading placeholder
// tg.expand(); // only if the main screen needs height (BottomSheet opens half by default)
tg.setHeaderColor(tg.themeParams.bg_color ?? '#ffffff');
tg.setBackgroundColor(tg.themeParams.bg_color ?? '#ffffff');
if (tg.setBottomBarColor) tg.setBottomBarColor(tg.themeParams.bottom_bar_bg_color ?? tg.themeParams.bg_color);
```

With React prefer `@tma.js/sdk-react` (`useLaunchParams`, `useThemeParams`; `mockTelegramEnv` dev-only, never prod).

Gate new APIs: `tg.isVersionAtLeast('8.0')` (fullscreen, safe-area, homescreen, share/download, geo, motion), `tg.isVersionAtLeast('7.10')` (SecondaryButton, bottomBarColor).

## Theme (live)

- `tg.colorScheme` (`light|dark`, CSS `var(--tg-color-scheme)`), `tg.themeParams` (bg/text/hint/link/button/button_text/secondary_bg/header_bg/bottom_bar_bg/accent/section_bg/section_header/section_separator/subtitle/destructive). Mirrored as `--tg-theme-*`.
- Subscribe: `tg.onEvent('themeChanged', applyTheme)`. Test BOTH schemes manually in Telegram settings.

## Viewport & safe area (most common bug)

- `viewportHeight` jumps during BottomSheet drag — NEVER pin footers to it.
- Pin to `viewportStableHeight` (`--tg-viewport-stable-height`). `viewportChanged` with `isStateStable=true` = animation end.
- Bot API 8.0+: `safeAreaInset` + `contentSafeAreaInset` (+ `safeAreaChanged`/`contentSafeAreaChanged`). Required in fullscreen.
- Fullscreen: `requestFullscreen()`/`exitFullscreen()`, `isFullscreen` flag. Transparent header + `setHeaderColor` for status-bar contrast. Landscape only for games/media.
- Desktop/Web: already maximized medium window, `expand()` is no-op. Don't break desktop with fixed 100dvh.

```css
.footer {
  position: sticky; bottom: 0;
  padding-bottom: calc(var(--tg-safe-area-inset-bottom, 0px) + var(--tg-content-safe-area-inset-bottom, 0px));
}
```

## Buttons

BackButton:
```js
tg.BackButton.show();
tg.onEvent('backButtonClicked', () => router.back());
if (isRoot) tg.BackButton.hide();
```
Click does nothing by itself — routing is yours. Remove listeners on unmount.

BottomButton (renamed from MainButton in 7.10):
```js
const main = tg.MainButton;
main.setParams({ text: 'Pay 450 ₽', color: tg.themeParams.button_color, text_color: tg.themeParams.button_text_color, is_visible: true, is_active: true });
main.onClick(async () => { main.showProgress(); try { await pay(); tg.HapticFeedback.notificationOccurred('success'); } catch { tg.HapticFeedback.notificationOccurred('error'); } finally { main.hideProgress(); } });
```
One final action per screen, verb + amount. SecondaryButton = alternative. SettingsButton = About/Support.

## Haptics, popups, misc

```js
tg.HapticFeedback.impactOccurred('medium');
tg.HapticFeedback.selectionChanged();
tg.HapticFeedback.notificationOccurred('success'); // error|warning
```
Sparingly — battery + annoyance (docs WARNING).

- `showPopup/showAlert/showConfirm` → `popupClosed`. `openLink(url,{try_instant_view:true})` only on user tap. `openTelegramLink` stays in-app (pre-7.0 closed). `openInvoice` → `invoiceClosed`. 8.0+: `shareToStory/shareMessage/downloadFile` native dialogs, `setEmojiStatus/requestEmojiStatusAccess`, `addToHomeScreen/checkHomeScreenStatus`.
- `requestWriteAccess/requestContact` → boolean callback, only on button with reason. `showScanQrPopup` → `qrTextReceived` (+`scanQrPopupClosed` 7.7+). `readTextFromClipboard` only attachment-menu + gesture. `switchInlineQuery`, `enableClosingConfirmation()` on dirty forms, `disableVerticalSwipes()` only on gesture conflict.
- `CloudStorage/DeviceStorage/SecureStorage` (9.0+) for user keys, no backend secrets. `BiometricManager` only with consent. `LocationManager/Accelerometer/Gyroscope` on button, handle denial.
- `sendData(≤4096B)` ONLY for KeyboardButton `web_app` (service message, no server). Inline `web_app` uses `query_id` + `answerWebAppQuery`.

## Launch paths (7 — know the right one)

1. MenuButton (`/setmenubutton` or `setChatMenuButton`) — fast entry, behaves like inline.
2. KeyboardButton `web_app` — only one with `sendData`, no server. Inputs/calendars/randomizers.
3. InlineKeyboardButton `web_app` — full (`query_id` + answerWebAppQuery). Shops/services.
4. Main Mini App (bot profile Launch + `t.me/bot?startapp=cmd&mode=compact`) — bot IS the app; Apps tab + Store (with Stars).
5. Direct link `t.me/bot/appname?startapp=cmd` — sharing, group/multiplayer via `chat_type/chat_instance`.
6. Inline mode (`InlineQueryResultsButton web_app` + `switchInlineQuery`).
7. Attachment menu (`/setattach`, test-env for everyone) + `settingsButtonClicked`.

`start_param/startapp` arrives as `initData.start_param` + `tgWebAppStartParam` GET param — deep links (`order_123`).

## Debugging WebView (mandatory evidence)

- Desktop Beta: Settings → Advanced → Experimental → Enable webview inspecting → right-click Inspect.
- Android: tap version twice → Enable WebView Debug → `chrome://inspect/#devices`.
- iOS: Safari Develop → iPhone → Telegram WebView. No Mac → `eruda` dev-only, strip in prod.
- Log `tg.version/tg.platform/initData.length` on splash — half of white screens are old clients.
