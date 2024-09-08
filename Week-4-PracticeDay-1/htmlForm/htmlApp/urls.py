from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.home, name="homePage"),
    path("form/", views.Form, name="htmlForm"),
    path("formApi", views.formApi, name="formApi"),
]
