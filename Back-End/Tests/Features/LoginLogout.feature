Feature: A customer needs to be able to login with their current credentials and also log out when they're done.

  Scenario Outline: As a customer, I input my login credentials incorrectly.
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    Then  I remain on the login page

    Examples:
      | email              | password |
      | "wrong@email.com"  | "info"   |
      | ""                 | "info"   |
      | ""wrong@email.com" |""        |
  Scenario Outline: As a customer, I input my login credentials incorrectly.
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    Then  I am routed to the home page

    Examples:
      | email            | password |
      | "test@email.com" | "work"   |

  Scenario: As a customer already logged in, I attempt to logout.
    Given I am on the home page
    When  I click the logout button
    Then  I am routed to the login page
