from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from plotly import express as px
from .models import *
from .forms import *
import pandas as pd

# Index view
def index(request):
    if request.user.is_authenticated:
        accounts = Account.objects.filter(user=request.user)
        account_numbers = [account.account_number for account in accounts]
        balances = [account.balance for account in accounts]
        chart_data = {
            'Account Number': account_numbers,
            'Balance': balances
        }
        chart_df = pd.DataFrame(chart_data)
        # Bar chart
        bar_chart = px.bar(chart_df, x='Account Number', y='Balance').to_html(full_html=False)
        # Pie chart
        pie_chart = px.pie(chart_df, names='Account Number', values='Balance').to_html(full_html=False)
        context = {
            'accounts': accounts,
            'user': request.user,
            'bar_chart': bar_chart,
            'pie_chart': pie_chart
        }
        return render(request, 'index.html', context)
    else:
        messages.error(request, 'You must be logged in to access this page, please register or login then try again!')
        return redirect('login')

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
                initial_transaction = Transaction.objects.create(user=request.user, amount=opening_balance, notes=opening_notes, type=DEPOSIT)
                TransactionAccount.objects.create(account=account, transaction=initial_transaction)
            messages.success(request, 'Account successfully created!')
            return redirect('home')
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
        return redirect('home')
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
                deposit_transaction = Transaction.objects.create(user=request.user, amount=amount, type=DEPOSIT, notes=notes)
                TransactionAccount.objects.create(account=account, transaction=deposit_transaction)
            messages.success(request, 'Deposit successful!')
            return redirect('home')
    else:
        form = DepositForm(initial={'account_number': account.account_number, 'current_balance': account.balance})
    context = {
        'form': form,
        'account': account
    }
    return render(request, 'account/deposit.html', context)
    
# Withdraw view
def withdraw(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            notes = form.cleaned_data['notes']
            with transaction.atomic():
                account.balance -= amount
                account.save()
                withdraw_transaction = Transaction.objects.create(user=request.user, amount=amount, type=WITHDRAW, notes=notes)
                TransactionAccount.objects.create(account=account, transaction=withdraw_transaction)
            messages.success(request, 'Withdraw successful!')
            return redirect('home')
    else:
        form = WithdrawForm(initial={'account_number': account.account_number, 'current_balance': account.balance})
    context = {
        'form': form,
        'account': account
    }
    return render(request, 'account/withdraw.html', context)
    