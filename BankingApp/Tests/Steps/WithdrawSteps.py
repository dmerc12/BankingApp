from behave import when, then

# when
@when(u'I click the Withdraw navigation button')
def step_impl(context):
    context.account_poms.withdraw_navigation().click()


@when(u'I select {account} from the withdraw account dropdown')
def step_impl(context, account: int):
    context.account_poms.withdraw_account_dropdown().send_keys(account)


@when(u'I input {amount} into the withdraw amount input')
def step_impl(context, amount: float):
    context.account_poms.withdraw_amount_input().send_keys(amount)


@when(u'I click the Withdraw button')
def step_impl(context):
    context.account_poms.withdraw_button().click()


# then
@then(u'I should be on a page with the title Making A Withdraw')
def step_impl(context):
    assert context.driver.title == "Making A Withdraw"
