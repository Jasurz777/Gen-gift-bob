from django import forms

from tg_bot.models import Interests


class InterestsForm(forms.ModelForm):
    class Meta:
        model = Interests
        fields = '__all__'

