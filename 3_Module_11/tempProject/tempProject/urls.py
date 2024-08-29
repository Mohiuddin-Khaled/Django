from django.contrib import admin
from django.urls import path, include
from tempProject.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="startPage"),
    path("tempApp/", include("tempApp.urls")),
]
