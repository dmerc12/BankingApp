Feature: Customers need to manage their relationships with banks and subsequent accounts

  Scenario: As a customer, I should not be allowed access to the home page without logging in first
    Given I am on the login page
    When  I click the Home tab
    Then  I should be on a page with the title Login

  Scenario: As a customer, I should not be allowed access to the manage customer information page without logging in first
    Given I am on the login page
    When  I click the Manage Customer Information tab
    Then  I should be on a page with the title Login

  Scenario: As a customer, I should not be allowed access to the manage accounts page without logging in first
    Given I am on the login page
    When  I click the Manage Accounts tab
    Then  I should be on a page with the title Login

  Scenario: As a customer, I should be able to go back to the login page from the register page using the login tab
    Given I am on the register page
    When  I click the Login tab
    Then  I should be on a page with the title Login

  Scenario Outline: As a customer, I should not be able to log into my account with incorrect login credentials
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password  |
      | incorrect      | customer  |
      | test@email.com | incorrect |

  Scenario Outline: As a customer, I should be able to log in with the correct credentials and visit the home page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    Then  I should be on a page with the title Home Dashboard

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to use the Manage Customer Information tab once logged in
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Customer Information tab
    Then  I should be on a page with the title Managing Your Information

    Examples:
      | email          | password |
      | test@email.com |work      |

  Scenario Outline: As a customer, I should be able to use the Manage Accounts tab once logged in
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts tab
    Then  I should be on a page with the title Managing Your Accounts

    Examples:
      | email          | password |
      | test@email.com |work      |

  Scenario Outline: As a customer, I should be able to use the Home tab once logged in
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Customer Information tab
    When  I click the Home tab
    Then  I should be on a page with the title Home Dashboard

    Examples:
      | email          | password |
      | test@email.com |work      |

  Scenario Outline: As a customer, I should be able to log out from the home page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Log Out button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to log out from the Manage Accounts page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts tab
    When  I click the Log Out button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to log out from the Create Account page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts tab
    When  I click the Create Account navigation button
    When  I click the Log Out button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to log out from the View Accounts page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts tab
    When  I click the View Accounts navigation button
    When  I click the View Transactions button
    When  I click the Back button
    When  I click the Log Out button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to log out from the View Transactions page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts tab
    When  I click the View Accounts navigation button
    When  I click the View Transactions button
    When  I click the Log Out button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to log out from the Deposit page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts tab
    When  I click the Deposit navigation button
    When  I click the Log Out button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to log out from the Withdraw page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts tab
    When  I click the Withdraw navigation button
    When  I click the Log Out button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to log out from the Transfer page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts tab
    When  I click the Transfer navigation button
    When  I click the Log Out button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to log out from the Delete Account page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Accounts tab
    When  I click the Delete Account navigation button
    When  I click the Log Out button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to log out from the Manage Customer Information page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Customer Information tab
    When  I click the Log Out button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to log out from the Update Information page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Customer Information tab
    When  I click the Update Information navigation button
    When  I click the Log Out button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to log out from the Delete Information page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Customer Information tab
    When  I click the Delete Information navigation button
    When  I click the Log Out button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |

  Scenario Outline: As a customer, I should be able to log out from the Change Password page
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Customer Information tab
    When  I click the Change Password navigation button
    When  I click the Log Out button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |