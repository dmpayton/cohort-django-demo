from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['title', 'created_at', 'status', 'author']
    list_filter = ['status', 'created_at', 'author']


admin.site.register(Post, PostAdmin)
