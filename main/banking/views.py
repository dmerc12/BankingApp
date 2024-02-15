from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction as database
from django.contrib import messages
from plotly import express as px
from .models import *
from .forms import *
import pandas as pd

# Index view
def index(request):
    if request.user.is_authenticated:
        accounts = Account.objects.filter(user=request.user)
        account_numbers = [str(account.account_number) for account in accounts]
        balances = [account.balance for account in accounts]
        chart_data = {
            'Account Number': account_numbers,
            'Balance': balances
        }
        chart_df = pd.DataFrame(chart_data)
        # Bar chart
        bar_chart = px.bar(chart_df, x='Account Number', y='Balance', orientation='v', category_orders={'Account Number': account_numbers}).to_html(full_html=False)
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
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            opening_balance = form.cleaned_data['opening_balance']
            timestamp = form.cleaned_data['timestamp']
            notes = form.cleaned_data['opening_notes']
            account_number = form.cleaned_data['account_number']
            bank_name = form.cleaned_data['bank_name']
            location = form.cleaned_data['location']
            notes = form.cleaned_data['opening_notes']
            if opening_balance <= 0:
                messages.error(request, 'Opening balance must be positive and non-zero, please try again!')
                return redirect('create-account')
            with database.atomic():
                account = Account.objects.create(user=request.user, account_number=account_number, bank_name=bank_name, location=location, balance=opening_balance, notes=notes)
                Transaction.objects.create(user=request.user, account=account, amount=opening_balance, notes=notes, timestamp=timestamp, type=DEPOSIT)
            messages.success(request, 'Account successfully created!')
            return redirect('home')
    else:
        form = CreateAccountForm()
    return render(request, 'banking/create_account.html', {'form': form})

# Update account view
def update_account(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if request.method == 'POST':
        form = UpdateAccountForm(request.POST, instance=account)
        if form.is_valid():
            account.account_number = form.cleaned_data['account_number']
            account.bank_name = form.cleaned_data['bank_name']
            account.location = form.cleaned_data['location']
            account.notes = form.cleaned_data['notes']
            account.save()
            messages.success(request, 'Account successfully updated!')
            return redirect('home')
    else:
        form = UpdateAccountForm(instance=account)
    context = {
        'form': form,
        'account': account
    }
    return render(request, 'banking/update_account.html', context)

# Delete account view
def delete_account(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if request.method == 'POST':
        account.delete()
        messages.success(request, f'Account {account.account_number} deleted!')
        return redirect('home')
    return  render(request, 'banking/delete_account.html', {'account': account})

# Deposit view
def deposit(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            timestamp = form.cleaned_data['timestamp']
            notes = form.cleaned_data['notes']
            with database.atomic():
                account.balance += amount
                account.save()
                Transaction.objects.create(user=request.user, account=account, amount=amount, timestamp=timestamp, type=DEPOSIT, notes=notes)
            messages.success(request, 'Deposit successful!')
            return redirect('home')
    else:
        form = DepositForm(initial={'account_number': account.account_number, 'current_balance': account.balance})
    context = {
        'form': form,
        'account': account
    }
    return render(request, 'banking/deposit.html', context)
    
# Withdraw view
def withdraw(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            timestamp = form.cleaned_data['timestamp']
            notes = form.cleaned_data['notes']
            with database.atomic():
                account.balance -= amount
                account.save()
                Transaction.objects.create(user=request.user, account=account, amount=amount, timestamp=timestamp, type=WITHDRAW, notes=notes)
            messages.success(request, 'Withdraw successful!')
            return redirect('home')
    else:
        form = WithdrawForm(initial={'account_number': account.account_number, 'current_balance': account.balance})
    context = {
        'form': form,
        'account': account
    }
    return render(request, 'banking/withdraw.html', context)
    
# Transfer view
def transfer(request, account_id):
    withdraw_account = get_object_or_404(Account, pk=account_id)
    if request.method == 'POST':
        form = TransferForm(request.user, withdraw_account.id, request.POST)
        if form.is_valid():
            deposit_account_id = form.cleaned_data['deposit']
            amount = form.cleaned_data['amount']
            timestamp = form.cleaned_data['timestamp']
            notes = form.cleaned_data['notes']
            deposit_account = Account.objects.get(pk=deposit_account_id)
            with database.atomic():
                withdraw_account.balance -= amount
                withdraw_account.save()
                deposit_account.balance += amount
                deposit_account.save()
                Transaction.objects.create(user=request.user, account=withdraw_account, timestamp=timestamp, amount=amount, type=WITHDRAW, notes=notes)
                Transaction.objects.create(user=request.user, account=deposit_account, timestamp=timestamp, amount=amount, type=DEPOSIT, notes=notes)
            messages.success(request, 'Transfer successful!')
            return redirect('home')
    else:
        form = TransferForm(request.user, withdraw_account.id, initial={'withdraw': f'{withdraw_account.account_number} - {withdraw_account.balance}'})
    context = {
        'form': form,
        'account': withdraw_account
    }
    return render(request, 'banking/transfer.html', context)

# View account transactions view
def transactions(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    transactions = Transaction.objects.filter(user=request.user, account=account)
    context = {
        'account': account,
        'transactions': transactions,
    }
    return render(request, 'banking/transaction_list.html', context)

# Delete transaction view
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    if request.method == 'POST':
        with database.atomic():
            if transaction.type == 'DEPOSIT':
                transaction.account.balance -= transaction.amount
            elif transaction.type == 'WITHDRAW':
                transaction.account.balance += transaction.amount
            transaction.account.save()
            if Transaction.objects.filter(account=transaction.account).count() > 1:
                transaction.delete()
                messages.success(request, 'Transaction successfully deleted!')
                return redirect('home')
            else:
                messages.error(request, 'If you wish to delete this transaction, please close the account!')
                return redirect('home')
    return render(request, 'banking/delete_transaction.html', {'transaction': transaction})

# Update transaction view
def update_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            updated_transaction = form.save(commit=False)
            if updated_transaction.amount != transaction.amount or updated_transaction.type != transaction.type:
                with database.atomic():
                    if transaction.type == 'DEPOSIT':
                        transaction.account.balance -= transaction.amount
                    elif transaction.type == 'WITHDRAW':
                        transaction.account.balance += transaction.amount
                    if updated_transaction.type == 'DEPOSIT':
                        transaction.account.balance += updated_transaction.amount
                    elif updated_transaction.type == 'WITHDRAW':
                        transaction.account.balance -= updated_transaction.amount
                    transaction.account.save()
                    updated_transaction.save()
                    messages.success(request, 'Transaction successfully updated!')
                    return redirect('home')
            else:
                updated_transaction.save()
                messages.success(request, 'Transaction successfully updated!')
                return redirect('home')
    else:
        form = TransactionForm(instance=transaction)
    context = {
        'form': form,
        'transaction': transaction
    }
    return render(request, 'banking/update_transaction.html', context)
