from behave import when
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.wait import WebDriverWait


@when(u'I click "Create a New Account"')
def step_impl(context):
    context.banking_poms.create_new_account_collapse_button().click()

@when(u'I click the Create Account button')
def step_impl(context):
    context.banking_poms.create_account_button().click()

@when(u'I enter {amount} in the starting amount')
def step_impl(context, amount: float):
    context.banking_poms.account_starting_balance_input().send_keys(amount)

@when(u'I click ok on the alert')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(title_contains("Customer Home"))
    context.banking_poms.press_ok_on_alert().click()
