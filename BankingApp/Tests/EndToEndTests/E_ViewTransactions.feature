Feature: Customers need to view their transactions

  Scenario Outline: As a customer I should be able to view my transactions
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts navigation button
    When  I click the View Accounts button
    When  I click the View Transactions button
    Then  I should be on a page with the title Analyzing Your Transactions

  Examples:
      | email          | password |
      | test@email.com |work      |
