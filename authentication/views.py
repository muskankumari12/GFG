from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def HomePage(request):                         # creating a functioncalled home to use request and response
    pass

def SignupPage(request):
    return render(request, 'templates/signup.html')

def LoginPage(request):
    pass
