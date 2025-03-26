import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Astronaut, Mission, Spacecraft
from django.db.models import Q, Count, Sum, F, Avg
from main_app.choices import MissionStatusChoices


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

def get_last_completed_mission() -> str:
    mission = (Mission.objects.filter(
        status=MissionStatusChoices.COMPLETED,
    ).select_related(
        'spacecraft', 'commander'
    ).prefetch_related(
        'astronauts'
    ).order_by(
        'launch_date'
    ).last())

    if not mission:
        return "No data."

    commander_name = mission.commander.name if mission.commander else 'TBA'
    astronauts = mission.astronauts.all().order_by('name')
    astronauts_names = ", ".join(a.name for a in astronauts)
    total_spacewalks = astronauts.aggregate(total=Sum('spacewalks'))['total']

    return (f"The last completed mission is: {mission.name}. "
            f"Commander: {commander_name}. "
            f"Astronauts: {astronauts_names}. "
            f"Spacecraft: {mission.spacecraft.name}. "
            f"Total spacewalks: {total_spacewalks}.")

def get_most_used_spacecraft() -> str:
    spacecraft = Spacecraft.objects.annotate(
        num_missions=Count('missions', distinct=True),
        num_astronauts=Count('missions__astronauts', distinct=True),
    ).order_by(
        '-num_missions',
        'name'
    ).first()

    if not spacecraft or spacecraft.num_missions == 0:
        return "No data."

    return (f"The most used spacecraft is: {spacecraft.name}, "
            f"manufactured by {spacecraft.manufacturer}, "
            f"used in {spacecraft.num_missions} missions, "
            f"astronauts on missions: {spacecraft.num_astronauts}.")

def decrease_spacecrafts_weight() -> str:
    num_spacecrafts = Spacecraft.objects.filter(
        missions__status=MissionStatusChoices.PLANNED,
        weight__gte=200.0,
    ).distinct().update(
        weight=F('weight') - 200.0
    )

    if num_spacecrafts == 0:
        return "No changes in weight."

    avg_weight = Spacecraft.objects.aggregate(
        avg=Avg('weight')
    )['avg']

    return (f"The weight of {num_spacecrafts} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {avg_weight:.1f}kg")
