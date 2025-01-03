from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True
        default_permissions = ()

class AbstractTimestampsModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Время изменения", auto_now=True)

    class Meta:
        abstract = True