from behave import when

# when
@when(u'I click the Manage Accounts navigation button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Manage Accounts navigation')


@when(u'I enter {amount} in the starting amount')
def step_impl(context, amount: float):
    raise NotImplementedError(u'STEP: When I enter -250.00 in the starting amount')


@when(u'I click the Create Account button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Create Account button')
