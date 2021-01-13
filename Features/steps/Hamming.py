from behave import *
from main.Hamming import *


@given("Hamming starts")
def step_impl(context):
    context.hamming = Hamming()


@when("given empty string and empty string")
def step_impl(context):
    context.result = context.hamming.distance("", "")


@when("given A and A")
def step_impl(context):
    context.result = context.hamming.distance("A", "A")


@when("given GGACTGAAATCTG and GGACTGAAATCTG")
def step_impl(context):
    context.result = context.hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG")


@then("Return 0")
def step_impl(context):
    assert context.result == 0


@when("given G and T")
def step_impl(context):
    context.result = context.hamming.distance("G", "T")


@then("Return 1")
def step_impl(context):
    assert context.result == 1


@when("given GGACGGATTCTG and AGGACGGATTCT")
def step_impl(context):
    context.result = context.hamming.distance("GGACGGATTCTG", "AGGACGGATTCT")


@then("Return 9")
def step_impl(context):
    assert context.result == 9


@when("given AATG and AATGG")
def step_impl(context):
    context.result = context.hamming.distance("AATG", "AATGG")


@when("given AATGG and AATG")
def step_impl(context):
    context.result = context.hamming.distance("AATGG", "AATG")


@when("given G and empty string")
def step_impl(context):
    context.result = context.hamming.distance("G", "")


@then("Return strings are not equally long")
def step_impl(context):
    assert context.result == "strings are not equally long"


@when("given G and array")
def step_impl(context):
    context.result = context.hamming.distance("G", [])


@when("given array and G")
def step_impl(context):
    context.result = context.hamming.distance([], "G")


@then("Return error")
def step_impl(context):
    assert context.result == "error"
