from behave import given, when, then

@given(u'I am on the login page')
def step_impl(context):
    context.driver.get('http://localhost:5173/')


@when(u'I click the register tab in the nav bar')
def step_impl(context):
    context.customer_poms.register_nav_button().click()


@when(u'I input {first_name} in the register first name input')
def step_impl(context, first_name):
    if first_name == "N/A":
        context.customer_poms.register_first_name_input().send_keys()
    else:
        context.customer_poms.register_first_name_input().send_keys(first_name)


@when(u'I input {last_name} in the register last name input')
def step_impl(context, last_name):
    if last_name == "N/A":
        context.customer_poms.register_last_name_input().send_keys()
    else:
        context.customer_poms.register_last_name_input().send_keys(last_name)


@when(u'I input {email} in the register email input')
def step_impl(context, email):
    if email == "N/A":
        context.customer_poms.register_email_input().send_keys()
    else:
        context.customer_poms.register_email_input().send_keys(email)


@when(u'I input {password} in the register password input')
def step_impl(context, password):
    if password == "N/A":
        context.customer_poms.register_password_input().send_keys()
    else:
        context.customer_poms.register_password_input().send_keys(password)


@when(u'I input {confirmation_password} in the register confirmation password input')
def step_impl(context, confirmation_password):
    if confirmation_password == "N/A":
        context.customer_poms.register_confirmation_password_input().send_keys()
    else:
        context.customer_poms.register_confirmation_password_input().send_keys(confirmation_password)


@when(u'I input {phone_number} in the register phone number input')
def step_impl(context, phone_number):
    if phone_number == "N/A":
        context.customer_poms.register_phone_number_input().send_keys()
    else:
        context.customer_poms.register_phone_number_input().send_keys(phone_number)


@when(u'I input {street_address} in the register street address input')
def step_impl(context, street_address):
    if street_address == "N/A":
        context.customer_poms.register_street_address_input().send_keys()
    else:
        context.customer_poms.register_street_address_input().send_keys(street_address)


@when(u'I input {city} in the register city input')
def step_impl(context, city):
    if city == "N/A":
        context.customer_poms.register_city_input().send_keys()
    else:
        context.customer_poms.register_city_input().send_keys(city)


@when(u'I input {state} in the register state input')
def step_impl(context, state):
    if state == "N/A":
        context.customer_poms.register_state_input().send_keys()
    else:
        context.customer_poms.register_state_input().send_keys(state)


@when(u'I input {zip_code} in the register zip code input')
def step_impl(context, zip_code):
    if zip_code == "N/A":
        context.customer_poms.register_zip_code_input().send_keys()
    else:
        context.customer_poms.register_zip_code_input().send_keys(zip_code)


@when(u'I click the register button')
def step_impl(context):
    context.customer_poms.register_button().click()


@when(u'I input {email} in the login email input')
def step_impl(context, email):
    if email == "N/A":
        context.customer_poms.login_email_input().send_keys()
    else:
        context.customer_poms.login_email_input().send_keys(email)


@when(u'I input {password} in the login password input')
def step_impl(context, password):
    if password == "N/A":
        context.customer_poms.login_password_input().send_keys()
    else:
        context.customer_poms.login_password_input().send_keys(password)


@when(u'I click the login button')
def step_impl(context):
    context.customer_poms.login_button().click()


@when(u'I click the logout button')
def step_impl(context):
    context.customer_poms.logout_nav_button().click()


@when(u'I click the manage information button')
def step_impl(context):
    context.customer_poms.manage_info_button().click()


@when(u'I click the change password modal')
def step_impl(context):
    context.customer_poms.change_password_modal().click()


@when(u'I input {password} in the change password input')
def step_impl(context, password):
    if password == "N/A":
        context.customer_poms.change_password_input().send_keys()
    else:
        context.customer_poms.change_password_input().send_keys(password)


@when(u'I input {confirmation_password} in the change password confirmation input')
def step_impl(context, confirmation_password):
    if confirmation_password == "N/A":
        context.customer_poms.change_confirmation_password_input().send_keys()
    else:
        context.customer_poms.change_confirmation_password_input().send_keys(confirmation_password)


@when(u'I click the change password button')
def step_impl(context):
    context.customer_poms.change_password_button().click()


@when(u'I click the update information modal')
def step_impl(context):
    context.customer_poms.update_profile_modal().click()


@when(u'I input {first_name} in the update first name input')
def step_impl(context, first_name):
    if first_name == "N/A":
        context.customer_poms.update_first_name_input().send_keys()
    else:
        context.customer_poms.update_first_name_input().send_keys(first_name)


@when(u'I input {last_name} in the update last name input')
def step_impl(context, last_name):
    if last_name == "N/A":
        context.customer_poms.update_last_name_input().send_keys()
    else:
        context.customer_poms.update_last_name_input().send_keys(last_name)


@when(u'I input {updated_email} in the update email input')
def step_impl(context, email):
    if email == "N/A":
        context.customer_poms.update_email_input().send_keys()
    else:
        context.customer_poms.update_email_input().send_keys(email)


@when(u'I input {phone_number} in the update phone number input')
def step_impl(context, phone_number):
    if phone_number == "N/A":
        context.customer_poms.update_phone_number_input().send_keys()
    else:
        context.customer_poms.update_phone_number_input().send_keys(phone_number)


@when(u'I input {street_address} in the update street address input')
def step_impl(context, street_address):
    if street_address == "N/A":
        context.customer_poms.update_street_address_input().send_keys()
    else:
        context.customer_poms.update_street_address_input().send_keys(street_address)


@when(u'I input {city} in the update city input')
def step_impl(context, city):
    if city == "N/A":
        context.customer_poms.update_city_input().send_keys()
    else:
        context.customer_poms.update_city_input().send_keys(city)


@when(u'I input {state} in the update state input')
def step_impl(context, state):
    if state == "N/A":
        context.customer_poms.update_state_input().send_keys()
    else:
        context.customer_poms.update_state_input().send_keys(state)


@when(u'I input {zip_code} in the update zip code input')
def step_impl(context, zip_code):
    if zip_code == "N/A":
        context.customer_poms.update_zip_code_input().send_keys()
    else:
        context.customer_poms.update_zip_code_input().send_keys(zip_code)


@when(u'I click the update information button')
def step_impl(context):
    context.customer_poms.update_button().click()


@when(u'I click the delete profile modal')
def step_impl(context):
    context.customer_poms.delete_profile_modal().click()


@when(u'I click the delete profile button')
def step_impl(context):
    context.customer_poms.delete_profile_button().click()


@then(u'I should see a toast notification saying {expected_toast}')
def step_impl(context, expected_toast):
    toast_message = context.customer_poms.toast_notification()
    print("expected: " + expected_toast)
    print("actual: " + toast_message.text)
    assert expected_toast == toast_message.text
