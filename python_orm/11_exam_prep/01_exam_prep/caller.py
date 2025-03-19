import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie
from main_app.choices import MovieGenreChoices
from django.db.models import Q, Count, Avg, F


def populate_db():
    # Populate Director model
    director1 = Director.objects.create(
        full_name="Christopher Nolan",
        birth_date="1970-07-30",
        nationality="British",
        years_of_experience=25
    )

    director2 = Director.objects.create(
        full_name="Quentin Tarantino",
        birth_date="1963-03-27",
        nationality="American",
        years_of_experience=30
    )
    director3 = Director.objects.create(
        full_name="Greta Gerwig",
        birth_date="1983-08-04",
        nationality="American",
        years_of_experience=10
    )

    # Populate Actor model
    actor1 = Actor.objects.create(
        full_name="Leonardo DiCaprio",
        birth_date="1974-11-11",
        nationality="American",
        is_awarded=True,
    )
    actor2 = Actor.objects.create(
        full_name="Margot Robbie",
        birth_date="1990-07-02",
        nationality="Australian",
        is_awarded=False,
    )
    actor3 = Actor.objects.create(
        full_name="Cillian Murphy",
        birth_date="1976-05-25",
        nationality="Irish",
        is_awarded=True
    )

    # Populate Movie model
    movie1 = Movie.objects.create(
        title="Inception",
        release_date="2010-07-16",
        storyline="A thief who enters dreams to steal secrets.",
        genre=MovieGenreChoices.ACTION,
        rating=8.8,
        is_classic=True,
        director=director1,
        starring_actor=actor1,
        is_awarded=True,
    )
    movie1.actors.add(actor2, actor3)

    movie2 = Movie.objects.create(
        title="Pulp Fiction",
        release_date="1994-10-14",
        storyline="Crime stories interwoven in a non-linear fashion.",
        genre=MovieGenreChoices.DRAMA,
        rating=8.9,
        is_classic=True,
        director=director2,
        starring_actor=actor1,
        is_awarded=True,
    )
    movie2.actors.add(actor2, actor3)

    movie3 = Movie.objects.create(
        title="Barbie",
        release_date="2023-07-21",
        storyline="Barbie embarks on a journey of self-discovery.",
        genre=MovieGenreChoices.COMEDY,
        rating=7.5,
        is_classic=False,
        director=director3,
        starring_actor=actor2,
        is_awarded=False,
    )
    movie3.actors.add(actor1, actor3)

def get_directors(search_name=None, search_nationality=None) -> str:
    if search_name is None and search_nationality is None:
        return ""

    query_name = Q(full_name__icontains=search_name)
    query_nationality = Q(nationality__icontains=search_nationality)

    if search_name is not None and search_nationality is not None:
        query = Q(query_name & query_nationality)
    elif search_name is not None:
        query = query_name
    else:
        query = query_nationality

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors:
        return ""

    return '\n'.join(
        f"Director: {d.full_name}, "
        f"nationality: {d.nationality}, "
        f"experience: {d.years_of_experience}"
        for d in directors
    )

def get_top_director() -> str:
    director = Director.objects.get_directors_by_movies_count().first()

    if not director:
        return ''

    return f"Top Director: {director.full_name}, movies: {director.movie_count}."

def get_top_actor() -> str:
    top_actor = (Actor.objects.prefetch_related('starring_movies')
                 .annotate(
                    starred_movie_count=Count('starring_movies'),
                    avg_rating=Avg('starring_movies__rating'),
                 )
                 .order_by('-starred_movie_count', 'full_name')
                 .first()
    )

    if not top_actor or not top_actor.starred_movie_count:
        return ''

    movie_titles = ', '.join(m.title for m in top_actor.starring_movies.all())

    return (f"Top Actor: {top_actor.full_name}, "
            f"starring in movies: {movie_titles}, "
            f"movies average rating: {top_actor.avg_rating:.1f}"
            )

def get_actors_by_movies_count() -> str:
    actors = (Actor.objects.prefetch_related('movies')
              .annotate(movies_count=Count('movies'))
              .order_by('-movies_count', 'full_name')[:3]
    )

    if not actors or not actors[0].movies_count:
        return ''

    return '\n'.join(f'{a.full_name}, participated in {a.movies_count} movies' for a in actors)

def get_top_rated_awarded_movie() -> str:
    top_movie = (Movie.objects.select_related('starring_actor')
             .prefetch_related('actors')
             .filter(is_awarded=True)
             .order_by('-rating', 'title')
             .first()
    )

    if not top_movie:
        return ''

    starring_actor = top_movie.starring_actor.full_name if top_movie.starring_actor else 'N/A'
    actors = (top_movie.actors.order_by('full_name')
              .values_list('full_name', flat=True))
    cast = ', '.join(actors)

    return (f"Top rated awarded movie: {top_movie.title}, "
            f"rating: {top_movie.rating:.1f}. "
            f"Starring actor: {starring_actor}. "
            f"Cast: {cast}.")

def increase_rating() -> str:
    movies_to_update = Movie.objects.filter(is_classic=True, rating__lt=10)

    if not movies_to_update:
        return "No ratings increased."

    updated_movies_count = movies_to_update.count()

    movies_to_update.update(rating=F('rating') + 0.1)

    return f"Rating increased for {updated_movies_count} movies."
