from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
)

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/create/", PostCreateView.as_view(), name="post_create"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
]
