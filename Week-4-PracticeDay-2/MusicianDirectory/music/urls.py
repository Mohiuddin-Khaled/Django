from django.urls import path, include
from music.views import createMusician, editMusician

urlpatterns = [
    path("create/", createMusician, name="create_musician"),
    path("edit/<int:id>", editMusician, name="edit_musician"),
]
