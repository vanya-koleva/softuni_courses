from django.http import HttpResponse
from django.shortcuts import render

from department.models import Department


def index(request):
    return HttpResponse("<h1>Departments Home Page</h1>")

def int_param_view(request, pk):
    return HttpResponse(f"<h1>You are looking at department number {pk}</h1>")

def str_param_view(request, name):
    return HttpResponse(f"<h1>Department Name: {name}</h1>")

def slug_param_view(request, slug):
    department = Department.objects.filter(slug=slug).first()
    return HttpResponse(department)