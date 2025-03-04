from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from accounts.constants import ACCOUNT_TYPE, GENDER_TYPE
from accounts.models import UserBankAccount, UserAddress


class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    street_address = forms.CharField(max_length=50)
    postal_code = forms.IntegerField()
    city = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "account_type",
            "first_name",
            "last_name",
            "birth_date",
            "gender",
            "street_address",
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
            street_address = self.cleaned_data.get("street_address")
            postal_code = self.cleaned_data.get("postal_code")
            city = self.cleaned_data.get("city")
            country = self.cleaned_data.get("country")

            UserBankAccount.objects.create(
                user=our_user,
                account_type=account_type,
                gender=gender,
                birth_date=birth_date,
                account_no=435234523 + our_user.id,
            )

            UserAddress.objects.create(
                user=our_user,
                street_address=street_address,
                postal_code=postal_code,
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
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    street_address = forms.CharField(max_length=50)
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
        # if account is exists
        if self.instance:
            try:
                user_account = self.instance.account
                user_address = self.instance.address
            except UserBankAccount.DoesNotExist:
                user_account = None
                user_address = None
            if user_account:
                self.fields["account_type"].initial = user_account.account_type
                self.fields["gender"].initial = user_account.gender
                self.fields["birth_date"].initial = user_account.birth_date
                self.fields["street_address"].initial = user_address.street_address
                self.fields["postal_code"].initial = user_address.postal_code
                self.fields["city"].initial = user_address.city
                self.fields["country"].initial = user_address.country

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_account, created = UserBankAccount.objects.get_or_create(user=user)
            user_address, created = UserAddress.objects.get_or_create(user=user)

            user_account.account_type = self.cleaned_data["account_type"]
            user_account.gender = self.cleaned_data["gender"]
            user_account.birth_date = self.cleaned_data["birth_date"]
            user_account.save()

            user_address.street_address = self.cleaned_data["street_address"]
            user_address.postal_code = self.cleaned_data["postal_code"]
            user_address.city = self.cleaned_data["city"]
            user_address.country = self.cleaned_data["country"]
            user_address.save()
        return user
