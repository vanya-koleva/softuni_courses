"""
# STEPS

1. pip install sqlalchemy
2. pip install alembic
3. pip install psycopg2-binary
4. Create a database
5. Create file for models
6. Create the Base class
7. alembic init alembic
8. Tell alembic which is our base model target_metadata = Base.metadata
9. Tell alembic how to connect to the db - sqlalchemy.url = postgresql+psycopg2://postgres:admin@localhost/sql_alchemy_exercise

"""
from typing import List, Type

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helpers import handle_session
from models import Recipe

engine = create_engine('postgresql+psycopg2://postgres-user:password@localhost/sql_alchemy_exercise')
Session = sessionmaker(bind=engine)
session = Session()


@handle_session(session)
def create_recipe(name: str, ingredients: str, instructions: str) -> None:
    new_recipe = Recipe(
        name=name,
        ingredients=ingredients,
        instructions=instructions,
    )

    session.add(new_recipe) # new_recipe.save()


@handle_session(session)
def update_recipe_by_name(name: str, new_name: str,  new_ingredients: str, new_instructions: str) -> None:
    session.query(Recipe).filter_by(name=name).update({
        Recipe.name: new_name,
        Recipe.ingredients: new_ingredients,
        Recipe.instructions: new_instructions,
    })


@handle_session(session)
def delete_recipe_by_name(name: str) -> None:
    session.query(Recipe).filter_by(name=name).delete()


@handle_session(session, autoclose=False)
def get_recipes_by_ingredient(ingredient_name: str) -> List[Type[Recipe]]:
    return session.query(Recipe).filter(
        Recipe.ingredients.ilike(f"%{ingredient_name}%"),
    ).all()


@handle_session(session)
def swap_recipe_ingredients_by_name(first_recipe_name: str, second_recipe_name: str) -> None:
    first_recipe = (
        session.query(Recipe)
        .filter_by(name=first_recipe_name)
        .with_for_update()  # locks the record preventing others to modify it until it's modified
        .one()
    )
    second_recipe = (
        session.query(Recipe)
        .filter_by(name=second_recipe_name)
        .with_for_update()
        .one()
    )

    first_recipe.ingredients, second_recipe.ingredients = second_recipe.ingredients, first_recipe.ingredients
