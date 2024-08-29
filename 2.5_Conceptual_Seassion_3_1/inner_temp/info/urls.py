from django.urls import path
from info.views import details

urlpatterns = [
    path("", details),
]
