from django.contrib import admin
from django.urls import path, include
from context_project.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("context_app/", include("context_app.urls")),
]
