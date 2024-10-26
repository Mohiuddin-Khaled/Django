
from album.models import AlbumModel
from album.forms import AlbumForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class createAlbum(LoginRequiredMixin, CreateView):
    model = AlbumModel
    template_name = "album_data.html"
    form_class = AlbumForm
    context_object_name = "form"
    success_url = reverse_lazy("home_page")


class editAlbumView(LoginRequiredMixin, UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = "album_data.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home_page")
