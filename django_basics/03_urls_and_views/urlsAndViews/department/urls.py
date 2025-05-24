from django.urls import path, re_path

from department import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.int_param_view),
    path('<uuid:id>/', views.uuid_param_view),
    path('<slug:slug>/',views.slug_param_view),
    path('<name>/', views.str_param_view),
    re_path(r'^archive/(?P<archive_year>202[0-4])/$', views.regex_view),
    path('<path:path_to_file>/', views.file_path_param_view),
]
