from django.shortcuts import render
from album.models import AlbumModel
from music.models import MusicianModel


def home(request):
    albums = AlbumModel.objects.all()
    return render(request, "home.html", {"albums": albums})


def delete(request, id):
    musician_id = MusicianModel.objects.get(pk=id)
    musician_id.delete()
    albums = AlbumModel.objects.all()
    return render(request, "home.html", {"albums": albums})
