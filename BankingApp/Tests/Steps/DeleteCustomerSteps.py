from behave import when

@when(u'I click "Leave the bank"')
def step_impl(context):
    context.customer_poms.delete_customer_collapse_button().click()


@when(u'I click the Delete CustomerRoutes button')
def step_impl(context):
    context.customer_poms.delete_customer_button().click()
