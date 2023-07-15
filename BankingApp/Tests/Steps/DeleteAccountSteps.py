from behave import when

@when(u'I select {account} from the delete account dropdown')
def step_impl(context, account: int):
    raise NotImplementedError(u'STEP: When I select -1 from the delete account dropdown')


@when(u'I click the Delete Account button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Delete Account button')
