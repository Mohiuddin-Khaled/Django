from django.urls import path
from authSYS.views import (
    userCreateView,
    userLoginView,
    userProfileView,
    userLogoutView,
    editProfile,
)


urlpatterns = [
    path("register/", userCreateView.as_view(), name="user_register"),
    path("login/", userLoginView.as_view(), name="user_login"),
    path("profile/", userProfileView, name="user_profile"),
    path("profile/edit/", editProfile.as_view(), name="edit_profile"),
    path("logout/", userLogoutView.as_view(), name="user_logout"),
]
