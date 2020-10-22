from django.shortcuts import render
from django.http import HttpResponse

# handle traffic from home page of blog.
# Map our url pattern to view function in url.py.

posts = [
    {
        'author': 'Tom',
        'title': 'My Name',
        'content': 'My first post.',
        'date_posted': '10/21/2020'
    },
    {
        'author': 'Micahel',
        'title': 'My Name Too',
        'content': 'Michael\'s post.',
        'date_posted': '10/21/2020'
    }
]


def home(request):
    global posts
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
