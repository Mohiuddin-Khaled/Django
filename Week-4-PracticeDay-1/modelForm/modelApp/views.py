from django.shortcuts import render, redirect
from . import forms


# Create your views here.
def home(request):
    if request.method == "POST":
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            std = form.save()
            return render(request, "info.html", {"std": std})

    else:
        form = forms.StudentForm()
    return render(request, "home.html", {"form": form})
