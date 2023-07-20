Feature: Customers need to be able to deposit into an existing account

  Scenario Outline: As a customer, I should not be able to make a deposit when there are no accounts
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts navigation button
    When  I click the Deposit navigation button
    Then  I should be on a page with the title Managing Your Accounts

    Examples:
      | email           | password |
      | no@accounts.com | no       |

  Scenario Outline: As a customer, I should not be able to make a deposit with a negative amount
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts navigation button
    When  I click the Deposit navigation button
    When  I select <account> from the deposit account dropdown
    When  I input <amount> into the deposit amount input
    When  I click the Deposit button
    Then  I should be on a page with the title Making A Deposit

    Examples:
      | email          | password | account | amount  |
      | test@email.com | work     | -1      | -500.00 |

  Scenario Outline: As a customer, I should be able to make a deposit with correct information
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts navigation button
    When  I click the Deposit navigation button
    When  I select <account> from the deposit account dropdown
    When  I input <amount> into the deposit amount input
    When  I click the Deposit button
    Then  I should be on a page with the title Managing Your Accounts

    Examples:
      | email          | password | account | amount |
      | test@email.com | work     |-1       |500.00  |