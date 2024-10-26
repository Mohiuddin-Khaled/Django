from django.urls import path
from authSYS.views import userCreateView, userLoginView, userProfileView, userLogoutView


urlpatterns = [
    path("register/", userCreateView.as_view(), name="user_register"),
    path("login/", userLoginView.as_view(), name="user_login"),
    path("profile/", userProfileView.as_view(), name="user_profile"),
    path("logout/", userLogoutView.as_view(), name="user_logout"),
]
