from django.contrib import admin
from .models import Word

class WordAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'definition']
    list_editable = ['title', 'definition']

admin.site.register(Word, WordAdmin)
