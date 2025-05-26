from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome to the forum app!")


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "Hello, world!",
                "author": "John Doe",
                "content": "This is my first post!",
                "created_at": datetime.now()
            },
            {
                "title": "how to work with templates?",
                "author": "",
                "content": "How can I work with templates in Django? This is my first time using templates.",
                "created_at": datetime.now()
            },
            {
                "title": "How to work with models?",
                "author": "Jane Doe",
                "content": "How can I work with models in Django? This is my first time using models.",
                "created_at": datetime.now()
            }
        ]
    }

    return render(request, 'base.html', context)
