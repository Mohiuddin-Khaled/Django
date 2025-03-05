from django.db import models
from accounts.models import UserBankAccount
from transactions.constants import TRANSACTION_TYPE
from books.models import BookList
import random
import string


class Transaction(models.Model):
    account = models.ForeignKey(
        to=UserBankAccount, related_name="transactions", on_delete=models.CASCADE
    )
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    transaction_type = models.IntegerField(
        choices=TRANSACTION_TYPE, null=True, blank=True
    )
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits=12)
    timestamp = models.DateTimeField(auto_now_add=True)
    TrxID = models.CharField(max_length=10, unique=True, null=True)
    book = models.ForeignKey(
        to=BookList, null=True, blank=True, on_delete=models.CASCADE
    )

    def generate_transaction_id(self):
        length = 10
        characters = string.ascii_uppercase + string.digits
        while True:
            TrxID = "".join(random.choices(characters, k=length))
            if not Transaction.objects.filter(TrxID=TrxID):
                return TrxID

    def save(self, *args, **kwargs):
        if not self.TrxID:
            self.TrxID = self.generate_transaction_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.TrxID
