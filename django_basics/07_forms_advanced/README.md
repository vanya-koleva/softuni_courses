# Forms Advanced

## Django Validators

-   Must be callable

-   Must raise `ValidationError` on error

-   Can be reused in multiple places, e.g., in forms and models

-   Validators are stored in migrations; if we delete the validator after makemigrations, migrations will fail

-   They are called automatically via `full_clean()`

-   `full_clean()` is triggered when calling `is_valid()` on a form

-   It's good practice to put validators in the model, so the same validation is enforced both on the client side and in the admin panel

```python
# validator with func
from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )
```

```python
# validator with class
from django.core.exceptions import ValidationError

class EvenValidator:
    def __init__(self, message=None, code=None):
        self.message = message or '%(value)s is not an even number'
        self.code = code or 'not_even'

    def __call__(self, value):
        if value % 2 != 0:
            raise ValidationError(
                self.message,
                code=self.code,
                params={'value': value},
            )

    def __repr__(self):
        return f'EvenValidator(message={self.message}, code={self.code})'

    def deconstruct(self):
        return (
            f"{self.__class__.__module__}.{self.__class__.__name__}",
            [],
            {'message': self.message, 'code': self.code}
        )
```

