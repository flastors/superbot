from .users import UserMiddleware

from aiogram import Dispatcher

def setup_middlewares(dp: Dispatcher) -> None:
    dp.update.middleware(UserMiddleware())