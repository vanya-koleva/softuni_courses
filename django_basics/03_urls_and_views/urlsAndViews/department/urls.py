from django.urls import path

from department import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.int_param_view),
    path('<slug:slug>/',views.slug_param_view),
    path('<name>/', views.str_param_view),
]
