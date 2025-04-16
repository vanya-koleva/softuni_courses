from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()   # same as models.Model

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        nullable=False,
    )

    ingredients = Column(
        Text,
        nullable=False,
    )

    instructions = Column(
        Text,
        nullable=False,
    )