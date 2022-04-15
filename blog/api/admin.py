from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'header', 'content',)
    search_fields = ('author', 'header')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'content', 'parent')
    search_fields = ('author', 'content', 'parent')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
