from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, null=True, unique=True, blank=True)

    def __str__(self):
        return self.name


class BookWriter(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BookList(models.Model):
    image = models.ImageField(upload_to="books/media/uploads/", blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    borrow_price = models.FloatField()
    author = models.ForeignKey(to=BookWriter, on_delete=models.CASCADE)
    borrower = models.ManyToManyField(to=User, blank=True, null=True)

    def __str__(self):
        return self.title
