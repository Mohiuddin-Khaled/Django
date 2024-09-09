from django.urls import path
from category.views import createCategory

urlpatterns = [
    path("create/", createCategory, name="create_category"),
]
