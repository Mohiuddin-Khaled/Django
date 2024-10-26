from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BrandModel(models.Model):
    brand = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.brand


class CarModel(models.Model):
    car_image = models.ImageField(upload_to="car/media/uploads/", blank=True, null=True)
    car_name = models.CharField(max_length=30)
    car_brand = models.ForeignKey(to=BrandModel, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    car_price = models.FloatField()
    car_buyer = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.car_name
