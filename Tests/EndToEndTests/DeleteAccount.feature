Feature:

  Scenario Outline: As a customer, I should be able to log in
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I click the Continue button
    Then  I should be on a page with the title Customer Home

    Examples:
      | username | password |
      | new      | customer |