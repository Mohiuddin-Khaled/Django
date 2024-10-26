from django.contrib import admin
from django.urls import path, include
from musicians_directory.views import homeListView, DeleteMusicianView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("music.urls")),
    path("", include("album.urls")),
    path("", include("authSYS.urls")),
    path("", homeListView.as_view(), name="home_page"),
    path("delete/<int:id>/", DeleteMusicianView.as_view(), name="delete_musician"),
]
