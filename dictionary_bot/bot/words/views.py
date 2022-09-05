from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseNotFound
from .models import Word

import random

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['pk', 'title', 'definition']

class RandomWord(APIView):
    def get(self, *args, **kwargs):
        all_words = Word.objects.all()
        random_word = random.choice(all_words)
        serialized_random_word = WordSerializer(random_word, many = False)
        return Response(serialized_random_word.data)

class Dictionary(APIView):
    def get(self, request):
        list = Word.objects.all()
        serialized_list = WordSerializer(list, many = True)
        return Response(serialized_list.data)



