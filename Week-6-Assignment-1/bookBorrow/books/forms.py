from django import forms
from books.models import BookList


class BookForm(forms.ModelForm):
    class Meta:
        model = BookList
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "cols": 15,
                }
            )
        }
