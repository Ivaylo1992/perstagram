
from django.db import models
from django.template.defaultfilters import slugify

from petstagram3.core.models import IHaveUser


class Pet(IHaveUser):
    NAME_MAX_LENGTH = 30
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )

    personal_photo = models.URLField()

    date_of_birth = models.DateField(
        null = True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=False,
    )


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name





