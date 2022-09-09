# тут будут все команды нашего бота

from aiogram.types import message
from aiogram import types
from .logger import log

from .db_helper import check_dictionary
from .keyboards import get_keyboard_for_menu 
from .bot import dp
from . import messages

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply(messages.M_WELCOME)

@dp.message_handler(commands = ['start'])
async def send_menu(message: types.Message):
    try:
        await message.answer(messages.main_menu_header, 
                            reply_markup = await get_keyboard_for_menu())
    except Exception as e:
        log.warning(f'Ошибка при команде /start :: {e}')