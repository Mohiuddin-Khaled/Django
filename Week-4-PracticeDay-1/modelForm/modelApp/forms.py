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
            "date": forms.DateTimeInput(attrs={"type": "date-time-local"}),
            "ip_address": forms.widgets.TextInput(),
        }
        help_text = {
            "name": "write your full name",
        }
        error_message = {
            "name": {"required": "name is required"},
        }
