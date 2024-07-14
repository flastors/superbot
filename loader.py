from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from motor.motor_tornado import MotorClient

from config import (BOT_TOKEN, MONGO_NAME, MONGO_URL)


bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

client = MotorClient(MONGO_URL)
db = client[MONGO_NAME]
