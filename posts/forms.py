from django import forms

from tinymce.widgets import TinyMCE

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug", "author", "content", "categories", "tags", "status"]
        widgets = {"content": TinyMCE(attrs={"class": "edit_by_tinemce"})}
