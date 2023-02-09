from behave import given, when, then
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.wait import WebDriverWait

@given(u'I am on the new customer page')
def step_impl(context):
    context.driver.get("C:/Users/Dylan/OneDrive/Desktop/personal projects/BankingApp/FrontEnd/NewCustomer.html")

@when(u'I click the New CustomerRoutes button')
def step_impl(context):
    context.customer_poms.indicate_new_customer().click()

@when(u'I {first_name} in the first name')
def step_impl(context, first_name: str):
    context.customer_poms.create_first_name_input().send_keys(first_name)

@when(u'I enter {last_name} in the last name')
def step_impl(context, last_name: str):
    context.customer_poms.create_last_name_input().send_keys(last_name)

@when(u'I enter {username} in the create username')
def step_impl(context, username: str):
    context.customer_poms.create_username_input().send_keys(username)


@when(u'I enter {password} in the create password')
def step_impl(context, password: str):
    context.customer_poms.create_password_input().send_keys(password)

@when(u'I enter {email} in the email address')
def step_impl(context, email: str):
    context.customer_poms.create_email_input().send_keys(email)

@when(u'I enter {phone_number} in the phone number')
def step_impl(context, phone_number: str):
    context.customer_poms.create_phone_number_input().send_keys(phone_number)

@when(u'I enter {address} in the address')
def step_impl(context, address: str):
    context.customer_poms.create_address_input().send_keys(address)

@when(u'I click the Create New CustomerRoutes button')
def step_impl(context):
    context.customer_poms.create_new_customer_button().click()

@then(u'I should be on a page with the title New CustomerRoutes')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(title_contains("New CustomerRoutes"))
    assert context.driver.title == "New CustomerRoutes"
