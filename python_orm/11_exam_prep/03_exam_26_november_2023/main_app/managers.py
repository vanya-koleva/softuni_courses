from django.db.models import manager, QuerySet, Count


class AuthorManager(manager.Manager):
    def get_authors_by_article_count(self) -> QuerySet:
        return self.annotate(
            article_count=Count('article')
        ).order_by(
            '-article_count', 'email'
        )
