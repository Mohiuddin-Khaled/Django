from django.db import models
from django.contrib.auth.models import User


class UserBankAccount(models.Model):
    user = models.OneToOneField(
        to=User, related_name="account", on_delete=models.CASCADE
    )
    account_no = models.IntegerField(unique=True)
    initial_deposit_date = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.account_no)
