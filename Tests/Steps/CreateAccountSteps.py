from behave import when

@when(u'I click "Create a New Account"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click "Create a New Account"')


@when(u'I enter a negative -250.00 in the starting amount')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a negative -250.00 in the starting amount')


@when(u'I click the Create Account button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Create Account button')


@when(u'I enter {amount} in the starting amount')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter {amount} in the starting amount')