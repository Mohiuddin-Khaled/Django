from django.urls import path
from album.views import createAlbum, editAlbumView

urlpatterns = [
    path("album/", createAlbum.as_view(), name="album_url"),
    path("edit_album/<int:id>/", editAlbumView.as_view(), name="edit_album"),
]
