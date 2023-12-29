
from django.contrib import admin
from django.urls import path,include
# from . import views
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('meal/', include('meal.urls')),
    path('about_us/', include('about_us.urls')),
]
