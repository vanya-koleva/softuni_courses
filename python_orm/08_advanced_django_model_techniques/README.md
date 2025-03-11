# Advanced Django Model Techniques

## Validation in Models

-   Validate the data entered in the fields.

-   The validators are not constraints. They only work **on Django level**.

-   Raise a `ValidationError`.

-   One or more validators can be passed as a list or a tuple.

-   **Built-in Validators**

    -   `MaxValueValidator`, `MinValueValidator`, `MaxLengthValidator`, `MinLengthValidator`

        -   Take two arguments:
            -   `limit` - required
            -   `message` - `message=None` is being passed by default

    -   `RegexValidator(regex, message)`

```python
class SampleModel(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)]  # Name should have a minimum length of 5 characters
    )

    age = models.IntegerField(
        validators=[MaxValueValidator(120)]  # Assuming age shouldn't exceed 120 years
    )

    phone = models.CharField(
        max_length=15,
        validators=[
	        RegexValidator(
	            regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
	    )]  # A simple regex for validating phone numbers
    )
```

-   **Custom Validators**

    -   A good practice is to write them in **validators.py**

```python
from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError('Value must be an even number!')
```

## Meta Options and Meta Inheritance

-   Specify **model-level** options.

-   **Meta Options**:

    -   Type of the class (`abstract`, `proxy`)

    -   `db_table` - Change the name of the table.

    -   `ordering` - A default order whne a collection is retrieved.

    -   `unique_together` - enforces uniqueness on a combination of two or more fields **at the database level**.

        -   May be deprecated in the future.

        -   Use `UniqueConstraint` with the `constraints` option instead.

    -   `verbose_name` - A human-readable name for the object, singular.

        -   The name of the object by default where CamelCase becomes camel case.

    -   `verbose_name_plural` - The plural name for the object.

        -   If this isn’t given, Django will use verbose_name + "s".

    -   `managed` - Controls whether Django should manage the corresponding database table.

        -   If False, no database table creation, modification, or deletion operations will be performed for this model.

        -   All other aspects of model handling are exactly the same as normal.

        -   Only affects schema management, not ORM queries

        -   It is useful when dealing with existing database tables or database views.

    -   `app_label` - Defines which app the model belongs to.

        -   When defining a model outside of an app's models.py.

        -   When working with abstract base models in a separate module.

```python
class SampleModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()

    class Meta:
        # Database table name
        db_table = 'custom_sample_model_table'

        # Default ordering (ascending by name)
        ordering = ['name'] # Happens on SELECT, not on INSERT

        # Unique constraint (unique combination of name and email)
        unique_together = ['name', 'email']
```

-   **Meta Inheritance**

    -   The ability to inherit Meta options.

    -   The Meta class is inherited **only** if the parent is an **abstract** class.

        -   The `abstract` option in the child becomes False.

        -   If the child defines its own Meta class, it **completely overrides** the parent's one **unless it extends it** by subclassing.

```python
class BaseModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True
        ordering = ['name']

class ChildModel(BaseModel):
    description = models.TextField()
    # ChildModel inherits the Meta options
```

-   Overriding example:

```python
class ChildModel(BaseModel):
    description = models.TextField()

    class Meta:
        pass
        # Child's Meta class completely overrides the parent's one and does not have it's options
```

-   Extending example:

```python
class ChildModel(BaseModel):
    description = models.TextField()

    class Meta(BaseModel.Meta):
        verbose_name_plural = 'Child Models'
        # ChildModel inherits all parent's Meta options and adds its own ones
```

## Indexing

-   Indexing helps us by organizing elements in a specific order or creating another structure that allows us to search faster.

-   We retrieve records quickly, but storing them takes more time.

-   We can add an index to a field by including the keyword argument `db_index=True` when defining a model field.

-   We can also create an index using the Meta class, allowing us to define composite indexes as well:

```python
class Meta:
    indexes=[
        models.Index(fields=["title", "author"]),  # speeds up searches using both criteria
        models.Index(fields=["publication_date"])
    ]
```

## Django Model Mixins

-   Reusable classes that we use to separate common functionality.

```python
class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
	class Meta:
    	    abstract = True
```

