from behave import when

# When step for clicking create account navigation button
@when(u'I click the create account navigation button')
def step_impl(context):
    context.create_account_poms.click_create_account_navigation_button()

# When step for inputting account number
@when(u'I input {account_number} in the create account account number field')
def step_impl(context, account_number):
    context.create_account_poms.enter_account_number_input(account_number)

# When step for inputting bank name
@when(u'I input {bank_name}in the create account bank name field')
def step_impl(context, bank_name):
    context.create_account_poms.enter_bank_name_input(bank_name)

# When step for inputting location
@when(u'I input {location} in the create account location field')
def step_impl(context, location):
    context.create_account_poms.enter_location_input(location)

# When step for inputting timestamp
@when(u'I input {timestamp} in the create account timestamp field')
def step_impl(context, timestamp):
    context.create_account_poms.enter_timestamp_input(timestamp)

# When step for inputting opening balance
@when(u'I input {opening_balance} in the create account opening balance field')
def step_impl(context, opening_balance):
    context.create_account_poms.enter_opening_balance_input(opening_balance)

# When step for inputting opening notes
@when(u'I input {opening_notes} in the create account opening notes field')
def step_impl(context, opening_notes):
    context.create_account_poms.enter_opening_notes_input(opening_notes)

# When step for clicking create account button
@when(u'I click the create account button')
def step_impl(context):
    context.create_account_poms.click_create_account_button()
