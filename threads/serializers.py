from rest_framework import serializers
from .models import Thread
from django.contrib.auth.models import User

class ThreadSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)  # Получаем username от пользователя

    class Meta:
        model = Thread
        fields = ['id', 'title', 'description', 'author', 'username']  # Указываем все необходимые поля