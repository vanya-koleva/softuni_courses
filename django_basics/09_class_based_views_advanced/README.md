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

