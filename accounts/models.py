from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

import uuid


class AuthorUsers(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(posts__isnull=False)


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField(verbose_name=_("biography"), blank=True, null=True)

    objects = UserManager()
    authors = AuthorUsers()

    def get_absolute_url(self):
        return reverse("user_detail", args=[self.id])
