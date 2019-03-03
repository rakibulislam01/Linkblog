from django.shortcuts import render
from .models import Post

# Create your views here.
posts = [
    {
        'author': 'Rakib',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'February 28'
    },
    {
        'author': 'Cory',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'March 1'
    }
]


def home(request):
    context = {
        'title':'home',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
