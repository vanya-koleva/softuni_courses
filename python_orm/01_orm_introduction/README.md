# Introduction to ORM

-   **Object-Relational Mapping (ORM)** maps content in a relational database to
    object-oriented code. Instead of tables, you write classes representing the data.

-   Python classes --> Database tables

## Benefits

-   **Speeds up** development by automating many aspects of database interactions
-   Reduces the risk of **SQL injection**.
-   Works very well with **CRUD**.
-   Better **readability**.
-   Easier **maintenance**.

## Disadvantages

-   Not very optimized for more complex queries.
-   **Reduced performance**.
-   **Reduced flexibility**.

## SQL injection

-   A type of cyber attack where an attacker manipulates an application's SQL queries by injecting malicious SQL code into input fields. This can allow unauthorized access to a database, data leakage, data modification, or even complete database destruction.

## Popular ORM Tools for Python

-   Django
-   web2py - An open source full-stack Python framework.
-   SQLObject
-   SQLAlchemy - Provides persistence patterns designed for efficient and high-performing database access.

## Database Driver

-   A software component that allows applications to communicate with a database management system (DBMS).

-   It acts as a bridge/adapter between the application and the database by translating the application's queries into commands that the database can understand.

-   **Psycopg2** - PostgreSQL database adapter for Python.
    -   External module.
    -   Used to:
        -   Connect to PostgreSQL.
        -   Perform SQL queries and database operations.
    -   Designed to handle heavy multi-threaded applications.
    -   Installation:
    ```bash
    pip install psycopg2
    ```

## Framework

-   A framework is a structured set of tools, libraries, and conventions designed to support the development of software applications.

-   It provides a **foundation** on which developers can **build programs** for a specific platform or domain.
-   Includes an API.

## Django

-   High-level Python Wed Framework
-   Fast
-   Secure
-   Scalable
-   Free and open source
-   Components:
    -   Core Libraries: Python standard libraries and Django-specific utilities.
    -   Routing: URL dispatcher for mapping URLs to views.
    -   Database Abstraction: Django ORM for database interactions.
    -   Templating: Django template engine for rendering HTML.
    -   Middleware: Built-in middleware for sessions, authentication, etc.
    -   Security: CSRF protection, password hashing.
    -   Admin Interface: A built-in admin panel for managing data.
    -   Testing Tools: Django test framework for writing tests.

## MVT

-   Django uses the **MVT (Model-View-Template)** architecture.

-   Similar the MVC (Model-View-Control).
-   Separates application design into three components:

    -   **Model**: Handles **data** structure through interacting with a database.

    -   **View**: Handles business logic.

    -   **Template**: Handles the presentation layer to display the data provided by View in the browser.

-   The framework itself acts as the controller.

## Django ORM

-   One of the best ORMs available in the industry today.
-   Very **efficient**.
-   Ability to handle medium to low complexity queries and medium to huge datasets.
-   Migrations.

## Django Project

-   A collection of configurations and apps for a particular website.
-   The project can contain multiple apps.

-   Create a location for the virtual environment:

```bash
python3 -m venv venv
```

-   Activate the virtual environment:

```bash
source venv/bin/activate
```

-   Create a Django project:

```bash
django-admin startproject ProjectName
```

-   Project structure:

    -   **\_\_init\_\_.py** - An empty file, telling Python this directory is a Python package.
    -   **settings.py** - The configuration file for this Django Project.
    -   **urls.py** - The URL declarations for this Django project.
    -   **manage.py** - A command-line utility that lets you interact with this Django project.
    -   **asgi.py** - An entry-point for ASGI-compatible servers.
    -   **wsgi.py** - An entry-point for WSGI-compatible servers.

-   Running the project:

    -   Shift + F10 or Run button in PyCharm.
    -   Terminal command:
        ```bash
        python manage.py runserver
        ```

## Django App

-   A Web application that does something - e.g., a blog system or a small task app.

-   One app can be used in multiple projects.

-   The app is created in the same directory as the manage.py file:

```bash
python manage.py startapp
```

-   Django automatically generates the basic directory structure of an app.

    -   admin.py
    -   models.py
    -   views.py
    -   migrations - Command-line utility for propagating changes in models.

-   The app can be moved inside the root directory of your Django project (a good way of project management).

-   To include an app in a project, add a reference to the app in the INSTALLED_APPS setting.
  
-   When you add new apps to INSTALLED_APPS, be sure to run manage.py migrate.

-   To configure our project to work with PostgreSQL, we need to set it up in the settings.py file.

## Django dbshell

-   An interactive command-line interface shell environment.
-   Runs the command-line client for the specified database, or the default database.

```bash
python manage.py dbshell
```

-   `\dt` command shows all tables in the current database.
-   `\d <table_name>` command shows a specific table.

## Workflow for the Course

Naviggate to the directory with `cd`
```bash
python3 -m venv .venv

source .venv/bin/activate   # .venv\Scripts\activate for Windows

pip install -r requirements.txt     

pip install psycopg2    # if needed
```
Add database source.  
Change settings.py:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "database-name",
        "USER": "postgres-user",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```
*Using `python3 -m venv .venv` will create a hidden virtual environment.
