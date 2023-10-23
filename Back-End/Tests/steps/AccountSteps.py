from behave import when


@when(u'I click the manage accounts button in the navigation bar')
def step_impl(context):
    context.account_poms.click_manage_accounts_nav_button()


@when(u'I click the manage accounts button')
def step_impl(context):
    context.account_poms.click_manage_accounts_button()


@when(u'I click the create account modal')
def step_impl(context):
    context.account_poms.click_create_account_modal()


@when(u'I input the {starting_balance} in the starting balance input')
def step_impl(context, starting_balance):
    context.account_poms.input_create_account_starting_balance(starting_balance)


@when(u'I click the create account button')
def step_impl(context):
    context.account_poms.click_create_account_button()


@when(u'I click the deposit modal on account {account_number}')
def step_impl(context, account_number):
    context.account_poms.click_deposit_modal(account_number)


@when(u'I input {amount} in the deposit amount input')
def step_impl(context, amount):
    context.account_poms.input_deposit_amount_input(amount)


@when(u'I click the deposit button')
def step_impl(context):
    context.account_poms.click_deposit_button()


@when(u'I click the withdraw modal on account {account_number}')
def step_impl(context, account_number):
    context.account_poms.click_withdraw_modal(account_number)


@when(u'I input {withdraw_amount} in the withdraw amount input')
def step_impl(context, withdraw_amount):
    context.account_poms.input_withdraw_amount_input(withdraw_amount)


@when(u'I click the withdraw button')
def step_impl(context):
    context.account_poms.click_withdraw_button()


@when(u'I click the transfer modal')
def step_impl(context):
    context.account_poms.click_transfer_modal()


@when(u'I click the transfer from account input')
def step_impl(context):
    context.account_poms.click_transfer_withdraw_account_input()


@when(u'I click account {withdraw_account_number} as transfer from account')
def step_impl(context, withdraw_account_number):
    context.account_poms.click_transfer_account(withdraw_account_number)


@when(u'I click the transfer to account input')
def step_impl(context):
    context.account_poms.click_transfer_deposit_account_input()


@when(u'I click account {deposit_account_number} as the transfer to account')
def step_impl(context, deposit_account_number):
    context.account_poms.click_transfer_account(deposit_account_number)


@when(u'I input {transfer_amount} in the transfer amount input')
def step_impl(context, transfer_amount):
    context.account_poms.input_transfer_amount(transfer_amount)


@when(u'I click the transfer button')
def step_impl(context):
    context.account_poms.click_transfer_button()


@when(u'I click on the delete modal on account {account_number}')
def step_impl(context, account_number):
    context.account_poms.click_delete_account_modal(account_number)


@when(u'I click the delete account button')
def step_impl(context):
    context.account_poms.click_delete_account_button()
