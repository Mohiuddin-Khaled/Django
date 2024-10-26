from django.urls import path
from music.views import createMusician, editMusicView

urlpatterns = [
    path("music/", createMusician.as_view(), name="music_url"),
    path("edit/<int:id>/", editMusicView.as_view(), name="edit_musician"),
]
