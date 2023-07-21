Feature: Customers need to view their accounts

  Scenario Outline: As a customer I should not be able to view my accounts if I do not have any
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts navigation button
    When  I click the View Accounts button
    Then  I should be on a page with the title Managing Your Accounts

  Examples:
    | email           | password |
    | no@accounts.com | work     |

  Scenario Outline: As a customer I should be able to view my accounts
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts navigation button
    When  I click the View Accounts button
    Then  I should be on a page with the title Viewing Your Accounts

  Examples:
      | email          | password |
      | test@email.com |work      |
