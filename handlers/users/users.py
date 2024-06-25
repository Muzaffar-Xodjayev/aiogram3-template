from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from loader import bot


router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Hello My Friend")
