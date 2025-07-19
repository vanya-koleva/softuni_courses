# Django Middlewares and Sessions

## Middlewares

-   A middleware is a functionality that is executed before and/or after each request.

-   It’s quite similar to creating a mixin, but with middleware, there is no need to inherit it anywhere. In other words, it becomes abstract.

-   The execution order is important.

-   Middlewares execute **top-down before** the request and **bottom-up after** it.

-   Defined in `settings.py`:

```py
MIDDLEWARES = [
   ...,
   Path.to.your.callable,  # callable - something that overwrites the method __call__
   ...,
]
```

-   Template for function middleware:

```py
   def measure_time(get_response):
      def middleware(request, *args, **kwargs): // looks like view
         result = get_response()

         return result

   return middleware
```

-   Example:

```py
   def measure_time(get_response):
      def middleware(request, *args, **kwargs): // looks like view
         start_time = time.time()
         result = get_response(request)
         end_time = time.time()

         print(f"{request.path} executed in {end_time - start_time} seconds.")

         return result

   return middleware
```

-   Class-based:

```py
import time

class RequestTimingMiddleware(MiddlewareMixin):
    """
    Middleware to measure the time taken to process a request using process_request and process_response.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        # Start time before processing the request
        self.start_time = time.time()

    def process_response(self, request, response):
        # End time after processing the request
        end_time = time.time()

        # Calculate the duration
        duration = end_time - self.start_time

        # Log the duration (you can use any logging mechanism here)
        print(f"Request to {request.path} took {duration:.4f} seconds.")

        return response
```

-   In addition to `process_request` and `process_response`, there's also `process_view`, which allows you to run code right before the view is executed.

-   In other words, each middleware is called three times — before the request, right before the view, and after the request.

## Session

-   HTTP is stateless – it doesn't retain any information; each request stands on its own.

-   A session is a way for the server to retain information about the user.

-   Django offers a foundational session management system that is ready to use, flexible, and extendable, but may require customization for more advanced use cases.

-   There is a `django_session` table which stores:

    -   a **`session_key`** (sent to the client)

    -   **`session_data`** (contains the serialized user-related data)

    -   **`expiration_date`** (the date when the session expires; default is 2 weeks)

-   If a user logs in from two browsers, there will be two separate sessions for that same user.

-   The session data is serialized in the database, but when accessed in a view, it is deserialized and can be treated like a regular Python object (a dictionary).

-   Keys used in the session must be strings and should not contain special characters.

```py
def view_counter(request):
 # Check if the 'counter' key exists in the session
 if 'counter' in request.session:
     # Increment the counter
     request.session['counter'] += 1
 else:
     # Initialize the counter if it's the first visit
     request.session['counter'] = 1

 counter = request.session['counter']

 return HttpResponse(f"View count: {counter}")
```

## Cookies

-   Metadata about the data.

-   The browser sends them with every request to the domain for which they were set.

-   Example: if a cookie `sessionId` is set for `localhost`, it will be sent with every request.

-   Cookies without an expiration date are deleted when the browser session ends.

-   We cannot create a cookie that lasts forever.

-   Cookies can be accessed using `request.COOKIES`.

```py
from django.http import HttpResponse
from django.utils.timezone import now
from django.views import View

class SetTimeCookieView(View):
    def dispatch(self, request, *args, **kwargs):
        # Call the parent dispatch method to get the response
        response = super().dispatch(request, *args, **kwargs)

        # Get the current time
        current_time = now()

        # Check if the 'last_visit' cookie exists
        last_visit = request.COOKIES.get('last_visit')
        if last_visit:
            # If the cookie exists, add a message about the last visit time
            response.content += f"Your last visit was on: {last_visit}<br>".encode()
        else:
            # If this is the first visit, add a message indicating that
            response.content += "This is your first visit!<br>".encode()

        # Set the current time as a cookie named 'last_visit'
        response.set_cookie('last_visit', current_time.strftime('%Y-%m-%d %H:%M:%S'))

        # Optionally, set the cookie to expire in a certain number of seconds (e.g., 1 day)
        # response.set_cookie('last_visit', current_time.strftime('%Y-%m-%d %H:%M:%S'), max_age=86400)

        # Add a message about setting the cookie
        response.content += f"Setting the current time ({current_time.strftime('%Y-%m-%d %H:%M:%S')}) as a cookie.".encode()

        return response
```

