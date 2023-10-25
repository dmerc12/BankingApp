Feature: A customer needs to be able to create a new account.

  Scenario Outline: As a customer, I incorrectly create a new account.
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage accounts button
    When  I click the create account modal
    When  I input the <starting_balance> in the starting balance input
    When  I click the create account button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email          | password | starting_balance | expected_toast_text                                            |
      | test@email.com | work     | 0.00             | The balance field must be greater than 0.00, please try again! |
      | test@email.com | work     | -57.95           | The balance field cannot be negative, please try again!        |

  Scenario Outline: As a customer, I successfully create a new account.
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage accounts button
    When  I click the create account modal
    When  I input the <starting_balance> in the starting balance input
    When  I click the create account button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email          | password | starting_balance | expected_toast_text           |
      | test@email.com | work     | 25.00            | Account successfully created! |
