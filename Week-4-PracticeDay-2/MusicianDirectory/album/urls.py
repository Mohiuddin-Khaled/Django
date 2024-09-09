from django.urls import path, include
from album.views import createAlbum, editAlbum

urlpatterns = [
    path("create/", createAlbum, name="create_album"),
    path("edit/<int:id>", editAlbum, name="edit_album"),
]
