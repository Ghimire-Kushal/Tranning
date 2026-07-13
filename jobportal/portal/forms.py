from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["full_name", "email", "phone", "cover_letter", "resume"]
        widgets = {
            "cover_letter": forms.Textarea(attrs={"rows": 6, "placeholder": "Why are you a good fit?"}),
            "full_name": forms.TextInput(attrs={"placeholder": "Enter your Full_Name "}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter Your Email"}),
            "phone": forms.TextInput(attrs={"placeholder": "Enter Your Number"}),
        }
    