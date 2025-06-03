from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from posts.forms import SearchForm
from posts.models import Post


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    search_form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == 'GET' and search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        posts = posts.filter(
            Q(title__icontains=query)
                |
            Q(content__icontains=query)
                |
            Q(author__icontains=query)
        )

    context = {
        'search_form': search_form,
        'posts': posts,
    }

    return render(request, 'posts/dashboard.html', context)


def post_details(request, pk:int ):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'posts/post-details.html', context)
