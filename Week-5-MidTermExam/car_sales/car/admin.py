from django.contrib import admin
from .models import BrandModel, CarModel

admin.site.register(CarModel)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("brand",)}
    list_display = ["brand", "slug"]


admin.site.register(BrandModel, CategoryAdmin)
