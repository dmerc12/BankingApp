from behave import when

# when
@when(u'I click the Delete Information navigation button')
def step_impl(context):
    context.customer_poms.delete_customer_navigation().click()


@when(u'I click the Delete Information button')
def step_impl(context):
    context.customer_poms.delete_button().click()
