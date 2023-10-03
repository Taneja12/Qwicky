from django.db import models
from django import forms
# Create your models here.

class Product(models.Model):
    Title = models.CharField(max_length=30)
    product_id= models.CharField(max_length=30,unique=True)
    Description = models.CharField(max_length=1000)
    price = models.FloatField(max_length=30)
    img = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=30)

def __str__(self):
        return self.product_id


class Contact(models.Model):
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.subject
    