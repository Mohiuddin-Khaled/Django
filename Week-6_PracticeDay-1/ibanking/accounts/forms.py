from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.constants import ACCOUNT_TYPE, GENDER_TYPE
from django.contrib.auth.models import User
from accounts.models import UserBankAccount, UserAddress


class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    user_address = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    city = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "account_type",
            "birth_date",
            "gender",
            "user_address",
            "postal_code",
            "city",
            "country",
        ]

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            account_type = self.cleaned_data.get("account_type")
            birth_date = self.cleaned_data.get("birth_date")
            gender = self.cleaned_data.get("gender")
            postal_code = self.cleaned_data.get("postal_code")
            user_address = self.cleaned_data.get("user_address")
            city = self.cleaned_data.get("city")
            country = self.cleaned_data.get("country")
            UserBankAccount.objects.create(
                user=our_user,
                account_type=account_type,
                gender=gender,
                birth_date=birth_date,
                account_no=100000 + our_user.id,
            )
            UserAddress.objects.create(
                user=our_user,
                postal_code=postal_code,
                user_address=user_address,
                city=city,
                country=country,
            )
        return our_user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": (
                        "appearance-none block w-full bg-gray-200 "
                        "text-gray-700 border border-gray-200 rounded "
                        "py-3 px-4 leading-tight focus:outline-none "
                        "focus:bg-white focus:border-gray-500"
                    )
                }
            )


class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    user_address = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    city = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": (
                        "appearance-none block w-full bg-gray-200 "
                        "text-gray-700 border border-gray-200 rounded "
                        "py-3 px-4 leading-tight focus:outline-none "
                        "focus:bg-white focus:border-gray-500"
                    )
                }
            )

        if self.instance:
            try:
                user_account = self.instance.account
                user_address = self.instance.address
            except UserBankAccount.DoesNotExist:
                user_account = None
                user_address = None
            if user_account:
                self.fields["birth_date"].initial = user_account.birth_date
                self.fields["gender"].initial = user_account.gender
                self.fields["account_type"].initial = user_account.account_type
                self.fields["user_address"].initial = user_address.user_address
                self.fields["postal_code"].initial = user_address.postal_code
                self.fields["city"].initial = user_address.city
                self.fields["country"].initial = user_address.country

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            user_account, created = UserBankAccount.objects.get_or_create(user=our_user)
            user_address, created = UserAddress.objects.get_or_create(user=our_user)

            user_account.account_type = self.cleaned_data["account_type"]
            user_account.birth_date = self.cleaned_data["birth_date"]
            user_account.gender = self.cleaned_data["gender"]
            user_account.save()

            user_address.user_address = self.cleaned_data["user_address"]
            user_address.postal_code = self.cleaned_data["postal_code"]
            user_address.city = self.cleaned_data["city"]
            user_address.country = self.cleaned_data["country"]
            user_address.save()
        return our_user
