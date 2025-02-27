import os
from typing import List

import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout
from main_app.choices import OperationSystemChoices, MealTypeChoices, DungeonDifficultyChoices, WorkoutTypeChoices
from django.db.models import Case, When, Value, QuerySet


def show_highest_rated_art() -> str:
    artwork = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f"{artwork.art_name} is the highest-rated art with a {artwork.rating} rating!"

def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    ArtworkGallery.objects.bulk_create([first_art, second_art])

def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()

def show_the_most_expensive_laptop() -> str:
    laptop = Laptop.objects.order_by('-price', '-id').first()
    return f"{laptop.brand} is the most expensive laptop available for {laptop.price}$!"

def bulk_create_laptops(args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(args)

def update_to_512_GB_storage() -> None:
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)

def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=["Apple", "Acer", "Dell"]).update(memory=16)

def update_operation_systems() -> None:
    Laptop.objects.update(
        operation_system=Case(
            When(brand="Asus", then=Value(OperationSystemChoices.WINDOWS)),
            When(brand="Apple", then=Value(OperationSystemChoices.MACOS)),
            When(brand__in=["Dell", "Acer"], then=Value(OperationSystemChoices.LINUX)),
            When(brand="Lenovo", then=Value(OperationSystemChoices.CHROME_OS))
        )
    )

def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()

def bulk_create_chess_players(args: List[ChessPlayer]) -> None:
    ChessPlayer.objects.bulk_create(args)

def delete_chess_players() -> None:
    ChessPlayer.objects.filter(title="no title").delete()

def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(title="GM").update(games_won=30)

def change_chess_games_lost() -> None:
    ChessPlayer.objects.filter(title="no title").update(games_lost=25)

def change_chess_games_drawn() -> None:
    ChessPlayer.objects.update(games_drawn=10)

def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")

def grand_chess_title_IM() -> None:
    ChessPlayer.objects.filter(rating__range=[2300, 2399]).update(title="IM")

def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(rating__range=[2200, 2299]).update(title="FM")

def grand_chess_title_regular_player() -> None:
    ChessPlayer.objects.filter(rating__range=[0, 2199]).update(title="regular player")

def set_new_chefs() -> None:
    Meal.objects.update(
        chef=Case(
            When(meal_type=MealTypeChoices.BREAKFAST, then=Value("Gordon Ramsay")),
            When(meal_type=MealTypeChoices.LUNCH, then=Value("Julia Child")),
            When(meal_type=MealTypeChoices.DINNER, then=Value("Jamie Oliver")),
            When(meal_type=MealTypeChoices.SNACK, then=Value("Thomas Keller")),
        )
    )

def set_new_preparation_times() -> None:
    Meal.objects.update(
        preparation_time=Case(
            When(meal_type=MealTypeChoices.BREAKFAST, then=Value("10 minutes")),
            When(meal_type=MealTypeChoices.LUNCH, then=Value("12 minutes")),
            When(meal_type=MealTypeChoices.DINNER, then=Value("15 minutes")),
            When(meal_type=MealTypeChoices.SNACK, then=Value("5 minutes")),
        )
    )

def update_low_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=[MealTypeChoices.BREAKFAST, MealTypeChoices.DINNER]).update(calories=400)

def update_high_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=[MealTypeChoices.LUNCH, MealTypeChoices.SNACK]).update(calories=700)

def delete_lunch_and_snack_meals() -> None:
    Meal.objects.filter(meal_type__in=[MealTypeChoices.LUNCH, MealTypeChoices.SNACK]).delete()

def show_hard_dungeons() -> str:
    hard_dungeons = Dungeon.objects.filter(
        difficulty=DungeonDifficultyChoices.HARD
    ).order_by('-location')

    return "\n".join(
        f"{d.name} is guarded by {d.boss_name} who has {d.boss_health} health points!"
        for d in hard_dungeons
    )

def bulk_create_dungeons(args: List[Dungeon]) -> None:
    Dungeon.objects.bulk_create(args)

def update_dungeon_names() -> None:
    Dungeon.objects.update(
        name=Case(
            When(difficulty=DungeonDifficultyChoices.EASY, then=Value("The Erased Thombs")),
            When(difficulty=DungeonDifficultyChoices.MEDIUM, then=Value("The Coral Labyrinth")),
            When(difficulty=DungeonDifficultyChoices.HARD, then=Value("The Lost Haunt"))
        )
    )

def update_dungeon_bosses_health() -> None:
    Dungeon.objects.exclude(difficulty=DungeonDifficultyChoices.EASY).update(boss_health=500)

def update_dungeon_recommended_levels() -> None:
    Dungeon.objects.update(
        recommended_level=Case(
            When(difficulty=DungeonDifficultyChoices.EASY, then=Value(25)),
            When(difficulty=DungeonDifficultyChoices.MEDIUM, then=Value(50)),
            When(difficulty=DungeonDifficultyChoices.HARD, then=Value(75)),
        )
    )

def update_dungeon_rewards() -> None:
    Dungeon.objects.filter(boss_health=500).update(reward="1000 Gold")
    Dungeon.objects.filter(location__startswith="E").update(reward="New dungeon unlocked")
    Dungeon.objects.filter(location__endswith="s").update(reward="Dragonheart Amulet")

def set_new_locations() -> None:
    Dungeon.objects.update(
        location=Case(
            When(recommended_level=25, then=Value("Enchanted Maze")),
            When(recommended_level=50, then=Value("Grimstone Mines")),
            When(recommended_level=75, then=Value("Shadowed Abyss")),
        )
    )

def show_workouts() -> str:
    workouts = Workout.objects.filter(
        workout_type__in=[WorkoutTypeChoices.CALISTHENICS, WorkoutTypeChoices.CROSS_FIT]
    ).order_by("id")

    return "\n".join(f"{w.name} from {w.workout_type} type has {w.difficulty} difficulty!" for w in workouts)

def get_high_difficulty_cardio_workouts() -> QuerySet:
    return Workout.objects.filter(workout_type=WorkoutTypeChoices.CARDIO, difficulty="High").order_by("instructor")

def set_new_instructors() -> None:
    Workout.objects.update(
        instructor=Case(
            When(workout_type=WorkoutTypeChoices.CARDIO, then=Value("John Smith")),
            When(workout_type=WorkoutTypeChoices.STRENGTH, then=Value("Michael Williams")),
            When(workout_type=WorkoutTypeChoices.YOGA, then=Value("Emily Johnson")),
            When(workout_type=WorkoutTypeChoices.CROSS_FIT, then=Value("Sarah Davis")),
            When(workout_type=WorkoutTypeChoices.CALISTHENICS, then=Value("Chris Heria")),
        )
    )

def set_new_duration_times() -> None:
    Workout.objects.update(
        duration=Case(
            When(instructor="John Smith", then=Value("15 minutes")),
            When(instructor="Sarah Davis", then=Value("30 minutes")),
            When(instructor="Chris Heria", then=Value("45 minutes")),
            When(instructor="Michael Williams", then=Value("1 hour")),
            When(instructor="Emily Johnson", then=Value("1 hour and 30 minutes")),
        )
    )

def delete_workouts() -> None:
    Workout.objects.exclude(workout_type__in=[WorkoutTypeChoices.CALISTHENICS, WorkoutTypeChoices.STRENGTH]).delete()
