from django.urls import path

from .views import PostListView, PostDetailView, UserDetailView, PostCreateView

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("post/create/", PostCreateView.as_view(), name="post_create"),
    path("users/<uuid:pk>/", UserDetailView.as_view(), name="user_detail"),
]
