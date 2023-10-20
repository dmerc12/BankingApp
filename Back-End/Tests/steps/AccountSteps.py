from behave import when

@when(u'I click the manage accounts button')
def step_impl(context):
    context.account_poms.manage_accounts_button().click()


@when(u'I click the create account modal')
def step_impl(context):
    context.account_poms.create_account_modal().click()


@when(u'I input the {amount} in the starting balance input')
def step_impl(context, amount):
    context.account_poms.create_account_starting_balance_input().send_keys(amount)


@when(u'I click the create account button')
def step_impl(context):
    context.account_poms.create_account_button().click()


@when(u'I click the deposit modal on account {account}')
def step_impl(context, account):
    context.account_poms.deposit_modal(account).click()


@when(u'I input {amount} in the deposit amount input')
def step_impl(context, amount):
    context.account_poms.deposit_amount_input().send_keys(amount)


@when(u'I click the deposit button')
def step_impl(context):
    context.account_poms.deposit_button().click()

