from behave import when

# When step for entering username on login page
@when(u'I enter {username} in the login username field')
def step_impl(context, username):
    context.login_poms.enter_login_username(username)
    
# When step for entering password on login page
@when(u'I enter {password} in the login password field')
def step_impl(context, password):
    context.login_poms.enter_login_password(password)
    
# When step for clicking the login button
@when(u'I click the login button')
def step_impl(context):
    context.universal_poms.click_login_button()
    