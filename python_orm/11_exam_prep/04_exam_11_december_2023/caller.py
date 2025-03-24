import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Q, Count

from main_app.models import TennisPlayer


def get_tennis_players(search_name=None, search_country=None) -> str:
    if search_name is None and search_country is None:
        return ""

    query_name = Q(full_name__icontains=search_name)
    query_country = Q(country__icontains=search_country)

    if search_name is not None and search_country is not None:
        query = Q(query_name & query_country)
    elif search_name is not None:
        query = query_name
    else:
        query = query_country

    players = TennisPlayer.objects.filter(query).order_by('ranking')

    if not players.exists():
        return ""

    return '\n'.join(
        f"Tennis Player: {p.full_name}, "
        f"country: {p.country}, "
        f"ranking: {p.ranking}"
        for p in players
    )

def get_top_tennis_player() -> str:
    top_player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    if top_player is None:
        return ""

    return (f"Top Tennis Player: {top_player.full_name} "
            f"with {top_player.wins_count} wins.")

def get_tennis_player_by_matches_count() -> str:
    player = TennisPlayer.objects.annotate(
        num_of_matches=Count('matches')
    ).order_by(
        '-num_of_matches', 'ranking'
    ).first()

    if player is None or player.num_of_matches == 0:
        return ""

    return (f"Tennis Player: {player.full_name} "
            f"with {player.num_of_matches} matches played.")
