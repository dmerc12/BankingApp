from behave import when, then
# when
@when(u'I enter {password} in the update password input')
def step_impl(context, password: str):
    context.customer_poms.change_password_input().send_keys(password)


@when(u'I enter {confirmation_password} in the update password confirmation input')
def step_impl(context, confirmation_password: str):
    context.customer_poms.change_password_confirmation_input().send_keys(confirmation_password)


@when(u'I click the Change Password button')
def step_impl(context):
    context.customer_poms.change_password_button().click()


# then
@then(u'I should be on a page with the title Changing Your Password')
def step_impl(context):
    assert context.driver.title == "Changing Your Password"
