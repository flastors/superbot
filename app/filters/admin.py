from aiogram.filters import Filter
from aiogram.types import Message
from typing import List

class AdminFilter(Filter):
    def __init__(self, admin_ids: List[int] | int = None):
        if isinstance(admin_ids, int):
            admin_ids = [admin_ids]
        self.admin_ids = admin_ids

    async def __call__(self, message: Message, **data) -> bool:
        return message.from_user.id in self.admin_ids