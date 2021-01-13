Feature: Hamming

  Scenario: Both strings are emtpy
    Given Hamming starts
    When given empty string and empty string
    Then Return 0

  Scenario: Both strings are only 1 char long and they are the same
    Given Hamming starts
    When given A and A
    Then Return 0

  Scenario: Both strings are equally long and they are the same
    Given Hamming starts
    When given GGACTGAAATCTG and GGACTGAAATCTG
    Then Return 0

  Scenario: Both strings are only 1 char long but they are different
    Given Hamming starts
    When given G and T
    Then Return 1

  Scenario: Both strings are equally long but different
    Given Hamming starts
    When given GGACGGATTCTG and AGGACGGATTCT
    Then Return 9

  Scenario: Both strings different length
    Given Hamming starts
    When given AATG and AATGG
    Then Return strings are not equally long

  Scenario: Both strings different length but on reversed places
    Given Hamming starts
    When given AATGG and AATG
    Then Return strings are not equally long

  Scenario: First element is OK and second is empty string
    Given Hamming starts
    When given G and empty string
    Then Return strings are not equally long

  Scenario: First element is string and second is array
    Given Hamming starts
    When given G and array
    Then Return error

  Scenario: First element is array and second is string
    Given Hamming starts
    When given array and G
    Then Return error