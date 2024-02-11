from django import forms
from .models import *

# Account form
class AccountForm(forms.ModelForm):
    opening_balance = forms.DecimalField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Opening Balance'}))
    opening_notes = forms.CharField(label="", max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'rows': 3, 'placeholder':'Opening Notes'}), required=False)

    class Meta:
        model = Account
        fields = ['opening_balance', 'opening_notes']
