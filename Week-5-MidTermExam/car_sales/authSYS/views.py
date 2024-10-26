from django.shortcuts import render
from authSYS.forms import RegistrationForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.models import User
from car.models import CarModel
from django.contrib.auth.decorators import login_required


class userCreateView(CreateView):
    form_class = RegistrationForm
    template_name = "register.html"
    context_object_name = "form"
    success_url = reverse_lazy("user_login")


class userLoginView(LoginView):
    template_name = "login.html"

    def form_valid(self, form: AuthenticationForm):
        return super().form_valid(form)

    def form_invalid(self, form: AuthenticationForm):
        return super().form_invalid(form)


@login_required
def userProfileView(request):
    car_info = CarModel.objects.filter(car_buyer=request.user)
    return render(request, "profile.html", {"car_data": car_info})


class userLogoutView(LoginRequiredMixin, TemplateView):
    template_name = "logout.html"

    def get(self, request):
        logout(request)
        return render(request, self.template_name)


class editProfile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = RegistrationForm
    template_name = "update_profile.html"
    success_url = reverse_lazy("user_profile")

    def get_object(self):
        return self.request.user
