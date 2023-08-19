from django.urls import path, include

from .views import LoggedOutView, UserDetailView, UserListView

urlpatterns = [
    path("", include("allauth.urls")),
    path("loggedout/", LoggedOutView.as_view(), name="logged_out"),
    path("users/list/", UserListView.as_view(), name="user_list"),
    path("users/<uuid:pk>/", UserDetailView.as_view(), name="user_detail"),
]
