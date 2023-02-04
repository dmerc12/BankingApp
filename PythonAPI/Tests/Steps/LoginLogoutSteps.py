from behave import given, when, then
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I am on the home page')
def step_impl(context):
    context.driver.get("C:/Users/Dylan/OneDrive/Desktop/personal projects/BankingApp/FrontEnd/CustomerHome.html")

@given(u'I am on the login page')
def step_impl(context):
    context.driver.get("C:/Users/Dylan/OneDrive/Desktop/personal projects/BankingApp/FrontEnd/Login.html")

@given(u'I am on the managing customer information page')
def step_impl(context):
    context.driver.get("C:/Users/Dylan/OneDrive/Desktop/personal projects/BankingApp/FrontEnd/ManageCustomer.html")

@given(u'I am on the managing accounts page')
def step_impl(context):
    context.driver.get("C:/Users/Dylan/OneDrive/Desktop/personal projects/BankingApp/FrontEnd/ManageAccounts.html")

@when(u'I enter {username} in the username')
def step_impl(context, username):
    context.customer_poms.login_username_input().send_keys(username)

@when(u'I enter {password} in the password')
def step_impl(context, password):
    context.customer_poms.login_password_input().send_keys(password)

@when(u'I click the Login button')
def step_impl(context):
    context.customer_poms.login_button().click()

@when(u'I am not logged in and see an error and I click the Continue button')
def step_impl(context):
    context.customer_poms.alert()

@when(u'I click "Log Out" from the home page')
def step_impl(context):
    context.customer_poms.home_log_out_collapse_button().click()

@when(u'I click "Log Out" from the managing customer information page')
def step_impl(context):
    context.customer_poms.manage_customer_information_logout_collapse_button().click()

@when(u'I click "Log Out" from the managing accounts page')
def step_impl(context):
    context.banking_poms.manage_accounts_logout_collapse_button().click()

@when(u'I click the Log Out button from the home page')
def step_impl(context):
    context.customer_poms.home_log_out_button().click()

@when(u'I click the Log Out button from the manage customer information page')
def step_impl(context):
    context.customer_poms.manage_customer_information_logout_button().click()

@when(u'I click the Log Out button from the managing accounts page')
def step_impl(context):
    context.banking_poms.manage_accounts_logout_button().click()

@when(u'I click "Manage Accounts"')
def step_impl(context):
    context.banking_poms.manage_accounts_collapse_button().click()

@when(u'I click the Create and Manage Accounts button')
def step_impl(context):
    context.banking_poms.create_and_manage_accounts_button().click()

@when(u'I click "Manage CustomerRoutes Information"')
def step_impl(context):
    context.customer_poms.manage_customer_information_collapse_button().click()

@when(u'I click the Manage CustomerRoutes Information button')
def step_impl(context):
    context.customer_poms.manage_customer_information_button().click()

@then(u'I am on a page with the title Managing CustomerRoutes')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(title_contains("Managing CustomerRoutes"))
    assert context.driver.title == "Managing CustomerRoutes"

@then(u'I should be on a page with the title Login Page')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(title_contains("Login Page"))
    assert context.driver.title == "Login Page"

@then(u'I should be on a page with the title CustomerRoutes Home')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(title_contains("CustomerRoutes Home"))
    assert context.driver.title == "CustomerRoutes Home"

@then(u'I should be on a page with the title Managing Accounts')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(title_contains("Managing Accounts"))
    assert context.driver.title == "Managing Accounts"
