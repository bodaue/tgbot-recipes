from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

from tgbot.db.models.user import User as DBUser


class DBUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        telegram_user: User = data.get("event_from_user")
        user = await DBUser.get_or_create(
            defaults=dict(
                name=telegram_user.full_name, username=telegram_user.username
            ),
            id=telegram_user.id,
        )

        data["db_user"] = user[0]
        return await handler(event, data)
