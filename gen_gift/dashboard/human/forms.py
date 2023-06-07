from django import forms

from tg_bot.models import Human


class HumanForm1(forms.ModelForm):
    class Meta:
        model = Human
        fields = '__all__'

