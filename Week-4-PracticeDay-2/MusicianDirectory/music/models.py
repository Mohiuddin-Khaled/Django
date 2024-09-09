from django.db import models


class MusicianModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(
        choices=[
            ("guitar", "Guitar"),
            ("piano", "Piano"),
            ("violin", "Violin"),
        ],
        max_length=20,
    )

    def __str__(self):
        return self.first_name
