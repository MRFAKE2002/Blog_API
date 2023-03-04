from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['title', 'author', 'text', 'status']
        # exclude = ['datetime_created', 'datetime_modified']
        fields = '__all__'
        # depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # fields = ['title', 'author', 'text', 'status']
        # exclude = ['datetime_created', 'datetime_modified']
        fields = '__all__'
        # depth = 1
