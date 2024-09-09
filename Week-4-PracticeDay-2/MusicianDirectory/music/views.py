from django.shortcuts import render, redirect
from music.forms import MusicianForm
from music.models import MusicianModel


# Create your views here.
def createMusician(request):
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect("homePage")
    else:
        form = MusicianForm()
        return render(request, "music/music_data.html", {"form": form})


def editMusician(request, id):
    musician = MusicianModel.objects.get(pk=id)
    form = MusicianForm(instance=musician)
    if request.method == "POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
        return redirect("homePage")
    return render(request, "music/music_data.html", {"form": form})
