from django.urls import path
from . import views

# from modelApp.views import home
urlpatterns = [
    path("", views.home, name="homePage"),
]
