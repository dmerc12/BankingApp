from behave import given, when

## Login steps
# When step for entering username on login page
@when(u'I enter {username} in the login username field')
def step_impl(context, username):
    context.login_poms.enter_username_input(username)
    
# When step for entering password on login page
@when(u'I enter {password} in the login password field')
def step_impl(context, password):
    context.login_poms.enter_password_input(password)
    
# When step for clicking the login button
@when(u'I click the login button')
def step_impl(context):
    context.universal_poms.click_login_button()
    

## Register steps
# Given step for going to the register page
@given(u'I am on the register page')
def step_impl(context):
    context.driver.get('http://127.0.0.1:8000/users/register/')


# When step for entering username on register page
@when(u'I enter {username} in the register username field')
def step_impl(context, username):
    context.register_poms.enter_username_input(username)


# When step for entering first name on register page
@when(u'I enter {first_name} in the register first name field')
def step_impl(context, first_name):
    context.register_poms.enter_first_name_input(first_name)


# When step for entering last name on register page
@when(u'I enter {last_name} in the register last name field')
def step_impl(context, last_name):
    context.register_poms.enter_last_name_input(last_name)

    
# When step for entering email on register page
@when(u'I enter {email} in the register email field')
def step_impl(context, email):
    context.register_poms.enter_email_input(email)

    
# When step for entering phone number on register page
@when(u'I enter {phone_number} in the register phone number field')
def step_impl(context, phone_number):
    context.register_poms.enter_phone_number_input(phone_number)
    
    
# When step for entering password1 on register page
@when(u'I enter {password1} in the register password1 field')
def step_impl(context, password1):
    context.register_poms.enter_password1_input(password1)
    
    
# When step for entering password2 on register page
@when(u'I enter {password2} in the register password2 field')
def step_impl(context, password2):
    context.register_poms.enter_password2_input(password2)

    
# When step for clicking the register button
@when(u'I click the register button')
def step_impl(context):
    context.register_poms.click_register_button()
    
