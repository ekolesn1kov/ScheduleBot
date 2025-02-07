import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode

logging.basicConfig(level=logging.INFO)
bot = Bot(token="8186948759:AAEqmTJU9w5lhVohhBMY4NCwJ43RaSL9hZQ")
dp = Dispatcher()

responses = {
    '/start': 'Добро пожаловать,<b>{}</b>!'
}

async def send_response(message: Message, key: str):
    if isinstance(responses[key], list):
        for response in responses[key]:
            await message.answer(response, parse_mode=ParseMode.HTML)
    else:
        await message.answer(responses[key].format(message.from_user.full_name), parse_mode=ParseMode.HTML)

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await send_response(message, '/start')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
