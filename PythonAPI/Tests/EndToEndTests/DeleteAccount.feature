Feature: Customers need to be able to delete an account

  Scenario: As a customer, I should not be allowed access to the managing accounts page without logging in first
    Given I am on the managing accounts page
    When  I click ok on the alert
    Then  I should be on a page with the title Login Page

  Scenario Outline: As a customer, I should be able to delete an account with correct information
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click ok on the alert
    When  I click the Create and Manage Accounts button
    When  I click "Delete an Account"
    When  I select an account
    When  I click the Delete Account button
    When  I click ok on the alert
    Then  I should be on a page with the title Managing Accounts

    Examples:
      | username | password |
      |please|work|
