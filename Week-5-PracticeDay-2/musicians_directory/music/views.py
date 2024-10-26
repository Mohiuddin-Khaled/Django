from music.models import MusicianModel
from music.forms import MusicianForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class createMusician(LoginRequiredMixin, CreateView):
    model = MusicianModel
    template_name = "music_data.html"
    form_class = MusicianForm
    context_object_name = "form"
    success_url = reverse_lazy("home_page")


class editMusicView(LoginRequiredMixin, UpdateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = "music_data.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home_page")
