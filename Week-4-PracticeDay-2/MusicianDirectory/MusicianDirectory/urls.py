from django.contrib import admin
from django.urls import path, include
from MusicianDirectory.views import home, delete

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="homePage"),
    path("musician/", include("music.urls")),
    path("album/", include("album.urls")),
    path("delete/<int:id>/", delete, name="delete_musician"),
]
