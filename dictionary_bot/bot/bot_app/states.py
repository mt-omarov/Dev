from aiogram.dispatcher.filters.state import State, StatesGroup

class GameStates(StatesGroup):
    start = State()
    random = State()
    dictionary = State()

class NewWord(StatesGroup):
    writing_word = State()
    writing_definition = State()

class ShowDictionary(StatesGroup):
    start = State()