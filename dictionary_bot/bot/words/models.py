from django.db import models

class Word(models.Model):
    title = models.CharField(verbose_name = 'Word', max_length = 100)
    definition = models.TextField(verbose_name = 'Meaning')
    
    def __str__(self):
        return f'{self.title}: {self.definition}'
    
    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Words'

class User(models.Model):
    username = models.CharField(max_length=500, verbose_name='Ссылка на tg', blank=True, null=True)
    telegram_id = models.CharField(max_length=250, verbose_name='chat_id пользователя', unique = True)
