from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from .models import *
from .forms import *

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
                initial_transaction = Transaction(amount=opening_balance, notes=opening_notes, type=DEPOSIT)
                initial_transaction.save()
                transaction_account = TransactionAccount(account=account, transaction=initial_transaction)
                transaction_account.save()
            messages.success(request, 'Account successfully created!')
            return redirect('home')
    else:
        form = AccountForm()
    return render(request, 'account/create.html', {'form': form})
