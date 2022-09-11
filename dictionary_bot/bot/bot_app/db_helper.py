from asgiref.sync import sync_to_async
from words.models import Word, User

@sync_to_async
def check_dictionary():
    if Word.objects.all().exists(): 
        return True
    else:
        return False

@sync_to_async
def check_word(word_id):
    if Word.objects.get(id = word_id).exists():
        return Word.objects.get(id = word_id)
    else:
        return False

@sync_to_async
def check_user(chat_id):
    if User.objects.filter(telegram_id = chat_id).exists():
        return True
    else:
        return False

@sync_to_async
def save_user(chat_id, username):
    user = User(telegram_id = chat_id, username = username)
    user.save()
    print(user.username)


@sync_to_async
def add_word(n_title, n_definition):
    word = Word(title = n_title, definition = n_definition)
    word.save()
    print(word.title)

@sync_to_async
def edit_word(word_id, new_title, new_definition):
    if Word.objects.filter(id = word_id).exists():
        word = Word.objects.get(id = word_id)  
        word.title = new_title
        word.definition = new_definition
        word.save()

@sync_to_async
def get_list_words():
    if Word.objects.exists():
        words_dictionary = dict()
        list_words = Word.objects.order_by('title')
        for i in list_words:
            words_dictionary[i.title] = i.definition
        return words_dictionary
    else:
        return None
