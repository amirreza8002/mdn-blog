import random

from django.views.generic.list import ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.defaultfilters import slugify
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse

from .models import Post, Comment
from .forms import CommentForm


class CommentGet(DetailView):
    model = Post
    template_name = "posts/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "posts/post_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        form.instance.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.get_object()
        return reverse("posts:post_detail", kwargs={"slug": article.slug})


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"

    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        self.get_object().hits += 1
        self.get_object().save()
        # return super().get(request, *args, **kwargs)  # + view(request, *args, **kwargs)
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Post.published.all()


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
