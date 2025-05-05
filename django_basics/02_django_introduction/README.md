# Django Introduction

## Framework - a working structure.

-   Offers a foundation to build upon.

-   We follow certain rules and structures.

-   Provides built-in functions and tools.

-   Framework vs Library:

    -   **Framework**:

        -   The framework calls your code (inversion of control).

        -   You build your application within the framework’s structure.

    -   **Library**:

        -   You call the library when you need it.

        -   You use the library within your own code, maintaining control of the flow.

## MVT Pattern

-   **Model View Template**

-   **Model** - defines the structure and behavior of **data**.

-   **View** - Contains the **business logic**. Receives an HTTP request and returns an HTTP response.

-   **Template** - Handles the **presentation**.Provides a convenient way to generate dynamic HTML pages by using a special template syntax (**DTL** - Django Template Language).

## Structure of a Django Project

-   `manage.py` – the entry point for working with Django; we use it to perform command-line operations.
-   projectFolder

    -   `settings.py` – contains the application's settings

    -   `urls.py` – the place where we define URLs that should be accessible to users

    -   `asgi.py` – setup for asynchronous requests

    -   `wsgi.py` – setup for synchronous requests

-   djangoApp – each app is responsible for a separate part of our project

## App vs Project

-   **Django App**:

    -   A web application that performs a specific function (e.g., blog, user authentication, task manager).

    -   **Something like a package which handles a specific problem.**

    -   Reusable, portable and self-contained — the same app can be used in multiple Django projects.

    -   For example:

        -   A blog app handles posts and comments.

        -   An auth app handles user registration and login.

-   **Django Project**:

    -   The overall web application composed of settings, configurations, and **one or more apps**.

## Creation of a Django App

-   `python manage.py startapp app_name`

-   Move the app to the project directory (optional)

-   Create a `urls.py` file

-   Register the Django app in `settings.py`

-   Register the URLs in the project

```bash
python manage.py runserver
```

## Databases

-   For PostgreSQL, install `psycopg2`

-   Configure it in `settings.py`

-   Create the database

-   Run `migrate`

## Views

-   Handle the main business logic.

-   Function-Based Views (FBV)

-   **A callable (a function or a class) which receives one or more parameters and returns a response.**

    -   It **always** receives the **request** which is passed by Django.

    -   It **always** returns a **HTTP response** (e.g., HttpResponse, JsonResponse, etc.).

        -   By default it is of MIME type text/html.

        -   The class `HttpResponse` is used to construct and return an HTTP response in a format that the browser (or client) can understand.

```python
def index(request):
    return HttpResponse("Hello world")
```

```python
HttpResponse("Hello world", headers={
    "Content-Type": "application/json",
})
```

-   The `render()` function:

    -   Combines a template with a context (data).

    -   Return an HTTP response (specifically, an HttpResponse object) with that rendered HTML.

    -   By default, the path passed to the `render()` function is relative to the templates directory listed in `'DIRS': [BASE_DIR / 'templates']` in settings.py.

```python
from django.shortcuts import render

def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }

    return render(request, 'tasks/index.html', context)
```

-   `request`: The HTTP request object (must always be passed).

-   `'tasks/index.html'`: The path to the template.

-   `context`: A dictionary of data to pass into the template, used to display data dynamically.

## URLs

-   In the `urls.py` file we configure which function or logic should be executed when reaching a given URL.

-   We create a variable named `urlpatterns` in `app/urls.py`.

    -   The variable **must** be named this way and must be an iterable.

-   There, we define which view should be executed for a given URL path.

-   The `path()` function says: on this path load this / these view/s, connecting a URL pattern to a view.

-   The `include()` function concatenates the URL in `path()` with the URLs that are passed to `include()`. It allows the URLs from another file to be included within the current URL pattern.

```python
from django.urls import path

from .views import index

urlpatterns = (
    path('home/', index),
)
```

-   Include the app's URLs in the `project/urls.py`

```python
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('project_name.app_name.urls')),
)
```

## Admin Panel

-   A built-in Django package which enables trusted users to manage content on the site.

-   Initially started as a third-party package, later added as an official package.

-   `/admin/` – to access the admin panel

-   `python manage.py createsuperuser` – to create an admin user

-   `admin.py` – we register the models we want to manage in the admin panel

```python
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
```

## Templates

-   In a template, we access data passed from the view using the variable names defined in the view’s context.

```python
    <ul>
        {% for task in tasks %}
            <li>{{ task.title }}</li>
        {% empty %}
            <li>No tasks</li>
        {% endfor %}
    </ul>
```

-   The key "tasks" in the context dictionary becomes the variable tasks in the template. It is passed from the view into the template context.
-   If there is something in "tasks", proceed with the loop. If it is empty, return 'No tasks'.

## Django Template Language (DTL)

-   Acts like dynamic HTML

-   Includes loops and if statements

-   We can render our own values

-   `{{ }}` – interpolation, variables

-   `{% %}` – template tags

## Project Creation Summary

-   STEP 1: Create a project
-   STEP 2: Create an app

```bash
django-admin startproject project_name

python manage.py startapp app_name
```

-   STEP 3: Add the app to INSTALLED_APPS
-   STEP 4: Replace DB settings with Postgres DB settings
-   STEP 5: Enter Postgres credentials
-   STEP 6: Install psycopg2
-   STEP 7: Create the database
-   Step 8: Run `migrate`

