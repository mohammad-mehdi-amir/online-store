from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('create/',order_create,name='order_create'),
    path('orders/',OrderListView.as_view(),name='order_list'),

    

]