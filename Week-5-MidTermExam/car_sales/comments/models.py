from django.db import models
from car.models import CarModel


# Create your models here.
class CommentModel(models.Model):
    car_info = models.ForeignKey(
        CarModel, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name}"
