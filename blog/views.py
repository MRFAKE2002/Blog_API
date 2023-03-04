from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Post


class PostListView(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    

class PostDetailView(generic.DetailView):
    # def get_object(self):
    #     return get_object_or_404(
    #         Post.objects.filter(status=True),
    #         pk = self.kwargs.get("pk")
    #     )
    model = Post
    template_name = 'blog/post_detail.html'
    