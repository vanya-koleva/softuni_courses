from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from department.models import Department


def index(request):
    return HttpResponse("<h1>Departments Home Page</h1>")


def int_param_view(request, pk):
    return HttpResponse(f"<h1>You are looking at department number {pk}</h1>")


def str_param_view(request, name):
    return HttpResponse(f"<h1>Department Name: {name}</h1>")


def slug_param_view(request, slug):
    # department = Department.objects.filter(slug=slug).first()
    #
    # if not department:
    #     raise Http404

    department = get_object_or_404(Department, slug=slug)

    return render(request, "slug_template.html", {"department": department})


def file_path_param_view(request, path_to_file):
    return HttpResponse(f"<h1>The file is located at: {path_to_file}</h1>")


def uuid_param_view(request, id):
    return HttpResponse(f"<h1>The UUID is: {id}</h1>")


def regex_view(request, archive_year):
    return HttpResponse(f"<h1>The year is: {archive_year}</h1>")
