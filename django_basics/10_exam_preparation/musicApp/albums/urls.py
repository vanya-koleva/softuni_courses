from django.urls import path, include

from albums import views

urlpatterns = [
    path('add/', views.AlbumCreateView.as_view(), name='create-album'),
    path('<int:id>/', include([
        path('details/', views.AlbumDetailsView.as_view(), name='album-details'),
    ]))
]