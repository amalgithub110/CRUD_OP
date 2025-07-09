from django import forms
from .models import add_money

class AddMoneyForm(forms.ModelForm):
    class Meta:
        model= add_money
        fields = '__all__'