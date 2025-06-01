## URL patterns

```python
# urls.py
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    # Static URL
    path('about/', views.about, name='about'),

    # Dynamic URL with converters
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<slug:slug>/', views.category_view, name='category_view'),

    # Regex URL with named groups
    re_path(r'^archive/(?P<year>[0-9]{4})/$', views.archive, name='archive'),

    # Include app URLs
    path('blog/', include('blog.urls')),
    path('shop/', include([
        path('cart/', views.cart, name='cart'),
        path('checkout/', views.checkout, name='checkout'),
    ])),
]
```

-   Django processes `urlpatterns` sequentially (first match wins)

-   Use `<converter:name>` for typed parameters:

    -   `int`, `str`, `slug`, `uuid`, `path`

-   `re_path` for complex patterns

    -   Name groups. Groups `(?P<name>pattern)` pass captured values as kwargs. All values are passed as strings.

## Function-Based Views

```python
def product_detail(request, pk):  # URL param name must match
    return HttpResponse(...)
```

-   Request Flow:

    -   URL pattern matches request

    -   Django calls view function with:

        -   `HttpRequest` object

        -   URL parameters as keyword arguments

    -   View returns `HttpResponse` object

## Response Types

```python
# Basic response
HttpResponse("Text content", status=200)

# JSON response
from django.http import JsonResponse
JsonResponse({'data': value}, status=201)

# Template rendering
from django.shortcuts import render
return render(request, 'template.html', {'key': value})

# Redirects
from django.shortcuts import redirect
redirect('view-name')             # By URL name
redirect('/absolute/path/')       # Hardcoded path
redirect('https://example.com')   # External URL

# File responses
from django.http import FileResponse
return FileResponse(open('file.pdf', 'rb'))
```

## Essential Shortcuts

```python
# Error handling
from django.http import Http404
raise Http404("Page not found")  # Customize via 404.html

# Object shortcuts
from django.shortcuts import get_object_or_404, get_list_or_404
obj = get_object_or_404(MyModel, pk=id)  # Auto 404 if missing

# URL reversing
from django.urls import reverse, reverse_lazy
reverse('urlname', args=[42])          # In views (e.g., dynamic URL)
reverse_lazy('urlname')                # For settings (e.g., LOGIN_URL)
resolve_url('urlname')                 # Handles URL names, views, models, or URLs
```

## Best Practices

-   URL Design:

    -   Use trailing slashes consistently

    -   Name all URLs

    -   Prefer path converters over regex where possible

-   Views:

    -   Use `get_object_or_404()` instead of `Model.objects.get()`

-   Security:

    -   Always use `{% csrf_token %}`in forms

    -   Validate user input

