from django.db import models


# Create your models here.
class MusicianModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=15)
    instrument = models.CharField(
        choices=[
            ("Guitar", "Guitar"),
            ("Piano", "Piano"),
            ("Drums", "Drums"),
            ("Violin", "Violin"),
            ("Flute", "Flute"),
            ("Trumpet", "Trumpet"),
            ("Ukulele", "Ukulele"),
        ],
        max_length=30,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.first_name
