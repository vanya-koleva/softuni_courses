from django.urls import path, include

from books_api import views

urlpatterns = [
    path('books/', views.ListBooksView.as_view(), name='books'),
    path('book/', include([
        path('', views.create_book, name='create-book'),
        path('<int:pk>/', views.BookViewSet.as_view(), name='book'),
    ]))
]