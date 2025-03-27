from django.db import models
from django.db.models import QuerySet, Count


class HouseManager(models.Manager):
    def get_houses_by_dragons_count(self) -> QuerySet:
        return self.annotate(
            num_dragons=Count('dragons')
        ).order_by(
            '-num_dragons',
            'name'
        )
