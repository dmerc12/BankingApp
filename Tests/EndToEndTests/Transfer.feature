Feature: Customers need to be able to transfer money between existing accounts

  Scenario: As a customer, I should not be allowed access to the managing accounts page without logging in first
    Given I am on the managing accounts
    When  I click ok on the alert
    Then  I should be on a page with the title Login Page

  Scenario Outline: As a customer, I should be able to log in
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click ok on the alert
    When  I am on a page with the title Customer Home
    Then  I should be on a page with the title Customer Home

    Examples:
      | username | password |
      | new      | customer |

  Scenario Outline: As a customer, I should not be able to use my account in transfers with malformed information
    Given I am on the home page
    When  I click the Create and Manage Accounts button
    When  I click "Transfer Money Between Accounts"
    When  I enter <withdraw-account-number>
    When  I enter <deposit-account-number>
    When  I enter <transfer-amount>
    When  I click the Transfer button
    When  I click ok on the alert
    Then  I should be on a page with the title Managing Accounts

    Examples:
      | withdraw-account-number | deposit-account-number | transfer-amount |
      | "1"                     | 1                      | 25.00           |
      | 1                       | "1"                    | 25.00           |
      | 1                       | 1                      | "25.00"         |
      | -500000000              | 1                      | 25.00           |
      | 1                       | -5000000               | 25.00           |
      | 1                       | -1                     | -25.00          |
      | 1                       | -1                     | 250000000000.00 |

  Scenario Outline: As a customer, I should be able to use my account in transfers with valid information
    Given I am on the home page
    When  I click the Create and Manage Accounts button
    When  I click "Transfer Money Between Accounts"
    When  I enter <withdraw-account-number>
    When  I enter <deposit-account-number>
    When  I enter <transfer-amount>
    When  I click the Transfer button
    When  I click ok on the alert
    Then  I should be on a page with the title Managing Accounts

  Examples:
    | withdraw-account-number | deposit-account-number | transfer-amount |
    | 1                       | -1                     | 25.00           |
