import time

from behave import when


@when(u'I click "Delete an Account"')
def step_impl(context):
    context.banking_poms.delete_account_collapse_button().click()

@when(u'I select an account')
def step_impl(context):
    context.banking_poms.select_account_to_delete()

@when(u'I click the Delete Account button')
def step_impl(context):
    context.banking_poms.delete_button().click()
