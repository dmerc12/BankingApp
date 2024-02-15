from django import forms
from .models import *

# Createccount form
class CreateAccountForm(forms.ModelForm):
    account_number = forms.IntegerField(label='Account Number', widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Account Number'}))
    bank_name = forms.CharField(label='Bank Name', max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bank Name'}))
    location = forms.CharField(label='Bank Location', max_length=250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bank Location'}))
    timestamp = forms.DateTimeField(label='Transaction Date and Time', widget=forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'}))
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
    timestamp = forms.DateTimeField(label='Transaction Date and Time', widget=forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'}))
    amount = forms.DecimalField(label='Deposit Amount', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Amount'}))
    notes = forms.CharField(label='Deposit Notes', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Notes'}), required=False)

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['account'].initial = self.initial.get('account_number')
            self.fields['current_balance'].initial = self.initial.get('current_balance')

# Withdrawl form
class WithdrawForm(forms.Form):
    account = forms.CharField(label='Account Number', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    current_balance = forms.CharField(label='Current Balance', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    timestamp = forms.DateTimeField(label='Transaction Date and Time', widget=forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'}))
    amount = forms.DecimalField(label='Withdraw Amount', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Amount'}))
    notes = forms.CharField(label='Withdraw Notes', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Notes'}), required=False)

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['account'].initial = self.initial.get('account_number')
            self.fields['current_balance'].initial = self.initial.get('current_balance')

# Transfer form
class TransferForm(forms.Form):
    withdraw = forms.CharField(label='Withdraw Account', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    deposit = forms.ChoiceField(label='Deposit Account', choices=[], widget=forms.Select(attrs={'class': 'form-control'}))
    timestamp = forms.DateTimeField(label='Transaction Date and Time', widget=forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'})) 
    amount = forms.DecimalField(label='Transfer Amount', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Amount'}))
    notes = forms.CharField(label='Transfer Notes', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Notes'}), required=False)

    def __init__(self, user, withdraw_account_id, *args, **kwargs):
        super(TransferForm, self).__init__(*args, **kwargs)
        self.fields['withdraw'].initial = self.initial.get('withdraw')
        deposit_accounts = Account.objects.filter(user=user).exclude(id=withdraw_account_id)
        deposit_choices = [(account.id, f"{account.account_number} - {account.balance}") for account in deposit_accounts]
        self.fields['deposit'] = forms.ChoiceField(choices=deposit_choices, label='Deposit Account', widget=forms.Select(attrs={'class': 'form-control'}))

class TransactionForm(forms.ModelForm):
    id = forms.CharField(label='Transaction ID', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    type = forms.CharField(label='Transaction Type', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    timestamp = forms.DateField(label='Transaction Date and Time', widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    amount = forms.DecimalField(label='Transaction Amount', widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Amount'}))
    notes = forms.CharField(label='Transaction Notes', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Notes'}), required=False)

    class Meta:
        model = Transaction
        fields = ['id', 'type', 'timestamp', 'amount', 'notes']
