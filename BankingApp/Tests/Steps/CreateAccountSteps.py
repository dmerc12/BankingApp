import time

from behave import when

@when(u'I click "Create a New AccountRoutes"')
def step_impl(context):
    context.banking_poms.create_new_account_collapse_button().click()

@when(u'I click the Create AccountRoutes button')
def step_impl(context):
    context.banking_poms.create_account_button().click()

@when(u'I enter {amount} in the starting amount')
def step_impl(context, amount: float):
    context.banking_poms.account_starting_balance_input().send_keys(amount)

@when(u'I click ok on the alert')
def step_impl(context):
    time.sleep(2)
    context.banking_poms.alert().accept()