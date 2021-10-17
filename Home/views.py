
from django.contrib import auth, messages
from django.db import models
from django.views.generic.list import ListView
from .models import Contact,Upload_Books,Orders,Seller
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contactus = Contact(name=name, email=email, phone=phone, desc=desc)
        contactus.save()
        # print(name)
    return render(request, 'Contactus.html')

def login1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutU(request):
    auth.logout(request)
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def upload_book(request):
    files = Upload_Books.objects.all()
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        # video_file = request.FILES.get('video_file')
        book_file = request.FILES.get('book_file')
        book_price = request.POST.get('book_price')

        file = Upload_Books.objects.create(book_name=book_name, book_file=book_file,book_price=book_price)

        file.save()
        return redirect('login.html')

    return render(request, 'upload_book.html', {"files": files})

def catalog(request):
    all_Materials = Upload_Books.objects.all()
    return render(request, 'catalog.html', {"Materials": all_Materials})


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id': id})
    return render(request, 'checkout.html')



def login_seller(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Seller.objects.filter(username=username, password=password):
            seller = Seller.objects.get(username=username)
            seller.save()
            return redirect('upload_book.html')

        else:
            messages.info(request, "Invalid Credentials")
            return redirect('/login_seller.html')

    return render(request, 'login_seller.html')
