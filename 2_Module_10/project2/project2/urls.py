from django.contrib import admin
from django.urls import path, include
from project2.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("first_app/", include("first_app.urls")),
]
