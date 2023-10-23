from behave import given, then

@given(u'I am on the login page')
def step_impl(context):
    context.driver.get('http://localhost:5173/')


@then(u'I am on a page with the title {title}')
def step_impl(context, title):
    assert context.driver.title == title


@then(u'I should see a toast notification saying {expected_toast}')
def step_impl(context, expected_toast):
    toast_message = context.customer_poms.toast_notification()
    assert expected_toast == toast_message.text
