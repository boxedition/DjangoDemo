from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Eduardo',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 17, 2019'
    },
    {
        'author': 'Antonio',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 16, 2019'
    },

]
# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})