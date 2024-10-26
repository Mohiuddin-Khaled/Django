from album.models import AlbumModel
from album.forms import AlbumForm
from music.models import MusicianModel

from django.urls import reverse_lazy

from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class homeListView(ListView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = "home.html"
    context_object_name = "object"


class DeleteMusicianView(LoginRequiredMixin, DeleteView):
    model = MusicianModel
    template_name = "delete.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = AlbumModel.objects.all()
        return context
