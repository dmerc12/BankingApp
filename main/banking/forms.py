from django import forms
from .models import *

# Createccount form
class CreateAccountForm(forms.ModelForm):
    account_number = forms.IntegerField(label='Account Number', widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Account Number'}))
    bank_name = forms.CharField(label='Bank Name', max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bank Name'}))
    location = forms.CharField(label='Bank Location', max_length=250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bank Location'}))
    timestamp = forms.DateTimeField(label='Opening Date', widget=forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'}))
    opening_balance = forms.DecimalField(label='Opening Balance', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Opening Balance'}))
    opening_notes = forms.CharField(label='Notes', max_length=300, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Opening Notes'}), required=False)

    class Meta:
        model = Account
        fields = ['account_number', 'bank_name', 'location', 'timestamp', 'opening_balance', 'opening_notes']

# Update account form
class UpdateAccountForm(forms.ModelForm):
    account_number = forms.IntegerField(label='Account Number', widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Account Number'}))
    bank_name = forms.CharField(label='Bank Name', max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bank Name'}))
    location = forms.CharField(label='Bank Location', max_length=250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bank Location'}))
    balance = forms.DecimalField(label='Opening Balance', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Opening Balance', 'readonly': True}))
    notes = forms.CharField(label='Notes', max_length=300, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Opening Notes'}), required=False)

    class Meta:
        model = Account
        fields = ['account_number', 'bank_name', 'location', 'balance', 'notes']

# Deposit form
class DepositForm(forms.Form):
    account = forms.CharField(label='Account Number', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    current_balance = forms.CharField(label='Current Balance', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    timestamp = forms.DateTimeField(label='Deposit Date', widget=forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'}))
    amount = forms.DecimalField(label='Deposit Amount', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Amount'}))
    notes = forms.CharField(label='Deposit Notes', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Notes'}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['account'].initial = self.initial.get('account_number')
        self.fields['current_balance'].initial = self.initial.get('current_balance')

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount

# Withdrawl form
class WithdrawForm(forms.Form):
    account = forms.CharField(label='Account Number', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    current_balance = forms.CharField(label='Current Balance', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    timestamp = forms.DateTimeField(label='Withdraw Date', widget=forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'}))
    amount = forms.DecimalField(label='Withdraw Amount', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Amount'}))
    notes = forms.CharField(label='Withdraw Notes', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Notes'}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['account'].initial = self.initial.get('account_number')
        self.fields['current_balance'].initial = self.initial.get('current_balance')

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount

class TransactionForm(forms.ModelForm):
    id = forms.CharField(label='Transaction ID', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    type = forms.CharField(label='Transaction Type', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    timestamp = forms.DateField(label='Transaction Date and Time', widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    amount = forms.DecimalField(label='Transaction Amount', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Amount'}))
    notes = forms.CharField(label='Transaction Notes', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Notes'}), required=False)

    class Meta:
        model = Transaction
        fields = ['id', 'type', 'timestamp', 'amount', 'notes']
