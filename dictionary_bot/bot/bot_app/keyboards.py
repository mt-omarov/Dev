from ast import keyword
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from . import messages

async def get_keyboard_for_menu():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.row(
        InlineKeyboardButton(text = messages.add_word_button, callback_data = "add_word"),
        InlineKeyboardButton(text = messages.show_dictionary, callback_data = "show_dictionary")
    )
    return keyboard