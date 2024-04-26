from django.db import models

from fundraisings.models import Collect
from users.models import User


class Payment(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Отправитель",
        on_delete=models.SET_NULL,
        related_name="payment",
        null=True,
    )
    collection = models.ForeignKey(
        Collect,
        verbose_name="Отправлено на",
        on_delete=models.DO_NOTHING,
        related_name="donations",
        null=False,
    )
    amount = models.IntegerField(verbose_name="Сумма доната", null=False, blank=False)
    date = models.DateTimeField(verbose_name="Дата отправления", auto_now=True)
    hidden = models.BooleanField(verbose_name="Показывать сумму", default=False)

    class Meta:
        verbose_name = "Донат"
        verbose_name_plural = "Донаты"
        ordering = [
            "date",
        ]
