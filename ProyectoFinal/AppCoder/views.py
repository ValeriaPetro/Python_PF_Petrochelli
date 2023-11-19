from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def inicio_view(xx):
    return HttpResponse("Welcome to Benchmarking Tool")

def us_view(xx):
    #return HttpResponse("Who we are")
    return render(xx, "AppCoder/padre.html")

def business_view(xx):
    return HttpResponse("What we do")

def tool_view(xx):
    return HttpResponse("Request our services")
