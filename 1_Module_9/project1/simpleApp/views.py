from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def appHome(request):
    return HttpResponse("This is app home page!")


def about(request):
    return HttpResponse("This is about page!")


def courses(request):
    return HttpResponse("This is courses page!")
