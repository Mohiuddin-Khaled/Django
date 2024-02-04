from django.urls import path, include

from . import views

urlpatterns = [
    path("form/", views.Form, name="htmlForm"),
    path("", views.home, name="homePage"),
    path("formApi", views.formApi, name="formApi"),
]
