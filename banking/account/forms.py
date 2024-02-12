from django import forms
from .models import *

# Account form
class AccountForm(forms.ModelForm):
    opening_balance = forms.DecimalField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Opening Balance'}))
    opening_notes = forms.CharField(label="", max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'rows': 3, 'placeholder':'Opening Notes'}), required=False)

    class Meta:
        model = Account
        fields = ['opening_balance', 'opening_notes']

# Deposit form
class DepositForm(forms.Form):
    account = forms.CharField(label='Account Number', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    amount = forms.DecimalField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Deposit Amount'}))
    notes = forms.CharField(label="", max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'rows': 3, 'placeholder':'Notes'}), required=False)

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['account'].initial = self.initial.get('account_number')

    class Meta:
        fields = ['account', 'amount']
