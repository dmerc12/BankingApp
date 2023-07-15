Feature: Customers need to be able to leave the bank

  Scenario: As a customer, I should not be allowed access to the manage customer page without logging in first
    Given I am on the managing customer information page
    When  I click ok on the alert
    Then  I should be on a page with the title Login Page

  Scenario Outline: As a customer, I should be able to end my relationship with the bank
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click ok on the alert
    When  I click the Manage Customer Information button
    When  I click "Leave the bank"
    When  I click the Delete Customer button
    When  I click ok on the alert
    Then  I should be on a page with the title Login Page

    Examples:
      | username | password |
      | new      | customer |