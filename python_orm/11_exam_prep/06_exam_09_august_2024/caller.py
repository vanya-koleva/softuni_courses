import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Q, Count
from main_app.models import House, Dragon


def get_houses(search_string=None) -> str:
    if not search_string:
        return  "No houses match your search."

    houses = House.objects.filter(
        Q(name__istartswith=search_string)
            |
        Q(motto__istartswith=search_string)
    ).order_by(
        "-wins",
        "name",
    )

    if not houses:
        return  "No houses match your search."

    return "\n".join(f"House: {h.name}, wins: {h.wins}, "
                     f"motto: {h.motto if h.motto else 'N/A'}"
                     for h in houses)

def get_most_dangerous_house() -> str:
    house = House.objects.get_houses_by_dragons_count().first()

    if not house or house.num_dragons == 0:
        return "No relevant data."

    return (f"The most dangerous house is the House of {house.name} "
            f"with {house.num_dragons} dragons. "
            f"Currently {'ruling' if house.is_ruling else 'not ruling'} the kingdom.")

def get_most_powerful_dragon() -> str:
    dragon = Dragon.objects.filter(
        is_healthy=True
    ).order_by(
        "-power", "name"
    ).first()

    if not dragon:
        return "No relevant data."

    num_quests = dragon.quests.count()

    return (f"The most powerful healthy dragon is {dragon.name} "
            f"with a power level of {dragon.power:.1f}, breath type {dragon.breath}, "
            f"and {dragon.wins} wins, coming from the house of {dragon.house.name}. "
            f"Currently participating in {num_quests} quests.")
