from django.urls import path, include

from posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('post/', include([
        path('details/<int:pk>/', views.post_details, name='post-details'),
    ]))
]