from django import forms
from tg_bot.models import Cash


class CashForm(forms.ModelForm):
    class Meta:
        model = Cash
        fields = '__all__'
