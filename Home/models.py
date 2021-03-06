from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
import string
import random

# Create your models here.
class Contact(models.Model):
    msgid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, default='')
    email = models.CharField(max_length=300, default='')
    phone = models.CharField(max_length=300, default='')
    desc = models.CharField(max_length=300, default='')

    def __str__(self):
             return self.email

class Upload_Books(models.Model):     
    # book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=200)
    book_file = models.FileField(upload_to="Material/", default="")
    book_price = models.CharField(max_length=200,default='')
    category = models.CharField(max_length=50, default="")

    def __str__(self):
             return self.book_name

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=300)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=300)
    state=models.CharField(max_length=300)
    zip_code=models.CharField(max_length=300)
    phone = models.CharField(max_length=300, default="")

    def __str__(self):
             return self.name


class Seller(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
