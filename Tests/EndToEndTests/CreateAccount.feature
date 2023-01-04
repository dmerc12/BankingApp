Feature: Customers need to create accounts

  Scenario: As a customer, I should not be allowed access to the managing accounts page without logging in first
    Given I am on the managing accounts
    When  I click the Continue button
    Then  I should be on a page with the title Login Page

  Scenario Outline: As a customer, I should be able to log in
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click the Continue button
    When  I am on a page with the title Customer Home
    When  I click "Manage Accounts"
    When  I click the Create and Manage Accounts button
    Then  I should be on a page with the title Managing Accounts

    Examples:
      | username | password |
      | new      | customer |

  Scenario Outline: As a customer I should not be able to create an account with a negative amount
    Given I am on the managing accounts page
    When  I click "Create a New Account"
    When  I enter a negative <starting amount> in the starting amount
    When  I click the Create Account button
    When  I click the continue button
    Then  I should be on a page with the title Managing Accounts

    Examples:
      | starting amount |
      | -250.00         |

  Scenario Outline: As a customer I should be able to create an account
    Given I am on the managing accounts page
    When  I click "Create a New Account"
    When  I enter <starting amount> in the starting amount
    When  I click the Create Account button
    When  I click the continue button
    Then  I should be on a page with the title Managing Accounts

    Examples:
      | starting amount |
      | 250.00          |