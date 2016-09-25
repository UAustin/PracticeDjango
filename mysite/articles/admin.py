from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "article", "created_time", "user",)

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("article", "name", "body", "created", "updated", "active")

admin.site.register(Comment, CommentAdmin)
