from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignupPage, name='signup'),   # creating a path for a file named home
    
]
