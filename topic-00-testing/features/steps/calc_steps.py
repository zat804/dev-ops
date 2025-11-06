from behave import *

import calc

from behave.api.pending_step import StepNotImplementedError
@given(u'we have included the calc module')
def step_impl(context):
    contents = dir(calc)


@when(u'we call the add function with 3 and 4')
def step_impl(context):
    context.result = calc.add(3,4)


@then(u'we will get 7')
def step_impl(context):
    assert context.result == 7

