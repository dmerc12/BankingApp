Feature: Customers need to create accounts

  Scenario Outline: As a customer I should not be able to create an account with a negative amount
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts navigation button
    When  I click the Create Account navigation button
    When  I enter <starting_amount> in the starting amount
    When  I click the Create Account button
    Then  I should be on a page with the title Creating An Account

    Examples:
      | starting_amount | email          | password |
      | -250.00         | test@email.com |work      |

  Scenario Outline: As a customer I should be able to create an account with correct information
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts navigation button
    When  I click the Create Account navigation button
    When  I enter <starting_amount> in the starting amount
    When  I click the Create Account button
    Then  I should be on a page with the title Managing Your Accounts

    Examples:
      | starting_amount | email          | password |
      | 250.00          | test@email.com |work      |
