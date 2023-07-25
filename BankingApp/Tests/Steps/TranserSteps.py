from behave import when, then

# when
@when(u'I click the Transfer navigation button')
def step_impl(context):
    context.account_poms.transfer_navigation().click()


@when(u'I select {withdraw_account} from the transfer withdraw account dropdown')
def step_impl(context, withdraw_account: int):
    context.account_poms.transfer_withdraw_account_dropdown().send_keys(withdraw_account)


@when(u'I select {deposit_account} from the transfer deposit account dropdown')
def step_impl(context, deposit_account: int):
    context.account_poms.transfer_deposit_account_dropdown().send_keys(deposit_account)


@when(u'I input {amount} into the transfer amount input')
def step_impl(context, amount: float):
    context.account_poms.transfer_amount_input().send_keys(amount)


@when(u'I click the Transfer button')
def step_impl(context):
    context.account_poms.transfer_button().click()


# then
@then(u'I should be on a page with the title Making A Transfer')
def step_impl(context):
    assert context.driver.title == "Making A Transfer"
