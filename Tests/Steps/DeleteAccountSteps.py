from behave import when


@when(u'I click "Delete an Account"')
def step_impl(context):
    context.banking_poms.delete_account_collapse_button().click()

@when(u'I enter {account_number} in the delete account input')
def step_impl(context, account_number):
    context.banking_poms.delete_account_input().send_keys(account_number)

@when(u'I click the Delete Account button')
def step_impl(context):
    context.banking_poms.delete_button().click()
