from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "htmlForm"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("htmlApp.urls")),
]
