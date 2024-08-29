from django.contrib import admin
from django.urls import path
from first_app.views import Index, about

urlpatterns = [
    path("", Index, name="home"),
    # path("about/", about, name="about"),
    # path("about/page/<int:id>/", about, name="about"),
    path("about/", about, name="about"),
]
