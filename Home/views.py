
from django.contrib import auth, messages
from django.db import models
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')
