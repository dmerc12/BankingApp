from behave import when

@when(u'I select {account} from the delete account dropdown')
def step_impl(context, account: int):
    context.account_poms.delete_account_dropdown().send_keys(account)


@when(u'I click the Delete Account button')
def step_impl(context):
    context.account_poms.delete_account_button().click()
