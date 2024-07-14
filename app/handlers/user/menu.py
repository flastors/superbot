from app.handlers.routers import user_router as router

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F

@router.message(Command('menu'))
async def _menu_command(msg: Message):
    await msg.answer('Твое меню, чепух', reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Чепух')]], resize_keyboard=True, one_time_keyboard=True))


@router.message()
async def _suka(msg: Message):
    await msg.answer('Чепух')