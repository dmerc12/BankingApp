from django import forms
from .models import *

# Createccount form
class CreateAccountForm(forms.ModelForm):
    account_number = forms.IntegerField(label='Account Number', widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Account Number'}))
    bank_name = forms.CharField(label='Bank Name', max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bank Name'}))
    location = forms.CharField(label='Bank Location', max_length=250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bank Location'}))
    opening_balance = forms.DecimalField(label='Opening Balance', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Opening Balance'}))
    opening_notes = forms.CharField(label='Notes', max_length=300, widget=forms.TextInput(attrs={'class':'form-control', 'row': 3, 'placeholder':'Opening Notes'}), required=False)

    class Meta:
        model = Account
        fields = ['account_number', 'bank_name', 'location', 'opening_balance', 'opening_notes']

# Update account form
class UpdateAccountForm(forms.ModelForm):
    account_number = forms.IntegerField(label='Account Number', widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Account Number'}))
    bank_name = forms.CharField(label='Bank Name', max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bank Name'}))
    location = forms.CharField(label='Bank Location', max_length=250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bank Location'}))
    balance = forms.DecimalField(label='Opening Balance', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Opening Balance', 'readonly': True}))
    notes = forms.CharField(label='Notes', max_length=300, widget=forms.TextInput(attrs={'class':'form-control', 'row': 3, 'placeholder':'Opening Notes'}), required=False)

    class Meta:
        model = Account
        fields = ['account_number', 'bank_name', 'location', 'balance', 'notes']

# Deposit form
class DepositForm(forms.Form):
    account = forms.CharField(label='Account Number', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    current_balance = forms.CharField(label='Current Balance', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    amount = forms.DecimalField(label='Deposit Amount', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Amount'}))
    notes = forms.CharField(label='Deposit Notes', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'rows': 3, 'placeholder':'Notes'}), required=False)

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['account'].initial = self.initial.get('account_number')
            self.fields['current_balance'].initial = self.initial.get('current_balance')

# Withdrawl form
class WithdrawForm(forms.Form):
    account = forms.CharField(label='Account Number', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    current_balance = forms.CharField(label='Current Balance', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    amount = forms.DecimalField(label='Withdraw Amount', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Amount'}))
    notes = forms.CharField(label='Withdraw Notes', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'rows': 3, 'placeholder':'Notes'}), required=False)

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['account'].initial = self.initial.get('account_number')
            self.fields['current_balance'].initial = self.initial.get('current_balance')
