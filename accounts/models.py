from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

import uuid


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField(verbose_name=_("biography"), blank=True, null=True)

    def get_absolute_url(self):
        return reverse("posts:user_detail", args=[self.id])
