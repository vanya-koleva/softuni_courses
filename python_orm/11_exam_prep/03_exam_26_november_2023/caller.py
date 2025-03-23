import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author
from django.db.models import Q, Count


def get_authors(search_name=None, search_email=None) -> str:
    if search_name is None and search_email is None:
        return ""

    query_name = Q(full_name__icontains=search_name)
    query_email = Q(email__icontains=search_email)

    if search_name is not None and search_email is not None:
        query = Q(query_name & query_email)
    elif search_name is not None:
        query = query_name
    else:
        query = query_email

    authors = Author.objects.filter(query).order_by('-full_name')

    if not authors.exists():
        return ""

    return "\n".join(f"Author: {a.full_name}, "
                     f"email: {a.email}, "
                     f"status: {'Banned' if a.is_banned else 'Not Banned'}"
                     for a in authors)

def get_top_publisher() -> str:
    author = Author.objects.get_authors_by_article_count().first()

    if author is None or author.article_count == 0:
        return ""

    return f"Top Author: {author.full_name} with {author.article_count} published articles."

def get_top_reviewer() -> str:
    reviewer = Author.objects.annotate(
            reviews_count=Count('reviews')
        ).order_by(
            '-reviews_count', 'email'
        ).first()

    if reviewer is None or reviewer.reviews_count == 0:
        return ""

    return f"Top Reviewer: {reviewer.full_name} with {reviewer.reviews_count} published reviews."
