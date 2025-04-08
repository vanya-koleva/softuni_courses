# SQL Alchemy

## Overview

-   SQL Alchemy - ORM - Object Relational Mapper

    -   **ORM** - an abstraction that allows us to write SQL using Python.

        -   Optional and can be used independently.

    -   **Core** - handles transactions, sending queries, sessions, and database pooling.

        -   **Engine** - manages DB connections and dialects.

        -   **SQL Expression Language** - builds SQL queries in Python.

        -   **Session** – manages object-level DB interactions.

## SetUp:

```bash
pip install sqlalchemy
pip install psycopg2
```

Import required modules:

```python
# main.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
```

Create a database connection:

```python
# main.py
DATABASE_URL =
'postgresql+psycopg2://your_username:your_password@your_host
/your_database'
engine = create_engine(DATABASE_URL)
```

## Models

-   Similar to Django, we inherit from a base class, `Base`, which we get by calling `declarative_base()`.

```python

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
```

## Migrations

### SetUp

-   Not included in SQLAlchemy; we can use **Alembic**.

-   `pip install alembic`

-   `alembic init alembic` - creates the folder structure for migrations.

-   `sqlalchemy.url = postgresql+psycopg2://username:password@localhost/db_name` – in the `alembic.ini` file.

-   `target_metadata = Base.metadata` – in the `env.py` file, so we can support autogenerate.

### Commands

-   `alembic revision --autogenerate -m "Add User Table"` – creates a migration with a message, similar to `makemigrations`.

-   `alembic upgrade head` – applies the migrations, like `migrate`.

-   `alembic downgrade -1` – rolls back one migration.

## CRUD

-   We open a connection to the database by starting a new session.

-   We always close the session after finishing our work.

-   We need to commit the result, similar to Django where we used `save()`.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session() # be careful when using this

with Session() as session: # a good practice
...
```

### Add

```python
with Session() as session:
    new_user = User(username='john_doe', email='john@example.com')
    session.add(new_user)
    session.commit()
```

### Query

```python
users = session.query(User).all()
```

### Update

```python

with engine.connect() as connection:
  # Create an update object
  upd = update(User).where(User.name == 'John').values(nickname='new_nickname')

  # Execute the update
  connection.execute(upd)
```

or

```python
session.query(User).filter(User.name == 'John').update({"nickname": "new_nickname"}, synchronize_session=False)
session.commit()
```

### Delete

```python
del_stmt = delete(User).where(User.name == 'John')
```

## Transactions

-   `session.begin()`

-   `session.commit()`

-   `session.rollback()`

```py
from main import Session
from models import User

# Start a session
session = Session()

try:
    # Begin a transaction
    session.begin()

    # Perform database operations within the transaction
    ...

    # Commit the transaction
    session.commit()

except Exception as e:
    # Rollback the transaction if an exception occurs
    session.rollback()
    print("An error occurred:", str(e))

finally:
    # Close the session
    session.close()
```

## Relations

### Many to One

```py
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
```

### One to One

-   `uselist=false`

```py
class User(Base):
 __tablename__ = 'users'
 id = Column(Integer, primary_key=True)
 profile = relationship("UserProfile", back_populates="user", uselist=False)

class UserProfile(Base):
 __tablename__ = 'profiles'
 id = Column(Integer, primary_key=True)
 user_id = Column(Integer, ForeignKey('users.id'))
 user = relationship("User", back_populates="profile")
```

### Many to many

```py
user_group_association = Table('user_group', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('group_id', Integer, ForeignKey('groups.id'))
)

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    users = relationship("User", secondary=user_group_association, back_populates="groups")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    groups = relationship("Group", secondary=user_group_association, back_populates="users")
```

## Database Pooling

-   A technique used to efficiently manage and reuse database connections.

-   Instead of opening and closing a new database connection for every request or operation, a connection pool maintains a set of pre-established database connections that can be reused.

-   `engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)` – sets the initial number of connections and the maximum number that can be created.

## Django ORM vs SQLAlchemy

| Django ORM                                          | SQLAlchemy                                          |
| --------------------------------------------------- | --------------------------------------------------- |
| Tightly integrated with the Django web framework    | A standalone library that can be used independently |
| High-Level Abstraction                              | Lower-Level Control                                 |
| Built-in Migration System                           | No Built-in Migration Capabilities (uses Alembic)   |
| Powerful Admin Interface                            | No Built-in Admin Interface                         |
| Authentication and Authorization built-in           | Not included                                        |
| Primarily single DB per project (multi-DB possible) | Built-in support for multiple databases             |

