from django.shortcuts import render
from django.views import generic

from .models import Post


class PostMixin(object):
    queryset = Post.objects.filter(status='P')


class PostList(PostMixin, generic.ListView):
    template_name = 'blog/post_list.html'


class PostDetail(PostMixin, generic.DetailView):
    template_name = 'blog/post_detail.html'
