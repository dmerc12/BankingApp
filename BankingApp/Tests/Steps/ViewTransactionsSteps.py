from behave import when, then

# when
@when(u'I click the View Transactions button')
def step_impl(context):
    context.account_poms.view_transactions_button().click()


@when(u'I click the Back button')
def step_impl(context):
    context.account_poms.view_transactions_back_button().click()


# then
@then(u'I should be on a page with the title Analyzing Your Transactions')
def step_impl(context):
    assert context.driver.title == "Analyzing Your Transactions"
