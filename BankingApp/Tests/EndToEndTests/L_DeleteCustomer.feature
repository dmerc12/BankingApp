Feature: Customers need to be able to leave the bank

  Scenario Outline: As a customer, I should be able to end my relationship with the bank
    Given I am on the login page
    When  I enter <email> in the login email input
    When  I enter <password> in the login password input
    When  I click the Login button
    When  I click the Manage Information navigation button
    When  I click the Delete Information navigation button
    When  I click the Delete Information button
    Then  I should be on a page with the title Login

    Examples:
      | email          | password |
      | test@email.com | work     |