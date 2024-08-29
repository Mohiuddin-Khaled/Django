from django.contrib import admin
from django.urls import path, include
from simple_page_navigation.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("navigation/", include("navigation.urls")),
]
