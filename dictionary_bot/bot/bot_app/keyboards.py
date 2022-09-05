from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

inline_button_first = InlineKeyboardButton('first', callback_data = 'first')
inline_kb = InlineKeyboardMarkup()
inline_kb.add(inline_button_first)