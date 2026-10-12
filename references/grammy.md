# grammY (Node.js bot alternative)

Use when the whole project is TypeScript. Same Telegram semantics as aiogram.

```ts
import { Bot, InlineKeyboard } from 'grammy';
const bot = new Bot(TOKEN);
bot.command('start', (ctx) => ctx.reply('Tap below 👇', {
  reply_markup: new InlineKeyboard().webApp('Open app', WEBAPP_URL),
}));
bot.on('message:web_app_data', (ctx) => ctx.reply(`Received: ${ctx.msg.web_app_data.data}`));
bot.callbackQuery('no_url', (ctx) => ctx.answerCallbackQuery({ text: 'Set WEBAPP_URL first' }));
bot.start(); // polling locally
```

- `ctx.answerWebAppQuery(query_id, result)` mirrors aiogram for inline send-back.
- Stars: `ctx.api.createInvoiceLink(...)` with `currency: 'XTR'`; verify `pre_checkout_query` + `message:successful_payment`.
- initData validation on YOUR API server still required (see backend-security.md) — grammY doesn't replace it; use `@tma.js/init-data-node`.
- Webhook prod: `webhookCallback(bot, 'express')` behind HTTPS only (see webhooks-prod.md).
