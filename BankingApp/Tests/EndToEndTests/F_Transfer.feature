Feature: Customers need to be able to transfer money between existing accounts

  Scenario: As a customer, I should not be allowed access to the managing accounts page without logging in first
    Given I am on the managing accounts page
    When  I click ok on the alert
    Then  I should be on a page with the title Login Page

  Scenario Outline: As a customer, I should not be able to use my account in transfers with malformed information
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click ok on the alert
    When  I click the Create and Manage Accounts button
    When  I click "Transfer Money Between Accounts"
    When  I select the withdraw account input
    When  I select the deposit account input
    When  I enter <transfer_amount> in the transfer amount input
    When  I click the Transfer button
    When  I click ok on the alert
    Then  I should be on a page with the title Managing Accounts

    Examples:
      | transfer_amount | username | password |
      | 25.00           | please   | work     |
      | 25.00           | please   | work     |
      | -25.00          | please   | work     |
      | 250000000000.00 | please   | work     |

  Scenario Outline: As a customer, I should be able to use my account in transfers with valid information
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click ok on the alert
    When  I click the Create and Manage Accounts button
    When  I click "Transfer Money Between Accounts"
    When  I select the withdraw account input
    When  I select the deposit account input
    When  I enter <transfer_amount> in the transfer amount input
    When  I click the Transfer button
    When  I click ok on the alert
    Then  I should be on a page with the title Managing Accounts

  Examples:
    | transfer_amount | username | password |
    | 25.00           | please   | work     |
