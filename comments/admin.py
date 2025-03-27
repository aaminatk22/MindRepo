from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'created_at', 'updated_at')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'article__title')