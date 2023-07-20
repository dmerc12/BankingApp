from behave import when, then

# when
@when(u'I click the Manage Accounts navigation button')
def step_impl(context):
    context.account_poms.manage_accounts_navigation().click()


@when(u'I enter {amount} in the starting amount')
def step_impl(context, amount: float):
    context.account_poms.create_account_amount_input().send_keys(amount)


@when(u'I click the Create Account button')
def step_impl(context):
    context.account_poms.create_account_button().click()


# then
@then(u'I should be on a page with the title Creating An Account')
def step_impl(context):
    assert context.driver.title == "Creating An Account"
