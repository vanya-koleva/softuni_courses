# Class-Based Views Basics

## Why use CBV (Class-Based Views)?

-   It's cleaner

-   Allows us to use inheritance

-   We get abstraction

## `views.View`

-   Base class view

```py
class IndexView(views.View):
   def get(self, request):
      # perform get logic

   def post(self, request):
      # perform post logic
```

