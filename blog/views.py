from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Post


class PostListView(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    