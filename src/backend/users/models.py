from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        verbose_name="Эл. почта",
        max_length=254,
        unique=True,
    )
    first_name = models.CharField(verbose_name="Имя", max_length=25)
    last_name = models.CharField(verbose_name="Фамилия", max_length=25)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = [
            "username",
        ]
