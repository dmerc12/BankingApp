from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
from datetime import datetime, timedelta
from django.urls import reverse
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
    # Test for deposit form initialization
    def test_deposit_form_initializatoin(self):
        form = DepositForm()
        self.assertIn('account', form.fields.keys())
        self.assertIn('current_balance', form.fields.keys())
        self.assertIn('timestamp', form.fields.keys())
        self.assertIn('amount', form.fields.keys())
        self.assertIn('notes', form.fields.keys())

    # Test deposit form validation with negative amount
    def test_deposit_form_validation_amount_negative(self):
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

    # Test deposit form validation with amount 0
    def test_deposit_form_validation_amount_0(self):
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

    # Test deposit form validation with timestamp not a date
    def test_deposit_form_validation_timestamp_not_date(self):
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

    # Test deposit form validation success
    def test_deposit_form_validation_success(self):
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
    # Test for withdraw form initialization
    def test_withdraw_form_initialization(self):
        form = WithdrawForm()
        self.assertIn('account', form.fields.keys())
        self.assertIn('current_balance', form.fields.keys())
        self.assertIn('timestamp', form.fields.keys())
        self.assertIn('amount', form.fields.keys())
        self.assertIn('notes', form.fields.keys())

    # Test for withdraw form validation amount negative
    def test_withdraw_form_validation_amount_negative(self):
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

    # Test for withdraw form validation amount 0
    def test_withdraw_form_validation_amount_0(self):
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

    # Test for withdraw form validation timestamp not date
    def test_withdraw_form_validation_timestamp_not_date(self):
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

    # Test for withdraw form validation success
    def test_withdraw_form_validation_success(self):
        data = {
            'account': self.account1.id,
            'current_balance': self.account1.balance,
            'timestamp': datetime.now().date(),
            'amount': 2.45,
            'notes': 'test'
        }
        form = WithdrawForm(data=data)
        self.assertTrue(form.is_valid())

# Tests for bank models
class TestBankModels(TestCase):

    # Setup before tests
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.account = Account.objects.create(user=self.user, account_number=1234567890, bank_name='test_bank', location='test_location', balance=34.57, notes='notes')
        self.transaction = Transaction.objects.create(user=self.user, account=self.account, amount=15.63, type='DEPOSIT', notes='test', timestamp=datetime.now().date())
    
    # Tests for account model
    # Test for account model string
    def test_account_model_str(self):
        account_str = str(self.account)
        expected_str = f'{self.account.account_number} - {self.account.balance}'
        self.assertEqual(account_str, expected_str)

    # Tests for transaction model
    # Test for transaction model string
    def test_transaction_model_str(self):
        transaction_str = str(self.transaction)
        expected_str = f'{self.transaction.id}'
        self.assertEqual(transaction_str, expected_str)

# Tests for bank views
class TestBankViews(TestCase):

    # Setup before tests
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.account1 = Account.objects.create(user=self.user, account_number=1234567890, bank_name='test_bank', location='test_location', balance=343484.57, notes='notes')
        self.account2 = Account.objects.create(user=self.user, account_number=1234567890, bank_name='test_bank', location='test_location', balance=332334.57, notes='notes')
        self.account3 = Account.objects.create(user=self.user, account_number=1234567890, bank_name='test_bank', location='test_location', balance=332334.57, notes='notes')
        self.transaction1 = Transaction.objects.create(account=self.account1, user=self.user, amount=9.38, type='DEPOSIT', notes='test notes', timestamp=datetime.now().date())
        self.transaction2 = Transaction.objects.create(account=self.account1, user=self.user, amount=9.38, type='WITHDRAW', notes='test notes', timestamp=datetime.now().date())
        self.transaction3 = Transaction.objects.create(account=self.account2, user=self.user, amount=9.38, type='DEPOSIT', notes='test notes', timestamp=datetime.now().date())

    # Tests for index view
    # Test for index view if not logged in
    def test_index_view_not_logged_in(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test for index view when logged in
    def test_index_view_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('accounts', response.context)
        self.assertIn('user', response.context)
        self.assertIn('bar_chart', response.context)
        self.assertIn('pie_chart', response.context)
        self.assertEqual(len(response.context['accounts']), 3)
        self.assertEqual(response.context['user'], self.user)

    # Tests for create account view
    # Test for create account view if not logged in
    def test_create_account_view_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('create-account'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test for create account rendering success
    def test_create_account_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create-account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'banking/create_account.html')
        self.assertIsInstance(response.context['form'], CreateAccountForm)

    # Test for create account success
    def test_create_account_success(self):
        self.client.force_login(self.user)
        data = {
            'account_number': 12472890127,
            'bank_name': 'test bank',
            'location': 'test location',
            'timestamp': datetime.now().date(),
            'opening_balance': 50.67,
            'opening_notes': 'test notes'
        }
        response = self.client.post(reverse('create-account'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Account.objects.filter(account_number=data['account_number'], bank_name=data['bank_name'], location=data['location']).exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Account successfully created!', messages)

    # Test for create account with invalid opening balance
    def test_create_account_invalid_balance(self):
        self.client.force_login(self.user)
        data = {
            'account_number': 12472890127,
            'bank_name': 'test bank',
            'location': 'test location',
            'timestamp': datetime.now().date(),
            'opening_balance': -50.67, 
            'opening_notes': 'test notes'
        }
        response = self.client.post(reverse('create-account'), data=data)
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('create-account'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Opening balance must be positive and non-zero, please try again!', messages)

    # Tests for update account view
    # Test for update account view if not logged in
    def test_update_account_view_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('update-account', args=[self.account1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test for update account view rendering success
    def test_update_account_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('update-account', args=[self.account1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'banking/update_account.html')
        self.assertIsInstance(response.context['form'], UpdateAccountForm)

    # Test for update account view success
    def test_update_account_view_success(self):
        self.client.force_login(self.user)
        data = {
            'account_number': self.account1.pk,
            'bank_name': 'updated bank name',
            'location': 'updated location',
            'balance': self.account1.balance,
            'notes': 'updated notes'
        }
        response = self.client.post(reverse('update-account', args=[self.account1.pk]), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Account.objects.filter(account_number=data['account_number'], bank_name=data['bank_name'], location=data['location']).exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Account successfully updated!', messages)
        
    # Tests for delete account view
    # Test for delete account view if not logged in
    def test_delete_account_view_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('delete-account', args=[self.account3.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test for delete account view rendering success
    def test_delete_account_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('delete-account', args=[self.account3.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'banking/delete_account.html')

    # Test for delete account view success
    def test_delete_account_view_success(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('delete-account', args=[self.account3.pk]))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(f'Account {self.account3.account_number} deleted!', messages)
        self.assertFalse(Account.objects.filter(pk=self.account3.pk).exists())

    # Tests for deposit view
    # Test for deposit view if not logged in
    def test_deposit_view_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('deposit', args=[self.account1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test for deposit view rendering success
    def test_deposit_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('deposit', args=[self.account1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'banking/deposit.html')

    # Test for deposit view success
    def test_deposit_view_success(self):
        self.client.force_login(self.user)
        data = {
            'account': self.account1.account_number,
            'current_balance': self.account1.balance,
            'timestamp': datetime.now().date(),
            'amount': 5.34,
            'notes': 'test notes'
        }
        response = self.client.post(reverse('deposit', args=[self.account1.pk]), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertAlmostEqual(float(Account.objects.get(pk=self.account1.pk).balance), (float(self.account1.balance) + 5.34), places=2)
        self.assertTrue(Transaction.objects.filter(account=self.account1, amount=data['amount'], type='DEPOSIT', timestamp=data['timestamp'], notes=data['notes']).exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Deposit successful!', messages)

    # Tests for withdraw view
    # Test for withdraw view if not logged in
    def test_withdraw_view_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('withdraw', args=[self.account1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test for withdraw view rendering success
    def test_withdraw_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('withdraw', args=[self.account1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'banking/withdraw.html')

    # Test for withdraw view success
    def test_withdraw_view_success(self):
        self.client.force_login(self.user)
        data = {
            'account': self.account1.account_number,
            'current_balance': self.account1.balance,
            'timestamp': datetime.now().date(),
            'amount': 5.34,
            'notes': 'test notes'
        }
        response = self.client.post(reverse('withdraw', args=[self.account1.pk]), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertAlmostEqual(float(Account.objects.get(pk=self.account1.pk).balance), (float(self.account1.balance) - 5.34), places=2)
        self.assertTrue(Transaction.objects.filter(account=self.account1, amount=data['amount'], type='WITHDRAW', timestamp=data['timestamp'], notes=data['notes']).exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Withdraw successful!', messages)

    # Tests for view account transactions view
    # Test for view account transactions view if not logged in
    def test_view_account_transactions_view_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('transactions', args=[self.account1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test for view account transactions view rendering success
    def test_view_account_transactions_view_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('transactions', args=[self.account1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'banking/transaction_list.html')

    # Tests for update transaction view
    # Test for update transaction view if not logged in
    def test_update_transactions_view_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('update-transaction', args=[self.transaction2.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test for update transaction view rendering success
    def test_update_transaction_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('update-transaction', args=[self.transaction1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'banking/update_transaction.html')

    # Test for update transaction view success for deposit
    def test_update_transaction_view_success_deposit(self):
        self.client.force_login(self.user)
        data = {
            'id': self.transaction1.pk,
            'type': self.transaction1.type,
            'timestamp': (datetime.now().date() + timedelta(days=3)),
            'amount': 29.38,
            'notes': 'updated'
        }
        response = self.client.post(reverse('update-transaction', args=[self.transaction1.pk]), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertAlmostEqual(float(Account.objects.get(pk=self.transaction1.account.pk).balance), (self.transaction1.account.balance - self.transaction1.amount + data['amount']), places=2)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Transaction successfully updated!', messages)

    # Test for update transaction view success for withdraw
    def test_update_transaction_view_success_withdraw(self):
        self.client.force_login(self.user)
        data = {
            'id': self.transaction2.pk,
            'type': self.transaction2.type,
            'timestamp': (datetime.now().date() + timedelta(days=3)),
            'amount': 28.32,
            'notes': 'updated'
        }
        response = self.client.post(reverse('update-transaction', args=[self.transaction2.pk]), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertAlmostEqual(float(Account.objects.get(pk=self.transaction2.account.pk).balance), (self.transaction2.account.balance + self.transaction1.amount - data['amount']), places=2)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Transaction successfully updated!', messages)

    # Test for update transaction view success with amount unchanged
    def test_update_transaction_view_success_amount_unchanged(self):
        self.client.force_login(self.user)
        data = {
            'id': self.transaction2.pk,
            'type': self.transaction2.type,
            'timestamp': (datetime.now().date() + timedelta(days=3)),
            'amount': self.transaction2.amount,
            'notes': 'updated'
        }
        response = self.client.post(reverse('update-transaction', args=[self.transaction2.pk]), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        updated_transaction = Transaction.objects.get(pk=self.transaction2.pk)
        self.assertEqual(updated_transaction.timestamp, data['timestamp'])
        self.assertEqual(updated_transaction.notes, data['notes'])
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Transaction successfully updated!', messages)

    # Tests for delete transaction view
    # Test for delete transaction view if not logged in
    def test_delete_transactions_view_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('delete-transaction', args=[self.transaction1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test for delete transaction view rendering success
    def test_delete_transaction_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('delete-transaction', args=[self.transaction1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'banking/delete_transaction.html')

    # Test for delete transaction view success for deposit
    def test_delete_transaction_view_success_deposit(self):
        self.client.force_login(self.user)
        initial_balance = self.transaction1.account.balance
        response = self.client.post(reverse('delete-transaction', args=[self.transaction1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertAlmostEqual(float(Account.objects.get(pk=self.account1.pk).balance), initial_balance - self.transaction1.amount, places=2)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Transaction successfully deleted!', messages)

    # Test for delete transaction view success for withdraw
    def test_delete_transaction_view_success_withdraw(self):
        self.client.force_login(self.user)
        initial_balance = self.transaction2.account.balance
        response = self.client.post(reverse('delete-transaction', args=[self.transaction2.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertAlmostEqual(float(Account.objects.get(pk=self.account1.pk).balance), initial_balance + self.transaction2.amount, places=2)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Transaction successfully deleted!', messages)

    # Test for delete transaction view when it's the only transaction associated with the account
    def test_delete_transaction_view_only_transaction(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('delete-transaction', args=[self.transaction3.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('If you wish to delete this transaction, please close the account!', messages)
