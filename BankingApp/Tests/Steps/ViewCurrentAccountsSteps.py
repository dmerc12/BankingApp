from behave import when, then

# when
@when(u'I click the View Accounts navigation button')
def step_impl(context):
    context.account_poms.view_accounts_navigation().click()


@when(u'I click the View Accounts button')
def step_impl(context):
    context.account_poms.view_accounts_button().click()


# then
@then(u'I should be on a page with the title Viewing Your Accounts')
def step_impl(context):
    assert context.driver.title == "Viewing Your Accounts"
