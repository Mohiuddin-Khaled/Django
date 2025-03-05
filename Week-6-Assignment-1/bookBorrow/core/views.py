from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from books.models import Categories, BookList


class BookListView(ListView):
    model = BookList
    template_name = "home_page.html"
    context_object_name = "book_data"

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            book_category = get_object_or_404(Categories, slug=category_slug)
            return BookList.objects.filter(author__category__name=book_category)
        else:
            return BookList.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_data"] = Categories.objects.all()
        return context
