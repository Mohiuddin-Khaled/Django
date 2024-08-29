from django.contrib import admin
from django.urls import path, include
from inner_temp.views import home, about

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("about/", about),
    path("info/", include("info.urls")),
]
