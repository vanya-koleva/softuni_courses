from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.choices import ArticleCategoryChoices


class ContentMixin(models.Model):
    content = models.TextField(
        validators=[
            MinLengthValidator(10)
        ]
    )

    class Meta:
        abstract = True


class PublishedOnMixin(models.Model):
    published_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    class Meta:
        abstract = True


class Author(models.Model):
    full_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3),
        ]
    )
    email = models.EmailField(
        unique=True,
    )
    is_banned = models.BooleanField(
        default=False,
    )
    birth_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2005),
        ]
    )
    website = models.URLField(
        blank=True,
        null=True,
    )


class Article(ContentMixin, PublishedOnMixin):
    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(5),
        ]
    )
    category = models.CharField(
        max_length=10,
        choices=ArticleCategoryChoices,
        default=ArticleCategoryChoices.TECHNOLOGY
    )
    authors = models.ManyToManyField(Author)


class Review(ContentMixin, PublishedOnMixin):
    rating = models.FloatField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    article =models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
