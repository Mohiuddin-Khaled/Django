from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from authSYS.forms import RegisterForm
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic.base import TemplateView


class userCreateView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    context_object_name = "form"
    success_url = reverse_lazy("user_login")


class userLoginView(LoginView):
    template_name = "login.html"

    def form_valid(self, form: AuthenticationForm):
        return super().form_valid(form)

    def form_invalid(self, form: AuthenticationForm):
        return super().form_invalid(form)


class userProfileView(LoginRequiredMixin, DetailView):
    form_class = RegisterForm
    template_name = "profile.html"
    context_object_name = "data"

    def get_object(self):
        return self.request.user


class userLogoutView(LoginRequiredMixin, TemplateView):
    template_name = "logout.html"

    def get(self, request):
        logout(request)
        return render(request, self.template_name)
