# тут будут все команды нашего бота
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from .db_helper import add_word, get_list_words, save_user, check_user
from .keyboards import get_keyboard_for_menu 
from . import messages
from .states import GameStates, NewWord


"""
@dp.message_handler(commands=['help'])
async def send_welcome(message: Message):
    await message.reply(messages.M_WELCOME)
"""

async def send_menu(message: Message):
    chat_id = message.chat.id
    if not await check_user(chat_id):
        await save_user(chat_id, message.from_user.username)
    await message.answer(
        messages.main_menu_header, 
        reply_markup = await get_keyboard_for_menu()
    )

"""
@dp.callback_query_handler(text = ['add_word'])
async def add_word(query: types.CallbackQuery, state = "*"):
    await NewWord.writing_word.set()
    await query.message.answer(
        f"Введите ваше слово:"
    )

@dp.message_handler(state = NewWord.writing_word)
async def writing_word(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['word'] = msg.text
    await bot.send_message(
        msg.from_user.id,
        f"Вы ввели слово <{msg.text}>. Введите ваше определение:"
    )
    #print(msg.text)

@dp.message_handler(state = NewWord.writing_word)
async def writing_definition(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        #print(f"{msg.text} type is {type(msg.text)}")
        await add_word('первое слово', 'любое')
    await bot.send_message(
        msg.from_user.id,
        f"Слово добавлено!" 
    )
    await GameStates.start.set()
"""

"""
@dp.message_handler(commands = ['show_dictionary'])
async def show_dictionary(message: types.Message, state = GameStates.start):
    d_dictionary = await get_list_words()
    if d_dictionary:
        m_dictionary = ''
        for key, value in d_dictionary.items():
            m_dictionary += f"• {key} – {value}\n"
        await message.reply(m_dictionary)
    else:
        await message.reply('Словарь пуст!')
"""
