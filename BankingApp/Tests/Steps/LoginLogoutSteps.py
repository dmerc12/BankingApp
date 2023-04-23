from behave import when, then


@when(u'I click the home tab in the navbar')
def step_impl(context):
    context.customer_poms.home_nav_button().click()


@when(u'I click the manage customer information tab in the navbar')
def step_impl(context):
    context.customer_poms.manage_customer_nav_button().click()


@when(u'I click the manage accounts tab in the navbar')
def step_impl(context):
    context.customer_poms.manage_accounts_nav_button().click()


@when(u'I enter {email} in the email')
def step_impl(context, email):
    context.customer_poms.login_email_input().send_keys(email)


@when(u'I enter {password} in the password')
def step_impl(context, password):
    context.customer_poms.login_password_input().send_keys(password)


@when(u'I click the Login button')
def step_impl(context):
    context.customer_poms.login_button().click()


@when(u'I click the Log Out button')
def step_impl(context):
    context.customer_poms.logout_button().click()


@then(u'I should be on a page with the title Login Page')
def step_impl(context):
    assert context.driver.title == "Login"


@then(u'I should be on a page with the title Home Dashboard')
def step_impl(context):
    assert context.driver.title == "Home Dashboard"
