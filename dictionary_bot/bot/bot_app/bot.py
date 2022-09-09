# инициализация бота
import asyncio
from aiogram import Bot, Dispatcher, executor
from .local_settings import API_KEY
from aiogram.contrib.fsm_storage.memory import MemoryStorage

loop = asyncio.get_event_loop()
bot = Bot(token = API_KEY)
dp = Dispatcher(bot, storage = MemoryStorage())

def bot_start():
    executor.start_polling(dp, skip_updates=True, loop=loop)
