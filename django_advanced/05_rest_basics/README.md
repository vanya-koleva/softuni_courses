# Django REST Basics

## API

-   Application Programming Interface

-   A way for us to connect to a given system; the collection of functionalities we can use on a system.

-   Abstract example:

    -   A phone's charging port and cable. The phone provides a way for us to charge it (with a cable).

## REST

-   ReprEsentational State Transfer

## REST API

-   A collection of endpoints through which we can interact with a system

-   Communication is primarily done via **JSON**, but we can send data in different formats

-   A REST API is **stateless**, meaning the client must store everything the API returns

-   We can have various clients:

    -   Mobile app
    -   Web app
    -   Washing machine
    -   ...

-   But they all send requests to the same API, which returns results in JSON format.

-   Examples:
    -   [Stripe](https://docs.stripe.com/api/connected-accounts)
    -   [Swapi](https://swapi.dev/)
    -   [PokeApi](https://pokeapi.co/)
    -   [Weather API](https://www.visualcrossing.com/weather-api?gad_source=1&gclid=CjwKCAjw59q2BhBOEiwAKc0ijb-nOtbeEpv4Mxv9iJdv6Okno4A4JNJiT1MATH_poGi5PHv2r32z9BoCF34QAvD_BwE)

## SPA vs MPA

-   **SPA - Single Page Application (Client Side Rendering)**

    -   An app usually built with a JS client (in the web context), which fetches new information by making API requests **without** reloading the page.

-   **MPA - Multi Page Application (Server Side Rendering)**

    -   Every time it needs to send new data, the app renders it as **HTML on the server** and sends back that HTML as a response. This results in the need to **reload** the page every time new data is needed or a request is made.

## Methods

-   We used forms in Django, but HTML forms support only POST and GET.

-   We can use all HTTP methods now.

## Django REST Framework

-   A package that allows us to create REST APIs

-   Very similar to Django

-   Provides us with **serialization**:

    -   A way to turn a Django model into a JSON object and vice versa

-   We could skip using it and return JSON using regular Django, but things become more complicated, as we would need to rewrite all Generic views, since they return templates by default.

```bash
pip install djangorestframework
```

```py
   INSTALLED_APPS = [
      ...,
      'rest_framework
      ...,
   ]
```

## Serializers

-   A way to convert a Django model into a JSON object and vice versa

-   Just like with forms, we have **Serializers** and **ModelSerializers**

```py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

// or with fbv

@api_view(['GET', 'POST'])
def book_list_create(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

## Django Generics vs DRF Generics

-   View

```py
   class SimpleView(View):
       def get(self, request, *args, **kwargs):
           context = {
               'message': 'Hello, this is a simple Django View!'
           }
           return render(request, 'simple_template.html', context)

   class SimpleAPIView(APIView):
       def get(self, request, *args, **kwargs):
           data = {
               'message': 'Hello, this is a simple APIView response!'
           }
           return Response(data)
```

-   ListView

```py
   # Django
   from django.views.generic import ListView
   from .models import Book

   class BookListView(ListView):
       model = Book
       template_name = 'books/book_list.html'

   # DRF
   from rest_framework import generics
   from .models import Book
   from .serializers import BookSerializer

   class BookListAPIView(generics.ListAPIView):
       queryset = Book.objects.all()
       serializer_class = BookSerializer

   @api_view(['GET'])
   def book_list(request):
       books = Book.objects.all()
       serializer = BookSerializer(books, many=True)
       return Response(serializer.data)
```

-   DetailView

```py
    from django.views.generic import DetailView
    from .models import Book

    class BookDetailView(DetailView):
        model = Book
        template_name = 'books/book_detail.html'

   # DRF
    from rest_framework import generics
    from .models import Book
    from .serializers import BookSerializer

    class BookDetailAPIView(generics.RetrieveAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer

    @api_view(['GET'])
    def book_detail(request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data)
```

-   CreateView

```py
   from django.views.generic import CreateView
   from .models import Book
   from .forms import BookForm

   class BookCreateView(CreateView):
       model = Book
       form_class = BookForm
       template_name = 'books/book_form.html'
       success_url = '/books/'

   # DRF
   from rest_framework import generics
   from .models import Book
   from .serializers import BookSerializer

   class BookCreateAPIView(generics.CreateAPIView):
       queryset = Book.objects.all()
       serializer_class = BookSerializer


   @api_view(['POST'])
   def book_create(request):
       serializer = BookSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

-   UpdateView

```py
from django.views.generic import UpdateView
from .models import Book
from .forms import BookForm

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = '/books/'

# DRF
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['PUT'])
def book_update(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

-   DeleteView

```py
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = '/books/'

# DRF
class BookDeleteAPIView(generics.DestroyAPIView):
   queryset = Book.objects.all()

@api_view(['DELETE'])
def book_delete(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
```

