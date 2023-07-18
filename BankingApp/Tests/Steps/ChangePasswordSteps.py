from behave import when, then
# when
@when(u'I enter {password} in the update password input')
def step_impl(context, password: str):
    raise NotImplementedError(u'STEP: When I enter this is too long and so it will fail and bring a desired error in the update password input')


@when(u'I enter {confirmation_password} in the update password confirmation input')
def step_impl(context, confirmation_password: str):
    raise NotImplementedError(u'STEP: When I enter this is fine in the update password confirmation input')


@when(u'I click the Change Password button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Change Password button')


# then
@then(u'I should be on a page with the title Changing Your Password')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be on a page with the title Changing Your Password')
