# Django ORM Cheatsheet

## 1. Basics

### Get All Records

```python
ModelName.objects.all()
```

### Create Records

```python
# Create and save instance
ModelName.objects.create(attribute='value', ...)

# Create a new instance without saving immediately
new_record = ModelName(attribute='value', ...)
new_record.save()   # Manually save the record

# Does not call .save().
# Does not work with child models in multi-table inheritance.
# Does not work with many-to-many relationships.
objs = ModelName.objects.bulk_create([
    ModelName(attribute='value1', ...),
    ModelName(attribute='value2', ...),
])
```

### Create Records with Many-to-Many Relationships

```python
# Create objects first
obj = ModelName.objects.create(attribute='value')
obj1 = RelatedModel.objects.create(attribute='value1')
obj2 = RelatedModel.objects.create(attribute='value2')

# Add relationships after saving
obj.many_to_many_field.add(obj1, obj2)
```

### Retrieve a Single Record

```python
# Returns a single object, raises exceptions if no match or multiple matches
ModelName.objects.get(id=1)

#Returns a QuerySet, lazy evaluation
ModelName.objects.filter(...).order_by("id")[:1]

#Returns an object or None
ModelName.objects.filter(...).first()
```

### Filter Records

```python
ModelName.objects.filter(attribute=value)
```

### Exclude Records

```python
ModelName.objects.exclude(attribute=value)
```

### Order Records

```python
#Ascending (default)
ModelName.objects.order_by('attribute')

#Descending
ModelName.objects.order_by('-attribute')
```

### Limit Records

```python
# Index starts from 0
ModelName.objects.all()[:10]
ModelName.objects.all()[5:10]
```

## 2. Field Lookups

```python
# Exact Match / Case-Insensitive Match
ModelName.objects.filter(attribute__exact=value)
ModelName.objects.filter(attribute__iexact=value)

# Contains / Case-Insensitive Contains
ModelName.objects.filter(attribute__contains=value)
ModelName.objects.filter(attribute__icontains=value)

# Greater / Less Than
ModelName.objects.filter(attribute__gt=value)
ModelName.objects.filter(attribute__lt=value)

# Greater / Less Than or Equal To
ModelName.objects.filter(attribute__gte=value)
ModelName.objects.filter(attribute__lte=value)

# Range (Inclusive of both start and end values)
ModelName.objects.filter(attribute__range=(start_value,
end_value))

# In a List
ModelName.objects.filter(attribute__in=[value1, value2])

# Starts / Ends With
ModelName.objects.filter(attribute__startswith=value)
ModelName.objects.filter(attribute__endswith=value)

# Case-insensitive Starts / Ends With
ModelName.objects.filter(attribute__istartswith=value)
ModelName.objects.filter(attribute__iendswith=value)

# Date
ModelName.objects.filter(attribute__date=date(2025, 1, 1))

#__year, __month, __day
ModelName.objects.filter(attribute__year=2025)

# NULL
Models.objects.filter(attribute__isnull=True)
```

## 3. Querying Related Objects

### Filter on Related Fields

```python
ModelName.objects.filter(related_name__field=value)
```

### Related Fields Greater Than

```python
ModelName.objects.filter(related_name__field__gt=value)
```

## 4. Efficiently Querying Related Objects

### `select_related()`

**-to-one** relationships (one-to-one, many-to-one)

Child --> Parent

Less queries are run because it uses JOIN

```python
ModelName.objects.select_related('foreign_key_field')
```

Example:

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

books_with_authors = Book.objects.select_related('author')

# SELECT * (simplified)
# FROM "myapp_book"
# JOIN "myapp_author"
# ON ("myapp_book"."author_id" = "myapp_author"."id")

# Accessing related data without extra queries
for book in books_with_authors:
    print(book.author.name)  # No additional DB queries
```

### `prefetch_related()`

**-to-many** relationships (one-to-many, many-to-many)

Parent --> Child

```python
ModelName.objects.prefetch_related('many_to_many_field')
```

Example:

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

authors_with_books = Author.objects.prefetch_related('book_set')

# 1. SELECT * FROM "myapp_author"
# 2. SELECT *
#    FROM "myapp_book"
#    INNER JOIN "myapp_book_authors"
#    ON ("myapp_book"."id" = "myapp_book_authors"."book_id")
```

## 5. Aggregation and Annotation

Calculates values across the entire table. Reduces the query to a single row.

Executes one SQL query instead of multiple.

### `aggregate()`

```python
ModelName.objects.aggregate(
    total=Sum('field'),
    average=Avg('field'),
    highest=Max('field'),
    lowest=Min('field')
)
"""
Output:
{
    'total': <sum_of_all_values> or None,
    'average': <average_of_all_values> or None,
    'highest': <maximum_value> or None,
    'lowest': <minimum_value> or None,
}
"""
```

### `annotate()`

Adds calculated values per record.

```python
ModelName.objects.annotate(
    related_count=Count('related_name')
)

"""
Output:
<QuerySet [
    ModelName(id=1, related_count=<count_of_related_objects>),
    ...
]>
"""
```

Use `F()` to reference another field in calculations:

```python
ModelName.objects.annotate(
    new_value=F('some_field') * 2
)
```

Add a field from a related model:

```python
objs = ModelName.objects.annotate(extra_field=F("RelatedModel__field"))

# Each object now has an additional attribute from the related model
[obj.extra_field for obj in objs]
```

`values()` **Before** `annotate()` → **Groups** results.

Selects only the fields specified in `values()`, and the annotated fields.

```python
# Get the count of books for each author
authors_with_book_count = Book.objects.values('author').annotate(book_count=Count('id'))
# `values('author')` → Groups the results by the author field.
# annotate(book_count=Count('id')) → Counts the number of books (id) for each author.

# Example output:
# [
#    {'author': 'J.K. Rowling', 'book_count': 7},
#    {'author': 'George Orwell', 'book_count': 3}
# ]
```

## 6. Query Expressions

### `Q()`

Filters in the database.

```python
# AND Condition
ModelName.objects.filter(Q(field1=value1) &
Q(field2=value2))

# OR Condition
ModelName.objects.filter(Q(field1=value1) |
Q(field2=value2))

# NOT Condition
ModelName.objects.filter(~Q(field=value))
```

### `F()`

References to a field's value (including related objects).

```python
ModelName.objects.update(field=F('other_field') * 2)
```

### `Case`

`Value()` represents a literal value.

`then=` and conditions can use `F()` or other expressions.

```python
ModelName.objects.annotate(new_field=Case(
    When(condition,then=Value('result')),
    default=Value('default')
    )
)
```

## Getting Data from QuerySets

### `values()`
Select only the specified fields.

Returns a dictionary.

```python
ModelName.objects.values('field1','field2')
```
