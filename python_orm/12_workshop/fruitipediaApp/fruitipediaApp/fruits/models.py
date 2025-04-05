from django.core.validators import MinLengthValidator
from django.db import models

from fruitipediaApp.fruits.validators import OnlyLettersValidator


# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator(
                message="Fruit name should contain only letters!"
            )
        ]
    )
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="fruits",
        null=True,
        blank=True,
    )
