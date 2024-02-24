from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from .models import *
from .forms import *

# Tests for bank forms
class TestBankForms(TestCase):

    # Setup before tests
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.account1 = Account.objects.create(user=self.user, account_number=1234567890, bank_name='test_bank', location='test_location', balance=34.57, notes='notes')
        self.account2 = Account.objects.create(user=self.user, account_number=1234567890, bank_name='test_bank', location='test_location', balance=34.57, notes='notes')

    # Tests for deposit form
    def test_deposit_form(self):
        # Test form initialization
        form = DepositForm()
        self.assertIn('account', form.fields.keys())
        self.assertIn('current_balance', form.fields.keys())
        self.assertIn('timestamp', form.fields.keys())
        self.assertIn('amount', form.fields.keys())
        self.assertIn('notes', form.fields.keys())

        ## Test form validation
        # Test amount negative
        data = {
            'account': self.account1.id,
            'current_balance': self.account1.balance,
            'timestamp': datetime.now().date(),
            'amount': -52.45,
            'notes': 'test'
        }
        form = DepositForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)

        # Test amount 0
        data = {
            'account': self.account1.id,
            'current_balance': self.account1.balance,
            'timestamp': datetime.now().date(),
            'amount': 0,
            'notes': 'test'
        }
        form = DepositForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)

        # Test timestamp not date
        data = {
            'account': self.account1.id,
            'current_balance': self.account1.balance,
            'timestamp': '1245392034',
            'amount': 0,
            'notes': 'test'
        }
        form = DepositForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('timestamp', form.errors)

        # Test success
        data = {
            'account': self.account1.id,
            'current_balance': self.account1.balance,
            'timestamp': datetime.now().date(),
            'amount': 52.45,
            'notes': 'test'
        }
        form = DepositForm(data=data)
        self.assertTrue(form.is_valid())

    # Tests for withdraw form
    def test_withdraw_form(self):
        # Test form initialization
        form = WithdrawForm()
        self.assertIn('account', form.fields.keys())
        self.assertIn('current_balance', form.fields.keys())
        self.assertIn('timestamp', form.fields.keys())
        self.assertIn('amount', form.fields.keys())
        self.assertIn('notes', form.fields.keys())

        ## Test form validation
        # Test amount negative
        data = {
            'account': self.account1.id,
            'current_balance': self.account1.balance,
            'timestamp': datetime.now().date(),
            'amount': -52.45,
            'notes': 'test'
        }
        form = WithdrawForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)

        # Test amount 0
        data = {
            'account': self.account1.id,
            'current_balance': self.account1.balance,
            'timestamp': datetime.now().date(),
            'amount': 0,
            'notes': 'test'
        }
        form = WithdrawForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)

        # Test timestamp not date
        data = {
            'account': self.account1.id,
            'current_balance': self.account1.balance,
            'timestamp': '1245392034',
            'amount': 0,
            'notes': 'test'
        }
        form = WithdrawForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('timestamp', form.errors)

        # Test success
        data = {
            'account': self.account1.id,
            'current_balance': self.account1.balance,
            'timestamp': datetime.now().date(),
            'amount': 2.45,
            'notes': 'test'
        }
        form = WithdrawForm(data=data)
        self.assertTrue(form.is_valid())

    # Test for transfer form
    def test_transfer_form(self):
        # Test form initialization
        form = TransferForm(user=self.user, withdraw_account_id=self.account2.id)
        self.assertIn('withdraw', form.fields.keys())
        self.assertIn('deposit', form.fields.keys())
        self.assertIn('timestamp', form.fields.keys())
        self.assertIn('amount', form.fields.keys())
        self.assertIn('notes', form.fields.keys())

        ## Test form validation
        # Test amount negative
        data = {
            'withdraw': self.account2.id,
            'deposit': self.account1.id,
            'timestamp': datetime.now().date(),
            'amount': -52.45,
            'notes': 'test'
        }
        form = TransferForm(user=self.user, withdraw_account_id=self.account2.id, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)

        # Test amount 0
        data = {
            'withdraw': self.account1.id,
            'deposit': self.account2.id,
            'timestamp': datetime.now().date(),
            'amount': 0,
            'notes': 'test'
        }
        form = TransferForm(user=self.user, withdraw_account_id=self.account2.id, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)

        # Test timestamp not date
        data = {
            'withdraw': self.account1.id,
            'deposit': self.account2.id,
            'timestamp': '1245392034',
            'amount': 0,
            'notes': 'test'
        }
        form = TransferForm(user=self.user, withdraw_account_id=self.account2.id, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('timestamp', form.errors)

        # Test success
        data = {
            'withdraw': self.account2.id,
            'deposit': self.account1.id,
            'timestamp': datetime.now().date(),
            'amount': 2.45,
            'notes': 'test'
        }
        form = TransferForm(user=self.user, withdraw_account_id=self.account2.id, data=data)
        self.assertTrue(form.is_valid())

