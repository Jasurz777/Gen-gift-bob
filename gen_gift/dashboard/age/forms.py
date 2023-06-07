from django import forms
from tg_bot.models import Agee


class AgeForm(forms.ModelForm):
    class Meta:
        model = Agee
        fields = '__all__'
