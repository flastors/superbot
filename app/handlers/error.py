from aiogram.types import ErrorEvent

from main import dp 
from utils import logger

@dp.error()
async def _error(event: ErrorEvent):
    logger.warning(event.exception)