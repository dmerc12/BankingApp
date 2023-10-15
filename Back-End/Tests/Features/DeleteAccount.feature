Feature: A customer needs to be able to delete an existing account.

  Scenario Outiline: As a customer, I delete an existing account.
    Given I am on the login page
    When  I input <email> in the login email input
    When  I input <password> in the login password input
    When  I click the login button
    When  I click the manage accounts button
    When  I click on the delete modal on account <account_number>
    When  I click the delete account button
    Then  I should see a toast notification saying <expected_toast_text>

    Examples:
      | email          | password | account_number | expected_toast_text           |
      | test@email.com | work     | 1              | Account Successfully Deleted! |
    