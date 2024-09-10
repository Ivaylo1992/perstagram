from django.core.exceptions import ValidationError


def image_size_validator(value):
    MAX_SIZE = 5242880
    if value.size > MAX_SIZE:
        raise ValidationError('The maximum file size that can be uploaded is MB')