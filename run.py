import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

from handlers import router

load_dotenv()

tg_token = os.getenv("TELEGRAM_TOKEN")

async def main():
    bot = Bot(token=tg_token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
