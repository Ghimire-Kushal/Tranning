from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["full_name", "email", "phone", "cover_letter", "resume"]
        widgets = {
            "cover_letter": forms.Textarea(attrs={"rows": 6, "placeholder": "Why are you a good fit?"}),
            "full_name": forms.TextInput(attrs={"placeholder": "Your full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+977 98..."}),
        }
        