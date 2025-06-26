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

