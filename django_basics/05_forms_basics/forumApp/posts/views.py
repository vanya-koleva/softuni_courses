from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from posts.forms import SearchForm, PostCreateForm, PostEditForm
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


def add_post(request):
    form = PostCreateForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'posts/add-post.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostEditForm(request.POST or None, instance=post)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'posts/edit-post.html', context)
