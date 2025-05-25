# Django Templates Basics

## Django Template Language (DTL)

-   DTL is used to **render** dynamic **content within templates**, utilizing **context** data passed **from the views**.

-   It allows us to write HTML that can vary depending on the data.

-   The only template engines Django supports out of the box are DTL and Jinja2.

-   We can render into HTML, TXT, XML, etc.

-   It is used for Server Side Rendering (SSR) - processing templates on the server before sending HTML to the client.

-   The default settings for DTL can be found in settings.py:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

## Variables

-   We fill them in from the context using `{{ }}`

    -   Context key → how you access it in the template;

    -   Context value → what shows up in the template.

-   Variable names should be in snake_case, using only letters and digits.

-   In a Django template, `.` can mean:

    -   Dictionary key lookup

    -   Object attribute access

    -   List index access

    -   Method call (only safe ones—no arguments allowed)

    -   Examples: `{{ my_list.1 }}`, `{{ person.full_name }}`, `{{ my_object.items }}`

```python
from django.shortcuts import render

def my_view(request):
    context = {
        "person": {
            "name": "Vanya",
            "age": 20,
        },
        "greeting": "Hello"
    }
    return render(request, "my_template.html", context)

# my_template.html
<p>{{ greeting }}, {{ person.name }}!</p>

# Output
Hello, Vanya!
```

-   Only “safe” methods can be called in templates:

    -   Must not require arguments

    -   Must not have side effects (e.g., altering data)

