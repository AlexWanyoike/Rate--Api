from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request ,'all-products/base.html')

def main(request):
    return render(request ,'all-products/main.html')

def details(request):
    return render(request ,'details.html')

def profile(request):
    return render(request ,'profile.html')

def register(request):
    return render(request ,'/accounts/login.html')

def login(request):
    return render(request ,'/registration/login.html')

def edit_profile(request):
    return render(request ,'edit_profile.html')