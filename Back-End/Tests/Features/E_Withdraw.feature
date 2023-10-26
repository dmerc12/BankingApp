Feature: A customer needs to be able to withdraw from an existing account.

  Scenario Outline: As a customer, I incorrectly withdraw from an existing account.
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage accounts button
    When  I click the withdraw modal on account <account_number>
    When  I input <withdraw_amount> in the withdraw amount input
    When  I click the withdraw button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email          | password | account_number | withdraw_amount | expected_toast_text                                                     |
      | test@email.com | work     | 1              | 568395.00       | Insufficient funds, please try again!                                   |
      | test@email.com | work     | 1              | -58.32          | The withdraw amount field cannot be negative or 0.00, please try again! |

  Scenario Outline: As a customer, I correctly withdraw from an existing account.
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage accounts button
    When  I click the withdraw modal on account <account_number>
    When  I input <withdraw_amount> in the withdraw amount input
    When  I click the withdraw button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email          | password | account_number | withdraw_amount | expected_toast_text  |
      | test@email.com | work     | 1              | 5.00            | Withdraw Successful! |
