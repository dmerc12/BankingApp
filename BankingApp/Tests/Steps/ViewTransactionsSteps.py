from behave import then

# then
@then(u'I should be on a page with the title Analyzing Your Transactions')
def step_impl(context):
    assert context.driver.title == "Analyzing Your Transactions"
