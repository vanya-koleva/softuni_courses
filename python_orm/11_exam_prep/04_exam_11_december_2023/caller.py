import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Q, Count

from main_app.models import TennisPlayer, Tournament, Match


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

def get_tournaments_by_surface_type(surface=None) -> str:
    if surface is None:
        return ""

    tournaments = (Tournament.objects.prefetch_related(
        'matches'
    ).annotate(
        num_matches=Count('matches')
    ).filter(
        surface_type__icontains=surface
    ).order_by(
        '-start_date'
    ))

    if not tournaments:
        return ""

    return "\n".join(f"Tournament: {t.name}, "
                     f"start date: {t.start_date}, "
                     f"matches: {t.num_matches}"
                     for t in tournaments)

def get_latest_match_info() -> str:
    match = Match.objects.prefetch_related(
        'players'
    ).order_by(
        'date_played', 'id'
    ).last()

    if match is None:
        return ""

    players = match.players.order_by('full_name')
    player1_full_name = players.first().full_name
    player2_full_name = players.last().full_name
    winner_full_name = match.winner.full_name if match.winner else "TBA"

    return (f"Latest match played on: {match.date_played}, "
            f"tournament: {match.tournament.name}, "
            f"score: {match.score}, "
            f"players: {player1_full_name} vs {player2_full_name}, "
            f"winner: {winner_full_name}, "
            f"summary: {match.summary}")

def get_matches_by_tournament(tournament_name=None) -> str:
    if tournament_name is None:
        return "No matches found."

    matches = Match.objects.select_related(
        'tournament', 'winner'
    ).filter(
        tournament__name=tournament_name
    ).order_by(
        '-date_played'
    )

    if not matches:
        return "No matches found."

    return "\n".join(
        f"Match played on: {m.date_played}, "
        f"score: {m.score}, "
        f"winner: {m.winner.full_name if m.winner else 'TBA'}"
        for m in matches
    )
