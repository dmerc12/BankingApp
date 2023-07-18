from behave import when, then

# when
@when(u'I click the Manage Information navigation button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Manage Information navigation button')


@when(u'I click the Update Your Information navigation button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Update Your Information navigation button')


@when(u'I enter {first_name} in the update first name input')
def step_impl(context, first_name: str):
    raise NotImplementedError(u'STEP: When I enter this is too long and so it will fail and bring a desired error in the update first name input')


@when(u'I enter {last_name} in the update last name input')
def step_impl(context, last_name: str):
    raise NotImplementedError(u'STEP: When I enter last in the update last name input')


@when(u'I enter{email} in the update email address input')
def step_impl(context, email: str):
    raise NotImplementedError(u'STEP: When I enter updated@email.com in the update email address input')


@when(u'I enter {phone_number} in the update phone number input')
def step_impl(context, phone_number: str):
    raise NotImplementedError(u'STEP: When I enter 1234567890 in the update phone number input')


@when(u'I enter {street_address} in the update street address input')
def step_impl(context, street_address: str):
    raise NotImplementedError(u'STEP: When I enter 123 T St in the update street address input')


@when(u'I enter {city} in the update city input')
def step_impl(context, city: str):
    raise NotImplementedError(u'STEP: When I enter Oats in the update city input')


@when(u'I enter {state} in the update state input')
def step_impl(context, state: str):
    raise NotImplementedError(u'STEP: When I enter OH in the update state input')


@when(u'I enter {zip_code} in the update zip code input')
def step_impl(context, zip_code: str):
    raise NotImplementedError(u'STEP: When I enter 43015 in the update zip code input')


@when(u'I click the Update Information button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Update Information button')


# then
@then(u'I should be on a page with the title Updating Your Information')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be on a page with the title Updating Your Information')


@then(u'I should be on a page with the title Managing Your Current Information')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be on a page with the title Managing Your Current Information')
