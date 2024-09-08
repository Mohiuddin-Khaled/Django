from django import forms
from modelApp.models import StudentModel


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"
        # fields = ['name', 'roll']
        # exclude = ['roll']
        labels = {
            "roll": "Student Roll",
            "name": "Student Name",
        }
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3, "cols": 5}),
            "date": forms.DateInput(),
            "ip_address": forms.widgets.TextInput(),
        }
        error_message = {
            "name": {"required": "name is required"},
        }
