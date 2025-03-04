from django import forms
from transactions.models import Transaction
from accounts.models import UserBankAccount


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "amount",
            "transaction_type",
        ]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop("account")
        super().__init__(*args, **kwargs)
        self.fields["transaction_type"].disabled = True
        self.fields["transaction_type"].widget = forms.HiddenInput()

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()


class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get("amount")
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f"You need to deposit at least $ {min_deposit_amount}!!"
            )
        return amount


class WithdrawForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance
        amount = self.cleaned_data.get("amount")
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f"You can withdraw at least $ {min_withdraw_amount}!!"
            )

        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f"You can withdraw at most $ {max_withdraw_amount}!!"
            )

        if amount > balance:
            raise forms.ValidationError(
                f"You have $ {balance} in your account. "
                "You can not withdraw more than your account balance!!"
            )
        return amount


class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        return amount


class TransferForm(forms.ModelForm):
    sender_account_no = forms.CharField(
        label="Sender Account Number",
        max_length=12,
        required=True,
        widget=forms.TextInput(
            attrs={
                "readonly": "readonly",
                "class": "shadow appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight border rounded-md border-gray-500 focus:outline-none focus:shadow-outline",
            }
        ),
    )
    recipient_account_no = forms.CharField(
        label="Recipient Account Number",
        max_length=12,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "shadow appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight border rounded-md border-gray-500 focus:outline-none focus:shadow-outline"
            }
        ),
    )

    class Meta:
        model = Transaction
        fields = ["amount", "transaction_type"]
        widgets = {
            "amount": forms.NumberInput(
                attrs={
                    "class": "shadow appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight border rounded-md border-gray-500 focus:outline-none focus:shadow-outline"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        self.sender_account = kwargs.pop("sender_account")
        super().__init__(*args, **kwargs)
        self.fields["transaction_type"].widget = forms.HiddenInput()
        self.fields["transaction_type"].initial = 5
        self.fields["sender_account_no"].initial = self.sender_account.account_no

    def clean(self):
        cleaned_data = super().clean()
        sender_account_no = cleaned_data.get("sender_account_no")
        recipient_account_no = cleaned_data.get("recipient_account_no")
        amount = cleaned_data.get("amount")

        try:
            sender_account = UserBankAccount.objects.get(account_no=sender_account_no)
            recipient_account = UserBankAccount.objects.get(
                account_no=recipient_account_no
            )
        except UserBankAccount.DoesNotExist:
            raise forms.ValidationError("Invalid account number!!")

        if sender_account == recipient_account:
            raise forms.ValidationError(
                "Sender and recipient accounts must be different!!"
            )
        if amount < 500:
            raise forms.ValidationError("Balance transfer at least $ 500!")
        if amount > 10000:
            raise forms.ValidationError("Balance transfer at most $ 10000!")

        return cleaned_data

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        sender_account_no = cleaned_data["sender_account_no"]
        recipient_account_no = cleaned_data["recipient_account_no"]
        amount = cleaned_data["amount"]

        sender_account = UserBankAccount.objects.get(account_no=sender_account_no)
        recipient_account = UserBankAccount.objects.get(account_no=recipient_account_no)

        sender_account.balance -= amount
        recipient_account.balance += amount

        if commit:
            sender_account.save()
            recipient_account.save()

        transaction = super().save(commit=False)
        transaction.account = sender_account
        transaction.balance_after_transaction = sender_account.balance
        if commit:
            transaction.save()

        return transaction
