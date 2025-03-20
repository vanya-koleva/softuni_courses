from django.db.models import manager, QuerySet, Count


class ProfileManager(manager.Manager):
    def get_regular_customers(self) -> QuerySet:
        return self.annotate(
            orders_count=Count('order')
        ).filter(
            orders_count__gt=2
        ).order_by(
            '-orders_count'
        )
