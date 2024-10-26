from django.urls import path
from comments.views import CarInfo, UpdateQuantity

urlpatterns = [
    path("car_details/<int:id>/", CarInfo.as_view(), name="car_comments"),
    path("buy_car/<int:car_id>/", UpdateQuantity, name="buy_car"),
]
