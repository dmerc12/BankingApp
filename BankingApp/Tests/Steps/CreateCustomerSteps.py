from behave import given, when, then

@given(u'I am on the login page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5000/")


@when(u'I click the Register Page button')
def step_impl(context):
    context.customer_poms.register_page().click()


@then(u'I should be on a page with the title Register')
def step_impl(context):
    assert context.driver.title == "Register"


@given(u'I am on the new customer page')
def step_impl(context):
    context.driver.get('http://127.0.0.1:5000/register')


@when(u'I enter {first_name} in the first name')
def step_impl(context, first_name):
    context.customer_poms.create_first_name_input().send_keys(first_name)


@when(u'I enter {last_name} in the last name')
def step_impl(context, last_name):
    context.customer_poms.create_last_name_input().send_keys(last_name)


@when(u'I enter {email} in the email address')
def step_impl(context, email):
    context.customer_poms.create_email_input().send_keys(email)


@when(u'I enter {password} in the create password')
def step_impl(context, password):
    context.customer_poms.create_password_input().send_keys(password)


@when(u'I enter {confirmation_password} in the confirmation password')
def step_impl(context, confirmation_password):
    context.customer_poms.create_confirmation_password_input().send_keys(confirmation_password)


@when(u'I enter {phone_number} in the phone number')
def step_impl(context, phone_number):
    context.customer_poms.create_phone_number_input().send_keys(phone_number)


@when(u'I enter {address} in the address')
def step_impl(context, address):
    context.customer_poms.create_address_input().send_keys(address)

@when(u'I click the Register button')
def step_impl(context):
    context.customer_poms.register_button().click()

@then(u'I should be on a page with the title Login')
def step_impl(context):
    assert context.driver.title == "Login"
