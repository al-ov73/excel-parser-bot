import asyncio
import logging
from aiogram import Bot, Dispatcher
from bot.handlers import router
from bot.db import init_db
from dotenv import load_dotenv
import os

from bot.utils import create_data_folder

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    create_data_folder()
    init_db()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
