from django.urls import path

from department import views

urlpatterns = [
    path('', views.index),
    path('<pk>/', views.int_param_view),
    path('<name>/', views.str_param_view),
]
