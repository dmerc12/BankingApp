from behave import when, then
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.wait import WebDriverWait


@when(u'I click "Update Customer Information"')
def step_impl(context):
    context.customer_poms.update_customer_collapsable().click()

@when(u'I {first_name} in the update first name')
def step_impl(context, first_name):
    context.customer_poms.update_first_name_input().send_keys(first_name)

@when(u'I enter {last_name} in the update last name')
def step_impl(context, last_name):
    context.customer_poms.update_last_name_input().send_keys(last_name)

@when(u'I enter {new_username} in the update username')
def step_impl(context, new_username):
    context.customer_poms.update_username_input().send_keys(new_username)

@when(u'I enter {new_password} in the update password')
def step_impl(context, new_password):
    context.customer_poms.update_password_input().send_keys(new_password)

@when(u'I enter {new_email} in the update email address')
def step_impl(context, new_email):
    context.customer_poms.update_email_input().send_keys(new_email)

@when(u'I enter {new_phone_number} in the update phone number')
def step_impl(context, new_phone_number):
    context.customer_poms.update_phone_number_input().send_keys(new_phone_number)

@when(u'I enter {new_address} in the update address')
def step_impl(context, new_address):
    context.customer_poms.update_address_input().send_keys(new_address)

@when(u'I click the Update Customer button')
def step_impl(context):
    context.customer_poms.update_customer_button().click()

@then(u'I should be on a page with the title Managing Customer')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(title_contains("Managing Customer"))
    assert context.driver.title == "Managing Customer"
