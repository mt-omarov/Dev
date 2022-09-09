# тут будут все команды нашего бота

from aiogram.types import message
from aiogram import types
from .logger import log
from .bot import dp, bot

from .db_helper import check_dictionary, add_word, get_list_words
from .keyboards import get_keyboard_for_menu 
from .bot import dp
from . import messages

from .states import GameStates, NewWord
from aiogram.dispatcher import FSMContext

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

@dp.message_handler(commands = ['add_word'])
async def add_word(message: types.Message, state = "*"):
    await NewWord.writing_word.set()
    await message.reply("Введите ваше слово:")

@dp.message_handler(state = NewWord.writing_word)
async def writing_word(message: types.Message, state: FSMContext):
    word = message.text
    async with state.proxy() as data:
        data['word'] = word
        #await message.reply(f"Вы ввели слово <{data['word']}>.")
    await NewWord.writing_definition.set()
    await message.reply(f"Вы ввели слово <{word}>. Введите ваше определение:")

@dp.message_handler(state= NewWord.writing_definition)
async def writing_definition(message: types.Message, state: FSMContext):
    definition = message.text
    await message.reply(f"Вы ввели определение <{definition}>.")
    async with state.proxy() as data:
        await add_word(data['word'], definition)
        #await message.reply(f"Вы вводили слово <{data['word']}>.")
        await message.reply(
            f"Слово {data['word']} добавлено!" 
        )
    await GameStates.start()
    
@dp.message_handler(commands = ['show_dictionary'])
async def show_dictionary(message: types.Message, state = '*'):
    try:
        d_dictionary = await get_list_words()
        m_dictionary = ''
        for key, value in d_dictionary:
            m_dictionary += f"{key} – {value}\n"
        
        if m_dictionary:
            message.reply(m_dictionary)
        else:
            message.reply('Словарь пуст')
    except Exception as e:
        log.warning(f'Ошибка при команде /show_dictionary :: {e}')
