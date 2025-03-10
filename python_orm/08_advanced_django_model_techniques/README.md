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

## Indexing

## Django Model Mixins

