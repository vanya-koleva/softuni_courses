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

-   `as_view`

    -   Returns the view as a callable

    -   Can be called with kwargs

```py
urlpatterns = [
     # Redirect to 'https://www.example.com/'
     path('redirect-example/', CustomRedirectView.as_view(url='https://www.example.com/'), name='custom-redirect'),
 ]
```

-   `dispatch`

    -   Used to call the appropriate methods based on the request

    -   We can use it for validation, e.g., to check if a user has access to a resource

```py
 import random
 from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed

 # Simulating a Django-like environment
 class SimulatedRequest:
     """A simple simulated request object."""
     def __init__(self, method):
         self.method = method.upper()
         self.user = 'SimulatedUser'  # Placeholder for user information

 class BaseView:
     def dispatch(self, request, *args, **kwargs):
         """
         Simulate the dispatch method, routing the request to the appropriate handler.
         For POST requests, check if the user has permission using a random choice.
         """
         if request.method == 'GET':
             return self.get(request, *args, **kwargs)
         elif request.method == 'POST':
             # Simulate permission checking
             has_permission = random.choice([True, False])
             print(f"Permission check for POST: {'Allowed' if has_permission else 'Denied'}")

             if has_permission:
                 return self.post(request, *args, **kwargs)
             else:
                 return HttpResponseForbidden("You do not have permission to perform this action.")
         else:
             return HttpResponseNotAllowed(['GET', 'POST'])

     def get(self, request, *args, **kwargs):
         return HttpResponse("Base GET response")

     def post(self, request, *args, **kwargs):
         return HttpResponse("Base POST response")

 class MyView(BaseView):
     def get(self, request, *args, **kwargs):
         return HttpResponse("MyView GET response")

     def post(self, request, *args, **kwargs):
         return HttpResponse("MyView POST response")

 # Simulating requests
 def simulate_request(view, method):
     request = SimulatedRequest(method)
     response = view.dispatch(request)
     print(f"Response to {method} request: {response.content.decode()} (Status Code: {response.status_code})\n")

 # Create an instance of MyView
 my_view = MyView()

 # Simulate GET request
 simulate_request(my_view, 'GET')

 # Simulate POST requests multiple times to observe permission variations
 for _ in range(3):
     simulate_request(my_view, 'POST')
```

