from aiogram import types
from .bot import dp, bot
from .keyboards import inline_kb
from .states import GameStates
from .data_fetcher import get_random
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands = ['train'], state = "*")
async def train(message: types.Message, state: FSMContext):
    await GameStates.random.set()
    res = await get_random()
    async with state.proxy() as data:
        data['step'] = 1
        data['answer'] = res.get('definition')
        data['word'] = res.get('title')
    
        await message.reply(f"{ data['step'] } of 1. Word is a { data['word'] }", reply_markup = inline_kb) 

@dp.callback_query_handler(lambda c: c.data in ['first'], state = GameStates.random)
async def button_click_callback(callback_querry: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_querry.id)
    answer = callback_querry.data
    async with state.proxy() as data:
        if answer == data.get(answer):
            res = await get_random()
            data['step'] += 1
            data['answer'] = res.get('definition')
            data['word'] = res.get('title')
            if data['step'] > 1:
                await bot.send_message(callback_querry.from_user.id, "The game is over!")
                await GameStates.start.set()
            else:
                await bot.send_message(callback_querry.from_user.id, "Правильно!")
        else:
            await bot.send_message(
                callback_querry.from_user.id, 
                f"Ответ неверный, подумай ещё.", 
                reply_markup = inline_kb
            )
