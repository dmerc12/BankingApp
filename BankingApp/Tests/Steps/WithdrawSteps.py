from behave import when

# when
@when(u'I select {account} from the withdraw account dropdown')
def step_impl(context, account: int):
    raise NotImplementedError(u'STEP: When I select -1 from the withdraw account dropdown')


@when(u'I input {amount} into the withdraw amount input')
def step_impl(context, amount: float):
    raise NotImplementedError(u'STEP: When I input -500.00 into the withdraw amount input')


@when(u'I click the Withdraw button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Withdraw button')
