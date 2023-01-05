Feature: Customers need to manage their relationships with banks and subsequent accounts

  Scenario: As a customer, I should not be allowed access to the home page without logging in first
    Given I am on the home page
    When  I click the Continue button
    Then  I should be on a page with the title Login Page

  Scenario Outline: As a customer, I should not be able to log into my account with incorrect login credentials
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    Then  I should be on a page with the title Login Page

    Examples:
      | username  | password  |
      | incorrect | customer  |
      | new       | incorrect |


  Scenario Outline: As a customer, I should be able to log into my account with correct login credentials
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    Then  I should be on a page with the title Customer Home

    Examples:
      | username | password |
      | please   | work     |

  Scenario: As a customer, I should be able to log out
    Given I am on the home page
    When  I click "Log Out"
    When  I click the Log Out button
    When  I click the Continue button
    Then  I should be on a page with the title Login Page

  Scenario Outline: As a customer, I should be able to log into my account with correct login credentials
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
      | please   | work     |

  Scenario: As a customer, I should be able to log out
    Given I am on the home page
    When  I click "Log Out"
    When  I click the Log Out button
    When  I click the Continue button
    Then  I should be on a page with the title Login Page

  Scenario Outline: As a customer, I should be able to log into my account with correct login credentials
    Given I am on the managing accounts page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click the Continue button
    When  I am on a page with the title Customer Home
    When  I click "Manage Customer Information"
    When  I click the Manage Customer Information button
    Then  I am on a page with the title Managing Customer

    Examples:
      | username | password |
      | please   | work     |

  Scenario: As a customer, I should be able to log out
    Given I am on the managing customer information page
    When  I click "Log Out"
    When  I click the Log Out button
    When  I click the Continue button
    Then  I should be on a page with the title Login Page