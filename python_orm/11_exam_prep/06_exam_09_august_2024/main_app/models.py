from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models

from main_app.choices import DragonBreathChoices
from main_app.mixins import NameMixin, ModifiedAtMixin, WinsMixin


class House(NameMixin, ModifiedAtMixin, WinsMixin):
    motto = models.TextField(
        blank=True,
        null=True,
    )
    is_ruling = models.BooleanField(
        default=False,
    )
    castle = models.CharField(
        max_length=80,
        blank=True,
        null=True,
    )


class Dragon(NameMixin, ModifiedAtMixin, WinsMixin):
    MIN_POWER = 1.0
    MAX_POWER = 10.0

    power = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(MIN_POWER),
            MaxValueValidator(MAX_POWER),
        ],
        default=1,
    )
    breath = models.CharField(
        max_length=9,
        choices=DragonBreathChoices,
        default=DragonBreathChoices.UNKNOWN,
    )
    is_healthy = models.BooleanField(
        default=True,
    )
    birth_date = models.DateField(
        default=date.today,
    )
    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
    )


class Quest(NameMixin, ModifiedAtMixin):
    code = models.CharField(
        max_length=4,
        unique=True,
        validators=[
            RegexValidator(regex=r'^[A-Za-z#]{4}$')
        ]
    )
    reward = models.FloatField(
        default=100.0,
    )
    start_time = models.DateTimeField()
    dragons = models.ManyToManyField(
        Dragon,
        related_name='quests',
    )
    host = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name='quests',
    )
