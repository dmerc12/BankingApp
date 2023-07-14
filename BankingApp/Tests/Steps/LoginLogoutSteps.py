from behave import when, then


@when(u'I enter {email} in the login email input')
def step_impl(context, email: str):
    context.customer_poms.login_email_input().send_keys(email)


@when(u'I enter {password} in the login password input')
def step_impl(context, password: str):
    context.customer_poms.login_password_input().send_keys(password)


@when(u'I click the Login button')
def step_impl(context):
    context.customer_poms.login_button().click()


@when(u'I click the Log Out button')
def step_impl(context):
    context.customer_poms.logout_button().click()


@when(u'I click the Home tab')
def step_impl(context):
    context.customer_poms.home_tab().click()


@when(u'I click the Manage Customer Information tab')
def step_impl(context):
    context.customer_poms.manage_customer_tab().click()


@when(u'I click the Manage Accounts tab')
def step_impl(context):
    context.customer_poms.manage_accounts_tab().click()

@when(u'I click the Login tab')
def step_impl(context):
    context.customer_poms.login_tab().click()


@when(u'I click the Create Account navigation button')
def step_impl(context):
    context.account_poms.create_account_navigation().click()


@when(u'I click the View Accounts navigation button')
def step_impl(context):
    context.account_poms.view_accounts_navigation().click()


@when(u'I click the View Transactions button')
def step_impl(context):
    context.account_poms.view_transactions_button().click()


@when(u'I click the Deposit navigation button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Deposit navigation button')


@when(u'I click the Withdraw navigation button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Withdraw navigation button')


@when(u'I click the Transfer navigation button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Transfer navigation button')


@when(u'I click the Delete Account navigation button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Delete Account navigation button')


@when(u'I click the Update Information navigation button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Update Information navigation button')


@when(u'I click the Delete Information navigation button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Delete Information navigation button')


@when(u'I click the Change Password navigation button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Change Password navigation button')


@then(u'I should be on a page with the title Managing Your Accounts')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be on a page with the title Managing Your Accounts')


@then(u'I should be on a page with the title Home Dashboard')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be on a page with the title Home Dashboard')


@then(u'I should be on a page with the title Managing Your Information')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be on a page with the title Managing Your Information')


