# Advanced Queries in Django

## Custom Managers

-   In Django, a manager is an interface through which **all database query operations** are performed.

-   By default, Django provides a manager called objects for every model.

-   We can use custom managers to extract business logic for frequently used queries in one place.

-   We do this by inheriting from the default manager `models.Manager`.

-   Created in managers.py

```python
class EmployeeManager(models.Manager):
    def by_job_title(self, job_title):
        # Access to filter through self, because self is objects
        return self.filter(job_title=job_title)

class Employee(models.Model):
    ...
    # Attach the custom manager to the Employee model
    objects = EmployeeManager()

# Calling the custom manager's method
print(Employee.objects.by_job_title("Software Engineer"))
```

## Aggregation

-   `aggregate()` - Returns a single value or multiple computed values as a dictionary.

-   It calculates values over the **entire** table, not over a record.

-   It does not group results like SQL’s GROUP BY; instead, it computes aggregates for the entire dataset.

-   Returns a **dict**.

-   Used for totals, averages, min/max values.

```python
result = Employee.objects.aggregate(
    total_employees=Count('id'),
    max_experience=Max('years_of_experience')
)
# Result: {'total_employees': 6, 'max_experience': 8}
```

## Annotation

-   `annotate()` – We use it to add new fields to the returned result, often based on some calculations.

-   Returns a **QuerySet**.

-   Using values() groups by the selected fields, and then annotate() computes aggregates for each group.

```python
# Annotating the queryset to get the count of books for each author
authors_with_book_count = Book.objects.values('author').annotate(book_count=Count('id'))
# `values('author')` → Groups the results by the author field.
# annotate(book_count=Count('id')) → Counts the number of books (id) for each author.
```

Example output:

```python
[
    {'author': 'J.K. Rowling', 'book_count': 7},
    {'author': 'George Orwell', 'book_count': 3}
]
```

## Queries for Model Relationships

-   Used to **optimize** database queries when dealing with **related** objects in our models.

-   **`select_related`** – Optimizes queries for **One-To-One** and **Many-To-One** relationships by using **SQL JOINs**.

    -   Instead of making **separate queries** for each related object, Django fetches all necessary data in **one query**, reducing database hits.

    -   ✅ `ForeignKey` & `OneToOneField`

    -   ✅ Child --> Parent

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

books_with_authors = Book.objects.select_related('author')
# SELECT * FROM "myapp_book" JOIN "myapp_author" ON ("myapp_book"."author_id" = "myapp_author"."id")
```

-   **`prefetch_related`** – Optimizes queries for **Many-To-Many** and **reverse ForeignKey** relationships by using **separate queries**, then linking the results in Python.

    -   **A fixed number of queries (relations + 1)**.

    -   ✅ `ManyToManyField` & `related_name`/`modelname_set`

    -   Parent --> Child

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

authors_with_books = Author.objects.prefetch_related('book_set')

# 1. SELECT * FROM "myapp_author"
# 2. SELECT * FROM "myapp_book" INNER JOIN "myapp_book_authors" ON ("myapp_book"."id" = "myapp_book_authors"."book_id")
```

## Query-related Tools

-   **Q object** - used to leverage the full potential of Boolean logic in queries.

    -   Used with filtrations.

    -   **`&`** - AND
    -   **`|`** - OR
    -   **`~`** - NOT
    -   **`^`** - XOR

```python
q = Q(title__icontains='Django') & (Q(pub_year__gt=2010) | Q(author='John Doe'))

books = Book.objects.filter(q)
```

-   **F object** - reference a field's value in a query expression.

    -   Does not fetch the values from the database into Python memory. Instead, all operations happen directly at the SQL level **inside the database**.

```python
from django.db.models import F

Book.objects.update(rating=F('rating') + 1)
```

-   Using F object for a more complex query:

```python
employees_above_avg_salary = Employee.objects.annotate(
    avg_department_salary=Avg('department__employees__salary')
).filter(salary__gt=F('avg_department_salary'))
```

## Debugging Queries

-   Debugging tools are invaluable during development, you should **avoid** using them in **production** environments due to security concerns and performance overhead.

```python
from django.db import connection, reset_queries

print(connection.queries) # All queries

reset_queries() # Resets the list of queries
```

-   **Django Debug Toolbar**

    -   [Installation](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

-   **Silk**

-   **django-querycount**

-   **django-extensions**

    -   `pip install django-extensions`

    -   Add 'django_extensions' to your INSTALLED_APPS list in your project's settings.

    -   Offers various other utilities such as graph generation, template rendering, and more.

    -   [Reference](https://django-extensions.readthedocs.io/en/latest/command_extensions.html)

-   **Shell Plus**

    -   `python manage.py shell_plus`

    -   Automatically imports your models and commonly used packages.

    -   Printing SQL queries with execution time: `python manage.py shell_plus --print-sql`

