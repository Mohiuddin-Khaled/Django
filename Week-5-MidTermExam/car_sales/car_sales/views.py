from django.shortcuts import render
from car.models import CarModel, BrandModel


def CarList(request, category_slug=None):
    car_data = CarModel.objects.all()
    if category_slug:
        try:
            brand = BrandModel.objects.get(slug=category_slug)
            car_data = CarModel.objects.filter(car_brand=brand)
        except BrandModel.DoesNotExist:
            car_data = CarModel.objects.none()

    brand_data = BrandModel.objects.all()
    return render(
        request, "home.html", {"car_data": car_data, "brand_data": brand_data}
    )
