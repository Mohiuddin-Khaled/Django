from django.urls import path
from accounts.views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserUpdateInfo,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView, name="logout"),
    path("profile/", UserUpdateInfo.as_view(), name="profile"),
]
