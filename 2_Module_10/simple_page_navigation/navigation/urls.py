from django.urls import path
from navigation.views import about, contact

urlpatterns = [
    path("about/", about),
    path("contact/", contact),
]
