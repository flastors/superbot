from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Update

from database.models import User
from loader import bot

class UserMiddleware(BaseMiddleware):
    async def __call__(
            self, 
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]], 
            event: Update, 
            data: Dict[str, Any]
            ) -> Any:
        if event.message:
            from_user = event.message.from_user
        if event.callback_query:
            from_user = event.callback_query.from_user
        if event.inline_query:
            from_user = event.inline_query.from_user
        user = await User.get_or_create(id=from_user.id, name=from_user.first_name, username=from_user.username)
        data['user'] = user
        if user.status == 'banned':
            await bot.send_message(from_user.id, 'YOU ARE BANNED')
            return
        
        return await handler(event, data)