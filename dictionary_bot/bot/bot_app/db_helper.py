from aiogram.types import InlineKeyboardButton
from asgiref.sync import sync_to_async
from django.db.models import Q
from words.models import Word
from .logger import log

@sync_to_async
def check_dictionary():
    try:
        if Word.objects.all().exists():
            db_word = Word.objects.first()
        else:
            return False
    except Exception as e:
        log.warning(f'Ошибка при вызове /check_dictionary:: {e}')

@sync_to_async
def check_word(word_id):
    try:
        if Word.objects.get(id = word_id).exists():
            word = Word.objects.get(id = word_id)  
        else:
            return False
    except Exception as e:
        log.warning(f'Ошибка при вызове /check_word:: {e} – {word_id}')

@sync_to_async
def add_word(title, definition):
    try:
        word = Word(title = title, definition = definition)
        word.save()
    except Exception as e:
        log.warning(f'Ошибка при вызове /add_word:: {e}')

@sync_to_async
def edit_word(word_id, new_title, new_definition):
    try:
        if Word.objects.get(id = word_id).exists():
            word = Word.objects.get(id = word_id)  
            word.title = new_title
            word.definition = new_definition
        else:
            return False
    except Exception as e:
        log.warning(f'Ошибка при вызове /edit_word:: {e} – {word_id}')

