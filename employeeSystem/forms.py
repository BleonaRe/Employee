from django import forms
from django.contrib.auth.models import User
from employeeSystem.models import Employee


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("The two password fields must match.")
        return cleaned_data


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "role", "department", "salary", "contact", "user"]
