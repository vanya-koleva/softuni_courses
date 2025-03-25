from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models

from main_app.choices import MissionStatusChoices
from main_app.mixins import NameMixin, UpdatedAtMixin, LaunchDateMixin


class Astronaut(NameMixin, UpdatedAtMixin):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(regex=r'^\d+$')
        ]
    )
    is_active = models.BooleanField(
        default=True
    )
    date_of_birth =models.DateField(
        null=True,
        blank=True
    )
    spacewalks = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )


class Spacecraft(NameMixin, UpdatedAtMixin, LaunchDateMixin):
    manufacturer = models.CharField(
        max_length=100,
    )
    capacity = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    weight = models.FloatField(
        validators=[
            MinValueValidator(0.0)
        ]
    )


class Mission(NameMixin, UpdatedAtMixin, LaunchDateMixin):
    description = models.TextField(
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=9,
        choices=MissionStatusChoices,
        default=MissionStatusChoices.PLANNED
    )
    spacecraft =models.ForeignKey(
        Spacecraft,
        on_delete=models.CASCADE,
        related_name='missions',
    )
    astronauts = models.ManyToManyField(
        Astronaut,
        related_name='missions',
    )
    commander =models.ForeignKey(
        Astronaut,
        on_delete=models.SET_NULL,
        null=True,
        related_name='commanded_missions'
    )
