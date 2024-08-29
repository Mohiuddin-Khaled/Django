from django.urls import path
from simpleApp.views import appHome, about, courses

urlpatterns = [
    path("", appHome),
    path("about/", about),
    path("courses/", courses),
]
