from aiogram import Dispatcher
from .user import router as user_router
from ..filters import AdminFilter
from config import OWNER

def setup_routers(dp: Dispatcher) -> None:
    user_router.message.filter(AdminFilter(OWNER))
    dp.include_routers(user_router)
