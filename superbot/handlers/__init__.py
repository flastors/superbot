from aiogram import Dispatcher
from .user import router as user_router


def setup_routers(dp: Dispatcher) -> None:
    dp.include_routers(user_router)
