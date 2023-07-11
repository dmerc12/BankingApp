from behave import given, when, then


# given
@given(u'I am on the login page')
def step_impl(context):
    context.driver.get('http://127.0.0.1:5000/login')

@given(u'I am on the register page')
def step_impl(context):
    context.driver.get('http://127.0.0.1:5000/register')


# when
@when(u'I click the Register tab')
def step_impl(context):
    context.customer_poms.register_tab().click()


@when(u'I {first_name} in the first name')
def step_impl(context, first_name: str):
    context.customer_poms.register_first_name_input().send_keys(first_name)


@when(u'I enter {last_name} in the last name')
def step_impl(context, last_name: str):
    context.customer_poms.register_last_name_input().send_keys(last_name)


@when(u'I enter {email} in the email address')
def step_impl(context, email: str):
    context.customer_poms.register_email_input().send_keys(email)


@when(u'I enter {password} in the create password')
def step_impl(context, password: str):
    context.customer_poms.register_password_input().send_keys(password)


@when(u'I enter {confirmation_password} in the confirmation password')
def step_impl(context, confirmation_password: str):
    context.customer_poms.register_confirmation_password_input().send_keys(confirmation_password)


@when(u'I enter {phone_number} in the phone number')
def step_impl(context, phone_number: str):
    context.customer_poms.register_phone_number_input().send_keys(phone_number)


@when(u'I enter {street_address} in the street address')
def step_impl(context, street_address: str):
    context.customer_poms.register_street_address_input(street_address)


@when(u'I enter {city} in the city')
def step_impl(context, city: str):
    context.customer_poms.register_city_input(city)


@when(u'I enter {state} in the state')
def step_impl(context, state: str):
    context.customer_poms.register_state_input(state)


@when(u'I enter {zip_code} in the zip code')
def step_impl(context, zip_code: str):
    context.customer_poms.register_zip_code_input(zip_code)


@when(u'I click the Register button')
def step_impl(context):
    context.customer_poms.register_button().click()


@then(u'I should be on a page with the title Register')
def step_impl(context):
    assert context.driver.title == "Register"


@then(u'I should be on a page with the title Login')
def step_impl(context):
    assert context.driver.title == "Login"

