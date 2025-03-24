from django.db.models import manager, QuerySet, Count


class TennisPlayerManager(manager.Manager):
    def get_tennis_players_by_wins_count(self) -> QuerySet:
        return self.annotate(
            wins_count=Count('matches_won')
        ).order_by(
            '-wins_count', 'full_name'
        )
