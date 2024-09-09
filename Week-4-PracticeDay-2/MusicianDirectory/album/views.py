from django.shortcuts import render, redirect
from album.forms import AlbumForm
from album.models import AlbumModel


# Create your views here.
def createAlbum(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("homePage")
    else:
        form = AlbumForm()
    return render(request, "album/album_data.html", {"form": form})


def editAlbum(request, id):
    album = AlbumModel.objects.filter(id=id).first()
    form = AlbumForm(instance=album)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
        return redirect("homePage")

    return render(request, "album/album_data.html", {"form": form})
