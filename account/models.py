from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_director = models.BooleanField(default=False, verbose_name="Director")
    is_archivist = models.BooleanField(default=False, verbose_name="Arxivchi")
    is_download = models.BooleanField(default=False, verbose_name="Download")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan vaqti")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"