from aiogram.fsm.state import State, StatesGroup

class GameStates(StatesGroup):
    start = State()

class NewWord(StatesGroup):
    writing_word = State()