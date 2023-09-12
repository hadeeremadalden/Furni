from django.db import models
from phone_field import PhoneField

# Create your models here.


class ContactUs(models.Model):
    address = models.CharField(max_length=3)
    email = models.EmailField()
    phone_number = PhoneField(blank=True, help_text='Contact phone number')

    

class Message(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Message'
        ordering = ['first_name']
        

    @property
    def name(self):
        return '{}  {}'.format(self.first_name , self.last_name)

    
