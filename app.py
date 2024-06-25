import asyncio

from loader import dp, bot
import handlers
from utils.set_bot_commands import set_default_commands


async def on_startup():
    await set_default_commands(bot)

    dp.include_routers(*handlers.routers_list)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(on_startup())
