from behave import given, when, then

@given(u'I am on the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the login page')


@when(u'I click the register tab in the nav bar')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the register tab in the nav bar')


@when(u'I input {first_name} in the register first name input')
def step_impl(context, first_name):
    raise NotImplementedError(u'STEP: When I input "" in the register first name input')


@when(u'I input {last_name} in the register last name input')
def step_impl(context, last_name):
    raise NotImplementedError(u'STEP: When I input "last" in the register last name input')


@when(u'I input {email} in the register email input')
def step_impl(context, email):
    raise NotImplementedError(u'STEP: When I input "first@email.com" in the register email input')


@when(u'I input {password} in the register password input')
def step_impl(context, password):
    raise NotImplementedError(u'STEP: When I input "first" in the register password input')


@when(u'I input {confirmation_password} in the register confirmation password input')
def step_impl(context, confirmation_password):
    raise NotImplementedError(u'STEP: When I input "first" in the register confirmation password input')


@when(u'I input {phone_number} in the register phone number input')
def step_impl(context, phone_number):
    raise NotImplementedError(u'STEP: When I input "1234567890" in the register phone number input')


@when(u'I input {street_address} in the register street address input')
def step_impl(context, street_address):
    raise NotImplementedError(u'STEP: When I input "123 First St" in the register street address input')


@when(u'I input {city} in the register city input')
def step_impl(context, city):
    raise NotImplementedError(u'STEP: When I input "First" in the register city input')


@when(u'I input {state} in the register state input')
def step_impl(context, state):
    raise NotImplementedError(u'STEP: When I input "OK" in the register state input')


@when(u'I input {zip_code} in the register zip code input')
def step_impl(context, zip_code):
    raise NotImplementedError(u'STEP: When I input "73072" in the register zip code input')


@when(u'I click the register button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the register button')


@then(u'I should see a toast notification saying {toast_text}')
def step_impl(context, toast_text):
    raise NotImplementedError(u'STEP: Then I should see a toast notification saying "The first name field cannot be left empty, please try again!"')
