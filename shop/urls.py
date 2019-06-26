from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    
    path('/', views.index , name = 'ShopMain'),
    path('/about', views.about , name = 'AboutUs'),
    path('/tracker', views.tracker , name = 'Tracker'),
    path('/search', views.search , name = 'Search'),
    path('/productView/<myid>', views.productView , name = 'ProductView'),
    path('/contact', views.contact , name = 'Contact'),
    path('/checkOut/<mid>', views.checkOut , name = 'CheckOut'),
    path('/productView', views.productView1 , name = 'ProductView'),
    path('/checkOut', views.check , name = 'Check'),
    path('/handlerequest', views.handlerequest , name = 'handlerequest'),
    

    
]