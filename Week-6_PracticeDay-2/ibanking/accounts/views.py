from django.shortcuts import redirect, render
from django.views.generic import FormView
from accounts.forms import UserRegistrationForm, UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.views import FormView, LoginView, PasswordChangeView
from django.views import View
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


def TransactionEmail(user, subject, template):
    message = render_to_string(
        template,
        {
            "user": user,
        },
    )
    send_email = EmailMultiAlternatives(subject, "", to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()


class UserRegistrationView(FormView):
    template_name = "accounts/user_registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("register")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(user)


class UserLoginView(LoginView):
    template_name = "accounts/user_login.html"

    def get_success_url(self):
        return reverse_lazy("home")


class UserOldPassChange(LoginRequiredMixin, PasswordChangeView):
    template_name = "accounts/pass_change.html"
    success_url = reverse_lazy("user_profile")

    def form_valid(self, form):
        update_session_auth_hash(self.request, form.user)
        TransactionEmail(
            self.request.user, "Old Password Change", "accounts/pass_email.html"
        )
        return super().form_valid(form)


class UserPassChange(LoginRequiredMixin, FormView):
    template_name = "accounts/pass_change.html"
    form_class = SetPasswordForm
    success_url = reverse_lazy("user_profile")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        TransactionEmail(
            self.request.user, "Password Change", "accounts/pass_email.html"
        )
        return super().form_valid(form)


class UserProfileView(View):
    template_name = "accounts/profile.html"

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("user_profile")
        return render(request, self.template_name, {"form": form})


def UserLogoutView(request):
    logout(request)
    return redirect("user_login")
