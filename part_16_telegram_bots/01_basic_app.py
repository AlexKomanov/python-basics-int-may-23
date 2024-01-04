import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


# Promise -> pending / fulfilled / rejected
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


# print(f"{__name__ = }")

if __name__ == "__main__":
    asyncio.run(main())

