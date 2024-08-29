from django.urls import path, include
from notes.views import index, notes, note

app_name = "notes"
urlpatterns = [
    path("home/", index, name="index"),
    path("notes/", notes, name="notes"),
    path("note/<int:note_id>", note, name="note"),
]
