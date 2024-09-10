
from django.db import models

from petstagram3.core.models import IHaveUser
from petstagram3.photos.models import PetPhoto


class PhotoComment(IHaveUser):
    TEXT_MAX_LENGTH = 300

    text = models.TextField(
        max_length=TEXT_MAX_LENGTH
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    to_photo = models.ForeignKey(
        to=PetPhoto,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["-date_time_of_publication"]


class PhotoLike(IHaveUser):
    to_photo = models.ForeignKey(
        to=PetPhoto,
        on_delete=models.CASCADE,
    )

