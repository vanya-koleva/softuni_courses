from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books_api import views

router = DefaultRouter()
router.register(r'', views.PublisherViewSet)

urlpatterns = [
    path('books/', views.ListBooksView.as_view(), name='books'),
    path('book/', include([
        path('', views.create_book, name='create-book'),
        path('<int:pk>/', views.BookViewSet.as_view(), name='book'),
    ])),
    path('publisher/', include(router.urls)),
    path('publisher-links/', views.PublisherHyperlinkView.as_view(), name='publisher-links')
]