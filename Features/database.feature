Feature: Database

  @db_connection
  Scenario: Add user without changing password
    Given Database start
    When login is "JANEK" password is "WODZIUNKA"
    And we don't want to change the password
    Then password is "WODZIUNKA"

  @db_connection
  Scenario: Add user and change password
    Given Database start
    When login is "JANEK" password is "WODZIUNKA"
    And change password to "KASZANKA"
    Then password is "KASZANKA"

  @db_connection
  Scenario: Add user and try to change password to too short one
    Given Database start
    When login is "JANEK" password is "WODZIUNKA"
    And change password to "ABC"
    Then password is too short

  @db_connection
  Scenario: Try to create user with too short password
    Given Database start
    When login is "JANEK" password is "ABC"
    Then password is too short

  @db_connection
  Scenario: Add user and try to change password to too short one
    Given Database start
    When login is "JANEK" password is "WODZIUNKA"
    And change password to "WODZIUNKA"
    Then password has not changed

  @db_connection
  Scenario: Try to add user with int instead of password and try again
    Given Database start
    When login is "JANEK" password is "123"
    And if there is an error try with "JANEK" and "BARZANT"
    Then password is "BARZANT"

  @db_connection
  Scenario: Try to add user with int instead of login and try again
    Given Database start
    When login is "123" password is "KOSTKA"
    And if there is an error try with "JANEK" and "KOSTKA"
    Then password is "KOSTKA"

  @db_connection
  Scenario: Try to add user with int instead of password
    Given Database start
    When login is "123" password is "KOSTKA"
    Then return ERROR from DB

  @db_connection
  Scenario: Try to add user with int instead of login
    Given Database start
    When login is "MARCINEK" password is "2137"
    Then return ERROR from DB

  @db_connection
  Scenario: Try to add user without login or password
    Given Database start
    When login is None password is None
    Then  return critical error
    And remove database
    Then check if db is removed