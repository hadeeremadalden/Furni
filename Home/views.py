from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    products = Product.objects.all()
    product_description = ProductDescription.objects.all()
    testimonials = Testimonials.objects.all()
    header = Header.objects.all()
    services = Services.objects.all()
    help = Help.objects.all()
    popular_product = PouplarProduct.objects.all()
    post = Post.objects.all()
    return render(request, 'Home/index.html' , {'products' : products , 'header':header  ,
    'services':services , 'testimonials' : testimonials , 'product_description':product_description ,
    'popular_product':popular_product, 'help':help , 'post' : post})

def cart(request , slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'Home/cart.html' , {'product': product})
