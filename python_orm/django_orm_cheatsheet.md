# Django ORM Cheatsheet

## Basics

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

## Field Lookups

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

## Querying Related Objects

### Filter on Related Fields

```python
ModelName.objects.filter(related_name__field=value)
```

### Related Fields Greater Than

```python
ModelName.objects.filter(related_name__field__gt=value)
```

## Efficiently Querying Related Objects

## `select_related()`

-to-one relationships (one-to-one, many-to-one)

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

