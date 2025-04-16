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