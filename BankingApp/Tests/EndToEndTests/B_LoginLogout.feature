Feature: Customers need to manage their relationships with banks and subsequent accounts

  Scenario: As a customer, I should not be allowed access to the home page without logging in first
    Given I am on the login page
    When  I click ok on the alert
    Then  I should be on a page with the title Login Page

  Scenario: As a customer, I should not be allowed access to the manage customer page without logging in first
    Given I am on the managing customer information page
    When  I click ok on the alert
    Then  I should be on a page with the title Login Page

  Scenario: As a customer, I should not be allowed access to the manage accounts page without logging in first
    Given I am on the managing accounts page
    When  I click ok on the alert
    Then  I should be on a page with the title Login Page

  Scenario Outline: As a customer, I should not be able to log into my account with incorrect login credentials
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click ok on the alert
    Then  I should be on a page with the title Login Page

    Examples:
      | username  | password  |
      | incorrect | customer  |
      | new       | incorrect |

  Scenario Outline: As a customer, I should be able to log in with the correct credentials and visit the home page
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click ok on the alert
    Then  I should be on a page with the title Customer Home

    Examples:
      | username | password |
      | please   | work     |

  Scenario Outline: As a customer, I should be able to log out from the home page
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click ok on the alert
    When  I click the Log Out button from the home page
    When  I click ok on the alert
    Then  I should be on a page with the title Login Page

    Examples:
      | username | password |
      | please   | work     |

  Scenario Outline: As a customer, I should be able to log out from the managing accounts page
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click ok on the alert
    When  I click the Create and Manage Accounts button
    When  I click the Log Out button from the managing accounts page
    When  I click ok on the alert
    Then  I should be on a page with the title Login Page

    Examples:
      | username | password |
      | please   | work     |

  Scenario Outline: As a customer, I should be able to log out from the managing customer page
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click ok on the alert
    When  I click the Manage Customer Information button
    When  I click the Log Out button from the manage customer information page
    When  I click ok on the alert
    Then  I should be on a page with the title Login Page

    Examples:
      | username | password |
      | please   | work     |
