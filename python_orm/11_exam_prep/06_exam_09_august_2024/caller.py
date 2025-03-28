import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Q, Count, F, Min, Avg
from main_app.models import House, Dragon, Quest


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

def update_dragons_data() -> str:
    num_of_dragons_affected = Dragon.objects.filter(
        is_healthy=False,
        power__gt=Dragon.MIN_POWER,
    ).update(
        power=F("power") - 0.1,
        is_healthy=True,
    )

    if num_of_dragons_affected == 0:
        return "No changes in dragons data."

    min_power = Dragon.objects.aggregate(Min("power"))["power__min"]

    return (f"The data for {num_of_dragons_affected} dragon/s has been changed. "
            f"The minimum power level among all dragons is {min_power:.1f}")

def get_earliest_quest() -> str:
    quest = Quest.objects.order_by("start_time").first()

    if not quest:
        return "No relevant data."

    day = quest.start_time.day
    month = quest.start_time.month
    year = quest.start_time.year

    dragons = quest.dragons.order_by("-power", "name")
    dragons_names = "*".join(d.name for d in dragons)
    avg_power_level = dragons.aggregate(Avg("power"))["power__avg"] or 0

    return (f"The earliest quest is: {quest.name}, "
            f"code: {quest.code}, start date: {day}.{month}.{year}, "
            f"host: {quest.host.name}. Dragons: {dragons_names}. "
            f"Average dragons power level: {avg_power_level:.2f}")

def announce_quest_winner(quest_code) -> str:
    quest = Quest.objects.filter(code__exact=quest_code).first()

    if not quest:
        return "No such quest."

    winning_dragon = quest.dragons.order_by("-power", "name").first()\

    winning_dragon.wins += 1
    winning_dragon.save()

    winning_dragon.house.wins += 1
    winning_dragon.house.save()

    quest.delete()

    return (f"The quest: {quest.name} "
            f"has been won by dragon {winning_dragon.name} "
            f"from house {winning_dragon.house.name}. "
            f"The number of wins has been updated as follows: "
            f"{winning_dragon.wins} total wins for the dragon and "
            f"{winning_dragon.house.wins} total wins for the house. "
            f"The house was awarded with {quest.reward:.2f} coins.")
