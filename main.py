import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from superbot.handlers import setup_routers
from config import BOT_TOKEN


dp = Dispatcher()
bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

async def on_startup():
    ...

async def on_shutdown():
    ...

async def main():
    setup_routers(dp=dp)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())