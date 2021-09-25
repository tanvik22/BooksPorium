from django.urls import path
from Home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactus', views.contactus, name='contactus'),
]