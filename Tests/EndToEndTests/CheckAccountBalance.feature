Feature:

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

