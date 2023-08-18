from django.urls import path

from .views import PostListView, PostDetailView, UserDetailView

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("users/<uuid:pk>/", UserDetailView.as_view(), name="user_detail"),
]
