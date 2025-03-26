import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Astronaut
from django.db.models import Q, Count


def get_astronauts(search_string=None) -> str:
    if search_string is None:
        return ""

    astronauts = Astronaut.objects.filter(
        Q(name__icontains=search_string)
            |
        Q(phone_number__icontains=search_string)
    ).order_by(
        'name'
    )

    if len(astronauts) == 0:
        return ""

    return "\n".join(
        f"Astronaut: {a.name}, "
        f"phone number: {a.phone_number}, "
        f"status: {'Active' if a.is_active else 'Inactive'}"
        for a in astronauts
    )

def get_top_astronaut() -> str:
    astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()

    if astronaut is None or astronaut.missions_count == 0:
        return "No data."

    return f"Top Astronaut: {astronaut.name} with {astronaut.missions_count} missions."

def get_top_commander() -> str:
    commander = Astronaut.objects.annotate(
        commanded_missions_count=Count('commanded_missions')
    ).order_by(
        '-commanded_missions_count',
        'phone_number',
    ).first()

    if commander is None or commander.commanded_missions_count == 0:
        return "No data."

    return (f"Top Commander: {commander.name} with "
            f"{commander.commanded_missions_count} commanded missions.")
