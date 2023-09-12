from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    productImage = models.ImageField(blank= True , null = True,  max_length = 10000000000000  )
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        ordering = ['-date_added'] 

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    product = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']