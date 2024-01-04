import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message()
async def answer_as_echo(message: types.Message):
    if message.text:
        await message.answer(text=message.text)
    elif message.sticker:
        await message.answer("Sticker was used...")
        await message.reply_sticker(sticker=message.sticker.file_id)
    else:
        await message.reply("A new media type was used!!! ")


@dp.message()
async def reply_as_echo(message: types.Message):
    await message.reply(text=message.text)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
