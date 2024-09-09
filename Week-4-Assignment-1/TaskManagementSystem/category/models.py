from django.db import models
from task.models import TaskModel


# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    task = models.ManyToManyField(to=TaskModel, related_name="categories")

    def __str__(self):
        return self.name
