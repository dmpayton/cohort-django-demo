from django.shortcuts import render, redirect
from django.views import generic

from .forms import CommentForm
from .models import Post, Comment


class PostMixin(object):
    queryset = Post.objects.filter(status='P')


class PostList(PostMixin, generic.ListView):
    template_name = 'blog/post_list.html'


class PostDetail(PostMixin, generic.DetailView):
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

class CreateComment(PostMixin, generic.View):
    def post(self, request, pk):
        post = self.queryset.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post.get_absolute_url())
        return redirect(post.get_absolute_url() + '?error=1')
