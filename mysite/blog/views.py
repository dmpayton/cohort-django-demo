from django.shortcuts import render
from django.views import generic

from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status='P')
    template_name = 'blog/post_list.html'


class PostDetail(generic.DetailView):
    queryset = Post.objects.filter(status='P')
    template_name = 'blog/post_detail.html'
