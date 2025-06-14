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

## ModelForm Factory

-   We can create ModelForms using `modelform_factory`

-   Allows dynamic form creation

-   We can generate different forms for different users or based on some conditions

```python
PersonForm = modelform_factory(Person, fields=('__all__', ))
```

## Customizing Forms

-   We can iterate through all fields in `__init__` and make them readonly (this can be done using a mixin)

```python
# mixins.py

class ReadOnlyFieldsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
```

```python
# forms.py

from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'email']

        labels = {  # custom labels
            'name': 'Your Name',
            'age': 'Your Age',
            'email': 'Your Email',
        }

        error_messages = {  # custom error messages
            'name': {
                'required': 'This field is required.',
                'max_length': 'Name cannot be longer than 100 characters.',
                'unique': 'Should be unique',
            },
            'age': {
                'required': 'This field is required.',
                'invalid': 'Enter a valid age.',
            },
            'email': {
                'required': 'This field is required.',
                'invalid': 'Enter a valid email address.',
            },
        }
```

-   We can validate form fields with `clean_<fieldname>()` methods:

```python
# forms.py

from django import forms
from .models import Person
from django.core.exceptions import ValidationError

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'email']


    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise ValidationError('First name should contain only alphabetic characters.')
        return first_name
```

-   Use the `clean()` method for cross-field validation:

```python
    def clean(self):
     cleaned_data = super().clean()
     last_name = cleaned_data.get("last_name")
     age = cleaned_data.get("age")

     if last_name and last_name.startswith("A"):
         if age is None or age < 18:
             raise ValidationError("If your last name starts with 'A', you must be at least 18 years old.")

     return cleaned_data
```

## `save()`

-   A method of `ModelForm`

-   Takes one parameter `commit` (default is `True`)

```python
    def save(self, commit=True):
     # Get the unsaved Person instance
     person = super().save(commit=False)

     # Custom logic before saving
     person.first_name = person.first_name.capitalize()
     person.last_name = person.last_name.capitalize()

     # Save the instance if commit is True
     if commit:
         person.save()

     # Custom logic after saving, e.g., sending a notification
     # send_notification(person)  # hypothetical function

     return person
```

## Formsets

-   Allow us to create and manage multiple forms at once

-   For example, in a quiz app, each question could be a separate form

```python
AuthorFormSet = modelformset_factory(Author, form=AuthorForm, extra=3)

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author
from .forms import AuthorFormSet

def manage_authors(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST, queryset=book.authors.all())
        if formset.is_valid():
            authors = formset.save(commit=False)
            for author in authors:
                author.book = book
                author.save()
            return redirect('book_detail', book_id=book.id)
    else:
        formset = AuthorFormSet(queryset=book.authors.all())
    return render(request, 'manage_authors.html', {'formset': formset, 'book': book})
```

## Styling Forms

-   Rendering:

```py
   {{ form.as_p }}
   {{ form.as_ul }}
   {{ form.as_div }}
   {{ form.as_table }}
```

-   Adding CSS classes:

```py
   self.fields['email'].widget.attrs['class'] = 'my-css-class'
```

-   Iterating over form fields in a template:

```py
   {% for field in form %}
               <div class="form-group">
                   <label for="{{ field.id_for_label }}">
                       {{ field.label }}
                       {% if field.field.required %}*{% endif %}
                       {# Display field properties for demonstration #}
                       (Type: {{ field.field.widget.input_type }},
                        Max Length: {{ field.field.max_length }},
                        Required: {{ field.field.required }})
                   </label>
                   <input
                       type="{{ field.field.widget.input_type }}"
                       name="{{ field.html_name }}"
                       id="{{ field.id_for_label }}"
                       class="{{ field.field.widget.attrs.class }}"
                       placeholder="{{ field.field.widget.attrs.placeholder }}"
                       maxlength="{{ field.field.max_length }}"
                       {% if field.value %} value="{{ field.value }}"{% endif %}
                   >
                   {# Display errors if any #}
                   {% if field.errors %}
                       <div class="error">
                           {{ f ield.errors }}
                       </div>
                   {% endif %}
               </div>
           {% endfor %}
```

