import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review
from django.db.models import Q, Count, Avg


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

def get_latest_article() -> str:
    article = Article.objects.prefetch_related(
        'authors', 'reviews'
    ).order_by(
        '-published_on'
    ).first()

    if article is None:
        return ""

    authors_names = ', '.join(a.full_name for a in article.authors.all().order_by('full_name'))
    num_reviews = article.reviews.count()
    avg_rating = article.reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    return (f"The latest article is: {article.title}. "
            f"Authors: {authors_names}. "
            f"Reviewed: {num_reviews} times. "
            f"Average Rating: {avg_rating:.2f}.")

def get_top_rated_article() -> str:
    article = Article.objects.annotate(
        avg_rating=Avg('reviews__rating'),
        num_reviews=Count('reviews')
    ).order_by(
        '-avg_rating', 'title'
    ).first()

    if article is None or article.num_reviews == 0:
        return ""

    return (f"The top-rated article is: {article.title}, "
            f"with an average rating of {article.avg_rating:.2f}, "
            f"reviewed {article.num_reviews} times.")

def ban_author(email=None) -> str:
    author = Author.objects.prefetch_related('reviews').filter(email__exact=email).first()

    if author is None or email is None:
        return "No authors banned."

    num_reviews = author.reviews.all().delete()[0]

    author.is_banned = True
    author.save()

    return (f"Author: {author.full_name} is banned! "
            f"{num_reviews} reviews deleted.")
