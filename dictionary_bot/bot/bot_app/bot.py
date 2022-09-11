# инициализация бота
import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import ParseMode
from .local_settings import API_KEY

loop = asyncio.get_event_loop()
bot = Bot(token = API_KEY, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

def bot_start():
    executor.start_polling(dp, skip_updates=True, loop=loop)
