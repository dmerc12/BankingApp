Feature: A customer needs to be able to login with their current credentials and also log out when they're done.

  Scenario Outline: As a customer, I input my login credentials incorrectly.
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email              | password | expected_toast_text                                             |
      | "wrong@email.com"  | "info"   | "Either the email or password are incorrect, please try again!" |
      | ""                 | "info"   | "The email field cannot be left empty, please try again!"       |
      | ""wrong@email.com" | ""       | "The password field cannot be left empty, please try again!"    |

  Scenario Outline: As a customer, I input my login credentials correctly.
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email            | password | expected_toast_text |
      | "test@email.com" | "work"   | "Welcome!"          |

  Scenario Outline: As a customer already logged in, I attempt to logout.
    Given I am on the home page
    When  I click the logout button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | expected_toast_text |
      | "Goodbye!"          |
