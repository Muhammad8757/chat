from django.db import models

from src.apps.accounts.models import User

class Room(models.Model):
    class Status(models.IntegerChoices):
        INACTIVE = 0, "INACTIVE"
        ACTIVE = 1, "ACTIVE"
    
    class TYPE(models.IntegerChoices):
        PRIVATE = 0, "Private chat"
        GROUP = 1, "Group chat"

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    members = models.ManyToManyField(User, verbose_name="Участники")

    name = models.CharField(
        verbose_name="Название чата",
        max_length=50,
        blank=True,
        null=True,
    )

    type = models.PositiveSmallIntegerField(choices=TYPE.choices, verbose_name="Тип чата", default=TYPE.GROUP)

    status = models.PositiveSmallIntegerField(
        verbose_name="Статус активности", choices=Status.choices, default=Status.ACTIVE
    )

    def __str__(self):
        return self.name
    
class Message(models.Model):
    class Status(models.IntegerChoices):
        INACTIVE = 0, "Inactive"
        ACTIVE = 1, "Active"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    content = models.TextField(
        verbose_name="Контент сообщения",
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        verbose_name="Название чата",
        related_name="message_room",
    )
    status = models.PositiveSmallIntegerField(verbose_name="Статус", choices=Status.choices, default=Status.ACTIVE)

    def __str__(self):
        return self.content