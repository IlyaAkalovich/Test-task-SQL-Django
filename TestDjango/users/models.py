from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from .utils import create_shortened_url


class User(AbstractUser):
    pass


class Shortener(models.Model):
    long_url = models.URLField()

    short_url = models.CharField(max_length=15, unique=True, blank=True)

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
        )

    def __str__(self):
        return f'{self.short_url}'


    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)
