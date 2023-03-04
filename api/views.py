from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics

from blog.models import Post
from .serializers import PostSerializer, UserSerializer


class PostListApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    
    serializer_class = PostSerializer
   

class PostDetailUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    
    serializer_class = PostSerializer


class UserListApiView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    
    serializer_class = UserSerializer


class UserDetailUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    
    serializer_class = UserSerializer

