from django.contrib import admin
from django.urls import path, include
from core.views import BookListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", BookListView.as_view(), name="home_page"),
    path(
        "category/<slug:category_slug>/", BookListView.as_view(), name="category_post"
    ),
    path("accounts/", include("accounts.urls")),
    path("reviews/", include("reviews.urls")),
    path("transaction/", include("transactions.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
