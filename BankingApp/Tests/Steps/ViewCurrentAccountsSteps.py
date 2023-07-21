from behave import when, then

# when
@when(u'I click the View Accounts button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the View Accounts button')


# then
@then(u'I should be on a page with the title Viewing Your Accounts')
def step_impl(context):
    assert context.driver.title == "Viewing Your Accounts"
