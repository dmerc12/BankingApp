from behave import given, when, then


# given
@given(u'I am on the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the login page')


# when
@when(u'I click the Register tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Register tab')


@given(u'I am on the new customer page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the new customer page')


@when(u'I {first_name} in the first name')
def step_impl(context, first_name: str):
    raise NotImplementedError(u'STEP: When I enter {first_name} in the first name')


@when(u'I enter {last_name} in the last name')
def step_impl(context, last_name: str):
    raise NotImplementedError(u'STEP: When I enter {last_name} in the last name')


@when(u'I enter {email} in the email address')
def step_impl(context, email: str):
    raise NotImplementedError(u'STEP: When I enter {email} in the email address')


@when(u'I enter {password} in the create password')
def step_impl(context, password: str):
    raise NotImplementedError(u'STEP: When I enter {password} in the create password')


@when(u'I enter {confirmation_password} in the confirmation password')
def step_impl(context, confirmation_password: str):
    raise NotImplementedError(u'STEP: When I enter {confirmation_password} in the confirmation password')


@when(u'I enter {phone_number} in the phone number')
def step_impl(context, phone_number: str):
    raise NotImplementedError(u'STEP: When I enter {phone_number} in the phone number')


@when(u'I enter {street_address} in the street address')
def step_impl(context, street_address: str):
    raise NotImplementedError(u'STEP: When I enter {street_address} in the street address')


@when(u'I enter {city} in the city')
def step_impl(context, city: str):
    raise NotImplementedError(u'STEP: When I enter {city} in the city')


@when(u'I enter {state} in the state')
def step_impl(context, state: str):
    raise NotImplementedError(u'STEP: When I enter {state} in the state')


@when(u'I enter {zip_code} in the zip code')
def step_impl(context, zip_code: str):
    raise NotImplementedError(u'STEP: When I enter {zip_code} in the zip code')


@when(u'I click the Register button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Register button')


@then(u'I should be on a page with the title Register')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be on a page with the title Register')


@then(u'I should be on a page with the title Login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be on a page with the title Login')

