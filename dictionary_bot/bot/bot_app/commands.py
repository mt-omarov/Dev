# тут будут все команды нашего бота

from aiogram.types import message
from aiogram import types 
from .bot import dp
from . import messages

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(messages.M_WELCOME)