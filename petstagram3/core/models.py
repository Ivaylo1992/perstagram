from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class IHaveUser(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    class Meta:
        abstract = True
