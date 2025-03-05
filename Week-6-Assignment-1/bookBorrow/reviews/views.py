from django.shortcuts import redirect
from django.views.generic import DetailView
from reviews.models import ReviewModel
from books.models import BookList
from reviews.forms import ReviewForm
from transactions.models import Transaction
from transactions.constants import PURCHASE
from django.contrib import messages


class CommentView(DetailView):
    model = BookList
    pk_url_kwarg = "book_id"
    template_name = "reviews/details_review.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        has_borrowed = Transaction.objects.filter(
            book=self.object, account__user=request.user, transaction_type=PURCHASE
        ).exists()

        if not has_borrowed:
            messages.error(
                request, "You must borrow this book before leaving a review!"
            )
            return self.render_to_response(self.get_context_data(form=form))

        if form.is_valid():
            ReviewModel.objects.create(
                book=self.object,
                user=request.user,
                comment=form.cleaned_data["comment"],
            )
            return redirect("book_info", book_id=self.object.id)
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book"] = self.object
        context["reviews"] = self.object.comments.all()
        context["form"] = ReviewForm()
        return context
