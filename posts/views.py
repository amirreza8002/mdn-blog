from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Count

from .models import Post, PostCategory
from accounts.models import CustomUser


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Post.published.all()


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"

    def get(self, request, *args, **kwargs):
        self.get_object().hits += 1
        self.get_object().save()
        return super().get(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     # slug = self.kwargs["slug"]
    #     # post = Post.objects.filter(slug__exact=slug)
    #     # print(post)
    #     # user = CustomUser.objects.get(username=post._meta.get_field("username"))
    #
    #     return context


class UserDetailView(DetailView):
    model = CustomUser
    template_name = "users/user_detail.html"
