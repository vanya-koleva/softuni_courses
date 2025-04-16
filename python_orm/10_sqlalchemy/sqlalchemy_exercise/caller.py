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
