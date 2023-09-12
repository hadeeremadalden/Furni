from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def Shop(request):
    products = Post.objects.all()
    return render(request, 'Shop/shop.html' , {'products' : products })  


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'Shop/post_detail.html', {'post': post, 'form': form})