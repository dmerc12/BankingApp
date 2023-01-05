from behave import given, when, then

@when(u'I click the New Customer button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the New Customer button')


@then(u'I should be on a page with the title New Customer')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be on a page with the title New Customer')


@given(u'I am on the new customer page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the new customer page')


@when(u'I {first name} in the first name')
def step_impl(context, first_name):
    raise NotImplementedError(u'STEP: When I enter {first name} in the first name')


@when(u'I enter {last name} in the last name')
def step_impl(context, last_name):
    raise NotImplementedError(u'STEP: When I enter {last name} in the last name')


@when(u'I enter {email} in the email address')
def step_impl(context, email):
    raise NotImplementedError(u'STEP: When I enter {email} in the email address')


@when(u'I enter {phone number} in the phone number')
def step_impl(context, phone_number):
    raise NotImplementedError(u'STEP: When I enter {phone number} in the phone number')


@when(u'I enter {address} in the address')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter {address in the address')


@when(u'I click the Create New Customer button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Create New Customer button')
