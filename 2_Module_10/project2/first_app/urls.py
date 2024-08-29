from django.urls import path
from first_app.views import home

# from . import views
# from first_app import views

urlpatterns = [
    path("", home),
]
