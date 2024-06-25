from aiogram import types
from aiogram.filters.base import Filter
from data.config import ADMINS


class IsAdmin(Filter):

    async def __call__(self, message: types.Message) -> bool:
        admins_data = []
        admins = [item['admin_id'] for item in admins_data if item.get("admin_id")]
        user_id = message.from_user.id
        return user_id in admins or user_id in ADMINS
