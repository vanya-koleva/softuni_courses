# Models Inheritance and Customization

## Types of Model Inheritance

-   **Multi-table**

    -   **Both** models **generate tables**.

    -   We extend a model with fields from another model without copying the fields themselves.

    -   What Django does internally is create a One-to-One relationship between the parent and child models.

    -   **Eager loading** - The data from both tables is joined at the time of retrieval. Whenever we retrieve data from the child model, Django automatically fetches not only the fields specific to the child but also all the fields from the parent model.

```python
class Person(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def is_student(self):
        """Check if this person is also a student."""
        return hasattr(self, 'student')

class Student(Person):
    student_id = models.CharField(max_length=15)
    major = models.CharField(max_length=50)
```

-   **Abstract Base Classes**

    -   The abstract model does **not generate a table**.

    -   Only the children generate tables while the abstract class serves as a template.

    -   This is achieved by modifying the inner class Meta.

```python
class AbstractBaseModel(models.Model):
    common_field1 = models.CharField(max_length=100)
    common_field2 = models.DateField()

    def common_method(self):
        return "This is a common method"

    class Meta:
        abstract = True
```

-   **Proxy Models**

    -   The proxy model does **not generate a table**.

    -   It does **not have its own fields**.

    -   It uses the same table as the original model.

    -   Used to add functionality to a model that we cannot directly modify.

        -   Example: If we need to add functionality to the models of Django Unfold, we can create proxy models based on their models.

    -   We can add methods, but not new fields.

```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()

class RecentArticle(Article):
    class Meta:
        proxy = True

    def is_new(self):
        return self.published_date >= date.today() - timedelta(days=7)

    @classmethod
    def get_recent_articles(cls):
        return cls.objects.filter(published_date__gte=date.today() - timedelta(days=7))
```

## Built-in Model Methods

-   `save()` - Called when saving an instance to the database.

    -   When overriding save():

        -   We must pass \*args and \*\*kwargs to it.

        -   We must call it through super() and pass \*args and \*\*kwargs to it to ensure the logic from Django's base Model class is executed.

        -   If we don’t call `super().save(*args, **kwargs)`, the object won’t actually be saved to the database.

```python
    def save(self, *args, **kwargs):
        # Check the price and set the is_discounted field
        if self.price < 5:
            self.is_discounted = True
        else:
            self.is_discounted = False

        # Call the "real" save() method
        super().save(*args, **kwargs)
```

-   `clean()` - Used for validating logic across multiple fields before saving.

    -   Automatically called by `full_clean()` when using Django **Forms** and ModelForms.

    -   It is **not** automatically called when saving a model instance using save().

    -   Good practice is to throw `ValidationError`.

    -   If we want to validate data only for one field, it is better to use a validator.

```python
    def clean(self):
        """Custom validation logic"""
        if self.discount > self.price:
            raise ValidationError("Discount cannot be greater than the price!")

    def save(self, *args, **kwargs):
        """Ensure validation runs before saving"""
        self.clean()
        super().save(*args, **kwargs)
```

## Custom Model Properties

-   We can use the `@property` decorator to create new attributes that are **not stored in the database**.

-   Calculated or derived from existing model fields.

-   Used for **dynamic calculations of values**.

```python
class Animal(models.Model):
    ...
    @property
    def age(self):
        age = date.today() - self.birth_date
        return age.days // 365
```

## Custom Model Fields

-   Created by subclassing:

    -   `django.db.models.Field`
    -   or one of the existing field classes.

-   It is a good practice to create the custom fields in a fields.py file.

-   Built-in custom field methods:

    -   **`from_db_value(value, expression, connection)`** - Called when retrieving the value **from the database** and converting it **into a Python** object.

        -   It is only used for database-to-Python conversion

    -   **`to_python(value)`** - **For validation**. Called during deserialization or when using the `clean()` method to ensure the value is in the correct Python format.

        -   ValidationError
        -   Ensures that all assigned values are properly converted to a Python-compatible type.
        -   Always used internally by Django forms and field validation.

    -   **`get_prep_value(value)`** - The reverse of `from_db_value`, converting a Python object into a format suitable for storage in the database. Mainly used for serialization.

    -   **`pre_save(model_instance, add)`** - Used for **last-minute changes** before saving the object to the database.

    -   **`validate(value, model_instance)`** - Called by `full_clean()`. Used for **field-level validation** before saving data to the database (only triggered for the specific field in which it is implemented, not for the whole model).

-   A good practice is to use `to_python()` instead of returning the result directly from `from_db_value()` to maintain consistency and ensure that the same conversion logic is applied regardless of where the data comes from.

    -   `to_python()` is **always called** when handling model fields.

    -   `from_db_value()` is **only called when fetching from the database**.

```python
class RGBColorField(models.TextField):
    # Convert the database format "R,G,B" to a Python tuple (R, G, B)
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self.to_python(value)

    # Convert any Python value to our desired format (tuple)
    def to_python(self, value):
        if isinstance(value, tuple) and len(value) == 3:
            return value
        if isinstance(value, str):
            return tuple(map(int, value.split(',')))
        raise ValidationError("Invalid RGB color format.")

    # Prepare the tuple format for database insertion
    def get_prep_value(self, value):
        # Convert tuple (R, G, B) to "R,G,B" for database storage
        return ','.join(map(str, value))
```

