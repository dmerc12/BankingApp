Feature: Customers need to be able to delete an account

  Scenario Outline: As a customer, I should not be able to delete an account when there are no accounts
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts navigation button
    When  I click the Delete Account navigation button
    Then  I should be on a page with the title Managing Your Accounts

    Examples:
      | email           | password |
      | no@accounts.com | no       |

  Scenario Outline: As a customer, I should be able to make a transfer when there is at least 1 account
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts navigation button
    When  I click the Delete Account navigation button
    When  I select <account> from the delete account dropdown
    When  I click the Delete Account button
    Then  I should be on a page with the title Managing Your Accounts

    Examples:
      | email          | password | account |
      | test@email.com | work     | -1      |
