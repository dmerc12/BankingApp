from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from .models import *
from .forms import *

# Account list view
@login_required
def account_list(request):
    accounts = Account.objects.filter(user=request.user)
    context = {
        'accounts': accounts,
        'user': request.user
    }
    return render(request, 'account/list.html', context)

# Create account view
def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            opening_balance = form.cleaned_data['opening_balance']
            opening_notes = form.cleaned_data['opening_notes']

            # Ensuring balance is positive and non-zero
            if opening_balance <= 0:
                messages.error(request, 'Opening balance must be positive and non-zero, please try again!')
                return redirect('create-account')
            with transaction.atomic():
                account = Account(user=request.user, balance=opening_balance)
                account.save()
                initial_transaction = Transaction.objects.create(amount=opening_balance, notes=opening_notes, type=DEPOSIT)
                TransactionAccount.objects.create(account=account, transaction=initial_transaction)
            messages.success(request, 'Account successfully created!')
            return redirect('account-list')
    else:
        form = AccountForm()
    return render(request, 'account/create.html', {'form': form})

# Delete account view
def delete_account(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if request.method == 'POST':
        transaction_accounts = TransactionAccount.objects.filter(account=account)
        for transaction_account in transaction_accounts:
            account_transaction = transaction_account.transaction
            account_transaction.delete()
        account.delete()
        messages.success(request, f'Account {account.account_number} deleted!')
        return redirect('account-list')
    return  render(request, 'account/delete.html', {'account': account})

# Deposit view
def deposit(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            notes = form.cleaned_data['notes']
            with transaction.atomic():
                account.balance += amount
                account.save()
                deposit_transaction = Transaction.objects.create(amount=amount, type=DEPOSIT, notes=notes)
                TransactionAccount.objects.create(account=account, transaction=deposit_transaction)
            messages.success(request, 'Deposit successful!')
            return redirect('account-list')
    else:
        form = DepositForm(initial={'account_number': account.account_number})
    context = {
        'form': form,
        'account': account
    }
    return render(request, 'account/deposit.html', context)
    