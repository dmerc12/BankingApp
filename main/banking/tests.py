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

# Tests for bank models
class TestBankModels(TestCase):

    # Setup before tests
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.account = Account.objects.create(user=self.user, account_number=1234567890, bank_name='test_bank', location='test_location', balance=34.57, notes='notes')
        self.transaction = Transaction.objects.create(user=self.user, account=self.account, amount=15.63, type='DEPOSIT', notes='test', timestamp=datetime.now().date())
    
    # Tests for account model
    def test_account_model(self):
        # Test account string method
        account_str = str(self.account)
        expected_str = f'{self.account.account_number} - {self.account.balance}'
        self.assertEqual(account_str, expected_str)

    # Tests for transaction model
    def test_transaction_model(self):
        # Test transaction string method
        transaction_str = str(self.transaction)
        expected_str = f'{self.transaction.id}'
        self.assertEqual(transaction_str, expected_str)

# Tests for bank views
class TestBankViews(TestCase):

    # Setup before tests
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.account1 = Account.objects.create(user=self.user, account_number=1234567890, bank_name='test_bank', location='test_location', balance=34.57, notes='notes')
        self.account2 = Account.objects.create(user=self.user, account_number=1234567890, bank_name='test_bank', location='test_location', balance=34.57, notes='notes')

    # Tests for index view
    def test_index_view(self):
        # Test redirect if not logged in
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

        # Test success
        self.client.force_login(self.user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('accounts', response.context)
        self.assertIn('user', response.context)
        self.assertIn('bar_chart', response.context)
        self.assertIn('pie_chart', response.context)
        self.assertEqual(len(response.context['accounts']), 2)
        self.assertEqual(response.context['user'], self.user)

    # Tests for create account view

    # Tests for update account view

    # Tests for delete account view

    # Tests for deposit view

    # Tests for withdraw view

    # Tests for transfer view

    # Tests for view account transactions view

    # Tests for delete transaction view

    # Tests for update transaction view
