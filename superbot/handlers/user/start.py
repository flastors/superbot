from aiogram import Router

from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def _start(msg: Message):
    await msg.reply('Hello blyat')
