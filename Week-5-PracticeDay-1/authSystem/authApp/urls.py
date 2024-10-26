from django.contrib import admin
from django.urls import path, include
from authApp.views import (
    user_signup,
    user_login,
    profile,
    user_logout,
    oldPasswordChange,
    passwordChange,
)

urlpatterns = [
    path("signup/", user_signup, name="user_signup"),
    path("login/", user_login, name="user_login"),
    path("profile/", profile, name="profile"),
    path("logout/", user_logout, name="user_logout"),
    path("old_password/", oldPasswordChange, name="old_password"),
    path("password/", passwordChange, name="password"),
]
