from django import forms

from tg_bot.models import Situation


class SituationForm(forms.ModelForm):
    class Meta:
        model = Situation
        fields = '__all__'

