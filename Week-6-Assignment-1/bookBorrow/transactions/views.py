from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from transactions.models import Transaction
from transactions.constants import DEPOSIT
from transactions.forms import DepositForm
from django.contrib.auth.mixins import LoginRequiredMixin
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


class TransactionView(LoginRequiredMixin, CreateView):
    template_name = "transactions/transaction_form.html"
    model = Transaction
    title = ""
    success_url = reverse_lazy("user_profile")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"account": self.request.user.account})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": self.title})

        return context


class DepositView(TransactionView):
    form_class = DepositForm
    title = "Deposit"

    def get_initial(self):
        initial = {"transaction_type": DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get("amount")
        account = self.request.user.account
        account.balance += amount
        account.save(update_fields=["balance"])

        messages.success(
            self.request,
            f'${"{:,.2f}".format(float(amount))} was deposited to your account successfully',
        )
        BorrowEmail(
            self.request.user,
            amount,
            "Deposit Amount",
            "transactions/deposit_email.html",
        )
        return super().form_valid(form)
