from behave import when

# when
@when(u'I select {account} from the account dropdown')
def step_impl(context, account: int):
    raise NotImplementedError(u'STEP: When I select -1 from the account dropdown')


@when(u'I input {amount} into the deposit amount input')
def step_impl(context, amount: float):
    raise NotImplementedError(u'STEP: When I input -500.00 into the deposit amount input')


@when(u'I click the Deposit button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Deposit button')
