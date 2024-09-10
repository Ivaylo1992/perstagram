from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models, get_user_model

from petstagram3.accounts.managers import PetstagramUserManager


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    objects = PetstagramUserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


UserModel = get_user_model()


class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"
        DO_NOT_SHOW = "Do not show"

    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    GENDER_MAX_LENGTH = max(len(choice) for _, choice in Gender.choices)

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LENGTH)
        ],
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH)
        ],
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=GENDER_MAX_LENGTH,
        choices=Gender.choices,
        default=Gender.DO_NOT_SHOW,
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return "Noname User"