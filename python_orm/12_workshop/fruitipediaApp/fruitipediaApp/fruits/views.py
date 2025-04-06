from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CategoryForm, FruitAddForm
from .models import Fruit, Category


def index_view(request):
    return render(request, "common/index.html")


def dashboard_view(request):
    fruits = Fruit.objects.all()
    context = {"fruits": fruits}

    return render(request, "common/dashboard.html", context)


def create_fruit_view(request):
    if request.method == "GET":
        form = FruitAddForm()
    else:
        form = FruitAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {"form": form}

    return render(request, "fruits/create-fruit.html", context)


def fruit_details_view(request, pk):
    return render(request, "fruits/details-fruit.html")


def edit_fruit_view(request, pk):
    return render(request, "fruits/edit-fruit.html")


def delete_fruit_view(request, pk):
    return render(request, "fruits/delete-fruit.html")


def create_category_view(request):
    if request.method == "GET":
        form = CategoryForm()
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {"form": form}

    return render(request, "categories/create-category.html", context)
