import os
from decimal import Decimal

import django
from django.db.models import QuerySet, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# from helpers import populate_model_with_data
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character
from main_app.choices import RoomTypeChoices, CharacterTypeChoices


# Create queries within functions
def create_pet(name: str, species: str) -> str:
    pet = Pet.objects.create(
        name=name,
        species=species
    )
    return f"{pet.name} is a very cute {pet.species}!"

def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    return f"The artifact {artifact.name} is {artifact.age} years old!"

def rename_artifact(artifact: Artifact, new_name: str) -> None:
    """
    UPDATE main_app_artifact
    SET name = new_name
    WHERE is_magical AND age > 250
    """
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()

def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()

def show_all_locations() -> str:
    locations = Location.objects.all().order_by("-id")

    return "\n".join(f"{l.name} has a population of {l.population}!" for l in locations)

def new_capital() -> None:
    location = Location.objects.first()
    location.is_capital = True
    location.save()

def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values("name")

def delete_first_location() -> None:
    Location.objects.first().delete()

def apply_discount() -> None:
    cars = Car.objects.all()

    for car in cars:
        percentage_off = Decimal(str(sum(int(digit) for digit in str(car.year)) / 100))
        discount = car.price * percentage_off
        car.price_with_discount = car.price - discount

    Car.objects.bulk_update(cars, ["price_with_discount"])

def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gt=2020).values("model", "price_with_discount")

def delete_last_car() -> None:
    Car.objects.last().delete()

def show_unfinished_tasks() -> str:
    tasks = Task.objects.filter(is_finished=False)
    return "\n".join(
        f"Task - {t.title} needs to be done until {t.due_date}!"
        for t in tasks
    )

def complete_odd_tasks() -> None:
    tasks = Task.objects.all()
    completed_tasks = []

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True
            completed_tasks.append(task)

    Task.objects.bulk_update(completed_tasks, ["is_finished"])

def encode_and_replace(text: str, task_title: str) -> None:
    encoded_text = "".join(chr(ord(c) - 3) for c in text)
    Task.objects.filter(title=task_title).update(description=encoded_text)

def get_deluxe_rooms() -> str:
    deluxe_rooms = HotelRoom.objects.filter(room_type=RoomTypeChoices.DELUXE)
    even_rooms = []

    for room in deluxe_rooms:
        if room.id % 2 == 0:
            even_rooms.append(room)

    return "\n".join(
        f"Deluxe room with number {r.room_number} costs {r.price_per_night}$ per night!"
        for r in even_rooms
    )

def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.filter(is_reserved=True).order_by("id")
    previous_room = None

    for room in rooms:
        if previous_room:
            room.capacity += previous_room.capacity
        else:
            room.capacity += room.id

        previous_room = room

        room.save()

def reserve_first_room() -> None:
    room = HotelRoom.objects.first()

    room.is_reserved = True
    room.save()

def delete_last_room() -> None:
    room = HotelRoom.objects.last()

    if not room.is_reserved:
        room.delete()

def update_characters() -> None:
    Character.objects.filter(class_name=CharacterTypeChoices.MAGE).update(
        level=F("level") + 3,
        intelligence=F("intelligence") - 7,
    )

    Character.objects.filter(class_name=CharacterTypeChoices.WARRIOR).update(
        hit_points=F("hit_points") / 2,
        dexterity=F("dexterity") + 4,
    )

    Character.objects.filter(class_name__in=[CharacterTypeChoices.ASSASSIN, CharacterTypeChoices.SCOUT]).update(
        inventory="The inventory is empty",
    )

def fuse_characters(first_character: Character, second_character: Character) -> None:
    fused_inventory = None
    if first_character.class_name in [CharacterTypeChoices.MAGE, CharacterTypeChoices.SCOUT]:
        fused_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    elif first_character.class_name in [CharacterTypeChoices.WARRIOR, CharacterTypeChoices.ASSASSIN]:
        fused_inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=f"{first_character.name} {second_character.name}",
        class_name=CharacterTypeChoices.FUSION,
        level=(first_character.level + second_character.level) // 2,
        strength=(first_character.strength + second_character.strength) * 1.2,
        dexterity=(first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence=(first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points=(first_character.hit_points + second_character.hit_points),
        inventory=fused_inventory,
    )

    first_character.delete()
    second_character.delete()

def grand_dexterity() -> None:
    Character.objects.all().update(dexterity=30)

def grand_intelligence() -> None:
    Character.objects.all().update(intelligence=40)

def grand_strength() -> None:
    Character.objects.all().update(strength=50)

def delete_characters() -> None:
    Character.objects.filter(inventory="The inventory is empty").delete()
