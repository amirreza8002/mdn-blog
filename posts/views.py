import random

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.defaultfilters import slugify


from .models import Post


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


# class UserAccount(LoginRequiredMixin, )


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = (
        "title",
        "content",
        "categories",
        "tags",
        "status",
    )
    template_name = "posts/post_create.html"

    def new_slug(self, slug):
        slug = slug + str(random.randint(1, 10**6))
        return slug

    def make_slug(self, slug):
        post = Post.objects.filter(slug=slug)
        if post.exists():
            slug = self.new_slug(slug)
            return self.make_slug(slug)

        return slug

    def form_valid(self, form):
        form.instance.author = self.request.user
        slug = slugify(self.request.POST.get("title"))
        form.instance.slug = self.make_slug(slug)

        return super().form_valid(form)
