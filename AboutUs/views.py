from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def AboutUs(request):
    header = Header.objects.all()
    testimonials = Testimonials.objects.all()
    services = Services.objects.all()
    team = Team.objects.all()
    return render(request, 'AboutUs/about.html' , { 'header':header ,
    'services':services , 'testimonials' : testimonials ,'team' : team })


