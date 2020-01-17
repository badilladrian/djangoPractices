from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts


# Create your views here.

def index(request):

    post = Posts.objects.all()

    context = {
         'title': 'Latest Publications',
         'posts' : post
    }
    return render(request, 'posts/index.html',context)

def details(request, id):
  post = Posts.objects.get(id=id)
  context = {
    'post': post
  }
  return render(request, 'posts/details.html', context)