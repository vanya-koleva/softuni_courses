from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class BadWordValidator:
    def __init__(self, bad_words: Optional[list], message: Optional[str]=None):
        self.bad_words = bad_words
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or "The text contains bad words."

    def __call__(self, value: str):
        for word in value.split():
            if word.lower() in self.bad_words:
                raise ValidationError(self.message)
