from django.urls import path
from context_app.views import context_data

urlpatterns = [
    path("", context_data),
]
