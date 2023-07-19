Feature: Customers need to be able to make transfers

  Scenario Outline: As a customer, I should not be able to make a transfer when there are no accounts
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts navigation button
    When  I click the Transfer navigation button
    Then  I should be on a page with the title Managing Your Accounts

    Examples:
      | email           | password |
      | no@accounts.com | no       |

  Scenario Outline: As a customer, I should not be able to make a transfer with a negative amount
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts navigation button
    When  I click the Transfer navigation button
    When  I select <withdraw_account> from the transfer withdraw account dropdown
    When  I select <deposit_account> from the transfer deposit account dropdown
    When  I input <amount> into the transfer amount input
    When  I click the Transfer button
    Then  I should be on a page with the title Making A Transfer

    Examples:
      | email          | password | withdraw_account | deposit_account | amount  |
      | test@email.com | work     | -2               | -1              | -500.00 |

  Scenario Outline: As a customer, I should be able to make a transfer with correct information
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts navigation button
    When  I click the Transfer navigation button
    When  I select <withdraw_account> from the transfer withdraw account dropdown
    When  I select <deposit_account> from the transfer deposit account dropdown
    When  I input <amount> into the transfer amount input
    When  I click the Transfer button
    Then  I should be on a page with the title Managing Your Accounts

    Examples:
      | email          | password | withdraw_account | deposit_account | amount |
      | test@email.com | work     | -2               | -1              | 500.00 |
