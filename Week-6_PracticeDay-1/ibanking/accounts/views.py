from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm, UserUpdateForm
from django.views.generic import FormView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView


class UserRegistrationView(FormView):
    template_name = "accounts/user_registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("register")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "accounts/user_login.html"

    def get_success_url(self):
        return reverse_lazy("home")


class UserUpdateInfo(View):
    template_name = "accounts/profile.html"

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
        return render(request, self.template_name, {"form": form})


def UserLogoutView(request):
    logout(request)
    return redirect("login")
