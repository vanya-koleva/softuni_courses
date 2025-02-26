# Working with Queries in Django

## Useful Methods

-   `.filter()` - Takes one or more keyword arguments (field=value). Returns a QuerySet with a subset of objects.

```python
# Both must return true - Female employees in Accounting department
employees = Emploee.objects.filter(department='Accounting', gender='Female')
```

-   `.exclude()` - Opposite of filter().

-   `.order_by()` - Returns a QuerySet with the sorted objects. A hyphen for descending order.

```python
ordered_desc_employees = Employee.objects.order_by('-last_name')
```

-   `.count()` - Returns an integer. Similar to len() but much faster because it doesn't fetch the data from the database; only retrieves the count, not the actual objects.

-   `.get()` - Returns a **single object**; accepts kwargs; raises exceptions if it finds no object or more than one object matching the kwargs.

## Chaining Methods

-   Every method works with what the result returned by the previous method.

## Lookup Keys

-   Used in filter, exclude, get

-   Added to the **field names** in the query to define the type of comparison or operation to be performed on the **field values**.

-   Format: `field__lookupkey=value`

-   `exact` - exact match (WHERE field=value)

-   `iexact` - case insensitive match (WHERE field ILIKE value)

-   `contains` - contains case sensitive match (WHERE field like %value%)

-   `icontains` - contains case insensitive match (WHERE field ilike %value%)

-   `in=[val_1, val_2, val_3...]` - iterable set (WHERE value IN (val_1, val_2, val_3, ...))

-   `gt` - greater than

-   `gte` - greater than or equal

-   `lt` - less than

-   `lte` - less than or equal
-   `startswith=value` - starts with value (WHERE field LIKE 'value%')

-   `istartswith`

-   `endswith=value`

-   `iendswith`

-   `range=(start, end)` - field in range with **both values inclusive** (WHERE field between start and end)

-   Date/time field allows chaining additional field lookups.

-   Format: `field__additional_field__lookupkey`

```python
employees = Employee.objects.filter(birth_date__year__gt=1999)
```

-   `date = datetime.date(value)` - exact date always cast value to datetie.date

-   `date__gt = datetime.date(value)` - can be combined with **gt, **gte, \_\_lt ....

-   `year = value` - exact year match (WHERE value BETWEEN 'year-01-01' AND 'year-12-31')

-   `month=value`

-   `month__gte = value` - exact month match (WHERE EXTRACT('month' FROM field) >= 'value')

-   `day`

-   `week`

-   `weekday = value` - weekday match 2=monday, 7=saturday

-   `isoweekday = value` - weekday match 1=monday, 6=saturday

-   `quater = value` - quater of the year, can be 1, 2, 3 or 4

-   `time=datetime.time(value)` - check for exact time

-   `time__range=(datetime.time(start), datetime.time(end))` - check for time range

-   `hour = value` - check for exact time hour

-   `hour__gte = value`

-   `minute`

-   `second`

-   `isnull = True` - check if field is null

-   `regex=r"regex_here"` - check for a regex in a field

-   `iregex`

## Bulk Methods

-   Used to perform operations on many objects simultaneously.

-   More efficient.

-   `.bulk_create()` - Creates many objects with one query. Accepts a list of object instances.

-   `.filter().update()`
-   `.filter().delete()`

