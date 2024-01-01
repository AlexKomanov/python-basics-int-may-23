import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

BOT_TOKEN = "6373447736:AAGMss0q40fPAHjXU8EPL5p8QTF1Z5bCf0c"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Promise -> pending / fulfilled / rejected
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


# print(f"{__name__ = }")

if __name__ == "__main__":
    asyncio.run(main())

