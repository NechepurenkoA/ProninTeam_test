from django.db import models

from users.models import User


class Collect(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name="Автор сбора",
        on_delete=models.CASCADE,
        related_name="collection",
    )
    title = models.CharField(verbose_name="Название сбора", max_length=50)
    reason = models.CharField(verbose_name="Повод сбора", max_length=50)
    description = models.TextField(verbose_name="Описание", null=True)
    to_collect = models.IntegerField(
        verbose_name="Сумма сбора", null=False, blank=False
    )
    collected = models.IntegerField(verbose_name="Собрано", default=0)
    users_donated = models.IntegerField(verbose_name="Задонатило", default=0)
    image = models.ImageField(
        verbose_name="Картинка сбора", upload_to="collections/image", null=True
    )
    collected_on = models.DateTimeField(
        verbose_name="Дата завершения сбора", default=None
    )

    class Meta:
        verbose_name = "Сбор"
        verbose_name_plural = "Сборы"
        ordering = [
            "pk",
        ]
