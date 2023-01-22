
from behave import when

@when(u'I click "Transfer Money Between Accounts"')
def step_impl(context):
    context.banking_poms.transfer_collapse_button().click()

@when(u'I enter {withdraw_account_number} in the withdraw account input')
def step_impl(context, withdraw_account_number):
    context.banking_poms.transfer_withdraw_account_input().send_keys(withdraw_account_number)

@when(u'I enter {deposit_account_number} in the deposit account input')
def step_impl(context, deposit_account_number):
    context.banking_poms.transfer_deposit_account_input().send_keys(deposit_account_number)

@when(u'I enter {transfer_amount} in the transfer amount input')
def step_impl(context, transfer_amount):
    context.banking_poms.transfer_amount_input().send_keys(transfer_amount)

@when(u'I click the Transfer button')
def step_impl(context):
    context.banking_poms.transfer_button().click()
