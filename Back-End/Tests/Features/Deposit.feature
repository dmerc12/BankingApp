Feature: A customer needs to be able to deposit into an existing account.

  Scenario Outline: As a customer, I incorrectly deposit into an existing account.
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage accounts button
    When  I click the deposit modal on account <account_number>
    When  I input <deposit_amount> in the deposit amount input
    When  I click the deposit button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email          | password | account_number | deposit_amount | expected_toast_text |
      | test@email.com | work     | 1              | 0.00           | The deposit amount field cannot be negative or 0.00, please try again! |

  Scenario Outline: As a customer, I correctly deposit into an existing account.
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage accounts button
    When  I click the deposit modal on account <account_number>
    When  I input <deposit_amount> in the deposit amount input
    When  I click the deposit button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email          | password | account_number | deposit_amount | expected_toast_text |
      | test@email.com | work     | 1              | 25.00          | Deposit Successful! |
