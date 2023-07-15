from behave import when

@when(u'I select {withdraw_account} from the transfer withdraw account dropdown')
def step_impl(context, withdraw_account: int):
    raise NotImplementedError(u'STEP: When I select -2 from the transfer withdraw account dropdown')


@when(u'I select {deposit_account} from the transfer deposit account dropdown')
def step_impl(context, deposit_account: int):
    raise NotImplementedError(u'STEP: When I select -1 from the transfer deposit account dropdown')


@when(u'I input {amount} into the transfer amount input')
def step_impl(context, amount: float):
    raise NotImplementedError(u'STEP: When I input 500.00 into the transfer amount input')


@when(u'I click the Transfer button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Transfer button')
