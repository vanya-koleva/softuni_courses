from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    points = models.IntegerField(
        null=True,
        blank=True,
    )
