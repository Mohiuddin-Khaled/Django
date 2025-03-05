from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from django.contrib.auth import login, logout
from accounts.forms import UserRegistrationForm, UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import ListView
from books.models import BookList
from transactions.models import Transaction
from accounts.models import UserBankAccount
from django.contrib import messages
from decimal import Decimal
from transactions.constants import PURCHASE, RETURN
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def BorrowEmail(user, amount, subject, template):
    message = render_to_string(
        template,
        {
            "user": user,
            "amount": amount,
        },
    )
    send_email = EmailMultiAlternatives(subject, "", to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()


class UserRegistrationView(FormView):
    template_name = "accounts/user_register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("home_page")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "accounts/user_login.html"

    def get_success_url(self):
        return reverse_lazy("user_profile")


@login_required
def UserLogoutView(request):
    logout(request)
    return redirect("user_login")


class UserUpdateView(LoginRequiredMixin, View):
    template_name = "accounts/user_profile.html"

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        transaction = Transaction.objects.filter(account__user=request.user)
        return render(
            request, self.template_name, {"form": form, "transactions": transaction}
        )

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("user_profile")
        return render(request, self.template_name, {"form": form})


class PurchaseView(LoginRequiredMixin, ListView):
    model = Transaction
    pk_url_kwargs = "book_id"

    def get(self, request, book_id):
        user_account = get_object_or_404(UserBankAccount, user=request.user)
        book = get_object_or_404(BookList, id=book_id)
        book_price = Decimal(str(book.borrow_price))

        if Transaction.objects.filter(
            account=user_account, book=book, transaction_type=PURCHASE
        ).exists():
            messages.error(request, f"You have already borrowed '{book.title}'.")
            return redirect("book_info", book_id)

        if user_account.balance < book_price:
            messages.error(request, "Insufficient balance!!")
            return redirect("book_info", book_id)

        try:
            user_account.balance -= book_price
            user_account.save()
            Transaction.objects.create(
                book=book,
                account=user_account,
                amount=book_price,
                transaction_type=PURCHASE,
                balance_after_transaction=user_account.balance,
                TrxID=Transaction().generate_transaction_id(),
            )
            book.borrower.add(request.user)
            messages.success(request, f"Successfully borrowed '{book.title}' book!")
            BorrowEmail(
                self.request.user,
                book_price,
                "Borrowed {book.title} book",
                "accounts/borrow_email.html",
            )
            return redirect("user_profile")

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect("book_info", book_id)


class ReturnBookView(LoginRequiredMixin, View):

    def get(self, request, book_id, *args, **kwargs):
        user_account = get_object_or_404(UserBankAccount, user=request.user)
        book = get_object_or_404(BookList, id=book_id)

        transaction = get_object_or_404(
            Transaction, account=user_account, book=book, transaction_type=PURCHASE
        )
        book_price = Decimal(str(book.borrow_price))
        user_account.balance += book_price
        user_account.save()

        Transaction.objects.create(
            book=book,
            account=user_account,
            amount=book_price,
            transaction_type=RETURN,
            balance_after_transaction=user_account.balance,
            TrxID=Transaction().generate_transaction_id(),
        )

        transaction.delete()
        messages.success(
            request,
            f"Book '{book.title}' returned successfully! ${book_price} has been refunded.",
        )
        return redirect("user_profile")
