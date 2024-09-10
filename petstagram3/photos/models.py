
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram3.core.models import IHaveUser
from petstagram3.pets.models import Pet
from petstagram3.pets.validators import image_size_validator


class PetPhoto(IHaveUser):
    class Meta:
        ordering = ("-date_of_publication",)

    DESCRIPTION_MAX_LENGTH = 300
    DESCRIPTION_MIN_LENGTH = 10
    LOCATION_MAX_LENGTH = 30

    photo = models.ImageField(
        null=False,
        blank=False,
        validators=[
            image_size_validator,
        ]
    )

    description = models.CharField(
        max_length=DESCRIPTION_MAX_LENGTH,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),
        ]
    )

    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        blank=True,
        null=True,
    )

    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
        null=True,
    )

    date_of_publication = models.DateTimeField(
        auto_now=True,
    )

