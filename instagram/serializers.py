from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

class PostSerializer(ModelSerializer):
    #author = AuthorSerializer()
    author_username = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = [
            'pk',
            'author_username',
            'message',
            'created_at',
            'updated_at',
            'is_public',
            'ip',
                  ]
