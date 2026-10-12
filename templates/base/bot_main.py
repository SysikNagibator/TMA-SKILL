import os, asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

TOKEN = os.environ.get("BOT_TOKEN", "")
URL = os.environ.get("WEBAPP_URL", "")
if not TOKEN:
    raise SystemExit("Set BOT_TOKEN env from @BotFather")

bot, dp = Bot(TOKEN), Dispatcher()

@dp.message(CommandStart())
async def start(m: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Open app", web_app={"url": URL})]] if URL else [[
        InlineKeyboardButton(text="Open app", callback_data="no_url")]])
    await m.answer("Tap below to open the Mini App 👇", reply_markup=kb)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
