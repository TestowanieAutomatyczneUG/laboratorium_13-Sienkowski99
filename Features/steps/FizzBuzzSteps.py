from behave import *
from main.FizzBuzz import *


@given("game starts")
def step_impl(context):
    context.fizzbuzz = FizzBuzz()


@when("given 30")
def step_impl(context):
    context.result = context.fizzbuzz.game(30)


@then("result Fizz Buzz")
def step_impl(context):
    assert context.result == "FizzBuzz"


@when("given 3")
def step_impl(context):
    context.result = context.fizzbuzz.game(3)


@then("result Fizz")
def step_impl(context):
    assert context.result == "Fizz"


@when("given 10")
def step_impl(context):
    context.result = context.fizzbuzz.game(10)


@then("result Buzz")
def step_impl(context):
    assert context.result == "Buzz"


@when("given 7")
def step_impl(context):
    context.result = context.fizzbuzz.game(7)


@then("result 7")
def step_impl(context):
    assert context.result == "7"


@when("given bagno")
def step_impl(context):
    context.result = context.fizzbuzz.game("bagno")


@when("given array")
def step_impl(context):
    context.result = context.fizzbuzz.game([])


@then("result err")
def step_impl(context):
    assert context.result == "err"
