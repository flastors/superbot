from app.handlers.routers import user_router as router

from aiogram.types import Message
from aiogram.filters import Command


@router.message(Command('start'))
async def _start(msg: Message):
    await msg.reply('Hello blyat')
