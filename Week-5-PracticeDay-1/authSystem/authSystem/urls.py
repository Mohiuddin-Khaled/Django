from django.contrib import admin
from django.urls import path, include
from authSystem.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="homePage"),
    path("", include("authApp.urls")),
]
