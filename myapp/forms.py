from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SignupForm(UserCreationForm):

    class Meta:
        model = Client
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            'shipping_address',
            'city',
            'province',
        ]


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
    interested = forms.ChoiceField(widget=forms.RadioSelect, choices=[(1, 'Yes'), (0, 'No')], label='Interested?')
    quantity = forms.IntegerField(initial=1, min_value=1,  label='Quantity')
    comments = forms.CharField(widget=forms.Textarea, required=False, label='Comments')
