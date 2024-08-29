from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("This is home page")


def about(request):
    return render(request, "about.html")
