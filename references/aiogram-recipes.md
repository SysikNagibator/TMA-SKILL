# aiogram 3 recipes

```python
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, States
from aiogram.fsm.context import FSMContext

bot, dp = Bot(TOKEN), Dispatcher()

# 1. Entry: inline web_app button (full power: query_id)
@dp.message(CommandStart())
async def start(m: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Open app", web_app={"url": WEBAPP_URL})]])
    await m.answer("Tap below 👇", reply_markup=kb)

# 2. Deep link: /start sku_123 → bot may preface, app reads start_param itself
@dp.message(CommandStart(deep_link=True))
async def deep(m: Message, command): ...

# 3. Reply-keyboard variant ONLY when you need sendData without a server
@dp.message(Command("form"))
async def form(m: Message):
    kb = ReplyKeyboardMarkup(keyboard=[[
        KeyboardButton(text="Fill form", web_app={"url": WEBAPP_URL})]], resize_keyboard=True)
    await m.answer("Open:", reply_markup=kb)

@dp.message(F.web_app_data)  # service message from sendData (≤4096B)
async def got_data(m: Message):
    await m.answer(f"Received: {m.web_app_data.data}")

# 4. Inline result back to chat (closes Mini App)
@dp.message(Command("x"))
async def x(m: Message): ...
# from webapp flow: bot.api.answer_web_app_query(query_id, result=InlineQueryResultArticle(...))

# 5. FSM for multi-step chat fallbacks (when user ignores the Mini App)
class Order(StatesGroup): name = States(); phone = States()

# 6. Stars invoice
link = await bot.create_invoice_link(title="Pro", description="...", payload=f"user:{uid}:pro",
    currency="XTR", prices=[{"label": "Pro", "amount": 100}])
# verify on pre_checkout_query + successful_payment updates; amounts from payload, never client
```

Polling locally: `await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())`. Log handler errors with user id (never initData raw).
