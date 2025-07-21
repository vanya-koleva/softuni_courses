from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from books_api.models import Book
from books_api.serializers import BookSerializer


class ListBooksView(generics.ListAPIView):
    queryset = Book.objects.all()  # better do this for N+1 problem -> prefetch_related('authors')
    serializer_class = BookSerializer


class BookViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
        serializer.data,
        status.HTTP_201_CREATED
    )
