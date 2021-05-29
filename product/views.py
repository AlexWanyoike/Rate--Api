from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render , redirect

# Create your views here.
def base(request):
    return render(request ,'all-products/base.html')

def main(request):
    return render(request ,'all-products/main.html')

def details(request):
    return render(request ,'details.html')

def profile(request):
    return render(request ,'profile.html')
