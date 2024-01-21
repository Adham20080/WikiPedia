import wikipedia
import logging
import asyncio
import sys
from config import Token
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram import Bot, types, Dispatcher

bot = Bot(Token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        f"Asslomu aleykum\n{message.from_user.full_name}\nMen sizga wikipedia saytidan ma'lumot olib beruvchi botman.")


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Bu bot sizga wikipediadan ma'lumot olib beradi,\nNima haqida ma'lumot olishni istaysiz ?")


@dp.message()
async def wiki(message: Message):
    try:
        await message.reply(f"<pre>{wikipedia.summary(message.text)}</pre>", parse_mode="HTML")
    except:
        await message.reply("Siz qidirgan mavzu topilmadi,\nQaytadan urunib ko'ring")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
