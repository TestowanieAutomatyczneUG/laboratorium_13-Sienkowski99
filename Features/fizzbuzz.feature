Feature: FizzBuzz

  Scenario: TestForFizzBuzz
    Given game starts
    When given 30
    Then result Fizz Buzz

  Scenario: TestForFizz
    Given game starts
    When given 3
    Then result Fizz

  Scenario: TestForBuzz
    Given game starts
    When given 10
    Then result Buzz

  Scenario: TestForOtherInt
    Given game starts
    When given 7
    Then result 7

  Scenario: TestForNotString
    Given game starts
    When given bagno
    Then result err

  Scenario: TestForArray
    Given game starts
    When given array
    Then result err