from django import forms
from .models import *


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'client',
            'product',
            'num_units',
        ]

    client = forms.RadioSelect()
    num_units = forms.IntegerField(min_value=1, initial=1, label='Quantity')


class InterestForm (forms.Form):
    intersted = forms.ChoiceField(widget=forms.RadioSelect, choices=[(1, 'Yes'), (0, 'No')], label='Interested?')
    quantity = forms.IntegerField(initial=1, min_value=1,  label='Quantity')
    comments = forms.CharField(widget=forms.Textarea, required=False, label='Comments')
