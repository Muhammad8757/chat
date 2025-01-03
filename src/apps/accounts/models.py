from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .manager.user_managers import UserManager
from src.apps.base.models import BaseModel

class User(BaseModel, AbstractBaseUser):

    username = models.CharField(
        max_length=150,
        unique=True
    )

    first_name = models.CharField(
        verbose_name="Имя пользователя",
        max_length=40
    )

    last_name = models.CharField(
        verbose_name="Фамилия пользователя",
        max_length=40
    )

    email = models.EmailField(
        verbose_name="Почта пользователя",
        null=True
    )
    phone = models.CharField(
        verbose_name="Телефон",
        max_length=15
    )

    password = models.CharField(_("password"), max_length=128)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
