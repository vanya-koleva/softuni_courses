from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class OnlyLettersValidator:
    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        for char in value:
            if not char.isalpha():
                raise ValidationError(self.message)
