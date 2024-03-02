
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from .views import *
from django.views import generic
urlpatterns = [
    path('profile/',login_required(AccountDetailView.as_view()),name='profile'),
    path('profile/info',account_nfo,name='profile_info'),
    
]
