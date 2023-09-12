from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def Blog(request):
    post = Blogs.objects.all()
    return render(request, 'Blog/blog.html' , {'post' : post})
