
from behave import when

@when(u'I click "Transfer Money Between Accounts"')
def step_impl(context):
    context.banking_poms.transfer_collapse_button().click()

@when(u'I select the withdraw account input')
def step_impl(context):
    context.banking_poms.transfer_withdraw_account_select()

@when(u'I select the deposit account input')
def step_impl(context):
    context.banking_poms.transfer_deposit_account_select()

@when(u'I enter {transfer_amount} in the transfer amount input')
def step_impl(context, transfer_amount):
    context.banking_poms.transfer_amount_input().send_keys(transfer_amount)

@when(u'I click the Transfer button')
def step_impl(context):
    context.banking_poms.transfer_button().click()
