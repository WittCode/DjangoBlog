from django.shortcuts import render
from .models import Post

# handle traffic from home page of blog.
# Map our url pattern to view function in url.py.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
