from django import forms

from tinymce.widgets import TinyMCE

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug", "author", "content", "categories", "tags", "status"]
        widgets = {"content": TinyMCE(attrs={"class": "edit_by_tinemce"})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)
        # widgets = {"comment": TinyMCE(attrs={"class": "edit_by_tinemce"})}
