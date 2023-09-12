from django.db import models

# Create your models here.



class Blogs(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    blogImage = models.ImageField(blank= True , null = True,  max_length = 10000000000000 )

    def __str__(self):
        return self.author