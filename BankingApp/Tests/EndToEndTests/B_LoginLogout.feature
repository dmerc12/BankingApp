Feature: Customers need to manage their relationships with banks and subsequent accounts

  Scenario: As a customer, I should not be allowed access to the home page without logging in first
    Given I am on the login page
    When  I click the home tab in the navbar
    Then  I should be on a page with the title Login Page

  Scenario: As a customer, I should not be allowed access to the manage customer information page without logging in first
    Given I am on the login page
    When  I click the manage customer information tab in the navbar
    Then  I should be on a page with the title Login Page

  Scenario: As a customer, I should not be allowed access to the manage accounts page without logging in first
    Given I am on the login page
    When  I click the manage accounts tab in the navbar
    Then  I should be on a page with the title Login Page

  Scenario Outline: As a customer, I should not be able to log into my account with incorrect login credentials
    Given I am on the login page
    When  I enter <email> in the email
    When  I enter <password> in the password
    When  I click the Login button
    Then  I should be on a page with the title Login Page

    Examples:
      | email          | password  |
      | incorrect      | customer  |
      | test@email.com | incorrect |

  Scenario Outline: As a customer, I should be able to log in with the correct credentials and visit the home page
    Given I am on the login page
    When  I enter <email> in the email
    When  I enter <password> in the password
    When  I click the Login button
    Then  I should be on a page with the title Home Dashboard

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to log out
    Given I am on the login page
    When  I enter <email> in the email
    When  I enter <password> in the password
    When  I click the Login button
    When  I click the Log Out button
    Then  I should be on a page with the title Login Page

    Examples:
      | email          | password |
      | test@email.com | work     |

