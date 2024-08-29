from django.contrib import admin
from django.urls import path, include
from project1.views import home, contact

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("contact/", contact),
    path("simpleApp/", include("simpleApp.urls")),
]
