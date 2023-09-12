from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def Service(request):
    header = Header.objects.all()
    services = Services.objects.all()
    return render(request, 'Services/services.html' , {'header':header , 'services' : services})
