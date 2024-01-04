import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
import os

from aiogram.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}. Let's begin!")


@dp.message()
async def answer_as_echo(message: types.Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except Exception:
        await message.answer("Unsupported media type...")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
