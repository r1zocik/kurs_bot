import asyncio
from aiogram import Bot, Dispatcher
import logging

from config import BOT_TOKEN
from database import init_db
from handlers import register, convert

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


logging.basicConfig(level=logging.INFO)
async def main():
    init_db()

    dp.include_router(register.router)
    dp.include_router(convert.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
