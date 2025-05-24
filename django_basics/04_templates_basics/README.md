# Django Templates Basics

## Django Template Language (DTL)

-   DTL is used to **render** dynamic **content within templates**, utilizing **context** data passed **from the views**.

-   It allows us to write HTML that can vary depending on the data.

-   The only template engines Django supports out of the box are DTL and Jinja2.

-   We can render into HTML, TXT, XML, etc.

-   It is used for Server Side Rendering (SSR) -  processing templates on the server before sending HTML to the client.

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

