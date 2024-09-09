from django.db import models
from music.models import MusicianModel
import datetime


class AlbumModel(models.Model):
    album_name = models.CharField(max_length=200)
    release_date = models.DateTimeField(auto_now=True)
    musician_name = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    rating = models.CharField(
        choices=[
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
        ],
        max_length=20,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.album_name
