from django import forms
from dashboard.models import RegistrationModel


class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegistrationModel
        fields = '__all__'
