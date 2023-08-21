from django.contrib import admin

from .models import Post, PostCategory, Tag, Comment
from .forms import PostForm


class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

    list_display = [
        "title",
        "status",
        "author",
        "publish",
        "created",
    ]
    list_filter = ["status", "created", "publish", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ["status", "publish"]

    form = PostForm


admin.site.register(PostCategory)
admin.site.register(Tag)
admin.site.register(Comment)
