# Django Migrations and Django Admin

## Django Migrations Advanced

-   Migrations are essential for managing changes in database schemas over time.

-   Help us build upon changes in our models.

-   Allow us to preserve previous states of our database.

-   Migration files are normal Python files with an agreed-upon object layout, written in a declarative style

-   To **apply** all migrations from all apps:

```bash
python manage.py migrate
```

-   To apply migrations **from one app**:

```bash
python manage.py migrate app_name
```

-   To apply **specific** migration:

```bash
python manage.py migrate app_name 0001
```

-   To **reverse** to a certain migration:

```bash
python manage.py migrate app_name 0001
```

-   To reverse **all** migrations:

```bash
python manage.py migrate app_name zero
```

-   A migration is irreversible if it contains any irreversible operations. Attempting to reverse such migrations will raise IrreversibleError.

-   The affected existing records disappear when we reverse a migration.

-   To **list** all migrations with their statuses:

```bash
python manage.py showmigrations
```

-   To list migrations **for a certain app**:

```bash
python manage.py showmigrations app_name
```

-   **Squashing** - Reducing an existing set of many migrations down to one (or sometimes a few) migrations which still represent the same changes. Django also optimizes the migration.

```bash
python manage.py squashmigrations app_name 0238
```

\*In the example, all migrations until 0238 will be squashed. 0238 is the last migration that will be included in the squashed file.

-   We cannot revert to a squashed migration.

-   Print the SQL for a given migration:

```bash
python manage.py sqlmigrate app_name 0001
```

## Custom / Data Migrations

-   Data Migrations - migrations that alter data.

-   Django cannot automatically generate Data Migrations.

-   Best written as separate migrations, sitting alongside your schema migrations.

-   When using Django ORM to insert data, you typically need to create **instances** of a model rather than inserting raw values.

-   Sometimes these migrations cannot squash well and should be squashed manually.

-   **Usage**:

    -   Rename a field and change the data type.
    -   Functions, procedures, triggers.
    -   When, for example, we add a new field and want to populate it with data based on already existing fields.

-   Create an empty migration:

```bash
python manage.py makemigrations --empty app_name
```

\*This way Django will put the file in the right place, suggest a name, and add dependencies.

-   `RunPython` expects a function. It is best to pass to it two functions - one for the code to be done, and one with reverse code in case we want to undo the cahnge.

-   The functions take **two arguments**:

    -   **apps** - A record of the database before the migration.

    -   **schema_editor** - A class that converts our Python code into SQL. We use it when creating, altering, or deleting a table.
        -   When using RunPython, in 95% of cases, we won’t need to use the Schema Editor, except when dealing with temporary tables, indexes, or schema changes.

-   If the reverse code is omitted, migrating backwards will raise an exception.

-   When writing a RunPython function that uses models from apps other than the one in which the migration is located, the migration’s dependencies attribute should include the latest migration of each app that is involved.

-   Example of the use of the Schema Editor:

```python
from django.db import migrations, models

def create_temporary_table(apps, schema_editor):
    # Get the model class
    Person = apps.get_model('your_app_name', 'Person')

    # Access the SchemaEditor to create a temporary table
    schema_editor.execute(
        "CREATE TEMPORARY TABLE temp_person_data AS SELECT id, first_name, last_name FROM your_app_name_person"
    )

    ...

class Migration(migrations.Migration):

    dependencies = [
        ('your_app_name', 'previous_migration'),
    ]

    operations = [
        migrations.RunPython(create_temporary_table),
    ]
```

## Django Admin Site

-   Built-in admin interface.

-   Create superuser:

```bash
python manage.py createsuperuser
```

-   Models are registered in admin.py:

```python
from django.contrib import admin
from main_app.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
```

-   **\_\_str\_\_()** in the Model class for human-readable representation.

-   **list_display** to display the model fields.

```python
list_display = ["first_name", "last_name", "age", "grade"]
```

-   **list_filter** to add filters to the model.

```python
list_filter = ["age", "grade", "date_of_birth"]
```

-   **search_fields** for a search box with fields that will be searched. Default is all fields.

```python
search_fields = ["first_name"]
```

-   **fields** for layout changes on "Add" and "Change" pages such as showing only a subset of available fields, modifying their order, or grouping them into rows.

```python
class EmployeeAdmin(admin.ModelAdmin):
    fields = [('first_name', 'last_name'), 'email_address']
```

-   **fieldsets** to customize the layout of "Add" and "Change" pages. `fieldsets` is a list of 2-tuples, in which each 2-tuple represents a `section` of the form.

```python
class StudentAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Personal Information", {"fields": ["first_name", "last_name"]}),
        ("Academic Information", {"fields": ["grade"]})
    ]
```

-   **date_hierarchy** to include a date-based drilldown navigation by that field.

```python
date_hierarchy = "birth_date"
```

-   **list_per_page** to control how many items appear on each paginated. Default is 100.

---

## values() vs values_list()

-   **values()** method returns a QuerySet containing dictionaries:

```python
#Syntax:
Model.objects.values('field1', 'field2', ...)

#Returns:
<QuerySet [
    {'field1': 'value', 'field2': 'value'},
    {'field1': 'value', 'field2': 'value'}
]>
```

-   **values_list()** method returns a QuerySet containing tuples:

```python
<QuerySet [('value',), ('value',)]>
<QuerySet [('value1', 'value2'), ('value1', 'value2')]>
```

-   If you are using values_list() with a single field, you can use `flat=True` to return a QuerySet of single values instead of 1-tuples:

```python
<QuerySet ['value', 'value']>
```

Example:

```python
employee_names = Employee.objects.values_list('name', flat=True)

print(employee_names)
# <QuerySet ['Alice', 'Bob']>

print(list(employee_names))
# ['Alice', 'Bob']
```

## F object

-   Used to refer to model field values directly in queries and updates, allowing you to perform database operations without fetching data into Python.

-   Keeps logic inside the database rather than looping in Python.

```python
from django.db.models import F


# UPDATE product SET price = price * 1.1;
Product.objects.update(price=F('price') * 1.1)
```

-   Operators:
    -   `gt` for greater than
    -   `gte` greater than or equal to
    -   `lt` for less than
    -   `lte` less than or equal to
    -   `exact` for equality
    -   `range` for inclusive range

```python
Model.objects.filter(field_name__gt=value)
```

-   Example:

```python
ItemModel.objects.update(
        rarity=Case(
            When(price__lte=10, then=Value('Rare')),
            When(price__lte=20, then=Value('Very Rare')),
            When(price__lte=30, then=Value('Extremely Rare')),
            When(price__gte=31, then=Value('Mega Rare')),
        )
    )
```

## Others

-   Use the **apps.get_model()** method to retrieve the model class:

```python
ShoeModel = apps.get_model('main_app', 'Shoe')
```

-   **bulk_create()**:

    -   Efficiently inserts multiple records into the database at once, avoiding multiple queries.

    -   Expects model instances, not just raw values.

