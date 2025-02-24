# Data Operations in Django with Queries

## Django QuerySet

-   A collection of queries to the database that correspond to the data we want to access.

-   The data is not retrieved until we explicitly request it.

-   Acts as an intermediary between the Python code and the database.

```python
cars = Cars.objects.all()  # <QuerySet []>

print(cars)  # <QuerySet [Car object(1)]>
```

-   **Lazy Evaluation** - The query is not sent to the database until the data is actually needed.
-   **Retrieving Objects**
-   **Chaining**

```python
MyModel.objects.filter(category='electronics').filter(price__lt=1000)
```

-   **Querying Related Objects** - Allows searching in related tables using the model.
-   **Ordering**

```python
ordered_objects = Product.objects.order_by('-price')
```

-   **Pagination**

```python
 from django.core.paginator import Paginator

  # Paginate queryset with 10 objects per page
  paginator = Paginator(queryset, per_page=10)
  page_number = 2
  print([x for x in paginator.get_page(2)])
```

## Object Manager

-   A special class attribute of the maodel used for database interaction.

-   Responsible for CRUD operations.

-   By default, every Django model has a built-in manager called `objects`.

-   Translates our Python code into SQL and returns a **QuerySet**.

-   **Custom Manager**: A subclass of `models.Manager`.

-   Why use custom managers?
    -   **Encapsulating** common or complex queries.
    -   Improved code **readability**.
    -   Avoiding repetition and enhancing **reusability**.
    -   **Modifying** query sets according to specific needs.

## Common Object Manager Methods

-   `.all()`

-   `.first()` - Returns the first record as an **object**. No lazy evaluation.

```python
first = Employee.objects.get(id=1)
```

-   `.last()`

-   `.get(**kwargs)` - Returns a **single object** that matches the **given argument** (must be given some).

    -   It must be able to return only one object.

    -   If multiple objects are found it will throw a **Model.MultipleObjectsReturned** error.

    -   If it doesn't find any object, it raises a **Model.DoesNotExist** exception.

-   `.create(**kwargs)`

-   `.filter(**kwargs)`

-   `.exclude(**kwargs)` - Returns a queryset containing objects that do not match the given arguments.

-   `.order_by(*fields)`

```python
all = Employee.objects.filter(gender='Female').order_by('-salary', 'id')
```

-   `.delete()` - Immediately deletes the object/s from the database.
    -   You should explicitly request the object.
    -   The method returns:
        -   The number of objects deleted.
        -   The number of deletions per object type.
    -   When deleting an object with foreign keys, it will follow the behavior of the SQL constraint ON DELETE.

Note:

-   If you instantiate or modify an object manually, you must call .save() to send it to the database. Otherwise, the change remains only in Python memory.

## Django Shell and SQL Logging

-   **Django Shell**
    -   Provides access to the whhole project

```bash
python manage.py shell
```

```python
# Import the necessary models
from main_app.models import Employee

all_employees = Employee.objects.all()
```

-   **SQL Logging**
    -   Provides details about the executed SQL query and execution time.
    -   Add to settings.py:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',  # Other levels CRITICAL, ERROR, WARNING, INFO, DEBUG
    },
    'loggers': {
        'django.db.backends': {  # responsible for the sql logs
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
```

