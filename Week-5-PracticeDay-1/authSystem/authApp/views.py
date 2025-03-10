from django.shortcuts import render, redirect
from authApp.forms import RegisterForm, changeUserData
from django.contrib import messages
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                messages.success(request, "Account Create Successfully!")
                form.save()
        else:
            form = RegisterForm()
        return render(request, "signup.html", {"form": form})
    else:
        return redirect("profile")


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["username"]
            user_pass = form.cleaned_data["password"]
            user = authenticate(username=user_name, password=user_pass)
            login(request, user)
            messages.success(request, "Logged In Successfully")
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = changeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, "Account updated successfully")
                form.save()
        else:
            form = changeUserData(instance=request.user)
        return render(request, "profile.html", {"form": form})
    else:
        return redirect("register")


def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("homePage")


def oldPasswordChange(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, "pass_change.html", {"form": form})
    else:
        return redirect("login")


def passwordChange(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, "pass_change.html", {"form": form})
    else:
        return redirect("login")
