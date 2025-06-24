from datetime import datetime

from django.db.models import Q
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import classonlymethod
from django.views.generic import TemplateView, RedirectView

from posts.forms import PostCreateForm, PostDeleteForm, SearchForm, CommentForm, CommentFormSet
from posts.models import Post


def index(request):
    return render(request, 'index.html')


class IndexView(TemplateView):
    # template_name = 'index.html'
    # extra_context = {
    #     'current_time': datetime.now(), # calculates it once
    # }

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        kwargs.update({
            'current_time': datetime.now(), # every time the view is loaded
        })
        return kwargs

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ['index_for_admin.html']

        return ['ghjb', 'index.html']


# # Simple example of Django under the hood
# class MyView:
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.method == 'GET':
#             return self.get(request, *args, **kwargs)
#         ...
#
#     @classonlymethod
#     def as_view(cls):
#         def view(request, *args, **kwargs):
#             self = cls()
#             return self.dispatch(request, *args, **kwargs)
#
#         return view


def dashboard(request):
    search_form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == "GET" and search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        posts = posts.filter(
            Q(title__icontains=query)
                |
            Q(content__icontains=query)
                |
            Q(author__icontains=query)
        )

    context = {
        "posts": posts,
        "search_form": search_form,
    }

    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    form = PostCreateForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'posts/add-post.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    if request.user.is_superuser:
        PostEditForm = modelform_factory(Post, fields='__all__')
    else:
        PostEditForm = modelform_factory(Post, fields=('content',),)

    form = PostEditForm(request.POST or None, instance=post)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'posts/edit-post.html', context)


def post_details(request, pk: int):
    post = Post.objects.get(pk=pk)
    comment_form_set = CommentFormSet(request.POST or None)

    if request.method == "POST" and comment_form_set.is_valid():
        for form in comment_form_set:
            comment = form.save(commit=False)
            comment.author = request.user.username
            comment.post = post
            comment.save()
            return redirect('post-details', pk=post.pk)

    context = {
        "post": post,
        "formset": comment_form_set,
    }

    return render(request, 'posts/post-details.html', context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == "POST":
        post.delete()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'posts/delete-post.html', context)


class MyRedirectView(RedirectView):
    # url = 'http://localhost:8000/dashboard/'
    # pattern_name = 'dashboard'

    def get_redirect_url(self, *args, **kwargs):
        return reverse('dashboard') + "?query=Django"