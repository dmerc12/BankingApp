from behave import when, then

@when(u'I click "Update Customer Information"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click "Update Customer Information"')

@when(u'I {first_name} in the update first name')
def step_impl(context, first_name):
    raise NotImplementedError(u'STEP: When I {first_name} in the update first name')

@when(u'I enter {last_name} in the update last name')
def step_impl(context, last_name):
    raise NotImplementedError(u'STEP: When I enter {last_name} in the update last name')

@when(u'I enter {new_username} in the update username')
def step_impl(context, new_username):
    raise NotImplementedError(u'STEP: When I enter {new_username} in the update username')

@when(u'I enter {new_password} in the update password')
def step_impl(context, new_password):
    raise NotImplementedError(u'STEP: When I enter {new_password} in the update password')

@when(u'I enter {new_email} in the update email address')
def step_impl(context, new_email):
    raise NotImplementedError(u'STEP: When I enter {new_email} in the update email address')

@when(u'I enter {new_phone_number} in the update phone number')
def step_impl(context, new_phone_number):
    raise NotImplementedError(u'STEP: When I enter {new_phone_number} in the update phone number')

@when(u'I enter {new_address} in the update address')
def step_impl(context, new_address):
    raise NotImplementedError(u'STEP: When I enter {new_address} in the update address')

@when(u'I click the Update Customer button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Update Customer button')

@then(u'I should be on a page with the title Managing Customer')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be on a page with the title Managing Customer')
