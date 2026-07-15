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


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
