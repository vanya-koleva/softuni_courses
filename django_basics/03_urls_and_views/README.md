# URLs and Views

## URLs

-   Each URL represents a path that loads a specific view.

-   Django looks for the `urlpatterns` variable in the `urls.py` file.

-   Django checks them sequentially for a match.

-   It calls the given view and passes an instance of the class `HttpRequest`.

```python
urlpatterns = [
    path('index/', index_view),
    path('index/', index_view_2)  # index_view_2 will never be reached
]
```

-   We need to include the URLs of each of our apps in the main URLs of our project.

-   We can add a common prefix that appears before every URL of a given app:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('departments/', include('departments.urls')),
]
```

-   `include` can accept a list of paths.

## Dynamic URLs

-   Sometimes we want a dynamic value in the URL (e.g., an ID):

```python
path('index/<int:pk> ', index_view),
```

-   Types of dynamic URLs:

    -   str
    -   int
    -   slug – a string that cannot have spaces or non-ASCII characters
    -   path – e.g. /some/path; it wouldn’t match a str because Django treats it as separate segments
    -   uuid

-   `re_path`

    -   Each captured argument is sent to the view
        as a string.

    -   Always written as a raw string (a string without escapes).

    -   It's recommended to use named groups in your regular expressions for better readability and maintainability.

