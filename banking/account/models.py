from django.contrib.auth.models import User
from django.db import models
import uuid

# Accounts
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=11, decimal_places=2)
    account_number = models.CharField(max_length=10, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account_number

    # Save generated account number to account
    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = self.generate_account_number()
        super().save(*args, **kwargs)

    # Function to generate account numbers
    def generate_account_number(self):
        return str(uuid.uuid4().fields[-1])[:10]

# Transaction types
DEPOSIT = 'DEPOSIT'
WITHDRAW = 'WITHDRAW'
TRANSFER = 'TRANSFER'

# Choices for transaction types
TRANSACTION_TYPES = [
    (DEPOSIT, 'Deposit'),
    (WITHDRAW, 'Withdraw'),
    (TRANSFER, 'Transfer'),
]

# Transactions for deposits, expenses, and transfers
class Transaction(models.Model):
    accounts = models.ManyToManyField(Account, through='TransactionAccount')
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    type = models.CharField(max_length=8, choices=TRANSACTION_TYPES)
    notes = models.TextField(max_length=250, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

# Accounts involved in transactions incase more than one
class TransactionAccount(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'Transaction: {self.transaction}, Account: {self.account.account_number}'
