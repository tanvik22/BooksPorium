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

