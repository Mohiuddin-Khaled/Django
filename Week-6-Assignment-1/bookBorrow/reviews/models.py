# reviews/models.py
from django.db import models
from django.contrib.auth.models import User
from books.models import BookList


class ReviewModel(models.Model):
    book = models.ForeignKey(
        BookList, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.book.title} by {self.user.username}"
