# Class Based Views - Advanced

## ListView

-   Provides us with a list of items

-   In the context, they are populated as `object_list` and `model_name_list`

```py
# views.py
   class FilteredBookListView(ListView):
       model = Book
       template_name = 'filtered_book_list.html'

       # for filtering (optional)
       def get_queryset(self):
           # Filter books published after January 1, 2020
           return Book.objects.filter(published_date__gt=date(2020, 1, 1))
```

-   Provides pagination

```py
class PaginatedBookListView(ListView):
    model = Book
    template_name = 'paginated_book_list.html'
    context_object_name = 'books'
    paginate_by = 10  # Number of books per page
```

-   Access in the template

-   Adds the page to the URL

```py
    <div class="pagination">
        <span class="step-links">
            {% if page_obj.has_previous %}
                <a href="?page=1">&laquo; first</a>
                <a href="?page={{ page_obj.previous_page_number }}">previous</a>
            {% endif %}

            <span class="current">
                Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
            </span>

            {% if page_obj.has_next %}
                <a href="?page={{ page_obj.next_page_number }}">next</a>
                <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
            {% endif %}
        </span>
    </div>
```

## Detail View

-   Similar to ListView, but works with a **single object**

<img src="https://codefellows.github.io/sea-python-401d6/_images/DetailView.png" />

## Useful CBV Methods

-   `get()`

    -   **Description**: This method is used to handle HTTP GET requests. Inside it, you can define the logic that should run when a GET request is made to a given URL.

-   `post()`

    -   **Description**: This method is used to handle HTTP POST requests. Similar to `get()`, but for POST requests—define the logic that should execute when a POST request is received.

-   `get_queryset()`

    -   **Description**: Used to retrieve the dataset (queryset) that will be processed and displayed by the view. Often used in CBVs like `ListView` and `DetailView` to define which data should be shown.

    -   **Static alternative**: You can set a static `queryset` attribute, but this method allows dynamic customization of the dataset.

-   `get_context_data()`

    -   **Description**: Used to add additional context to the template. Here you can pass any extra data you want to provide to the template.

    -   **Static alternative**: If you don't need dynamic context, you can set static data using the class attribute `extra_context`.

-   `dispatch()`

    -   **Description**: The `dispatch()` method determines which HTTP method (e.g., GET or POST) is being used for the request and calls the corresponding method (`get()`, `post()`, etc.). It routes the request to the appropriate handler. It can also be used for user access control checks.

-   `get_template_names()`

    -   **Description**: This method returns a list of template names to be used for rendering the view. It can be used to dynamically determine which template should be used based on certain conditions.

    -   **Static alternative**: You can normally set the template name using the `template_name` attribute. Use `get_template_names()` for more dynamic behavior.

-   `get_context_object_name()`

    -   **Description**: Used in views like `DetailView` and `ListView` to define the name of the context variable that will be used in the template. This variable holds the object or list of objects passed to the template.

    -   **Static alternative**: Instead of using this method, you can set the context variable name directly with the `context_object_name` attribute.

-   `get_success_url()`

    -   **Description**: Used in views like `CreateView`, `UpdateView`, and `DeleteView` to determine the URL to redirect the user to after successfully completing an action (e.g., creating, updating, or deleting an object).

    -   **Static alternative**: You can set the URL statically using the `success_url` attribute.

-   `render_to_response()`

    -   **Description**: This method is used to render a template with a given context and return an `HttpResponse` object. It is the main method for rendering in CBVs.

    -   **Static alternative**: If you want to always use the same context and template, you can define them statically via methods like `get_context_data()` and `get_template_names()`.

## Decorators

-   Often used to modify the behavior of a given method.

-   `login_required`

-   `permission_required`

