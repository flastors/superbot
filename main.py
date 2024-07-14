import asyncio
from utils import logger
from app.handlers import setup_routers
from app.middlewares import setup_middlewares
from loader import dp, bot

async def on_startup():
    logger.info('Bot started!')

async def on_shutdown():
    logger.info('Bot stopped!')

async def main():
    setup_middlewares(dp)
    setup_routers(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())