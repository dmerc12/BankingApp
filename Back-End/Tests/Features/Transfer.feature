Feature: A customer needs to be able to transfer money between existing accounts.

  Scenario Outline: As a customer, I incorrectly transfer between accounts.
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage accounts button
    When  I click the transfer modal
    When  I click the transfer from account input
    When  I click account <withdraw_account_number> as transfer from account
    When  I click the transfer to account input
    When  I click account <deposit_account_number> as the transfer to account
    When  I input <transfer_amount> in the transfer amount input
    When  I click the transfer button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email          | password | withdraw_account_number | deposit_account_number | transfer_amount   | expected_toast_text                                                     |
      | test@email.com | work     | -1                      | 1                      | 98087680987765.00 | Insufficient funds, please try again!                                   |
      | test@email.com | work     | -1                      | 1                      | 0.00              | The transfer amount field cannot be negative or 0.00, please try again! |
      | test@email.com | work     | 1                       | 1                      | 5.00              | The deposit and withdraw accounts cannot be the same, please try again!                                                    |


  Scenario Outline: As a customer, I correctly transfer between accounts.
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage accounts button
    When  I click the transfer modal
    When  I click the transfer from account input
    When  I click account <withdraw_account_number> as transfer from account
    When  I click the transfer to account input
    When  I click account <deposit_account_number> as the transfer to account
    When  I input <transfer_amount> in the transfer amount input
    When  I click the transfer button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email          | password | withdraw_account_number | deposit_account_number | transfer_amount | expected_toast_text  |
      | test@email.com | work     | -1                      | 1                      | 5.00            | Transfer Successful! |
