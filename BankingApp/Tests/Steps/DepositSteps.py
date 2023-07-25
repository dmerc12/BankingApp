from behave import when, then

# when
@when(u'I click the Deposit navigation button')
def step_impl(context):
    context.account_poms.deposit_navigation().click()


@when(u'I select {account} from the deposit account dropdown')
def step_impl(context, account: int):
    context.account_poms.deposit_account_dropdown().send_keys(account)


@when(u'I input {amount} into the deposit amount input')
def step_impl(context, amount: float):
    context.account_poms.deposit_amount_input().send_keys(amount)


@when(u'I click the Deposit button')
def step_impl(context):
    context.account_poms.deposit_button().click()


# then
@then(u'I should be on a page with the title Making A Deposit')
def step_impl(context):
    assert context.driver.title == "Making A Deposit"

