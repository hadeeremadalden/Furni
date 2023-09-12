from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.Shop, name="index"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
 
]
