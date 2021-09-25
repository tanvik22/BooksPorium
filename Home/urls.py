from django.urls import path
from Home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login.html', views.login1,name = 'login1'),
    path('contactus', views.contactus, name='contactus'),
    path('logout', views.logoutU,name = 'logout'),
    path('signup.html', views.signup,name = 'signup.html'),
    path('upload_book.html', views.upload_book, name='upload_book'),
]