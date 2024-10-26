from django.contrib import admin
from django.urls import path, include
from car_sales.views import CarList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("authSYS.urls")),
    path("", include("comments.urls")),
    path("", CarList, name="home_page"),
    path("category/<slug:category_slug>/", CarList, name="category_wise_post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
