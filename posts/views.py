from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.defaultfilters import slugify

from .models import Post, PostCategory
from .forms import PostForm
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


class UserDetailView(DetailView):
    model = CustomUser
    template_name = "users/user_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = "title", "content", "categories", "tags", "status"
    template_name = "posts/post_create.html"
    # form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(self.request.POST.get("title"))
        return super().form_valid(form)
