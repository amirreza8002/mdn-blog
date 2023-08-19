from django.contrib.auth.views import LogoutView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import CustomUser


class LoggedOutView(LogoutView):
    template_name = "account/logged_out.html"


class UserDetailView(DetailView):
    model = CustomUser
    template_name = "users/user_detail.html"


class UserListView(ListView):
    model = CustomUser
    template_name = "users/user_list.html"
    context_object_name = "user_list"

    def get_queryset(self):
        return CustomUser.authors.all()
