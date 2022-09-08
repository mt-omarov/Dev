from ast import keyword
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from . import messages

inline_button_first = InlineKeyboardButton('first', callback_data = 'first')
inline_kb = InlineKeyboardMarkup()
inline_kb.add(inline_button_first)

async def get_keyboard_for_menu():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.row(
        InlineKeyboardButton(text = messages.add_word_button, callback_data = "add_word"),
        InlineKeyboardButton(text = messages.show_dictionary, callback_data = "show_words")
    )
    return keyboard