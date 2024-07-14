from aiogram.types import ErrorEvent

from main import dp 
import logging

@dp.error()
async def _error(event: ErrorEvent):
    logging.warning(event.exception)