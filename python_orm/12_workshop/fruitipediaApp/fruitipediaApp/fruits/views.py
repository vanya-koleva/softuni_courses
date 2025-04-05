from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    return render(request, "common/index.html")


def dashboard_view(request):
    return render(request, "common/dashboard.html")


def create_fruit_view(request):
    return render(request, "fruits/create-fruit.html")


def fruit_details_view(request, pk):
    return render(request, "fruits/details-fruit.html")


def edit_fruit_view(request, pk):
    return render(request, "fruits/edit-fruit.html")


def delete_fruit_view(request, pk):
    return render(request, "fruits/delete-fruit.html")


def create_category_view(request):
    return render(request, "categories/create-category.html")
