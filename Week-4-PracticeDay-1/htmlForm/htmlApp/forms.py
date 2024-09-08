from django import forms
from django.forms.widgets import NumberInput
from django.core import validators

# favorite
color_choice = [
    ("blue", "Blue"),
    ("green", "Green"),
    ("black", "Black"),
]


# django form Api
class contactForm(forms.Form):
    name = forms.CharField(
        label="Full Name", help_text="Type your name", required=False
    )
    # comment = forms.CharField(widget=forms.Textarea)
    # email = forms.EmailField(label="User Email")
    age = forms.IntegerField(
        validators=[
            validators.MaxValueValidator(35, message="Age must be maximum 35"),
            validators.MinValueValidator(20, message="Age must be minimum 20"),
        ]
    )
    email_address = forms.EmailField(required=False, help_text="Type your email")
    # date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={"type": "date"}))
    # favorite_color = forms.ChoiceField(choices=color_choice)
    password = forms.CharField(widget=forms.PasswordInput())
    favorite_color = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=color_choice
    )
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    file_field = forms.FileField(
        validators=[
            validators.FileExtensionValidator(
                allowed_extensions=["pdf", "txt"],
                message="file extension must be ended with .txt .pdf",
            )
        ]
    )
    agree = forms.BooleanField()
