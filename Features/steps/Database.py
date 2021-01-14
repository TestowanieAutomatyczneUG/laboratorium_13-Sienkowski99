from behave import *
from main.Database import *


@given("database start")
def step_impl(context):
    context.database = Database()


@when("login is None password is None")
def step_impl(context):
    context.result = context.database.add_user(None, None)


@when(u'login is "{login}" password is "{password}"')
def step_impl(context, login, password):
    try:
        context.result = context.database.add_user(int(login), int(password))
    except:
        try:
            context.result = context.database.add_user(int(login), password)
        except:
            try:
                context.result = context.database.add_user(login, int(password))
            except:
                context.result = context.database.add_user(login, password)


@step(u'if there is an error try with "{login}" and "{password}"')
def step_impl(context, login, password):
    if context.result == "ERROR":
        context.result = context.database.add_user(login, password)


@step("we don't want to change the password")
def step_impl(context):
    context.result = context.result


@then(u'password is "{password}"')
def step_impl(context, password):
    assert context.result["password"] == password


@step(u'change password to "{new_password}"')
def step_impl(context, new_password):
    context.result = context.database.change_password(context.result["login"], new_password)


@then(u'password is too short')
def step_impl(context):
    assert context.result == "password is too short"


@then(u'password has not changed')
def step_impl(context):
    assert context.result == "password has not changed"


@then(u'return ERROR from DB')
def step_impl(context):
    assert context.result == "ERROR"


@then(u'return critical error')
def step_impl(context):
    assert context.result == "critical error"


@step('remove database')
def step_impl(context):
    context.database = None


@step('check if db is removed')
def step_impl(context):
    assert context.database is None
