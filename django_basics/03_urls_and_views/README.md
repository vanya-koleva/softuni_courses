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
        as a **string**.

    -   Always written as a raw string (a string without escapes).

    -   It's recommended to use **named groups** in your regular expressions for better readability and maintainability.

        -   `(?P<name_of_the_group>pattern)`

        -   If you use both named groups and unnamed groups within a given regex, any unnamed groups are ignored and only named groups are passed to the view function.

## `include()`

-   If a **string** is passed to `include()`, Django attempts to import the corresponding URL configuration module. This module must define a `urlpatterns` variable — a list of URL patterns — which Django then iterates over and includes as part of the overall URLconf.

-   If a **list or tuple** of URL patterns is passed directly to `include()`, Django includes the list as-is without attempting to import a module.

-   Whenever you use `include()`, you are extending the current URL path with additional URLs.

## Views

Function-Based Views (FBVs)

-   Accept an HTTP request and return an HTTP response (or a subclass of it).

-   Besides the request, they can receive other parameters defined in the URL.

    -   The name of the variable in the URL pattern must match the name of the parameter in the view function.

## Response Types

-   `HttpResponse`

    -   An object responsible for serializing our response (breaking it into packets, etc.)

    -   An object responsible for serializing our response (breaking it into packets, etc.)

    -   We can pass `content` to it.

    -   We can pass a `status_code` to it.

```python
   return HttpResponse(content="Hi my name is", status=201)
```

-   `JsonResponse`

```python
content = json.dumps({
  "name": "Dido",
  "age": 20
})

return HttpResponse(content=content, content_type="application/json")
# or
return JsonResponse(content,)
```

## Django Shortcuts

-   `render()`

    -   Renders the `context` into an HTML template.

        -   `context` - A dictionary containing values that are added to the template context.
        
        -   The variable names in the `context` correspond to the variables used in the HTML template.

    -   Returns an HttpResponse object with the rendered text.

```python
   return render(request, 'core/index.html', context)  # context is optional
```

-   `redirect()`

    -   Redirects to another URL.

    -   Can be **permanent**
        -   Used when we always want to redirect from this page to another.

```python
redirect('https://softuni.bg')  # absolute URL since we redirect to another app
redirect('my_view_name', pk=10)  # using view name for better abstraction
```

-   `reverse()`

    -   Takes a URL name, looks it up among registered names, and returns the URL for that name.

-   `reverse_lazy()`

    -   Used for configuration.

    -   Loads the URL when it actually exists.

```python
   # settings.py
   LOGIN_URL = reverse('index') # throws an error
   LOGIN_URL = reverse_lazy('index') # works fine
```

-   `resolve_url()`

    -   Uses Django’s URL resolver to find the URL for a view or a model (if the model has get_absolute_url).

-   `get_object_or_404()` / `get_list_or_404()`

```python
article = get_object_or_404(Article, pk=article_id)
# If no such Article exists in the database, the function raises a 404 error instead of crashing or returning None.
```

## Django Errors

-   `raise Http404`

-   `return HttpResponseNotFound`

-   Both achieve the same result.

-   You can customize the 404 page by creating a template named `404.html`.

