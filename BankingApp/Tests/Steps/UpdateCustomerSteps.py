from behave import when, then

# when
@when(u'I click the Update Information navigation button')
def step_impl(context):
    context.customer_poms.update_customer_navigation().click()


@when(u'I click the Update Your Information navigation button')
def step_impl(context):
    context.customer_poms.update_customer_navigation().click()


@when(u'I enter {first_name} in the update first name input')
def step_impl(context, first_name: str):
    context.customer_poms.update_first_name_input().clear()
    context.customer_poms.update_first_name_input().send_keys(first_name)


@when(u'I enter {last_name} in the update last name input')
def step_impl(context, last_name: str):
    context.customer_poms.update_last_name_input().clear()
    context.customer_poms.update_last_name_input().send_keys(last_name)


@when(u'I enter{email} in the update email address input')
def step_impl(context, email: str):
    context.customer_poms.update_email_input().clear()
    context.customer_poms.update_email_input().send_keys(email)


@when(u'I enter {phone_number} in the update phone number input')
def step_impl(context, phone_number: str):
    context.customer_poms.update_phone_number_input().clear()
    context.customer_poms.update_phone_number_input().send_keys(phone_number)


@when(u'I enter {street_address} in the update street address input')
def step_impl(context, street_address: str):
    context.customer_poms.update_street_address_input().clear()
    context.customer_poms.update_street_address_input().send_keys(street_address)


@when(u'I enter {city} in the update city input')
def step_impl(context, city: str):
    context.customer_poms.update_city_input().clear()
    context.customer_poms.update_city_input().send_keys(city)


@when(u'I enter {state} in the update state input')
def step_impl(context, state: str):
    context.customer_poms.update_state_input().send_keys(state)


@when(u'I enter {zip_code} in the update zip code input')
def step_impl(context, zip_code: str):
    context.customer_poms.update_zip_code_input().send_keys(zip_code)


@when(u'I click the Update Information button')
def step_impl(context):
    context.customer_poms.update_button().click()


# then
@then(u'I should be on a page with the title Updating Your Information')
def step_impl(context):
    assert context.driver.title == "Updating Your Information"
