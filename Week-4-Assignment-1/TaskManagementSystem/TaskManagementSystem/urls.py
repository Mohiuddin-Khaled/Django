from django.contrib import admin
from django.urls import path, include
from TaskManagementSystem.views import home


urlpatterns = [
    path("", home, name="homePage"),
    path("admin/", admin.site.urls),
    path("task/", include("task.urls")),
    path("category/", include("category.urls")),
]
