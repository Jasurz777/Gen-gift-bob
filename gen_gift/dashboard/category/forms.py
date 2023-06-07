from django import forms
from tg_bot.models import Category


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
