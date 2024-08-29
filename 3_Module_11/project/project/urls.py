from django.contrib import admin
from django.urls import path, include
from project.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("first/", include("first_app.urls")),
]
