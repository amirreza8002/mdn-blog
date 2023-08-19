from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from tinymce.models import HTMLField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class PostCategory(models.Model):
    category = models.CharField(_("category"), max_length=50)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(_("tag"), max_length=50)

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")

    def __str__(self):
        return self.tag


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Publish"

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(_("title"), max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    content = HTMLField(verbose_name=_("content"))
    categories = models.ManyToManyField(PostCategory, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")
    publish = models.DateTimeField(verbose_name=_("published at"), default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.DRAFT
    )
    hits = models.PositiveIntegerField(verbose_name="view", default=0)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def get_absolute_url(self):
        return reverse("posts:post_detail", args=[self.slug])

    def __str__(self):
        return self.title
