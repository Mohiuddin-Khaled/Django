from django.shortcuts import render
from .forms import contactForm


# Create your views here.
def Form(request):
    return render(request, "bootstrapForm.html")


# html bootstrap form
def home(request):
    if request.method == "POST":
        # print(request.POST)
        name = request.POST.get("username")
        email = request.POST.get("email")
        select = request.POST.get("select")
        return render(
            request,
            "home.html",
            {"name": name, "email": email, "select": select},
        )
    else:
        return render(request, "base.html")


# django form ---> form Api
def formApi(request):
    if request.method == "POST":
        print(request.POST)
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = contactForm()
    return render(request, "formApi.html", {"form": form})
