from django.db import models

# Create your models here.

class Header(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    headerImage =models.ImageField(blank= True , null = True,  max_length = 10000000000000 )



class Services(models.Model):
    title =  models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    service_title1 = models.CharField(max_length=50)
    service_description1 = models.CharField(max_length=200)
    service_title2 = models.CharField(max_length=50)
    service_description2 = models.CharField(max_length=200)
    service_title3 = models.CharField(max_length=50)
    service_description3 = models.CharField(max_length=200)
    service_title4 = models.CharField(max_length=50)
    service_description4 = models.CharField(max_length=200)
    Image = models.ImageField(blank= True , null = True,  max_length = 10000000000000 )
  
    def __str__(self):
        return "service"

class Team(models.Model):
    name = models.CharField(max_length=15)
    role = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    Image = models.ImageField(blank= True , null = True,  max_length = 10000000000000 )
   
    def __str__(self):
        return self.name
    

class Testimonials(models.Model):
    name = models.CharField(max_length=15)
    role = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    Image1 = models.ImageField(blank= True , null = True,  max_length = 10000000000000 )
    Image2 = models.ImageField(blank= True , null = True,  max_length = 10000000000000 )
    Image3 = models.ImageField(blank= True , null = True,  max_length = 10000000000000 )


    def __str__(self):
        return self.name
