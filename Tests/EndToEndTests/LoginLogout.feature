Feature: Customers need to manage their relationships with banks and subsequent accounts

  Scenario Outline: As a customer, I should not be able to log into my account with incorrect login credentials
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I am not logged in and see an error
    When  I click the continue button
    Then  I should be on a page with the title Login Page

    Examples:
      | username  | password |
      | incorrect | customer |

  Scenario Outline: As a customer, I should not be able to log into my account with incorrect login credentials
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I am not logged in and see an error
    When  I click the continue button
    Then  I should be on a page with the title Login Page

    Examples:
      | username | password  |
      | new      | incorrect |

  Scenario Outline: As a customer, I should not be able to log into my account with empty login credentials
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I am not logged in and see an error
    When  I click the continue button
    Then  I should be on a page with the title Login Page

    Examples:
      | username | password  |
      |          | incorrect |

  Scenario Outline: As a customer, I should not be able to log into my account with empty login credentials
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I am not logged in and see an error
    When  I click the continue button
    Then  I should be on a page with the title Login Page

    Examples:
      | username | password |
      | new      |          |

  Scenario Outline: As a customer, I should be able to log into my account with correct login credentials
    Given I am on the login page
    When  I enter <username> in the username
    When  I enter <password> in the password
    When  I click the Login button
    When  I am not logged in and see an error
    When  I click the continue button
    Then  I should be on a page with the title Customer Home

    Examples:
      | username | password |
      | new      | customer |

  Scenario: As a customer, I should be able to log out
    Given I am on the home page
    When  I click "Log Out"
    When  I click the Log Out button
    When  I click the Continue button
    Then  I should be on a page with the title Login Page
