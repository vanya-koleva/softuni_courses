from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AlphaNumericUnderscoreValidator:
    def __init__(self, message: str=None) -> None:
        self.message = message or "Ensure this value contains only letters, numbers, and underscore."

    def __call__(self, value: str) -> None:
        if not value.replace("_", "").isalnum():
            raise ValidationError(self.message)
