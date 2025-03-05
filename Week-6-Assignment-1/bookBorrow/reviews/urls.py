# reviews/urls.py
from django.urls import path
from reviews.views import CommentView

urlpatterns = [
    path("details/<int:book_id>/", CommentView.as_view(), name="book_info"),
]
