from django.contrib import admin

from .models import Post, Comment


class CommentInline(admin.StackedInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['title', 'created_at', 'status', 'author']
    list_filter = ['status', 'created_at', 'author']
    inlines = [CommentInline]




admin.site.register(Post, PostAdmin)
