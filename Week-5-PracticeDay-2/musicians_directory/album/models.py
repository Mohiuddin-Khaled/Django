from django.db import models
from music.models import MusicianModel


# Create your models here.
class AlbumModel(models.Model):
    album_name = models.CharField(max_length=30)
    musician_name = models.ForeignKey(to=MusicianModel, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
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
