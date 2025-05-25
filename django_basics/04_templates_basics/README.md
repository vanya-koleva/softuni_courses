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

-   Call functions by using them like regular variables

    -   No parenthesis

    -   `{{ some_function }}`

## Filters

-   Used to transform and format data in the template.

-   They are applied using the pipe symbol (`|`), e.g. `{{ value|filter_name }}`.

-   Some filters accept arguments, which are passed using a colon (`:`), e.g. `{{ value|filter_name:arg }}`.

    -   They can receive only one argument.

-   Common built-in filters:

    -   `truncatechars:number`

        -   Truncates the string after a specified number of characters, appending `...` if truncation occurs.

        -   `{{ text|truncatechars:10 }}` → `"Some tex..."`

    -   `truncatewords:number`

        -   Truncates after a given number of words.

        -   `{{ text|truncatewords:3 }}` → `"This is..."`

    -   `join:separator`

        -   Joins a list with the given string as a separator.

        -   `{{ my_list|join:", " }}` → `"a, b, c"`

    -   `date:format_string`

        -   Formats a datetime object according to a specified format string (Django date format syntax).

        -   `{{ my_date|date:"Y-m-d" }}` → `"2025-05-25"`

    -   `default:value`

        -   Outputs the given value if the original variable is falsy.

        -   `{{ username|default:"Guest" }}`

    -   `add:value`

        -   Adds a numeric or string value to the variable.

        -   `{{ count|add:"2" }}` → adds 2 to `count`

    -   `capfirst`

        -   Capitalizes the first character of the string.

        -   `{{ name|capfirst }}` → `"John"`

