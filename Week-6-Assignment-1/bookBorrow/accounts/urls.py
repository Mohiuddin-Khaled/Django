from django.urls import path
from accounts.views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserUpdateView,
    PurchaseView,
    ReturnBookView,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user_register"),
    path("login/", UserLoginView.as_view(), name="user_login"),
    path("logout/", UserLogoutView, name="user_logout"),
    path("profile/", UserUpdateView.as_view(), name="user_profile"),
    path("purchase/<int:book_id>/", PurchaseView.as_view(), name="purchase_book"),
    path("return_book/<int:book_id>/", ReturnBookView.as_view(), name="return_book"),
]
