from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers', views.customers, name='customers'),
    path('createAnAccount', views.createAnAccount, name='createAnAccount'),
    path('transfer', views.transfer, name='trasfer'),
    path('accountDetails/<str:pk>', views.accountDetails, name='accountDetails'),
    path('transferHistory', views.transferHistory, name='transferHistory'),
    
]