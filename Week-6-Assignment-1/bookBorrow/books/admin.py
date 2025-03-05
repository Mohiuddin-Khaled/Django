from django.contrib import admin
from books.models import Categories, BookWriter, BookList


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(BookWriter)
admin.site.register(BookList)
