from django.contrib.auth.models import User
from django.db import models

# Accounts
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.PositiveIntegerField()
    bank_name = models.CharField(max_length=150)
    location = models.TextField(max_length=250)
    balance = models.DecimalField(max_digits=11, decimal_places=2)
    notes = models.TextField(max_length=300, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account_number

# Transaction types
DEPOSIT = 'DEPOSIT'
WITHDRAW = 'WITHDRAW'

# Choices for transaction types
TRANSACTION_TYPES = [
    (DEPOSIT, 'Deposit'),
    (WITHDRAW, 'Withdraw'),
]

# Transactions for deposits, expenses, and transfers
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accounts = models.ManyToManyField(Account, through='TransactionAccount')
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    type = models.CharField(max_length=8, choices=TRANSACTION_TYPES)
    notes = models.TextField(max_length=250, blank=True, null=True)
    timestamp = models.DateField()

    def __str__(self):
        return str(self.id)

# Accounts involved in transactions incase more than one
class TransactionAccount(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'Transaction: {self.transaction}, Account: {self.account.account_number}'
