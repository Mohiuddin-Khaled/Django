from django import forms
from music.models import MusicianModel


class MusicianForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = "__all__"

    help_text = {
        "email": "must use @ in email address",
    }
    error_massage = {
        "phone_number": {"required": "already exists"},
    }
