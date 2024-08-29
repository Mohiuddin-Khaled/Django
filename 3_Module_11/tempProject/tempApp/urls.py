from django.contrib import admin
from django.urls import path
from tempApp.views import Index, about

urlpatterns = [
    path("", Index, name="home"),
    path("about", about, name="about"),
]
