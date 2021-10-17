from django.urls import path
from Home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login.html', views.login1,name = 'login1'),
    path('contactus', views.contactus, name='contactus'),
    path('catalog', views.catalog,name = 'catalog'),
    path('logout', views.logoutU,name = 'logout'),
    path('signup.html', views.signup,name = 'signup.html'),
    path('upload_book.html', views.upload_book, name='upload_book'),
    path('checkout', views.checkout,name = 'checkout'),
    path('login_seller.html', views.login_seller,name = 'login_seller'),
    path('vieworders', views.vieworders,name = 'vieworders'),
]