from behave import given, when, then

@given(u'I am on the home page')
def step_impl(context):
    context.driver.get("C:/Users/Dylan/OneDrive/Desktop/personal projects/PythonBank/FrontEnd/CustomerHome.html")

@given(u'I am on the login page')
def step_impl(context):
    context.driver.get("C:/Users/Dylan/OneDrive/Desktop/personal projects/PythonBank/FrontEnd/Login.html")

@given(u'I am on the managing customer information page')
def step_impl(context):
    context.driver.get("C:/Users/Dylan/OneDrive/Desktop/personal projects/PythonBank/FrontEnd/ManageCustomer.html")

@given(u'I am on the managing accounts page')
def step_impl(context):
    context.driver.get("C:/Users/Dylan/OneDrive/Desktop/personal projects/PythonBank/FrontEnd/ManageAccounts.html")

@when(u'I click the Continue button')
def step_impl(context):
    context.customer_poms.press_ok_on_alert()

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
    context.customer_poms.press_ok_on_alert()

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

@when(u'I click "Manage Customer Information"')
def step_impl(context):
    context.customer_poms.manage_customer_information_collapse_button().click()

@when(u'I click the Manage Customer Information button')
def step_impl(context):
    context.customer_poms.manage_customer_information_button().click()

@then(u'I am on a page with the title Managing Customer')
def step_impl(context):
    assert context.driver.title == "Managing Customer"

@then(u'I should be on a page with the title Login Page')
def step_impl(context):
    assert context.driver.title == "Login Page"

@then(u'I should be on a page with the title Customer Home')
def step_impl(context):
    assert context.driver.title == "Customer Home"

@then(u'I should be on a page with the title Managing Accounts')
def step_impl(context):
    assert context.driver.title == "Managing Accounts"
