from django.contrib import admin
from .models import Article, Comment


# for inline both models
# class CommentInline(admin.StackedInline):
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
