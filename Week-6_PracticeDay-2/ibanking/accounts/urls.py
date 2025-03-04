from django.urls import path
from accounts.views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    UserPassChange,
    UserOldPassChange,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="user_login"),
    path("pass_change/", UserPassChange.as_view(), name="pass_change"),
    path("old_pass_change/", UserOldPassChange.as_view(), name="old_pass_change"),
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path("logout/", UserLogoutView, name="user_logout"),
]
