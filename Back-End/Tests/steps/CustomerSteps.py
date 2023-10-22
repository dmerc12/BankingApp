from behave import when

@when(u'I click the manage information button in the navigation bar')
def step_impl(context):
    context.customer_poms.click_manage_info_nav_button()

@when(u'I click the register button in the navigation bar')
def step_impl(context):
    context.customer_poms.click_register_nav_button()


@when(u'I click the login button in the navigation bar')
def step_impl(context):
    context.customer_poms.click_login_nav_button()


@when(u'I click the home button in the navigation bar')
def step_impl(context):
    context.customer_poms.click_home_nav_button()


@when(u'I input {first_name} in the register first name input')
def step_impl(context, first_name):
    if first_name == "N/A":
        pass
    else:
        context.customer_poms.input_register_first_name(first_name)


@when(u'I input {last_name} in the register last name input')
def step_impl(context, last_name):
    if last_name == "N/A":
        pass
    else:
        context.customer_poms.input_register_last_name(last_name)


@when(u'I input {email} in the register email input')
def step_impl(context, email):
    if email == "N/A":
        pass
    else:
        context.customer_poms.input_register_email(email)


@when(u'I input {password} in the register password input')
def step_impl(context, password):
    if password == "N/A":
        pass
    else:
        context.customer_poms.input_register_password(password)


@when(u'I input {confirmation_password} in the register confirmation password input')
def step_impl(context, confirmation_password):
    if confirmation_password == "N/A":
        pass
    else:
        context.customer_poms.input_register_confirmation_password(confirmation_password)


@when(u'I input {phone_number} in the register phone number input')
def step_impl(context, phone_number):
    if phone_number == "N/A":
        pass
    else:
        context.customer_poms.input_register_phone_number(phone_number)


@when(u'I input {street_address} in the register street address input')
def step_impl(context, street_address):
    if street_address == "N/A":
        pass
    else:
        context.customer_poms.input_register_street_address(street_address)


@when(u'I input {city} in the register city input')
def step_impl(context, city):
    if city == "N/A":
        pass
    else:
        context.customer_poms.input_register_city(city)


@when(u'I input {state} in the register state input')
def step_impl(context, state):
    if state == "N/A":
        pass
    else:
        context.customer_poms.input_register_state(state)


@when(u'I input {zip_code} in the register zip code input')
def step_impl(context, zip_code):
    if zip_code == "N/A":
        pass
    else:
        context.customer_poms.input_register_zip_code(zip_code)


@when(u'I click the register button')
def step_impl(context):
    context.customer_poms.click_register_button()


@when(u'I input {email} in the login email input')
def step_impl(context, email):
    if email == "N/A":
        pass
    else:
        context.customer_poms.input_login_email(email)


@when(u'I input {password} in the login password input')
def step_impl(context, password):
    if password == "N/A":
        pass
    else:
        context.customer_poms.input_login_password(password)


@when(u'I click the login button')
def step_impl(context):
    context.customer_poms.click_login_button()


@when(u'I click the logout button')
def step_impl(context):
    context.customer_poms.click_logout_nav_button()


@when(u'I click the manage information button')
def step_impl(context):
    context.customer_poms.click_manage_info_button()


@when(u'I click the change password modal')
def step_impl(context):
    context.customer_poms.click_change_password_modal()


@when(u'I input {password} in the change password input')
def step_impl(context, password):
    if password == "N/A":
        pass
    else:
        context.customer_poms.input_change_password(password)

@when(u'I input {confirmation_password} in the change password confirmation input')
def step_impl(context, confirmation_password):
    if confirmation_password == "N/A":
        pass
    else:
        context.customer_poms.input_change_confirmation_password(confirmation_password)


@when(u'I click the change password button')
def step_impl(context):
    context.customer_poms.click_change_password_button()


@when(u'I click the update information modal')
def step_impl(context):
    context.customer_poms.click_update_profile_modal()


@when(u'I input {first_name} in the update first name input')
def step_impl(context, first_name):
    if first_name == "N/A":
        pass
    else:
        context.customer_poms.input_update_first_name(first_name)


@when(u'I input {last_name} in the update last name input')
def step_impl(context, last_name):
    if last_name == "N/A":
        pass
    else:
        context.customer_poms.input_update_last_name(last_name)


@when(u'I input {email} in the update email input')
def step_impl(context, email):
    if email == "N/A":
        pass
    else:
        context.customer_poms.input_update_email(email)


@when(u'I input {phone_number} in the update phone number input')
def step_impl(context, phone_number):
    if phone_number == "N/A":
        pass
    else:
        context.customer_poms.input_update_phone_number(phone_number)


@when(u'I input {street_address} in the update street address input')
def step_impl(context, street_address):
    if street_address == "N/A":
        pass
    else:
        context.customer_poms.input_update_street_address(street_address)


@when(u'I input {city} in the update city input')
def step_impl(context, city):
    if city == "N/A":
        pass
    else:
        context.customer_poms.input_update_city(city)


@when(u'I input {state} in the update state input')
def step_impl(context, state):
    if state == "N/A":
        pass
    else:
        context.customer_poms.input_update_state(state)


@when(u'I input {zip_code} in the update zip code input')
def step_impl(context, zip_code):
    if zip_code == "N/A":
        pass
    else:
        context.customer_poms.input_update_zip_code(zip_code)


@when(u'I click the update information button')
def step_impl(context):
    context.customer_poms.click_update_button()


@when(u'I click the delete profile modal')
def step_impl(context):
    context.customer_poms.click_delete_profile_modal()


@when(u'I click the delete profile button')
def step_impl(context):
    context.customer_poms.click_delete_profile_button()
