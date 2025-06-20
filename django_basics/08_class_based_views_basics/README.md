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

## Custom Class Based View

```py
class BaseView:
    @classonlymethod  # allows calling only via class
    def as_view(cls):
        def view(request, *args, **kwargs):
            self = cls()  # Create an instance of the view
            if request.method == "GET":
                return self.get(request, *args, **kwargs)
            elif request.method == "POST":
                return self.post(request, *args, **kwargs)
            else:
                return HttpResponseNotAllowed(['GET', 'POST'])  # Handle unsupported methods

        return view

    def get(self, request, *args, **kwargs):
        raise NotImplementedError("GET method not implemented")

    def post(self, request, *args, **kwargs):
        raise NotImplementedError("POST method not implemented")


class MyView(BaseView):
    def get(self, request, *args, **kwargs):
        # perform some get logic
        return HttpResponse("This is a GET response")

    def post(self, request, *args, **kwargs):
        # perform some post logic
        return HttpResponse("This is a POST response")
```

```py
urlpatterns = [
   path('cbv/', MyView.as_view())  # as_view returns a callable - our view
]
```

